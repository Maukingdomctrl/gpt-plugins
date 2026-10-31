Nice. That's a fair comparison: the same desk, the same 6 h, the same screen-on time and the same 1 bar of LTE. The only difference is Wi-Fi.

## Battery diagnostic report: Galaxy M15 5G (SM-M156B, One UI 7.0 / Android 15)
**Round:** 2  **Date:** 2026-10-31

### 7. Before/after comparison
| | Before (round 1) | After (round 2) |
|---|---|---|
| Change | — | Connected to office Wi-Fi (1 change) |
| Conditions | Basement desk, 6 h, ~10 min screen-on, LTE 1 bar | Same (Observed) |
| Battery | 90 → 78 % (12 points) | 90 → 83 % (7 points) (Observed) |
| Standby rate | 2.0 %/h ± 0.17 → 120 mA-eq | 7 ÷ 6 = **1.17 %/h ± 0.17** → 1.167 ÷ 100 × 6,000 = **70 mA-eq** (Calculated) |
| Change | 2.0 − 1.17 = **0.83 %/h lower**, against a combined uncertainty of √(0.167² + 0.167²) ≈ ±0.24. That's about 42 % lower. | |

**Verdict: improved.** Weak cellular signal is now supported as a main cause: moving data to Wi-Fi gave a measured improvement of 0.83 %/h (±0.24). It isn't resolved, because 70 mA-eq is still in the skill's **elevated** band (heuristic: 50–100).

That remaining drain is what I warned about. The phone stays registered on the 1-bar LTE network for calls and SMS. Hypothesis: most of the remaining excess comes from that. Wi-Fi can't remove it.

### Next steps
1. **Keep the office Wi-Fi.**
2. **How many SIMs are active?** If you have a second SIM you don't need at work, the next single change would be to switch that SIM off during the workday (INT-NET-04):
   - **Path:** Settings > Connections > **SIM manager** > toggle the unused SIM off. [U] Search Settings for "SIM manager" if it's not there.
   - **What it does:** that SIM stops registering on, and searching for, the network.
   - **Why it may help here:** a second SIM on a 1-bar basement signal also keeps searching.
   - **Disadvantages:** no calls or SMS on that SIM while it's off.
   - **How to reverse:** toggle it back on.
3. **For context (no change needed):** if you can, send one idle measurement from somewhere with good signal, e.g. a few hours at home. If that comes out in the expected range, it confirms the phone itself is fine and the basement signal explains the rest.

If you only use one SIM, there's no further setting I'd change. The remaining drain is then the cost of poor coverage in that room. I'm not suggesting Airplane mode at work, because you need to stay reachable.

### 8. Limits
I haven't inspected the phone. The bands are heuristics.
