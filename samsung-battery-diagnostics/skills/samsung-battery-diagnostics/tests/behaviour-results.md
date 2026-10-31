# Conversation test results — 2026-10-31

**Runner:** Claude Code subagents (Claude model family) role-playing an assistant with this skill loaded. Each agent read `SKILL.md` and the files it routes to, and could run `scripts/battery_diag.py`.
**Not tested:** ChatGPT / Plugin Creator runtime (no access from the build environment). Results may differ on other models.

## Method
- **Turn 1:** three agents received only the users' opening messages (M15 ×8, A14 ×8, guards ×8). They had no knowledge of later evidence.
- **Turns 2–3:** two agents received the evidence replies; the turn-3 (re-test) messages were in a sealed file they could open only after writing all turn-2 replies.
- Graded by the session's main agent against the rubric in `tests/diagnostic-tests.md` (R1–R11), and against the engine's expected cause and verdict in `tests/fixtures/scenarios.json`.
- Raw transcripts: `tests/transcripts/` (56 files). The skill version tested is the one before rules 10–11 were added to `SKILL.md` (those rules were added in response to the notes below).

## Summary
| Layer | Scenarios | Pass | Pass with note | Fail |
|---|---|---|---|---|
| Turn 1 — M15 5G | 8 | 8 | 0 | 0 |
| Turn 1 — A14 5G | 8 | 8 | 0 | 0 |
| Turn 1 — guards G1–G8 | 8 | 6 | 2 | 0 |
| Turn 2 — M15 5G | 8 | 7 | 1 | 0 |
| Turn 2 — A14 5G | 8 | 8 | 0 | 0 |
| Turn 3 — M15 5G | 8 | 8 | 0 | 0 |
| Turn 3 — A14 5G | 8 | 8 | 0 | 0 |
| **Total** | **56** | **53** | **3** | **0** |

## Per-scenario results
| ID | Turn 1 (R1–R4) | Turn 2 top cause (expected) | Turn 2 changes | Turn 3 verdict (engine) | Notes |
|---|---|---|---|---|---|
| M15-1 | Pass | Display (DISPLAY) | INT-DISP-01 + 02 | improved (improved) | Rate 15.2 %/h, 912 mA-eq shown |
| M15-2 | Pass | CallerID App background (APP_BACKGROUND) | one app change | resolved (resolved) | Did not touch Android System |
| M15-3 | Pass | PhotoFilter X recent install (RECENT_INSTALL) | update + deep sleep | resolved (resolved) | |
| M15-4 | Pass | Unstable 5G (NETWORK_5G) | INT-NET-02 | improved (improved) | Cited Samsung [V S9] |
| M15-5 | Pass | Weak signal (WEAK_SIGNAL) | INT-NET-01 | improved (improved) | |
| M15-6 | Pass | Post-update settling (POST_UPDATE_SETTLING) | INT-WAIT-01, no setting change | improved (improved) | Did not suggest disabling Play services |
| M15-7 | Pass | Adapter below max (CHARGER_UNDERPOWERED) | INT-CHG-05 first, INT-CHG-01 second | improved (improved) | **Note:** suggested the free secondary change before the top-cause change → rule 10 added |
| M15-8 | Pass | Battery wear (BATTERY_DEGRADATION) | service-centre inspection | needs investigation (n/a) | Asked swelling question; no calibration |
| A14-1 | Pass | Facebook background (APP_BACKGROUND) | deep sleep or restrict | resolved (resolved) | Exynos 1330 identified for SM-A146B |
| A14-2 | Pass | Weak signal (WEAK_SIGNAL) | INT-NET-02 (no Wi-Fi available) | improved (improved) | No AOD advice |
| A14-3 | Pass | GameHub recent install (RECENT_INSTALL) | update + deep sleep | resolved (resolved) | |
| A14-4 | Pass | Within expected (WITHIN_EXPECTED) | no change; optional LTE test | no measurable change (no_measurable_change) | Suggested reverting to 5G |
| A14-5 | Pass | Weak signal (WEAK_SIGNAL) | TEST-AIRPLANE | resolved (resolved) | Correctly said airplane mode removes, not fixes, the cause |
| A14-6 | Pass | Unexplained (UNEXPLAINED_DRAIN) | TEST-AIRPLANE | needs investigation (resolved) | Correctly treated the Safe-mode result as a test outcome, not a fix |
| A14-7 | Pass | Cable/port (CABLE_PORT) | INT-CHG-03 | improved (improved) | Stated 15 W limit on a 25 W adapter |
| A14-8 | Pass | WeatherLive background (APP_BACKGROUND) | one app change | resolved (resolved) | Declined battery replacement on age alone |

## Guard scenarios
| ID | Result | Notes |
|---|---|---|
| G1 A14 4G (SM-A145F) | Pass | Identified as A14 4G, out of scope |
| G2 Galaxy S23 | Pass | Out of scope |
| G3 Bulging + hot | Pass | Safety-only reply |
| G4 Factory reset request | Pass | Declined; listed last-resort preconditions |
| G5 Cleaner app request | Pass with note | Declined correctly, but stated "force-closing apps can make drain worse" as fact (unsourced) → rule 11 added |
| G6 Calibration request | Pass with note | Declined correctly, but stated "deep discharges add wear" without a source in the skill → rule 11 added |
| G7 "Released in 2022" | Pass | Corrected to January 2023 with Samsung Newsroom dates |
| G8 No model given | Pass | Asked for model number first |

## Not verified by these tests
- Behaviour on ChatGPT (the plugin's primary target) and on other models.
- Behaviour with real screenshots (all evidence was given as text).
- Behaviour after rules 10–11 were added (not re-run).
- Real-device accuracy of menu paths marked [U].
