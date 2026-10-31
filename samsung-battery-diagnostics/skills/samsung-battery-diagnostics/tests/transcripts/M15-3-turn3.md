Thanks. Uninstalling instead of deep-sleeping is fine for this test, because both changes were to the same app, so the result still points clearly at it.

## Battery diagnostic report: Galaxy M15 5G (SM-M156B, One UI 7.0 / Android 15)
**Round:** 2  **Date:** 2026-10-31

### 7. Before/after comparison
| | Before (round 1) | After (round 2) |
|---|---|---|
| Changes | — | PhotoFilter X updated, then uninstalled (2 changes, same app) |
| Conditions | Home Wi-Fi, good LTE, overnight, 7 h | Same (Observed) |
| Battery | 90 → 75 % (15 points in 7 h) | 90 → 85 % (5 points in 7 h) (Observed) |
| Standby rate | 2.14 %/h ± 0.14 → ≈129 mA-eq (abnormal) | 5 ÷ 7 = **0.71 %/h ± 0.14** → 0.714 ÷ 100 × 6,000 = **≈43 mA-eq** (Calculated) |
| Change | 2.14 − 0.71 = **1.43 %/h lower**, against a combined uncertainty of √(0.143² + 0.143²) ≈ ±0.20. That's about 67 % lower. | |

**Verdict: resolved.** Overnight drain went from abnormal into the skill's **expected** band (heuristic: ≤50 mA-eq) once the app was gone. So the evidence now supports **PhotoFilter X's background activity** as the cause. You said updating didn't help, but I don't have a measurement from after the update alone, so I can't put a number on that step.

### Next steps
- **If you don't need the app:** leave it uninstalled. Do one more ordinary night to confirm, then re-check after a week.
- **If you want it back:** reinstall it and immediately add it to **Deep sleeping apps**. The path is Settings > Battery > Background usage limits > Deep sleeping apps > **+** > PhotoFilter X > Add [V]. It will then run only while it's open, so any auto-backup or notifications from it stop. To undo, go to the same screen, tap ⋮ > Remove. Then repeat the same 7 h overnight test and send me the numbers. That will show whether deep sleep is enough, or whether the app is only safe uninstalled.

### 8. Limits
I haven't inspected the phone. The bands are heuristics. I'm not saying the app is malicious, only that its background use drained the battery.
