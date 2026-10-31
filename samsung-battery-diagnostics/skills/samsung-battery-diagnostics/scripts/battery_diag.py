#!/usr/bin/env python3
"""Deterministic helper for the samsung-battery-diagnostics skill.

Standard library only. Supports exactly two devices:
  * Samsung Galaxy M15 5G  (SM-M156B family)
  * Samsung Galaxy A14 5G  (SM-A146 family)

Sub-commands (all print JSON):
  identify <MODEL_CODE>               -> which supported device, or why not
  rate     <measurement.json>         -> drain/charge rate, uncertainty, class
  rank     <evidence.json>            -> ranked causes, missing evidence, interventions
  compare  <before.json> <after.json> -> comparability check and verdict

Every threshold here is a SKILL HEURISTIC, not a Samsung specification.
The primary judgement is always the user's own before/after comparison.
"""
from __future__ import annotations

import json
import math
import re
import sys
from datetime import datetime

# ---------------------------------------------------------------------------
# Device profiles (facts sourced in references/samsung-documentation.md)
# ---------------------------------------------------------------------------
DEVICES = {
    "galaxy-m15-5g": {
        "name": "Samsung Galaxy M15 5G",
        "typical_mah": 6000,  # Samsung ID product page [S1]
        "rated_mah": 5880,  # Samsung ID product page [S1]
        "max_wired_w": 25,  # Samsung ID product page, adapter sold separately [S1]
        "display": "Super AMOLED, 6.5in, 1080x2340, up to 90Hz",
        "aod_supported": True,  # AMOLED; verify menu on device
        "profile_file": "devices/galaxy-m15-5g.md",
    },
    "galaxy-a14-5g": {
        "name": "Samsung Galaxy A14 5G",
        "typical_mah": 5000,  # Samsung PH product page [S4]
        "rated_mah": 4900,  # Samsung PH product page [S4]
        "max_wired_w": 15,  # Samsung Newsroom Indonesia [S6]
        "display": "PLS LCD, 6.6in, 1080x2408, up to 90Hz",
        "aod_supported": False,  # LCD panel; see device profile
        "profile_file": "devices/galaxy-a14-5g.md",
    },
}

# Chipset by A14 5G model-code suffix letter(s).
A14_CHIPSET = {
    "B": ("Exynos 1330", "verified: Samsung Newsroom India [S5] (SM-A146B sold in India)"),
    "P": ("MediaTek Dimensity 700", "verified: Samsung Newsroom Indonesia [S6]; SM-A146P product page [S4]"),
    "U": ("MediaTek Dimensity 700", "reported: GSMArena review of the US unit [S22]; not on a Samsung page"),
}

# Model codes that are easily confused with the supported devices.
LOOKALIKES = [
    (r"^SM-A145", "Galaxy A14 (4G/LTE) - a different phone with a different chipset; not supported"),
    (r"^SM-M146", "Galaxy M14 5G - a different phone; not supported"),
    (r"^SM-E146", "Galaxy F14 5G - a different phone; not supported"),
    (r"^SM-A156", "Galaxy A15 5G - a different phone; not supported"),
    (r"^SM-E156", "Galaxy F15 5G - a sibling of the M15 5G but a different product; not supported"),
    (r"^SM-M156[^B]", "an M15-family code that is not SM-M156B; regional variant not verified; not supported"),
]

# ---------------------------------------------------------------------------
# Heuristic thresholds, expressed as average current equivalent (mA) so that
# both batteries are judged on the same physical scale:
#   mA_eq = rate_pct_per_h / 100 * typical_mAh
# ---------------------------------------------------------------------------
STANDBY_BANDS = [(50, "expected"), (100, "elevated"), (math.inf, "abnormal")]
ACTIVE_BANDS = {
    "light": [(600, "expected"), (900, "elevated"), (math.inf, "abnormal")],
    "moderate": [(900, "expected"), (1300, "elevated"), (math.inf, "abnormal")],
    # heavy = gaming, camera, navigation, hotspot, video calls: not classified
}
MIN_STANDBY_HOURS = 4.0  # 6+ recommended
MIN_ACTIVE_SCREEN_ON_H = 0.5
MIN_DROP_POINTS = 3  # below this, 1% display resolution dominates
READING_UNCERTAINTY_PTS = 1.0  # two readings, each +/-0.5 percentage point
CONTAMINATION_FRACTION = 0.05  # screen-on > 5% of a standby window


def _err(msg: str) -> dict:
    return {"ok": False, "error": msg}


# ---------------------------------------------------------------------------
# identify
# ---------------------------------------------------------------------------
def identify(model_code: str) -> dict:
    code = (model_code or "").strip().upper().replace(" ", "")
    if not code:
        return _err("No model number given. Ask for Settings > About phone > Model number.")
    if not code.startswith("SM-"):
        code = "SM-" + code if re.match(r"^[AMEF]\d{3}", code) else code
    for pattern, why in LOOKALIKES:
        if re.match(pattern, code):
            return {"ok": False, "model_code": code, "supported": False, "reason": why}
    if code.startswith("SM-M156B"):
        return {
            "ok": True,
            "supported": True,
            "model_code": code,
            "device": "galaxy-m15-5g",
            "name": DEVICES["galaxy-m15-5g"]["name"],
            "chipset": "MediaTek Dimensity 6100+",
            "chipset_basis": "verified: Samsung Newsroom India [S2]",
            "profile_file": DEVICES["galaxy-m15-5g"]["profile_file"],
        }
    a146 = re.match(r"^SM-A146([A-Z0-9]*)", code)
    if a146 or code.startswith("SM-S146VL"):  # SM-S146VL: US prepaid code listed by GSMArena [S20]
        suffix = a146.group(1) if a146 else ""
        # Only the exact family letters B, P and U (not U1) have a sourced chipset.
        key = suffix[:1] if suffix[:1] in A14_CHIPSET and not suffix.startswith("U1") else ""
        chip, basis = A14_CHIPSET.get(
            key,
            (
                "unverified (no chipset source for this code)",
                "unverified: no official Samsung or reliable third-party source maps this code to a chipset",
            ),
        )
        return {
            "ok": True,
            "supported": True,
            "model_code": code,
            "device": "galaxy-a14-5g",
            "name": DEVICES["galaxy-a14-5g"]["name"],
            "chipset": chip,
            "chipset_basis": basis,
            "profile_file": DEVICES["galaxy-a14-5g"]["profile_file"],
        }
    return {
        "ok": False,
        "model_code": code,
        "supported": False,
        "reason": "Not a Galaxy M15 5G (SM-M156B...) or Galaxy A14 5G (SM-A146...). This skill supports only those two devices.",
    }


# ---------------------------------------------------------------------------
# rate
# ---------------------------------------------------------------------------
def _hours(meas: dict) -> float | None:
    if "duration_h" in meas and meas["duration_h"] is not None:
        return float(meas["duration_h"])
    if meas.get("start_time") and meas.get("end_time"):
        t0 = datetime.fromisoformat(meas["start_time"])
        t1 = datetime.fromisoformat(meas["end_time"])
        return (t1 - t0).total_seconds() / 3600.0
    return None


def _band(value: float, bands) -> str:
    for limit, label in bands:
        if value <= limit:
            return label
    return bands[-1][1]


def rate(meas: dict) -> dict:
    dev_key = meas.get("device")
    if dev_key not in DEVICES:
        return _err("measurement.device must be 'galaxy-m15-5g' or 'galaxy-a14-5g'")
    dev = DEVICES[dev_key]
    kind = meas.get("kind")
    if kind not in ("standby", "active", "mixed", "charging"):
        return _err("measurement.kind must be standby, active, mixed or charging")
    try:
        start = float(meas["start_pct"])
        end = float(meas["end_pct"])
    except (KeyError, TypeError, ValueError):
        return _err("start_pct and end_pct are required numbers (battery % read from the phone)")
    hours = _hours(meas)
    if hours is None or hours <= 0:
        return _err("duration_h (or start_time and end_time) is required and must be positive")
    screen_on_h = float(meas.get("screen_on_min", 0) or 0) / 60.0
    warnings: list[str] = []
    out: dict = {"ok": True, "device": dev_key, "kind": kind, "hours": round(hours, 2)}

    if kind == "charging":
        gain = end - start
        if gain <= 0:
            return _err("charging measurement needs end_pct > start_pct")
        minutes = hours * 60
        r = gain / minutes
        u = READING_UNCERTAINTY_PTS / minutes
        out.update(
            gain_pts=gain,
            charge_rate_pct_per_min=round(r, 3),
            uncertainty_pct_per_min=round(u, 3),
            charger_w=meas.get("charger_w"),
            classification="not_classified",
            note="Charging speed is compared only against the same phone's own runs (same start %, adapter, cable, temperature). No absolute target is assumed.",
        )
        if gain < MIN_DROP_POINTS:
            warnings.append("Gain under 3 points: too small to compare reliably. Measure for longer.")
        if start >= 80:
            warnings.append("Started at 80% or above: charging normally slows near full. Start below 50% for speed tests.")
        out["warnings"] = warnings
        return out

    drop = start - end
    if drop < 0:
        return _err("end_pct is higher than start_pct; was the phone charged during the window? Exclude charging periods.")
    if meas.get("charging_during"):
        return _err("Phone was charged during the window; the measurement is invalid. Repeat without charging.")
    out["drop_pts"] = drop
    if drop < MIN_DROP_POINTS:
        warnings.append("Drop under 3 points: the 1% display step dominates. Extend the window before concluding.")

    if kind == "standby":
        if hours < MIN_STANDBY_HOURS:
            warnings.append(f"Standby window under {MIN_STANDBY_HOURS:g} h; 6 h or more (overnight) is recommended.")
        if screen_on_h > CONTAMINATION_FRACTION * hours:
            warnings.append("Screen was on for more than 5% of the standby window: result mixes active and idle use.")
        r = drop / hours
        u = READING_UNCERTAINTY_PTS / hours
        bands = STANDBY_BANDS
    elif kind == "active":
        if screen_on_h <= 0:
            return _err("active measurement needs screen_on_min (from Settings > Battery usage / Screen time)")
        if screen_on_h < MIN_ACTIVE_SCREEN_ON_H:
            warnings.append("Less than 30 min screen-on time: too short to classify.")
        if hours - screen_on_h > 1.0:
            warnings.append("More than 1 h of screen-off time inside an 'active' window; use kind 'mixed' with a standby baseline.")
        r = drop / screen_on_h
        u = READING_UNCERTAINTY_PTS / screen_on_h
        workload = meas.get("workload", "unknown")
        bands = ACTIVE_BANDS.get(workload)
        out["workload"] = workload
    else:  # mixed
        base = meas.get("standby_rate_pct_per_h")
        if screen_on_h <= 0:
            return _err("mixed measurement needs screen_on_min")
        if base is None:
            r_total = drop / hours
            out.update(
                overall_rate_pct_per_h=round(r_total, 3),
                classification="not_classified",
                missing=["standby_rate_pct_per_h from a separate overnight standby test, needed to split screen-on from screen-off drain"],
                warnings=warnings,
            )
            return out
        off_h = max(hours - screen_on_h, 0.0)
        on_drop = drop - float(base) * off_h
        if on_drop < 0:
            warnings.append("Standby baseline explains the whole drop; screen-on drain could not be isolated.")
            on_drop = 0.0
        r = on_drop / screen_on_h
        base_u = float(meas.get("standby_uncertainty_pct_per_h", 0.25))
        u = (READING_UNCERTAINTY_PTS + base_u * off_h) / screen_on_h  # baseline error scales with off-time
        workload = meas.get("workload", "unknown")
        bands = ACTIVE_BANDS.get(workload)
        out["workload"] = workload
        out["estimated_screen_on_drop_pts"] = round(on_drop, 2)

    ma = r / 100.0 * dev["typical_mah"]
    out.update(
        rate_pct_per_h=round(r, 3),
        uncertainty_pct_per_h=round(u, 3),
        mA_equivalent=round(ma, 1),
        rate_basis="per screen-on hour" if kind in ("active", "mixed") else "per hour of standby",
    )
    if bands is None:
        out["classification"] = "not_classified"
        out["classification_note"] = "Heavy or unknown workload (gaming, camera, navigation, hotspot, calls): no expected range is assumed."
    else:
        out["classification"] = _band(ma, bands)
        out["classification_note"] = "Skill heuristic on mA-equivalent from typical capacity, not a Samsung specification."
    if out.get("drop_pts", 99) < MIN_DROP_POINTS:
        out["classification"] = "insufficient_data"
    projected = (100.0 / r) if r > 0 else None
    if projected:
        key = "projected_screen_on_hours_per_full_charge" if kind != "standby" else "projected_standby_hours_per_full_charge"
        out[key] = round(projected, 1)
    out["warnings"] = warnings
    return out


# ---------------------------------------------------------------------------
# rank: deterministic cause scoring
# ---------------------------------------------------------------------------
CAUSES = {
    "SAFETY_STOP": ("Physical safety concern (swelling, burning smell, too hot to hold, liquid damage)", "diagnostics/battery-health.md"),
    "APP_BACKGROUND": ("A specific app is consuming battery in the background", "diagnostics/app-drain.md"),
    "RECENT_INSTALL": ("A recently installed or updated app started the drain", "diagnostics/app-drain.md"),
    "POST_UPDATE_SETTLING": ("Post-update or new-setup background work (temporary)", "diagnostics/battery-drain.md"),
    "SYSTEM_PROCESS": ("High consumption attributed to a system component (often caused by apps or sync using it)", "diagnostics/battery-drain.md"),
    "WEAK_SIGNAL": ("Weak cellular signal makes the modem work harder", "diagnostics/network-drain.md"),
    "NETWORK_5G": ("5G connection overhead (5G NSA uses LTE and 5G together)", "diagnostics/network-drain.md"),
    "CONNECTIVITY_EXTRAS": ("Hotspot, Bluetooth devices or Wi-Fi/Bluetooth scanning", "diagnostics/network-drain.md"),
    "DISPLAY": ("Display settings (brightness, timeout, refresh rate, AOD)", "diagnostics/display-drain.md"),
    "LOCATION_SYNC": ("Location access or account synchronisation by apps", "diagnostics/app-drain.md"),
    "BATTERY_DEGRADATION": ("Battery wear (physical capacity loss)", "diagnostics/battery-health.md"),
    "CHARGER_UNDERPOWERED": ("Adapter/source cannot deliver the phone's fast-charging power", "diagnostics/charging.md"),
    "FAST_CHARGING_OFF": ("Fast charging switched off in settings", "diagnostics/charging.md"),
    "CABLE_PORT": ("Cable, port debris or connector problem", "diagnostics/charging.md"),
    "MOISTURE": ("Moisture detected in the USB-C port", "diagnostics/charging.md"),
    "THERMAL_CHARGING": ("Heat or heavy use during charging slows or pauses charging", "diagnostics/charging.md"),
    "CHARGE_LIMIT": ("Battery protection is limiting the charge level by design", "diagnostics/charging.md"),
    "WITHIN_EXPECTED": ("Measured consumption is within the expected range for the usage described", "workflows/verification.md"),
    "UNEXPLAINED_DRAIN": ("Elevated drain with no identified cause yet; isolate with airplane-mode and Safe-mode tests", "diagnostics/standby-drain.md"),
}

INTERVENTIONS = {
    "SAFETY_STOP": ["SAFE-01"],
    "APP_BACKGROUND": ["INT-APP-01", "INT-APP-02"],
    "RECENT_INSTALL": ["INT-APP-03", "INT-APP-01"],
    "POST_UPDATE_SETTLING": ["INT-WAIT-01"],
    "SYSTEM_PROCESS": ["INT-SYS-01"],
    "WEAK_SIGNAL": ["INT-NET-01", "INT-NET-02"],
    "NETWORK_5G": ["INT-NET-02"],
    "CONNECTIVITY_EXTRAS": ["INT-NET-03"],
    "DISPLAY": ["INT-DISP-01", "INT-DISP-02"],
    "LOCATION_SYNC": ["INT-APP-04", "INT-APP-05"],
    "BATTERY_DEGRADATION": ["INT-HEALTH-01", "INT-HEALTH-02"],
    "CHARGER_UNDERPOWERED": ["INT-CHG-01"],
    "FAST_CHARGING_OFF": ["INT-CHG-02"],
    "CABLE_PORT": ["INT-CHG-03"],
    "MOISTURE": ["INT-CHG-04"],
    "THERMAL_CHARGING": ["INT-CHG-05"],
    "CHARGE_LIMIT": ["INT-CHG-06"],
    "WITHIN_EXPECTED": ["INT-NONE-01"],
    "UNEXPLAINED_DRAIN": ["TEST-AIRPLANE", "TEST-SAFE"],
}

# Evidence the assistant must have before concluding, per reported symptom.
REQUIRED_EVIDENCE = {
    "rapid_screen_on": ["active_measurement", "top_consumers", "display", "network"],
    "overnight": ["standby_measurement", "top_consumers", "network"],
    "after_install": ["recent_install", "top_consumers", "standby_measurement"],
    "5g": ["network", "standby_measurement", "top_consumers"],
    "weak_signal": ["network", "standby_measurement"],
    "idle": ["standby_measurement", "top_consumers", "network"],
    "slow_charging": ["charging"],
    "degradation": ["health", "standby_measurement"],
}

EVIDENCE_PROMPTS = {
    "active_measurement": "Battery % at start and end of a period of normal use, with screen-on time for that period and what you were doing (light/moderate/heavy).",
    "standby_measurement": "Battery % at bedtime and on waking (screen off, not charging) with the exact times.",
    "top_consumers": "Screenshot of Settings > Battery > View details (or Battery usage) listing apps and their % since last full charge.",
    "display": "Brightness level (auto or manual), screen timeout, Motion smoothness setting; M15 5G only: whether Always On Display is on.",
    "network": "5G or 4G/LTE shown in the status bar, signal bars, Wi-Fi on/off and connected, and whether this was at home or travelling.",
    "recent_install": "Name of the app installed or updated just before the drain began and the date.",
    "charging": "Adapter wattage and brand, cable, what the lock screen says while charging (e.g. 'Super fast charging', 'Fast charging', 'Charging'), % gained over a timed period, and whether the phone felt hot.",
    "health": "Samsung Members > Support > Phone diagnostics > Battery status result, phone age, any unexpected shutdowns and at what %.",
}


def _add(scores: dict, cause: str, pts: int, basis: str, note: str) -> None:
    entry = scores.setdefault(cause, {"points": 0, "observations": [], "hypotheses": []})
    entry["points"] += pts
    (entry["observations"] if basis == "observation" else entry["hypotheses"]).append(note)


def rank(ev: dict) -> dict:
    dev_key = ev.get("device")
    if dev_key not in DEVICES:
        return _err("evidence.device must be 'galaxy-m15-5g' or 'galaxy-a14-5g' (identify the model first)")
    dev = DEVICES[dev_key]
    symptoms = ev.get("symptoms", [])
    scores: dict = {}

    # --- safety overrides everything -----------------------------------
    safety = ev.get("safety", {}) or {}
    if any(safety.get(k) for k in ("swelling", "burning_smell", "too_hot_to_hold", "liquid_damage")):
        _add(scores, "SAFETY_STOP", 100, "observation", "User reported a physical safety sign: " + ", ".join(k for k, v in safety.items() if v))

    # --- measurements ----------------------------------------------------
    standby = rate(dict(ev["standby_measurement"], device=dev_key)) if ev.get("standby_measurement") else None
    active = rate(dict(ev["active_measurement"], device=dev_key)) if ev.get("active_measurement") else None
    standby_cls = standby.get("classification") if standby and standby.get("ok") else None
    active_cls = active.get("classification") if active and active.get("ok") else None
    standby_high = standby_cls in ("elevated", "abnormal")
    active_high = active_cls in ("elevated", "abnormal")

    # --- app evidence ------------------------------------------------------
    consumers = ev.get("top_consumers") or []
    apps = [c for c in consumers if c.get("type") == "app"]
    systems = [c for c in consumers if c.get("type") == "system"]
    top_app = max(apps, key=lambda c: c.get("pct", 0), default=None)
    recent = ev.get("recent_install") or {}
    if top_app and top_app.get("pct", 0) >= 15:
        pts = 3 if (standby_high or top_app.get("background_heavy") or not top_app.get("heavily_used", False)) else 1
        _add(scores, "APP_BACKGROUND", pts, "observation", f"{top_app['name']} shows {top_app['pct']}% of battery use")
    if recent.get("name"):
        days = recent.get("days_ago", 99)
        if days <= 14 and "after_install" in symptoms:
            _add(scores, "RECENT_INSTALL", 2, "observation", f"Drain began after installing/updating {recent['name']} {days} day(s) ago")
        if any(c.get("name", "").lower() == recent["name"].lower() and c.get("pct", 0) >= 10 for c in consumers):
            _add(scores, "RECENT_INSTALL", 3, "observation", f"{recent['name']} is among the top consumers")
    if systems:
        top_sys = max(systems, key=lambda c: c.get("pct", 0))
        if top_sys.get("pct", 0) >= 20:
            _add(scores, "SYSTEM_PROCESS", 2, "observation", f"System item '{top_sys['name']}' shows {top_sys['pct']}%")
            _add(scores, "SYSTEM_PROCESS", 0, "hypothesis", "System components often carry work requested by apps or sync; do not disable them")

    upd = ev.get("recent_update_days")
    if upd is not None and upd <= 3:
        _add(scores, "POST_UPDATE_SETTLING", 2, "hypothesis", f"Software update or new setup {upd} day(s) ago; background optimisation can raise drain for a few days")

    # --- network ---------------------------------------------------------
    net = ev.get("network") or {}
    signal = net.get("signal")
    on_wifi = net.get("wifi_connected")
    if signal == "weak" and not on_wifi:
        _add(scores, "WEAK_SIGNAL", 3, "observation", "User reports weak cellular signal while on mobile data")
        if standby_high:
            _add(scores, "WEAK_SIGNAL", 2, "observation", "Standby drain is elevated while on weak cellular signal")
    elif signal == "weak" and on_wifi:
        _add(scores, "WEAK_SIGNAL", 1, "hypothesis", "Weak cellular signal; the modem still stays registered on cellular even on Wi-Fi")
    if net.get("mode") == "5G":
        pts = 1
        if signal in ("weak", "fluctuating") or net.get("switching"):
            pts += 2
        if "5g" in symptoms:
            pts += 1
        _add(scores, "NETWORK_5G", pts, "observation" if pts >= 3 else "hypothesis", "Phone uses 5G; Samsung notes 5G can use more power and suggests LTE in weak 5G areas [S9]")
    if net.get("hotspot") or net.get("bluetooth_devices_connected"):
        _add(scores, "CONNECTIVITY_EXTRAS", 2, "observation", "Hotspot or Bluetooth accessories in use during the drain window")

    # --- display ---------------------------------------------------------
    disp = ev.get("display") or {}
    screen_top = any(c.get("type") == "screen" and c.get("pct", 0) >= 30 for c in consumers)
    if active_high or "rapid_screen_on" in symptoms:
        if disp.get("brightness") in ("high", "max") and not disp.get("auto_brightness", False):
            _add(scores, "DISPLAY", 2, "observation", "Manual high brightness during screen use")
        if screen_top:
            _add(scores, "DISPLAY", 1, "observation", "Screen is a top battery consumer")
    if (disp.get("timeout_s") or 0) >= 300:
        _add(scores, "DISPLAY", 1, "observation", f"Screen timeout is {disp['timeout_s']} s")
    if disp.get("aod") and dev["aod_supported"] and standby_high:
        _add(scores, "DISPLAY", 1, "hypothesis", "Always On Display is on while standby drain is elevated (M15 5G)")

    # --- location / sync -------------------------------------------------
    if (ev.get("apps_with_location_always") or 0) >= 1 and standby_high:
        _add(scores, "LOCATION_SYNC", 1, "hypothesis", f"{ev['apps_with_location_always']} app(s) allowed location all the time")
    if ev.get("sync_heavy"):
        _add(scores, "LOCATION_SYNC", 1, "hypothesis", "Many accounts or frequent sync reported")

    # --- battery health --------------------------------------------------
    h = ev.get("health") or {}
    status = (h.get("members_status") or "").lower()
    if status == "bad":
        _add(scores, "BATTERY_DEGRADATION", 5, "observation", "Samsung Members battery status: Bad")
    elif status == "weak":
        _add(scores, "BATTERY_DEGRADATION", 3, "observation", "Samsung Members battery status: Weak")
    elif status == "normal":
        _add(scores, "BATTERY_DEGRADATION", -2, "observation", "Samsung Members battery status: Normal")
    if (h.get("shutdown_above_pct") or 0) >= 10:
        _add(scores, "BATTERY_DEGRADATION", 3, "observation", f"Unexpected shutdown at {h['shutdown_above_pct']}% remaining")
    if h.get("pct_jumps"):
        _add(scores, "BATTERY_DEGRADATION", 2, "observation", "Battery percentage jumps or drops suddenly")
    if (h.get("age_months") or 0) >= 24:
        _add(scores, "BATTERY_DEGRADATION", 1, "hypothesis", f"Phone is {h['age_months']} months old")

    # --- charging --------------------------------------------------------
    ch = ev.get("charging") or {}
    if ch:
        w = ch.get("adapter_w")
        if ch.get("source") == "pc" or (w is not None and w < dev["max_wired_w"]):
            _add(scores, "CHARGER_UNDERPOWERED", 3, "observation", f"Charging source: {ch.get('source', 'adapter')} {w or '?'} W vs device maximum {dev['max_wired_w']} W")
        if ch.get("fast_charging_setting") is False:
            _add(scores, "FAST_CHARGING_OFF", 4, "observation", "Fast charging toggle is off")
        if ch.get("cable_damaged") or ch.get("port_debris") or ch.get("interruptions"):
            _add(scores, "CABLE_PORT", 3, "observation", "Cable damage, port debris or connect/disconnect interruptions reported")
        if ch.get("moisture_warning"):
            _add(scores, "MOISTURE", 4, "observation", "Moisture-detected warning shown")
        if ch.get("hot_while_charging") or ch.get("used_while_charging"):
            _add(scores, "THERMAL_CHARGING", 2, "observation", "Phone hot or in heavy use while charging")
        if ch.get("stops_at_pct") in (80, 85, 90, 95) or ch.get("protect_battery_on"):
            _add(scores, "CHARGE_LIMIT", 4, "observation", f"Charging stops at {ch.get('stops_at_pct', 'a limit')}% - consistent with Battery protection")

    # --- nothing abnormal measured --------------------------------------
    measured = [c for c in (standby_cls, active_cls) if c]
    if measured and all(c == "expected" for c in measured) and not any(
        k in scores for k in ("SAFETY_STOP", "BATTERY_DEGRADATION")
    ):
        _add(scores, "WITHIN_EXPECTED", 3, "observation", "All measured rates fall in the skill's expected range")

    # --- elevated but unexplained --------------------------------------
    strong = [k for k, v in scores.items() if v["points"] >= 3]
    if (standby_high or active_high) and not strong:
        _add(scores, "UNEXPLAINED_DRAIN", 2, "observation", "Measured drain is elevated but no evidence points to a specific cause")

    # --- missing evidence -------------------------------------------------
    have = {
        "active_measurement": bool(ev.get("active_measurement")),
        "standby_measurement": bool(ev.get("standby_measurement")),
        "top_consumers": bool(consumers),
        "display": bool(disp),
        "network": bool(net),
        "recent_install": bool(recent.get("name")),
        "charging": bool(ch),
        "health": bool(h.get("members_status")),
    }
    needed: list[str] = []
    for s in symptoms:
        for item in REQUIRED_EVIDENCE.get(s, []):
            if not have.get(item) and item not in needed:
                needed.append(item)
    if not symptoms:
        needed.append("symptom_description")

    ranked = sorted(
        ({"cause": k, **v} for k, v in scores.items() if v["points"] > 0),
        key=lambda e: (-e["points"], list(CAUSES).index(e["cause"])),
    )
    for e in ranked:
        e["title"], e["module"] = CAUSES[e["cause"]]
        e["confidence"] = "high" if e["points"] >= 5 and e["observations"] else "medium" if e["points"] >= 3 else "low"
        e["interventions"] = INTERVENTIONS[e["cause"]]

    safety_stop = bool(ranked) and ranked[0]["cause"] == "SAFETY_STOP"
    conclusion_allowed = safety_stop or (not needed and bool(ranked))
    recommend = []
    if conclusion_allowed and ranked:
        already_done = {"INT-HEALTH-01"} if status else set()  # Members check result already supplied
        recommend = [i for i in ranked[0]["interventions"] if i not in already_done][:2]
    return {
        "ok": True,
        "device": dev_key,
        "measurements": {"standby": standby, "active": active},
        "ranked_causes": ranked[:5],
        "missing_evidence": [{"item": i, "ask": EVIDENCE_PROMPTS.get(i, "Describe the battery problem in your own words.")} for i in needed],
        "conclusion_allowed": conclusion_allowed,
        "recommended_interventions": recommend,
        "rule": "If missing_evidence is not empty, ask for it before naming a cause (except SAFETY_STOP). Recommend at most two changes, then re-measure.",
    }


# ---------------------------------------------------------------------------
# compare
# ---------------------------------------------------------------------------
CONDITION_KEYS = ["network_mode", "wifi_connected", "signal", "location", "workload", "temperature"]


def compare(before: dict, after: dict) -> dict:
    if before.get("device") != after.get("device"):
        return _err("before and after must be the same device")
    if before.get("kind") != after.get("kind"):
        return {"ok": True, "verdict": "not_comparable", "mismatches": ["kind: measurement types differ"]}
    rb, ra = rate(before), rate(after)
    if not rb.get("ok") or not ra.get("ok"):
        return _err(f"invalid measurement: before={rb.get('error')} after={ra.get('error')}")
    mism = []
    cb, ca = before.get("conditions", {}) or {}, after.get("conditions", {}) or {}
    allowed = set(after.get("intervention_changes", []) or [])
    for k in CONDITION_KEYS:
        if k in allowed:
            continue
        if k in cb or k in ca:
            if cb.get(k) != ca.get(k):
                mism.append(f"{k}: before={cb.get(k)!r} after={ca.get(k)!r}")
    hb, ha = rb["hours"], ra["hours"]
    if not (0.5 <= ha / hb <= 2.0):
        mism.append(f"duration: {hb} h vs {ha} h (more than 2x apart)")
    if before.get("kind") == "charging" and abs(float(before["start_pct"]) - float(after["start_pct"])) > 10:
        mism.append("charging start % differs by more than 10 points")
    if before.get("intervention_count", 1) > 2 or after.get("changes_since_before", 1) > 2:
        mism.append("more than two changes were made between runs; cause cannot be attributed")
    if mism:
        return {"ok": True, "verdict": "not_comparable", "mismatches": mism, "before": rb, "after": ra,
                "advice": "Repeat the after-measurement under the same conditions as the before-measurement."}

    if before["kind"] == "charging":
        vb, va = rb["charge_rate_pct_per_min"], ra["charge_rate_pct_per_min"]
        ub, ua = rb["uncertainty_pct_per_min"], ra["uncertainty_pct_per_min"]
        delta = va - vb  # higher is better
        better_is = "higher"
    else:
        vb, va = rb["rate_pct_per_h"], ra["rate_pct_per_h"]
        ub, ua = rb["uncertainty_pct_per_h"], ra["uncertainty_pct_per_h"]
        delta = vb - va  # lower drain is better
        better_is = "lower"
    unc = math.sqrt(ub ** 2 + ua ** 2)
    rel = delta / vb if vb else 0.0
    insufficient = rb.get("classification") == "insufficient_data" or ra.get("classification") == "insufficient_data"
    if insufficient:
        verdict = "inconclusive_insufficient_data"
    elif delta > unc and before["kind"] != "charging" and ra.get("classification") == "expected" and rb.get("classification") in ("elevated", "abnormal"):
        verdict = "resolved"
    elif delta > unc and rel >= 0.20:
        verdict = "improved"
    elif delta < -unc:
        verdict = "worse"
    else:
        verdict = "no_measurable_change"
    return {
        "ok": True,
        "verdict": verdict,
        "before_value": vb,
        "after_value": va,
        "better_is": better_is,
        "improvement": round(delta, 3),
        "relative_improvement_pct": round(rel * 100, 1),
        "combined_uncertainty": round(unc, 3),
        "before": rb,
        "after": ra,
        "next_step": {
            "resolved": "Keep the change. Re-check after a week of normal use.",
            "improved": "Keep the change; if still elevated, move to the next ranked cause.",
            "no_measurable_change": "Revert the change if it has a cost, then test the next ranked cause.",
            "worse": "Revert the change, confirm conditions were comparable, then re-assess.",
            "inconclusive_insufficient_data": "Measure for longer (larger % change) before deciding.",
        }[verdict],
    }


# ---------------------------------------------------------------------------
def _load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd = argv[1]
    if cmd == "identify" and len(argv) == 3:
        res = identify(argv[2])
    elif cmd == "rate" and len(argv) == 3:
        res = rate(_load(argv[2]))
    elif cmd == "rank" and len(argv) == 3:
        res = rank(_load(argv[2]))
    elif cmd == "compare" and len(argv) == 4:
        res = compare(_load(argv[2]), _load(argv[3]))
    else:
        print(__doc__, file=sys.stderr)
        return 2
    print(json.dumps(res, indent=2))
    return 0 if res.get("ok", False) or res.get("supported") is False else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
