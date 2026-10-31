That's a big drop. The conditions were the same as before, and you changed only one thing.

## Battery diagnostic report: Galaxy M15 5G (SM-M156B, One UI 7.0 / Android 15)
**Round:** 2  **Date:** 2026-10-31

### 7. Before/after comparison
| | Before (round 1) | After (round 2) |
|---|---|---|
| Change | — | CallerID App background use restricted (1 change) |
| Conditions | Home Wi-Fi, LTE good signal, AOD on, 23:00–07:00 | Same (Observed) |
| Battery | 85 → 70 % (15 points in 8 h) | 85 → 79 % (6 points in 8 h) (Observed) |
| Standby rate | 1.88 %/h ± 0.13 → ≈113 mA-eq (abnormal) | 6 ÷ 8 = **0.75 %/h ± 0.13** → 0.75 ÷ 100 × 6,000 = **45 mA-eq** (Calculated) |
| Change | 1.875 − 0.75 = **1.13 %/h lower**, against a combined uncertainty of √(0.125² + 0.125²) ≈ ±0.18. That's 60 % lower. | |

**Verdict: resolved.** The improvement is larger than the uncertainty, and overnight drain has moved from abnormal into the skill's **expected** band (heuristic: ≤50 mA-eq). The evidence now supports CallerID App's background activity as the main cause of your overnight loss.

### Next steps
- **Keep the change.** Check over the next few days that CallerID App still identifies incoming calls the way you need. If it misses calls you care about, set it back to Unrestricted (Settings > Apps > CallerID App > Battery) and tell me. We'd then look for a middle ground.
- **Confirm once more:** one more ordinary night under the same conditions. One good night can be chance. Then re-check after a week of normal use.
- **Always On Display:** no need to change it. Turning it off is only an optional extra if you want even more standby time.
- If you can, glance at the morning battery screen to see whether Android System has also dropped. That would fit the idea that it was carrying work for the caller-ID app, though that's still a hypothesis.

### 8. Limits
I haven't inspected the phone. The bands are heuristics, not Samsung specifications.
