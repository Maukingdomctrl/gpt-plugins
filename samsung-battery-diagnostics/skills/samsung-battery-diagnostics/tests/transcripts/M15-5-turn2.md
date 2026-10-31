Thanks, this fits together well. I can't see your phone, so everything below comes from what you sent. Each line is labelled **Observed** (what you told me), **Calculated** (my arithmetic on it) or **Hypothesis** (still to be tested).

## Battery diagnostic report: Galaxy M15 5G
**Round:** 1  **Date:** 2026-10-31

### 1. Device
| Item | Value | Source |
|---|---|---|
| Model number | SM-M156B | Observed |
| Chipset | MediaTek Dimensity 6100+ | [V] |
| One UI / Android | 7.0 / 15 | Observed |
| Battery (typical / rated) | 6,000 / 5,880 mAh | [V] |
| Last update installed | not provided | — |

### 2. Problem as reported
"Drains in basement office." Tags: `weak_signal`, `idle`

### 3. Evidence received
| Evidence | Value | Label |
|---|---|---|
| Idle workday | 90 % → 78 %, so 12 points in 6 h; screen on about 10 min | Observed |
| Validity | 10 min ÷ 360 min ≈ 2.8 % screen-on, under the 5 % limit, so this counts as standby | Calculated |
| Standby rate | 12 ÷ 6 = **2.0 %/h ± 0.17** (±1 point ÷ 6 h) | Calculated |
| mA-equivalent | 2.0 ÷ 100 × 6,000 = **120 mA-eq (±10)** | Calculated |
| Class (heuristic) | The skill's rough standby bands are ≤50 expected, 50–100 elevated, >100 abnormal. **Abnormal**. | Calculated |
| Network | LTE, **1 bar**, mobile data only; office Wi-Fi exists but you're not connected | Observed |
| Battery screen | Teams 9 % is the top app | Observed |

**Missing evidence:** none that blocks this round. You didn't send a comparison from home, so I can't yet show that the same phone idles normally elsewhere.

### 4. Ranked causes
| # | Cause | Evidence for | Evidence against | Confidence |
|---|---|---|---|---|
| 1 | **Weak cellular signal in the basement** | 1 bar of LTE on mobile data all day; abnormal idle drain; with weak signal the modem transmits at higher power and searches more | Not yet confirmed by a test | **High** (still a hypothesis until the re-test) |
| — | A specific app | — | The top app is only 9 % (Teams). Teams is a work app you need, so I wouldn't restrict it anyway. | Not supported |

### 5. Recommended change: one change at the office

**Join the office Wi-Fi** (INT-NET-01)
- **Applies to:** Galaxy M15 5G
- **Path:** Settings > **Connections** > **Wi-Fi** > select the office network. [R] Check with your IT team first if the office network has rules for personal phones.
- **What it does:** moves your data traffic (Teams, email, etc.) from the 1-bar LTE connection to Wi-Fi.
- **Why it may help here:** on 1 bar, every bit of data has to go over a struggling cellular link. On Wi-Fi, the modem does much less.
- **Disadvantages:** the phone still stays registered on cellular for calls and SMS, so the weak signal still costs some battery. The improvement is likely to be partial. Office Wi-Fi may also come with your employer's network policies.
- **How to reverse:** forget the network or turn Wi-Fi off.

I'm not suggesting Airplane mode at work, because you need to stay reachable.

### 6. Re-test instructions
Repeat a comparable workday:
- Same desk, about 6 h, screen on about as little as last time (around 10 min). No charging.
- Write down the % and time at the start and end, and check the signal bars.
- Office Wi-Fi connected the whole time. Change nothing else (Power saving off, same apps).
- Before charging, send a screenshot of Settings > Battery > View details.

### 7. Before/after comparison
Round 1, so there's nothing to compare yet.

### 8. Limits of this report
I haven't inspected the phone. This report is based only on the information above. The bands are skill heuristics, not Samsung specifications.
