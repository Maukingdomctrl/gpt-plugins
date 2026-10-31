Thanks. You ran the Safe-mode night rather than the Airplane-mode night. That's fine: it's the other test on the plan, and it's a clean single change. Same home Wi-Fi, same 8 h, so the two nights are comparable.

**Before and after (Galaxy A14 5G, overnight 8 h, home Wi-Fi, good LTE)**
| | Normal | Safe mode |
|---|---|---|
| Observed | 80% → 64% | 80% → 74% |
| Calculated rate | 16 ÷ 8 = **2.0 %/h** (±0.13) | 6 ÷ 8 = **0.75 %/h** (±0.13) |
| mA-equivalent | 100, elevated | **37.5, expected** (up to 50) |

- **Reduction:** 2.0 − 0.75 = **1.25 %/h**. The combined reading error is ±0.18 %/h, so this is a real change. It's a 62.5% reduction.

**What this tells us**
- Safe mode switches off downloaded apps. The drain fell into the expected range without them, so **a downloaded app is the likely cause**. The phone's own system and the battery are not the likely cause. This is strong evidence, but it doesn't name the app yet.
- Battery wear remains unsupported. Members says Normal, and the phone idles normally in Safe mode.
- **Verdict: needs more investigation.** Safe mode is a test, not a fix. Restart the phone normally to leave it.

**Next step: find the app (no changes yet)**
After a normal night, before charging, please send:
1. The **full** list from Settings > Battery > View details. Scroll down to include every app with a percentage.
2. For the top two or three downloaded apps, tap each one and screenshot the detail screen. It may show background use.
3. Any apps you **installed or updated** around when the idle drain started.

From that, I'll suggest one app to restrict or deep-sleep for a night, and we'll compare again. Chrome was 9%, which isn't enough on its own to blame it. I won't guess.
