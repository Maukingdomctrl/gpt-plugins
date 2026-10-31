# Module B — Standby drain

Overnight loss, idle consumption, background synchronisation, and wake-lock-related symptoms (where evidence exists).

## Evidence to request
1. Bedtime % and time; wake-up % and time; phone not charging; screen not used (or screen-on minutes if it was).
2. Network overnight: Wi-Fi connected? Mobile data on? 5G or LTE icon? Signal bars at the bedside.
3. Battery usage screenshot taken in the morning **before charging**.
4. Is Always On Display on? (**M15 5G only**.)
5. Anything connected: smartwatch, earbuds, hotspot.
6. Optional: `adb shell dumpsys batterystats` output (see `workflows/adb-evidence.md`) for wake-lock evidence.

## Calculation (show it)
Standby rate = (bedtime % − morning %) ÷ hours. mA-eq = rate ÷ 100 × typical mAh (M15 5G 6000, A14 5G 5000).
Example (A14 5G): 80 % → 68 % over 8 h = 1.5 %/h → 75 mA-eq → **elevated** (heuristic). M15 5G with the same 1.5 %/h → 90 mA-eq → also elevated.

Heuristic bands: ≤50 mA-eq expected, 50–100 elevated, >100 abnormal. Phones on weak cellular signal can be elevated with no fault; that is a network cause, not a defect.

## Decision tree
```
B1. Valid? (≥4 h, ideally ≥6 h; not charging; screen-on <5 % of window; ≥3 points drop)
    no → ask to repeat overnight properly.
B2. Classify standby rate.
    expected → WITHIN_EXPECTED for standby; if the complaint is daytime drain → Module A.
B3. Elevated/abnormal. Which signals are present?
    a) An app with large background share in the morning screenshot → Module E (INT-APP-01/02).
    b) Weak signal at bedside and on mobile data → Module C (INT-NET-01; TEST-AIRPLANE to confirm).
    c) 5G icon overnight with weak/fluctuating signal → Module C (INT-NET-02).
    d) AOD on (M15 5G) → INT-DISP-04 as a secondary change.
    e) Smartwatch/earbuds/hotspot connected → INT-NET-03 if not needed.
    f) Many accounts syncing (email, cloud photos) → INT-APP-05 for unneeded ones.
    g) Update within last 3 days → INT-WAIT-01 first.
B4. No signal found → TEST-AIRPLANE night, then TEST-SAFE night (one per night).
    Airplane much lower → network or network-using app.
    Safe mode much lower → a downloaded app (find it with Module E).
    Neither lower → Module F (battery health) and, if Members "Normal", service-centre software check.
```

## Wake locks
Without `adb` output, you cannot see wake locks. Do **not** claim a wake lock exists. You may say "symptoms are consistent with something keeping the phone awake (a hypothesis)". With `dumpsys batterystats` output, cite only what is in the text (e.g. a named wake lock with a duration), and quote it.

## Device-specific notes
- **M15 5G:** AOD available (AMOLED) [U for exact menu]; test it off for one night if on.
- **A14 5G:** no AOD; do not mention it.
