# Verification (Steps 9–10)

## Step 9 — Compare
Use `scripts/battery_diag.py compare before.json after.json`, or by hand:
1. **Comparability check.** Same type; same network mode, Wi-Fi state, signal, location, workload, temperature category; durations within 2× of each other; charging tests start within 10 points; at most two changes between runs. Any mismatch → verdict **not comparable**; ask for a repeat. Do not "adjust" numbers for differing conditions.
2. **Rates.** Drain: before rate − after rate (lower is better). Charging: after − before (higher is better).
3. **Uncertainty.** Each rate ±(1 ÷ hours) (standby/charging) or ±(1 ÷ screen-on hours) (active). Combined = √(u_before² + u_after²).
4. **Verdict**
   | Condition | Verdict |
   |---|---|
   | either run under 3 points change | **inconclusive — insufficient data** |
   | improvement > combined uncertainty AND after-run in expected band AND before-run elevated/abnormal (drain only) | **resolved** |
   | improvement > combined uncertainty AND ≥20 % relative improvement | **improved** |
   | worsening > combined uncertainty | **worse** |
   | otherwise | **no measurable change** |

## Step 10 — Decide next action
| Verdict | Next |
|---|---|
| Resolved | Keep the change; re-check after a week of normal use. Close with the report. |
| Improved | Keep; if still elevated, move to the next ranked cause (new round). |
| No measurable change | Revert the change if it has a cost; test the next ranked cause. |
| Worse | Revert; check conditions; re-assess. |
| Not comparable / inconclusive | Repeat the after-run correctly; don't conclude. |
| Two rounds without improvement | Run TEST-SAFE / TEST-AIRPLANE, then Module F; consider a service-centre check. LAST-RESORT reset only with all its preconditions. |

## Honesty rules for the verdict
- Say "measured improvement of X %/h (±Y)", not "fixed", unless the verdict is resolved.
- One good day can be chance. Recommend one more confirmation run for "resolved".
- Mention any condition you could not verify (e.g. user didn't report signal for the after-run).
