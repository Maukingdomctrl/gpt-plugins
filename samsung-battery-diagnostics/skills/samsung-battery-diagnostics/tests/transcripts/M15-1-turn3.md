That's a clear improvement. Same workload, same Wi-Fi, same screen-on time, so the two runs compare fairly.

## Battery diagnostic report: Galaxy M15 5G (SM-M156B, One UI 8.0 / Android 16)
**Round:** 2  **Date:** 2026-10-31

### 7. Before/after comparison
| | Before (round 1) | After (round 2) |
|---|---|---|
| Changes | — | Adaptive brightness on, timeout 30 s (2 changes, both display) |
| Conditions | Instagram + browsing, home Wi-Fi, 9:00–12:00 | Same (Observed) |
| Battery | 100 → 62 % (38 points), screen-on 2.5 h | 100 → 74 % (26 points), screen-on 2.5 h (Observed) |
| Rate per screen-on hour | 38 ÷ 2.5 = 15.2 %/h ± 0.4 → 912 mA-eq | 26 ÷ 2.5 = **10.4 %/h ± 0.4** → 10.4 ÷ 100 × 6,000 = **624 mA-eq** (Calculated) |
| Change | 15.2 − 10.4 = **4.8 %/h better**, against a combined uncertainty of √(0.4² + 0.4²) ≈ ±0.57. That's 4.8 ÷ 15.2 ≈ **32 % lower**. | |

**Verdict: improved.** The measured improvement is 4.8 %/h (±0.6). In runtime terms, 100 ÷ 10.4 ≈ **9.6 h** of this kind of screen-on use per charge, up from about 6.6 h (Calculated).

It isn't "resolved" yet. 624 mA-eq is still just inside the skill's **elevated** band for light use (heuristic: ≤600 expected). Because both changes were made together, I can't split the gain between brightness and timeout. Both were display changes, so keep both.

### Next round: one more display change
**Motion smoothness to Standard (60 Hz)** (INT-DISP-03)
- **Applies to:** Galaxy M15 5G
- **Path:** Settings > Display > **Motion smoothness** > **Standard**. [U] Not verified for the M15 on One UI 8.0. If the option names differ, search Settings for "motion smoothness".
- **What it does:** caps the screen at 60 Hz instead of up to 90 Hz.
- **Why it may help here:** you're just above the expected range, and scrolling apps like Instagram keep a higher refresh rate active much of the time.
- **Disadvantages:** scrolling and animations look less smooth.
- **How to reverse:** same screen > **Adaptive**.

**Re-test:** run the same 3 hours of Instagram and browsing on home Wi-Fi, starting from 100 %. Keep Adaptive brightness and the 30 s timeout. Send the end %, the screen-on time, and how warm the phone felt. If the rate doesn't improve beyond the uncertainty, switch back to Adaptive, since smoothness is the only thing you'd be giving up.

### 8. Limits
I haven't inspected the phone. The bands are heuristics, and one good run can be chance.
