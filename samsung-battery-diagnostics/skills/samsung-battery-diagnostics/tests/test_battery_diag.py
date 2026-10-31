#!/usr/bin/env python3
"""Unit tests for scripts/battery_diag.py (standard library only).

Run:  python3 tests/test_battery_diag.py -v
"""
import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import battery_diag as bd  # noqa: E402

with open(os.path.join(HERE, "fixtures", "scenarios.json"), encoding="utf-8") as fh:
    SCENARIOS = json.load(fh)


class TestIdentify(unittest.TestCase):
    def test_m15_codes(self):
        for code in ("SM-M156B", "SM-M156B/DSN", "sm-m156bzavxid", "M156B"):
            r = bd.identify(code)
            self.assertTrue(r["supported"], code)
            self.assertEqual(r["device"], "galaxy-m15-5g")
            self.assertIn("6100+", r["chipset"])

    def test_a14_5g_variants(self):
        self.assertIn("Exynos 1330", bd.identify("SM-A146B/DS")["chipset"])
        self.assertIn("Dimensity 700", bd.identify("SM-A146P")["chipset"])
        self.assertIn("Dimensity 700", bd.identify("SM-A146U")["chipset"])
        self.assertIn("reported", bd.identify("SM-A146U")["chipset_basis"])
        for code in ("SM-A146U1", "SM-A146W", "SM-A146M", "SM-S146VL"):
            r = bd.identify(code)
            self.assertEqual(r["device"], "galaxy-a14-5g", code)
            self.assertTrue(r["chipset"].startswith("unverified"), code)

    def test_lookalikes_rejected(self):
        for code, word in (("SM-A145F", "4G"), ("SM-M146B", "M14"), ("SM-E156B", "F15"),
                           ("SM-A156B", "A15"), ("SM-E146B", "F14"), ("SM-M156S", "not verified")):
            r = bd.identify(code)
            self.assertFalse(r["supported"], code)
            self.assertIn(word, r["reason"], code)

    def test_other_phone_rejected(self):
        self.assertFalse(bd.identify("SM-S911B")["supported"])
        self.assertFalse(bd.identify("")["ok"])


class TestRate(unittest.TestCase):
    def test_standby_bands_scale_with_capacity(self):
        m = {"kind": "standby", "start_pct": 80, "end_pct": 68, "duration_h": 8}
        a14 = bd.rate(dict(m, device="galaxy-a14-5g"))
        m15 = bd.rate(dict(m, device="galaxy-m15-5g"))
        self.assertAlmostEqual(a14["rate_pct_per_h"], 1.5)
        self.assertEqual(a14["mA_equivalent"], 75.0)
        self.assertEqual(m15["mA_equivalent"], 90.0)
        self.assertEqual(a14["classification"], "elevated")
        self.assertEqual(m15["classification"], "elevated")

    def test_uncertainty(self):
        r = bd.rate({"device": "galaxy-a14-5g", "kind": "standby", "start_pct": 80, "end_pct": 72, "duration_h": 8})
        self.assertAlmostEqual(r["uncertainty_pct_per_h"], 0.125)

    def test_small_drop_is_insufficient(self):
        r = bd.rate({"device": "galaxy-m15-5g", "kind": "standby", "start_pct": 80, "end_pct": 78, "duration_h": 8})
        self.assertEqual(r["classification"], "insufficient_data")

    def test_charging_inside_window_rejected(self):
        r = bd.rate({"device": "galaxy-m15-5g", "kind": "standby", "start_pct": 50, "end_pct": 60, "duration_h": 8})
        self.assertFalse(r["ok"])

    def test_contaminated_standby_warns(self):
        r = bd.rate({"device": "galaxy-m15-5g", "kind": "standby", "start_pct": 80, "end_pct": 70, "duration_h": 6, "screen_on_min": 60})
        self.assertTrue(any("5%" in w for w in r["warnings"]))

    def test_heavy_workload_not_classified(self):
        r = bd.rate({"device": "galaxy-a14-5g", "kind": "active", "start_pct": 100, "end_pct": 60, "duration_h": 2, "screen_on_min": 110, "workload": "heavy"})
        self.assertEqual(r["classification"], "not_classified")

    def test_mixed_needs_baseline(self):
        r = bd.rate({"device": "galaxy-a14-5g", "kind": "mixed", "start_pct": 100, "end_pct": 40, "duration_h": 14, "screen_on_min": 300, "workload": "light"})
        self.assertEqual(r["classification"], "not_classified")
        self.assertTrue(r["missing"])

    def test_mixed_split(self):
        r = bd.rate({"device": "galaxy-a14-5g", "kind": "mixed", "start_pct": 100, "end_pct": 40, "duration_h": 14,
                     "screen_on_min": 300, "workload": "light", "standby_rate_pct_per_h": 1.0})
        # off-time 9 h * 1 %/h = 9 points; screen-on drop 51 over 5 h = 10.2 %/h
        self.assertAlmostEqual(r["rate_pct_per_h"], 10.2)
        self.assertEqual(r["classification"], "expected")

    def test_iso_times(self):
        r = bd.rate({"device": "galaxy-m15-5g", "kind": "standby", "start_pct": 90, "end_pct": 84,
                     "start_time": "2026-11-01T23:00", "end_time": "2026-11-02T07:00"})
        self.assertEqual(r["hours"], 8.0)

    def test_unknown_device_rejected(self):
        self.assertFalse(bd.rate({"device": "galaxy-s24", "kind": "standby", "start_pct": 90, "end_pct": 80, "duration_h": 8})["ok"])


class TestScenarios(unittest.TestCase):
    """The 16 device-specific scenarios from tests/diagnostic-tests.md."""

    def test_each_device_has_all_eight_scenarios(self):
        for dev in ("M15", "A14"):
            ids = [s["id"] for s in SCENARIOS if s["id"].startswith(dev)]
            self.assertEqual(len(ids), 8, dev)

    def test_incomplete_evidence_blocks_conclusion(self):
        for s in SCENARIOS:
            with self.subTest(s["id"]):
                r = bd.rank(s["incomplete_evidence"])
                self.assertTrue(r["ok"])
                self.assertFalse(r["conclusion_allowed"], "must ask for evidence first")
                self.assertEqual(r["recommended_interventions"], [])
                got = [m["item"] for m in r["missing_evidence"]]
                self.assertEqual(sorted(got), sorted(s["expected_missing"]))

    def test_full_evidence_ranks_expected_cause(self):
        for s in SCENARIOS:
            with self.subTest(s["id"]):
                r = bd.rank(s["evidence"])
                self.assertTrue(r["conclusion_allowed"], r["missing_evidence"])
                self.assertEqual(r["ranked_causes"][0]["cause"], s["expected_top"], r["ranked_causes"])
                self.assertEqual(r["recommended_interventions"], s["expected_interventions"])
                self.assertLessEqual(len(r["recommended_interventions"]), 2)

    def test_before_after_verdicts(self):
        for s in SCENARIOS:
            if not s["before"]:
                continue
            with self.subTest(s["id"]):
                r = bd.compare(s["before"], s["after"])
                self.assertEqual(r["verdict"], s["expected_verdict"], r)

    def test_device_separation_in_interventions(self):
        """AOD/dark-mode interventions must never be produced for the A14 5G."""
        for s in SCENARIOS:
            if s["device"] != "galaxy-a14-5g":
                continue
            r = bd.rank(s["evidence"])
            for c in r["ranked_causes"]:
                for i in c["interventions"]:
                    self.assertNotIn(i, ("INT-DISP-04", "INT-DISP-05"))

    def test_aod_ignored_on_a14(self):
        ev = {"device": "galaxy-a14-5g", "symptoms": ["overnight"],
              "standby_measurement": {"kind": "standby", "start_pct": 80, "end_pct": 64, "duration_h": 8},
              "top_consumers": [{"name": "X", "type": "app", "pct": 5}],
              "network": {"mode": "LTE", "signal": "good", "wifi_connected": True},
              "display": {"aod": True}}
        r = bd.rank(ev)
        self.assertNotIn("DISPLAY", [c["cause"] for c in r["ranked_causes"]])


class TestSafetyAndGuards(unittest.TestCase):
    def test_swelling_overrides(self):
        r = bd.rank({"device": "galaxy-a14-5g", "symptoms": ["degradation"], "safety": {"swelling": True}})
        self.assertEqual(r["ranked_causes"][0]["cause"], "SAFETY_STOP")
        self.assertTrue(r["conclusion_allowed"])
        self.assertEqual(r["recommended_interventions"], ["SAFE-01"])

    def test_age_alone_never_degradation(self):
        r = bd.rank({"device": "galaxy-a14-5g", "symptoms": ["degradation"],
                     "standby_measurement": {"kind": "standby", "start_pct": 80, "end_pct": 74, "duration_h": 8},
                     "health": {"members_status": "normal", "age_months": 40}})
        self.assertNotIn("BATTERY_DEGRADATION", [c["cause"] for c in r["ranked_causes"]])

    def test_a14_with_25w_adapter_not_underpowered(self):
        r = bd.rank({"device": "galaxy-a14-5g", "symptoms": ["slow_charging"],
                     "charging": {"source": "adapter", "adapter_w": 25, "fast_charging_setting": True}})
        self.assertNotIn("CHARGER_UNDERPOWERED", [c["cause"] for c in r["ranked_causes"]])

    def test_m15_with_15w_adapter_is_underpowered(self):
        r = bd.rank({"device": "galaxy-m15-5g", "symptoms": ["slow_charging"],
                     "charging": {"source": "adapter", "adapter_w": 15}})
        self.assertEqual(r["ranked_causes"][0]["cause"], "CHARGER_UNDERPOWERED")

    def test_unidentified_device_refused(self):
        self.assertFalse(bd.rank({"symptoms": ["overnight"]})["ok"])

    def test_no_symptoms_asks_for_description(self):
        r = bd.rank({"device": "galaxy-m15-5g"})
        self.assertIn("symptom_description", [m["item"] for m in r["missing_evidence"]])
        self.assertFalse(r["conclusion_allowed"])


class TestCompareGuards(unittest.TestCase):
    base = {"device": "galaxy-m15-5g", "kind": "standby", "start_pct": 80, "end_pct": 68, "duration_h": 8,
            "conditions": {"network_mode": "LTE", "wifi_connected": True, "signal": "good", "location": "home"}}

    def test_condition_mismatch_not_comparable(self):
        after = dict(self.base, end_pct=74, conditions=dict(self.base["conditions"], signal="weak"))
        self.assertEqual(bd.compare(self.base, after)["verdict"], "not_comparable")

    def test_declared_change_allowed(self):
        after = dict(self.base, end_pct=74, conditions=dict(self.base["conditions"], network_mode="5G"),
                     intervention_changes=["network_mode"])
        self.assertNotEqual(bd.compare(self.base, after)["verdict"], "not_comparable")

    def test_duration_mismatch(self):
        after = dict(self.base, duration_h=3, end_pct=75)
        self.assertEqual(bd.compare(self.base, after)["verdict"], "not_comparable")

    def test_too_many_changes(self):
        after = dict(self.base, end_pct=76, changes_since_before=4)
        self.assertEqual(bd.compare(self.base, after)["verdict"], "not_comparable")

    def test_worse(self):
        after = dict(self.base, end_pct=58)
        self.assertEqual(bd.compare(self.base, after)["verdict"], "worse")

    def test_insufficient(self):
        b = dict(self.base, end_pct=78)
        a = dict(self.base, end_pct=79)
        self.assertEqual(bd.compare(b, a)["verdict"], "inconclusive_insufficient_data")

    def test_different_devices_rejected(self):
        after = dict(self.base, device="galaxy-a14-5g")
        self.assertFalse(bd.compare(self.base, after)["ok"])

    def test_charging_start_mismatch(self):
        b = {"device": "galaxy-a14-5g", "kind": "charging", "start_pct": 20, "end_pct": 40, "duration_h": 0.5}
        a = {"device": "galaxy-a14-5g", "kind": "charging", "start_pct": 60, "end_pct": 75, "duration_h": 0.5}
        self.assertEqual(bd.compare(b, a)["verdict"], "not_comparable")


if __name__ == "__main__":
    unittest.main()
