Thanks. That explains a lot. I can't see your phone, so everything below comes from what you sent. Each line is labelled **Observed** (what you told me), **Calculated** (my arithmetic on it) or **Hypothesis** (still to be tested).

## Battery diagnostic report: Galaxy M15 5G
**Round:** 1  **Date:** 2026-10-31

### 1. Device
| Item | Value | Source |
|---|---|---|
| Model number | SM-M156B | Observed |
| Chipset | MediaTek Dimensity 6100+ | [V] |
| One UI / Android | 7.0 / 15 | Observed |
| Battery (typical / rated) | 6,000 / 5,880 mAh | [V] |
| Max wired charging | Up to 25 W "Super Fast Charging"; adapter sold separately | [V] Samsung spec |

### 2. Problem as reported
"Takes forever to charge." Tag: `slow_charging`

### 3. Evidence received
| Evidence | Value | Label |
|---|---|---|
| Adapter | 15 W, from your old phone | Observed |
| Timed run | 30 % → 48 %, so 18 points in 30 min, **while watching videos** | Observed |
| Charging rate | 18 ÷ 30 = **0.60 %/min ± 0.03** (±1 point ÷ 30 min) | Calculated |
| Lock-screen message | "Fast charging" | Observed |
| Fast charging toggle | On | Observed |
| Moisture warning / cable | None / looks fine | Observed |

Samsung doesn't publish a "normal" charging time for the M15 5G, so I won't judge 0.60 %/min against a target. I'll only compare it with your own later runs.

**Missing evidence and its impact:** you didn't say whether the phone got **warm or hot** while charging. Please note it next time. Also, because you were watching video, this run isn't a clean charging test: the screen and video playback used some of the power that would otherwise go into the battery.

### 4. Ranked causes
| # | Cause | Evidence for | Evidence against | Confidence |
|---|---|---|---|---|
| 1 | **Adapter below the phone's maximum** | A 15 W adapter on a phone that supports up to 25 W. "Fast charging" rather than "Super fast charging" is the label you'd expect with a non-25 W adapter. (Expected label, not verified on this exact model [U].) | — | **Medium** |
| 2 | **Using the phone while charging** | Video playback during the run takes power away from charging and adds heat | Heat not reported | Low |
| — | Fast charging off, moisture, charge limit | — | Toggle on, no warning, no limit reported | Not supported |

In short: nothing looks faulty. The phone is fast charging at what a 15 W adapter can give, while also running video.

### 5. Recommended changes: one at a time, each with its own timed run

**Change 1 (free, do this first): charge idle and cool** (INT-CHG-05)
- **Applies to:** Galaxy M15 5G
- **Action:** same 15 W adapter and cable, wall socket, screen off, no videos, room temperature, no thick case if it gets warm. [V] Samsung charging guidance
- **What it does:** all the adapter's power goes into the battery, and the phone stays cooler. A hot phone may slow charging.
- **Why it may help here:** your run was done while streaming video.
- **Disadvantages:** you can't use the phone heavily while it charges.
- **How to reverse:** nothing to reverse.

**Change 2 (optional, only after Change 1's run): a 25 W adapter** (INT-CHG-01)
- **Applies to:** Galaxy M15 5G
- **Action:** a **Samsung 25 W** (or certified equivalent) USB-C adapter in a wall socket, with a USB-C to USB-C cable. Look for "Super fast charging" on the lock screen. I can't confirm from Samsung's M15 page that every USB-C PD adapter will trigger Super fast charging [U], so a Samsung 25 W adapter is the safe choice.
- **What it does:** lets the phone use its 25 W mode instead of the 15 W adapter's level.
- **Why it may help here:** your 15 W adapter is below the phone's 25 W maximum.
- **Disadvantages:** cost of a new adapter, and slightly more heat while charging.
- **How to reverse:** go back to the old adapter.

### 6. Re-test instructions
**Run A (Change 1):**
- Start between 25 % and 35 %, so it's within 10 points of last time.
- Same 15 W adapter and cable, wall socket.
- Screen off, phone idle, room temperature, 30 minutes.
- Write down the start %, end % and minutes, what the lock screen says, and whether the phone felt cool, warm or hot.

**Run B (only if you buy a 25 W adapter):** repeat Run A exactly, changing only the adapter.

### 7. Before/after comparison
Round 1, so there's nothing to compare yet.

### 8. Limits of this report
I haven't inspected the phone or the charger. This report is based only on the information above.
