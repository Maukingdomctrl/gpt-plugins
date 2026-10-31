# Diagnostic test scenarios

Two layers of tests:

1. **Engine tests (automated):** `python3 tests/test_battery_diag.py -v` runs the deterministic engine against `tests/fixtures/scenarios.json` (16 scenarios = 8 per device) plus guard cases. `python3 tests/validate_skill.py` checks the skill files.
2. **Conversation tests (behavioural):** give the assistant (with this skill loaded) the **opening message** below, then the **evidence reply**, and grade each turn with the rubric. These need a model run; record results in the table at the end, and only mark tests that were actually run.

## Universal rubric (applies to every scenario)
| Code | Turn | Pass criterion |
|---|---|---|
| R1 | 1 | Confirms or asks for the **model number** (and One UI/Android version if missing) |
| R2 | 1 | Asks for the evidence the symptom needs; **does not name a cause as fact** before evidence |
| R3 | 1 | No generic tips list before evidence |
| R4 | all | Never claims to have inspected/scanned the phone; no invented numbers |
| R5 | 2 | Labels observed vs calculated vs hypothesis; shows arithmetic for rates |
| R6 | 2 | Ranked causes consistent with the engine's expected top cause |
| R7 | 2 | ≤2 changes; each has device, path (+ verification/version note), what it does, why, disadvantages, how to reverse |
| R8 | 2 | Device separation: no M15-only advice (AOD, dark mode saving, 25 W) to A14 5G users; no A14 specs to M15 users |
| R9 | 2 | Asks for a repeat measurement under comparable conditions |
| R10 | all | No factory reset, calibration, optimizer/cleaner apps, disabling system services, or unjustified battery replacement |
| R11 | 3 | Verdict matches the engine (`compare`) and next step follows `workflows/verification.md` |

---

## Galaxy M15 5G

### M15-1 Rapid drain during screen use
- **Opening:** "My Galaxy M15 5G (SM-M156B/DSN, One UI 8.0, Android 16) dies quickly when I'm using it."
- **Expected turn 1:** asks for start/end %, screen-on time, workload, battery usage screenshot, brightness/timeout/Motion smoothness, network. No cause yet.
- **Evidence reply:** "100 % at 9:00, 62 % at 12:00, screen-on 2 h 30 min, Instagram and browsing on home Wi-Fi. Battery screen: Screen 40 %, Instagram 25 %. Brightness manual near max, timeout 10 minutes, Motion smoothness Adaptive."
- **Expected analysis:** 38 points / 2.5 h = 15.2 %/screen-on-h ≈ 912 mA-eq (6000 mAh) → abnormal for light use (heuristic). Top cause DISPLAY; Instagram use is mostly active (expected).
- **Expected changes:** INT-DISP-01 (Adaptive brightness) + INT-DISP-02 (timeout 30 s), M15 5G paths, trade-offs, reversal.
- **Re-test:** same 3 h light use, same Wi-Fi. After: 100 → 74 % with 2 h 30 min screen-on → 10.4 %/h → **improved** (still elevated; next: Motion smoothness Standard as round 2).

### M15-2 Excessive overnight drain
- **Opening:** "My M15 5G loses a lot overnight." (model SM-M156B, One UI 7)
- **Expected turn 1:** bedtime/wake % and times (not charging), morning battery usage screenshot before charging, network overnight, AOD on/off.
- **Evidence:** "85 % at 23:00, 70 % at 07:00. Screenshot: CallerID App 30 %, Android System 22 %. Home Wi-Fi, LTE, good signal. AOD always on."
- **Expected:** 15 / 8 = 1.875 %/h ≈ 112 mA-eq → abnormal. Top APP_BACKGROUND (CallerID App), secondary SYSTEM_PROCESS (do not disable), AOD as a low-weight hypothesis.
- **Changes:** INT-APP-02 or INT-APP-01 for CallerID App (warn about missed caller-ID if deep-slept). Not both AOD + app in round 1 unless justified.
- **Re-test:** same night conditions → 85 → 79 % → 0.75 %/h → **resolved**.

### M15-3 Drain after installing an app
- **Opening:** "Since I installed a new photo app a few days ago my M15 5G battery is worse."
- **Expected turn 1:** app name and date, battery usage screenshot, an overnight standby measurement.
- **Evidence:** "PhotoFilter X, 3 days ago. Overnight 90 → 75 % in 7 h. It shows 28 % in battery usage, mostly background."
- **Expected:** 2.14 %/h ≈ 129 mA-eq → abnormal; RECENT_INSTALL (high), APP_BACKGROUND.
- **Changes:** update the app; if still high, uninstall or deep-sleep for one test period (INT-APP-03 / INT-APP-01).
- **Re-test:** 90 → 85 % in 7 h → **resolved**.

### M15-4 Drain while using 5G
- **Opening:** "My M15 5G drains more since I started using 5G."
- **Evidence:** "Overnight 80 → 66 % in 8 h on mobile data; the icon keeps switching between 5G and LTE; no Wi-Fi at home. Battery screen: nothing above 15 %."
- **Expected:** 1.75 %/h ≈ 105 mA-eq → abnormal. NETWORK_5G (Samsung: 5G can use 4G and 5G together [S9]). Weak-signal check.
- **Change:** INT-NET-02 (Network mode → LTE/3G/2G), with speed trade-off and reversal; per-SIM note.
- **Re-test:** 80 → 72 % same conditions with LTE → 1.0 %/h → **improved**; user decides whether to keep LTE.

### M15-5 Drain with weak cellular signal
- **Opening:** "At my office (basement) my M15 5G drains while sitting on the desk."
- **Evidence:** "6 h workday idle 90 → 78 %, screen on about 10 min, LTE 1 bar, no Wi-Fi connected."
- **Expected:** 2.0 %/h ≈ 120 mA-eq → abnormal; WEAK_SIGNAL (high).
- **Change:** INT-NET-01 (connect to office Wi-Fi) — explain cellular still registered.
- **Re-test:** same day pattern on Wi-Fi: 90 → 83 % → **improved**.

### M15-6 Unexpected consumption while idle (after update)
- **Opening:** "Yesterday I updated my M15 5G and now it drains even when I'm not using it."
- **Evidence:** "70 → 61 % in 4.5 h idle on Wi-Fi. Google Play services 26 %."
- **Expected:** 2.0 %/h → abnormal; POST_UPDATE_SETTLING (hypothesis) and SYSTEM_PROCESS. Must **not** suggest disabling Google Play services.
- **Change:** INT-WAIT-01 (2–3 days, apps updated, one restart), then re-measure.
- **Re-test:** 3 days later 70 → 66 % → **improved**; if still elevated, INT-SYS-01/TEST-SAFE.

### M15-7 Slow charging
- **Opening:** "My M15 5G takes forever to charge."
- **Expected turn 1:** adapter wattage/brand, cable, on-screen charging message, timed run from ~30 %, heat, use while charging, Fast charging toggle.
- **Evidence:** "15 W adapter from my old phone, I watch videos while charging. 30 → 48 % in 30 min. Fast charging is on."
- **Expected:** CHARGER_UNDERPOWERED (15 W vs 25 W max; adapter sold separately), THERMAL_CHARGING secondary. Don't quote a 0–100 time.
- **Change:** INT-CHG-01 (25 W Samsung adapter) and idle while charging.
- **Re-test:** 30 → 58 % in 30 min → **improved**.

### M15-8 Battery degradation symptoms
- **Opening:** "My M15 5G sometimes shuts off at 18 % and the percentage jumps."
- **Expected turn 1:** Samsung Members battery status, age, conditions of shutdowns, a standby measurement; safety questions (swelling).
- **Evidence:** "Members says Weak. 20 months old. 60 → 52 % overnight. No swelling."
- **Expected:** BATTERY_DEGRADATION (high, evidence-based). INT-HEALTH-02 service-centre inspection; no calibration; back up first.

---

## Galaxy A14 5G

### A14-1 Rapid drain during screen use
- **Opening:** "My A14 5G (SM-A146B) dies so fast when I use it."
- **Expected turn 1:** One UI version, measurement, screenshot, display settings, network. Must not mention AOD.
- **Evidence:** "90 → 50 % in 3 h, screen-on 2 h 40 min, browsing on Wi-Fi. Facebook 35 % (mostly background — I barely open it). Auto brightness on, timeout 30 s."
- **Expected:** 40 / 2.667 = 15 %/h ≈ 750 mA-eq (5000 mAh) → elevated; APP_BACKGROUND (Facebook).
- **Change:** INT-APP-02 or INT-APP-01 for Facebook (A14 5G One UI Core: confirm labels via Settings search).
- **Re-test:** 90 → 60 % same pattern → 11.25 %/h ≈ 562 mA-eq → **resolved**.

### A14-2 Excessive overnight drain
- **Opening:** "My A14 5G loses 18 % overnight."
- **Expected turn 1:** times, screenshot, network.
- **Evidence:** "80 % at 23:00 → 62 % at 07:00, 5G icon, 1 bar, no Wi-Fi. Nothing big in battery usage."
- **Expected:** 2.25 %/h ≈ 112 mA-eq → abnormal; WEAK_SIGNAL (high), NETWORK_5G (medium). Must **not** suggest AOD (A14 5G has none).
- **Change:** INT-NET-02 (LTE) since no Wi-Fi available.
- **Re-test:** LTE: 80 → 70 % → **improved**.

### A14-3 Drain after installing an app
- **Opening:** "I installed GameHub 5 days ago and my A14 5G battery got worse."
- **Expected turn 1:** screenshot and an overnight measurement (app name and date already given).
- **Evidence:** "70 → 58 % overnight (8 h), GameHub 18 % background."
- **Expected:** RECENT_INSTALL (high). **Change:** update → deep sleep/uninstall for one test.
- **Re-test:** 70 → 64 % → **resolved**.

### A14-4 Drain while using 5G (normal result)
- **Opening:** "Does 5G drain my A14 5G? It feels worse."
- **Evidence:** "Overnight on 5G with good signal: 80 → 74 % in 8 h. YouTube 12 % (I watched videos)."
- **Expected:** 0.75 %/h ≈ 37.5 mA-eq → **within expected**. Must not invent a 5G fault; explain the heuristic; optional LTE comparison.
- **If the user tests LTE anyway:** 80 → 75 % → **no measurable change** (difference within uncertainty) → keep 5G if they want speed.

### A14-5 Drain with weak cellular signal
- **Opening:** "My A14 5G battery is bad where I live; signal is poor."
- **Expected turn 1:** network details (icon, bars, Wi-Fi), overnight measurement.
- **Evidence:** "85 → 65 % in 9 h, LTE 1 bar, no Wi-Fi."
- **Expected:** WEAK_SIGNAL (high). **Diagnostic:** TEST-AIRPLANE night (if the user can be unreachable) or INT-NET-02.
- **Re-test:** airplane night 85 → 80 % → network confirmed as the cause (verdict **resolved** for the test); discuss practical options (Wi-Fi calling only if the carrier supports it — [U]; don't promise).

### A14-6 Unexpected consumption while idle (unexplained)
- **Opening:** "My A14 5G drains when idle and I don't know why."
- **Evidence:** "80 → 64 % in 8 h on home Wi-Fi with good LTE. Chrome 9 %, Android System 11 %. Samsung Members says Normal. Phone is 30 months old."
- **Expected:** 2.0 %/h ≈ 100 mA-eq → elevated; no cause ≥3 points → UNEXPLAINED_DRAIN → TEST-AIRPLANE then TEST-SAFE, one per night. Must **not** blame battery age (Members Normal).
- **Re-test (Safe mode night):** 80 → 74 % → much lower → a downloaded app is implicated → Module E to find it.

### A14-7 Slow charging
- **Opening:** "My A14 5G charges slowly and sometimes stops and starts."
- **Evidence:** "Samsung 25 W adapter, cable is frayed, it disconnects when I move it. Fast charging on. 25 → 40 % in 30 min."
- **Expected:** CABLE_PORT. Must say the A14 5G charges at up to **15 W** even on a 25 W adapter. Port inspection without metal/liquid.
- **Re-test:** new cable 25 → 47 % in 30 min → **improved**.

### A14-8 Degradation suspected because of age
- **Opening:** "My A14 5G is almost 3 years old. Is the battery dying? Should I replace it?"
- **Expected turn 1:** Members battery status, shutdown history, standby measurement — not a replacement recommendation.
- **Evidence:** "Members says Normal, no shutdowns. 80 → 70 % overnight. WeatherLive 20 % background, 2 apps with location always."
- **Expected:** degradation **not supported**; APP_BACKGROUND (WeatherLive) + LOCATION_SYNC. No replacement advice.
- **Re-test:** 80 → 75 % → **resolved**.

---

## Guard scenarios (both devices)
| ID | Opening | Pass criterion |
|---|---|---|
| G1 | "My Galaxy A14 (SM-A145F) battery drains." | Identifies A14 **4G**, says out of scope, no device advice |
| G2 | "Galaxy S23 battery drains." | Out of scope |
| G3 | "My M15 5G back is bulging and it's hot." | SAFE-01 immediately; no other diagnostics |
| G4 | "Should I just factory reset my A14 5G?" | Declines as a first step; explains LAST-RESORT preconditions; offers diagnostics |
| G5 | "Which battery saver / cleaner app should I install?" | Declines; explains built-in options with trade-offs |
| G6 | "Should I calibrate my battery by draining to 0 %?" | Declines; no calibration |
| G7 | "A14 5G released in 2022, right?" | Corrects: announced January 2023 |
| G8 | User gives only "it drains fast" with no model | Asks for model number first |

---

## Results log
Fill only with runs that were actually executed. See the repository's PR description / README for the latest recorded results.

| Date | Runner | Layer | Scenarios | Result |
|---|---|---|---|---|
