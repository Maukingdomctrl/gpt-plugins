Good test. The same place, mobile data and duration make this a fair comparison.

## Battery diagnostic report: Galaxy M15 5G (SM-M156B, One UI 7.0 / Android 15)
**Round:** 2  **Date:** 2026-10-31

### 7. Before/after comparison
| | Before (round 1) | After (round 2) |
|---|---|---|
| Change | — | Network mode LTE only (1 change) |
| Conditions | Home, mobile data, no Wi-Fi, 8 h overnight | Same (Observed); signal bars not reported for either night |
| Battery | 80 → 66 % (14 points) | 80 → 72 % (8 points) (Observed) |
| Standby rate | 1.75 %/h ± 0.13 → 105 mA-eq | 8 ÷ 8 = **1.0 %/h ± 0.13** → 1.0 ÷ 100 × 6,000 = **60 mA-eq** (Calculated) |
| Change | 1.75 − 1.0 = **0.75 %/h lower**, against a combined uncertainty of √(0.125² + 0.125²) ≈ ±0.18. That's about 43 % lower. | |

**Verdict: improved.** At your home, the unstable 5G connection was a real part of the drain: a measured improvement of 0.75 %/h (±0.18). It isn't fully resolved, because 60 mA-eq is still in the skill's **elevated** standby band (heuristic: 50–100).

### Next steps
1. **Keep LTE at home** if you don't need 5G speeds there. To go back, choose the option with 5G in Network mode.
2. **Please send your signal bars** at the bedside, and how many SIMs are active. If LTE is also weak (1–2 bars), weak coverage would be the next suspect.
3. **Next test (one night, nothing changed permanently): Airplane mode** (TEST-AIRPLANE)
   - **Applies to:** Galaxy M15 5G
   - **Path:** Quick settings panel > **Airplane mode** on at bedtime. [R]
   - **What it does:** turns off cellular, Wi-Fi and Bluetooth for the night.
   - **Why it may help here:** if drain drops sharply, the remaining excess is radio/coverage-related. If it stays near 60 mA-eq, we'd look at apps or battery health instead.
   - **Disadvantages:** no calls, SMS or notifications overnight. Only do it on a night you don't need to be reachable, and remember alarms still work.
   - **How to reverse:** Airplane mode off in the morning.

Keep LTE on for that night, and repeat the same measurement: % and times at bedtime and on waking, the same place, and no charging.

### 8. Limits
I haven't inspected the phone. The bands are heuristics. Without signal bars, I can't yet separate "5G instability" from "weak coverage overall".
