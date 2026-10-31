Thanks for waiting it out. That's a fair comparison: the same 4.5 h, the same place, the same home Wi-Fi.

## Battery diagnostic report: Galaxy M15 5G (SM-M156B, One UI 7.0 / Android 15)
**Round:** 2  **Date:** 2026-10-31

### 7. Before/after comparison
| | Before (round 1, day after update) | After (round 2, day 3+) |
|---|---|---|
| Steps | — | Waited 3 days, updated apps, restarted once |
| Conditions | Home Wi-Fi, good LTE, idle 4.5 h | Same (Observed) |
| Battery | 70 → 61 % (9 points) | 70 → 66 % (4 points) (Observed) |
| Standby rate | 2.0 %/h ± 0.22 → 120 mA-eq | 4 ÷ 4.5 = **0.89 %/h ± 0.22** → 0.889 ÷ 100 × 6,000 = **≈53 mA-eq** (Calculated) |
| Change | 2.0 − 0.89 = **1.11 %/h lower**, against a combined uncertainty of √(0.222² + 0.222²) ≈ ±0.31. That's about 56 % lower. | |

**Verdict: improved.** This fits the post-update settling hypothesis. Because the improvement came with waiting, app updates and a restart together, I can't say which step did it.

It isn't "resolved" on these numbers. About 53 mA-eq sits just above the skill's expected line (heuristic: ≤50). With a 4-point drop, the uncertainty is ±13 mA-eq, so the true value could be on either side of the line.

### Next step: a longer confirmation run (no changes)
Do one **overnight** idle test of about 6–8 h at home on Wi-Fi, under the same conditions. Write down the % and times at bedtime and on waking, with no charging. Send the morning battery screenshot so I can see whether Google Play services has come down. A longer window shrinks the uncertainty enough to tell whether you're now in the expected range.

- If it comes out ≤50 mA-eq (about 0.83 %/h or less), we'll call it resolved and just re-check after a week.
- If it's still elevated, the next step is one night in **Airplane mode**, then one night in **Safe mode**. Those show whether the network or a downloaded app is behind what's left. Neither changes anything permanently. I'll give you the exact steps if we need them.

Please keep not disabling or force-stopping Google Play services. It usually just carries other apps' work.

### 8. Limits
I haven't inspected the phone. The bands are heuristics.
