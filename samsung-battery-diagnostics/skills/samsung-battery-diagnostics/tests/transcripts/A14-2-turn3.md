Thanks. Same place, same 1 bar, no Wi-Fi, and only the network mode changed, so the two nights are comparable.

**Before and after (Galaxy A14 5G, overnight 23:00–07:00, 8 h)**
| | Before (5G) | After (LTE) |
|---|---|---|
| Observed | 80% → 62% | 80% → 70% |
| Calculated rate | 18 ÷ 8 = **2.25 %/h** (±0.13) | 10 ÷ 8 = **1.25 %/h** (±0.13) |
| mA-equivalent | 112.5, abnormal | **62.5, elevated** |

- **Improvement:** 2.25 − 1.25 = **1.0 %/h**. The combined reading error is ±0.18 %/h, so this is a real change. It's a 44% reduction.
- **Verdict: improved.** Overnight drain is still above the expected range (up to 50 mA-eq). That range is a rule of thumb, not a Samsung figure.

**What this tells us**
- Weak 5G was adding a lot of drain. **Keep LTE at home.** The downside is slower peak speed where 5G is good. To undo it, go to Settings > Connections > Mobile networks > Network mode and pick the 5G option.
- What's left fits the top-ranked cause: a **weak signal (1 bar) on mobile data**. LTE alone can't fix poor coverage.

**Next round: one diagnostic night in Airplane mode (Galaxy A14 5G)**
- **Path [R]:** Quick settings panel > **Airplane mode** at bedtime.
- **What it does:** turns off the mobile, Wi-Fi and Bluetooth radios.
- **Why:** if the drain falls sharply, the weak signal is confirmed as the remaining cause. If it stays around 1.25 %/h, something else is involved, and we'll test Safe mode next.
- **Downsides:** no calls, SMS or notifications overnight.
- **To undo:** turn Airplane mode off in the morning.
- Keep LTE as it is.
- Same conditions: about 8 h, not charging, not touched.
- Send me the bedtime and wake-up % with times, and before you charge, a screenshot of Settings > Battery > View details.

If you have a second SIM, tell me. A second SIM in poor coverage also keeps searching for signal.
