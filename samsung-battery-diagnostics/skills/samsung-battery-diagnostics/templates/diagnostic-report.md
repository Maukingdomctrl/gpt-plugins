# Diagnostic report template

Fill every section. Write "not provided" rather than guessing. Label each fact **Observed**, **Calculated** or **Hypothesis**.

---

## Battery diagnostic report — <Galaxy M15 5G | Galaxy A14 5G>
**Round:** <1, 2, …>  **Date:** <YYYY-MM-DD>

### 1. Device
| Item | Value | Source |
|---|---|---|
| Model number | <SM-…> | Observed (user, Settings > About phone) |
| Chipset | <…> | Device file label [V]/[R]/[U] |
| One UI / Android | <…> / <…> | Observed |
| Battery (typical / rated) | <6000/5880 or 5000/4900> mAh | [V] |
| Last update installed | <date or not provided> | Observed |

### 2. Problem as reported
<user's words, short> — tags: <rapid_screen_on, overnight, …>

### 3. Evidence received
| Evidence | Value | Label |
|---|---|---|
| Measurement 1 | <type, start→end %, hours, screen-on min> | Observed |
| Rate | <x %/h ± u> = <mA-eq> mA-eq → <class, heuristic> | Calculated |
| Top consumers | <app %, …> | Observed (screenshot) |
| Network | <5G/LTE, bars, Wi-Fi> | Observed |
| Other | <…> | |

**Missing evidence and its impact:** <list, or "none">

### 4. Ranked causes
| # | Cause | Evidence for | Evidence against | Confidence |
|---|---|---|---|---|
| 1 | <…> | <…> | <…> | <high/medium/low> |
| 2 | | | | |
| 3 | | | | |

### 5. Recommended change(s) — max two
For each:
- **Applies to:** <device>
- **Path:** <…> (<[V]/[R]/[U]>, One UI <version>)
- **What it does:** <…>
- **Why it may help here:** <link to the evidence>
- **Disadvantages:** <…>
- **How to reverse:** <…>

### 6. Re-test instructions
<type, duration, conditions to keep identical, what to send back>

### 7. Before/after comparison (from round 2 onward)
| | Before | After |
|---|---|---|
| Conditions | <…> | <…> |
| Rate | <…> | <…> |
| Change | <improvement ± combined uncertainty> | |
**Verdict:** <resolved / improved / no measurable change / worse / not comparable / inconclusive>
**Next step:** <…>

### 8. Limits of this report
I have not inspected the phone. This report is based only on the information above. Thresholds are heuristics, not Samsung specifications.
