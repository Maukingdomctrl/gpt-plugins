Thanks for checking. Good that there's no swelling or heat. I can't see your phone, so everything below comes from what you sent. Each line is labelled **Observed** (what you told me), **Calculated** (my arithmetic on it) or **Hypothesis** (still to be tested).

## Battery diagnostic report: Galaxy M15 5G
**Round:** 1  **Date:** 2026-10-31

### 1. Device
| Item | Value | Source |
|---|---|---|
| Model number | SM-M156B | Observed |
| Chipset | MediaTek Dimensity 6100+ | [V] |
| One UI / Android | 7.0 / 15 | Observed |
| Battery (typical / rated) | 6,000 / 5,880 mAh | [V] |
| Phone age | 20 months | Observed |

### 2. Problem as reported
"Shuts off at 18 %, percentage jumps." Tag: `degradation`

### 3. Evidence received
| Evidence | Value | Label |
|---|---|---|
| Samsung Members battery status | **Weak** | Observed |
| Shutdowns | Switches off at 18 % | Observed |
| % behaviour | Jumps | Observed |
| Safety signs | No swelling, not hot | Observed |
| Overnight standby | 60 % → 52 %, so 8 points in 8 h | Observed |
| Standby rate | 8 ÷ 8 = **1.0 %/h ± 0.13** (±1 point ÷ 8 h) | Calculated |
| mA-equivalent | 1.0 ÷ 100 × 6,000 = **60 mA-eq (±7.5)** | Calculated |
| Class (heuristic) | The skill's rough standby bands are ≤50 expected, 50–100 elevated, >100 abnormal. **Mildly elevated**. | Calculated |

**Missing evidence and its impact:** I don't know the overnight network or which apps used the battery overnight. I can't explain the mildly elevated standby, but that doesn't affect the main finding below.

### 4. Ranked causes
| # | Cause | Evidence for | Evidence against | Confidence |
|---|---|---|---|---|
| 1 | **Battery wear** | Samsung Members says **Weak**; the phone **shuts down with 18 % still showing**; the **% jumps**. Together, those are the pattern of a worn battery. | At 20 months, wear is a bit earlier than usual, but age alone proves nothing either way | **High** |
| 2 | Some extra software standby drain | Mildly elevated overnight rate | Small; doesn't explain shutdowns at 18 % | Low |

I can't tell you a capacity figure (e.g. "your battery is at X %"). Samsung Members gives only Normal / Weak / Bad.

### 5. Recommended change: get the battery inspected

**Service-centre battery inspection** (INT-HEALTH-02)
- **Applies to:** Galaxy M15 5G
- **Action:** **back up your phone first** (Samsung Cloud or Google). Then book a visit to an **authorised Samsung service centre** and tell them: Members battery status Weak, shutdowns at 18 %, percentage jumps. They can test the battery and advise whether it needs replacing.
- **What it does:** gets a proper hardware test of the battery.
- **Why it may help here:** Samsung advises a service-centre check when the battery status isn't Normal and symptoms persist. Your Weak status plus shutdowns with charge left meets that bar.
- **Disadvantages:** possible cost, and time without your phone.
- **How to reverse:** nothing to reverse.

**Until then:**
- Treat about 18 % as your real "empty", and charge before you get there, especially in the cold or before using the camera or navigation.
- **Don't** try "calibration" (draining to 0 % or calibration apps). Samsung doesn't ask for it, and it won't fix a worn battery.
- If the phone ever starts to swell, smells of burning or gets too hot to hold, stop charging and using it and take it in straight away.

### 6. Re-test instructions
After the service-centre visit (or after any battery replacement), please send:
- what the service centre found, and the Members battery status afterwards;
- one overnight measurement as before (% and time at bedtime and on waking, no charging, about 8 h), plus where it was and whether it was on Wi-Fi or mobile data;
- whether any shutdowns or % jumps happened since.

If you can't go soon, still send any further shutdowns (at what %, how cold it was, what you were doing).

### 7. Before/after comparison
Round 1, so there's nothing to compare yet.

### 8. Limits of this report
I haven't inspected the phone. This report is based only on the information above. Samsung Members' status is a rough check, not a capacity measurement. Only a service-centre test can confirm the battery's condition.
