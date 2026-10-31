Thanks. Same 8 h night on Wi-Fi, so the two nights are comparable.

**Before and after (Galaxy A14 5G, overnight 8 h, Wi-Fi)**
| | Before | After |
|---|---|---|
| Observed | 80% → 70% | 80% → 75% |
| Calculated rate | 10 ÷ 8 = **1.25 %/h** (±0.13) | 5 ÷ 8 = **0.625 %/h** (±0.13) |
| mA-equivalent | 62.5, elevated | **31.25, expected** (up to 50) |

- **Improvement:** 1.25 − 0.625 = **0.625 %/h**. The combined reading error is ±0.18 %/h, so this is a real change. It's a 50% reduction.
- **Verdict: resolved, provisionally.** Overnight drain is now in the expected range. That range is a rule of thumb, not a Samsung figure.

**One caveat:** you made two changes at once: you restricted WeatherLive and changed location for both apps. Two changes is within the limit, but I can't tell which one did most of the work. Both affect background activity, so either could explain it.
- If you're happy with both trade-offs, keep them.
  - Restricting WeatherLive means its alerts may arrive late.
  - With location set to "only while using", features like background tracking or location-based reminders in those two apps stop working.
- If you miss something, undo **one** change at a time and repeat this night. That will show which change mattered.

**Your original question: should you replace the battery?**
**No, not on this evidence.** Samsung Members says Normal, you've had no shutdowns, and the overnight drain returned to the expected range after app changes alone. That points to app behaviour, not battery wear.

**Next**
- Do **one more** identical night to confirm, since one good night can be chance.
- Re-check Samsung Members > Support > Phone diagnostics > Battery status every few months.
- If it ever shows Weak or Bad, or the phone shuts down with charge left, tell me and we'll look at the battery again.
