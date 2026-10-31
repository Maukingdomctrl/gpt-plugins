# Module A — Battery consumption analysis

Covers screen-on consumption, screen-off consumption, app-wise usage, system processes and abnormal background activity. Entry point for "my battery drains fast".

## Evidence to request
1. Battery usage screen screenshot (newer: Settings > Battery > View details; older: Settings > Battery and device care > Battery) **[V S10]** showing the app list and percentages since last full charge, plus **Screen on time / Screen off time** where shown.
2. Battery % at start and end of a known period, and screen-on time in that period.
3. What the user did (light: messaging, social, browsing; moderate: video streaming, music + maps briefly; heavy: gaming, camera recording, navigation, hotspot, video calls).
4. Network (Wi-Fi or mobile data; 5G or LTE; signal bars).

## Reading the battery usage screen
- Percentages on that screen are **shares of the battery used**, not % of capacity. "App X 30 %" means 30 % of whatever was used since the last full charge. Convert only with the user's numbers: share × total drop.
- Check whether the app's usage is **foreground** or **background** if the screen shows it (tap the app). Heavy background use by an app the user barely opens is the strongest app signal.
- The list resets after charging; ask for the screenshot **before** the next charge.

## Decision tree
```
A1. Is the measurement valid? (not charging, ≥3 points drop, period known)
    no  → ask for a valid measurement (workflows/controlled-testing.md); stop.
A2. Split: is drain mostly while screen off?  (screen-off time large and % lost overnight/idle high)
    yes → go to Module B (standby-drain.md).
A3. Screen-on rate (Calculated) by workload:
    heavy workload → not classified; explain heavy loads are expected to drain fast; check heat (Module F).
    light/moderate → classify with heuristic bands (SKILL.md).
A4. Top consumer is an app with ≥15 % share?
    yes, and user rarely uses it / mostly background → APP_BACKGROUND (Module E).
    yes, and it's what the user was actively using → expected; display/network are the levers.
A5. Top consumer is a system item (Android System, Google Play services, Samsung services) ≥20 %?
    yes → SYSTEM_PROCESS: INT-SYS-01 then TEST-SAFE. Never disable it.
A6. Screen is the top consumer and brightness manual-high / long timeout?
    yes → DISPLAY (Module D).
A7. Weak signal or 5G during the period?
    yes → Module C.
A8. All rates expected? → WITHIN_EXPECTED; explain; no change needed.
A9. Rates elevated with no app/system/display/network signal?
    → ask for Samsung Members battery status (Module F) and run TEST-SAFE.
```

## Device-specific notes
- **M15 5G:** 6,000 mAh typical [V]. The same %/h is ~20 % more current than on the A14 5G; compare devices only by mA-equivalent, never by %/h. AMOLED: dark content lowers display power.
- **A14 5G:** 5,000 mAh typical [V]. LCD: power depends on brightness, not on dark content. Exynos 1330 (SM-A146B) and Dimensity 700 (SM-A146P) differ in efficiency, but no official comparative data exists. **Do not claim either chip "drains more".**

## Do not conclude
- That an app is "bad" from one day of data, or from usage that matches what the user actually did.
- That the phone is faulty because a lab claim (e.g. "up to 25 h video", "up to 2 days") was not reached; those use test profiles.
