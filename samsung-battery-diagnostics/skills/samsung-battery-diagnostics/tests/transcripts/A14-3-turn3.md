Thanks. Same 8 h night on home Wi-Fi, so the two runs are comparable.

**Before and after (Galaxy A14 5G, overnight 8 h, home Wi-Fi)**
| | Before | After (GameHub in deep sleep) |
|---|---|---|
| Observed | 70% → 58% | 70% → 64% |
| Calculated rate | 12 ÷ 8 = **1.5 %/h** (±0.13) | 6 ÷ 8 = **0.75 %/h** (±0.13) |
| mA-equivalent | 75, elevated | **37.5, expected** (up to 50) |

- **Improvement:** 1.5 − 0.75 = **0.75 %/h**. The combined reading error is ±0.18 %/h, so this is a real change. It's a 50% reduction.
- **Verdict: resolved, provisionally.** Overnight drain is now in the expected range. That range is a rule of thumb, not a Samsung figure.
- This supports the top-ranked cause: **GameHub's background activity after you installed it**. I'm only counting this as confirmed because the drain fell after a change that affected only GameHub.

**Notes**
- You mentioned deep sleep, but not whether you also updated GameHub. Either way, both changes affected only GameHub.
- While GameHub is in deep sleep you won't get its notifications or background downloads until you open it.
- To undo: Settings > Battery > Background usage limits > Deep sleeping apps > ⋮ > Remove.

**Next**
- Keep GameHub in deep sleep.
- Do **one more** identical night to confirm. One good night can be chance.
- Before charging, send the % and times plus a screenshot of Settings > Battery > View details, so we can check GameHub's share has dropped.
- If it creeps back up after a GameHub update, tell me.
