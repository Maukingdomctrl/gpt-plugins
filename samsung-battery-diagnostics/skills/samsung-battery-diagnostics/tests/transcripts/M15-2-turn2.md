Thanks. That's a clean overnight measurement. I can't see your phone, so everything below comes from what you sent. Each line is labelled **Observed** (what you told me), **Calculated** (my arithmetic on it) or **Hypothesis** (still to be tested).

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
"Loses a lot overnight." Tag: `overnight`

### 3. Evidence received
| Evidence | Value | Label |
|---|---|---|
| Overnight standby | 85 % at 23:00 → 70 % at 07:00, so 15 points in 8 h; phone not touched | Observed |
| Standby rate | 15 ÷ 8 = **1.88 %/h ± 0.13** (±1 point ÷ 8 h) | Calculated |
| mA-equivalent | 1.875 ÷ 100 × 6,000 = **≈113 mA-eq (±8)** | Calculated |
| Class (heuristic) | The skill's rough standby bands are ≤50 expected, 50–100 elevated, >100 abnormal. **Abnormal**, and still above 100 at the bottom of the uncertainty range. | Calculated |
| Battery screen | CallerID App 30 % (mostly background), Android System 22 % | Observed |
| Network | Home Wi-Fi, LTE, good signal | Observed |
| Display | Always On Display: always on | Observed |

The 30 % and 22 % are shares of the battery used over the period the list covers, not % of capacity. I can't convert them to points without knowing when you last fully charged.

**Missing evidence:** none that blocks this round.

### 4. Ranked causes
| # | Cause | Evidence for | Evidence against | Confidence |
|---|---|---|---|---|
| 1 | **CallerID App running in the background** | Largest single share at 30 %, mostly background, while the phone was untouched and the standby rate was abnormal | One night of data; not yet tested | **Medium** |
| 2 | High Android System entry | 22 % share | Android System often carries work requested by apps, possibly by the caller-ID app. Hypothesis: it may drop once the app is restricted. | Low |
| 3 | Always On Display | Always on during an abnormal night | AOD adds some standby load, but it doesn't explain a single app taking 30 % | Low |
| — | Network | — | Wi-Fi with good LTE signal; network isn't supported as a cause | Not supported |

### 5. Recommended change: one app, one test
First, open the Play Store > Manage apps and **update CallerID App** if an update is available. Then restrict it with **one** of the two options below.

A caller-ID app's main job is to identify incoming calls, so you may need it to keep running. That's why I suggest the milder option first:

**Restrict CallerID App's background battery use** (INT-APP-02)
- **Applies to:** Galaxy M15 5G
- **Path:** Settings > Apps > **CallerID App** > **Battery** > **Restricted** (or **Optimised**). [U] I haven't verified this path for One UI 7 on the M15. Older path [V]: Settings > Apps > ⋮ > Special access > Optimise battery usage. If you can't find it, search Settings for "battery usage".
- **What it does:** limits what the app can do in the background.
- **Why it may help here:** the app took 30 % of the battery, mostly in the background, overnight while the phone was idle.
- **Disadvantages:** caller identification, spam warnings or the app's notifications may be delayed or may not appear for some calls.
- **How to reverse:** set it back to **Unrestricted** on the same screen.

*Alternative, only if you don't actually rely on it to identify calls:* put it in **Deep sleeping apps** (INT-APP-01). The path is Settings > Battery > Background usage limits > Deep sleeping apps > **+** > CallerID App > Add [V]. With deep sleep, the app runs only when you open it, so it won't identify incoming calls. To undo it, go to the same screen, tap ⋮ > Remove and select the app.

**Not changing this round:** keep Always On Display and everything else as it is. If drain is still above the expected range after this test, turning AOD off for one night is the next step. **Don't** disable or force-stop Android System.

### 6. Re-test instructions
Repeat the same overnight test:
- At bedtime, write down the % and time. In the morning, write down the % and time again. Aim for about 8 h, with no charging and no use.
- Keep the same: home Wi-Fi on, AOD always on, Power saving off.
- Before charging, send a **morning screenshot** of Settings > Battery > View details. I want to see whether CallerID App and Android System have both dropped.

### 7. Before/after comparison
Round 1, so there's nothing to compare yet.

### 8. Limits of this report
I haven't inspected the phone. This report is based only on the information above. The bands are skill heuristics, not Samsung specifications.
