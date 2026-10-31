Thanks. I can't see your phone, so everything below comes from what you sent. Each line is labelled **Observed** (what you told me), **Calculated** (my arithmetic on it) or **Hypothesis** (still to be tested).

## Battery diagnostic report: Galaxy M15 5G
**Round:** 1  **Date:** 2026-10-31

### 1. Device
| Item | Value | Source |
|---|---|---|
| Model number | SM-M156B | Observed |
| Chipset | MediaTek Dimensity 6100+ | [V] |
| One UI / Android | 7.0 / 15 | Observed |
| Battery (typical / rated) | 6,000 / 5,880 mAh | [V] |
| Last update installed | "yesterday" (type of update not stated) | Observed |

### 2. Problem as reported
"Updated yesterday, drains when idle." Tag: `idle`

### 3. Evidence received
| Evidence | Value | Label |
|---|---|---|
| Idle run | 70 % → 61 %, so 9 points in 4.5 h | Observed |
| Standby rate | 9 ÷ 4.5 = **2.0 %/h ± 0.22** (±1 point ÷ 4.5 h) | Calculated |
| mA-equivalent | 2.0 ÷ 100 × 6,000 = **120 mA-eq (±13)** | Calculated |
| Class (heuristic) | The skill's rough standby bands are ≤50 expected, 50–100 elevated, >100 abnormal. **Abnormal**. | Calculated |
| Battery screen | Google Play services 26 % is the top item | Observed |
| Network | Home Wi-Fi, good LTE signal | Observed |

**Missing evidence and its impact:** I don't know whether yesterday's update was a system software update (Settings > Software update) or app updates. Please check Settings > About phone > Software information and confirm the One UI version. If a major update moved it past 7.0, some menu paths will differ. This doesn't change this round's plan.

### 4. Ranked causes
| # | Cause | Evidence for | Evidence against | Confidence |
|---|---|---|---|---|
| 1 | **Temporary background work after the update** | The update was 1 day ago and drain is high while idle. Samsung says battery life on a new phone typically improves after a few days of use; the same may apply after an update. | This is a hypothesis; only re-measuring in a few days can confirm it | Low |
| 2 | High Google Play services entry | 26 % share | Play services carries work requested by apps, sync and location, so it's a symptom, not necessarily the cause. **Never disable or force-stop it.** | Low |
| — | Network | — | Wi-Fi with good signal | Not supported |

No cause has strong evidence yet. If drain is still high after the waiting period, the next step is a pair of isolation tests: one night in Airplane mode, then one in Safe mode.

Samsung hasn't acknowledged any M15 5G update battery fault. Some users report drain after updates on community forums, but those reports are anecdotal.

### 5. Recommended steps (no settings changed)

**Step 1: let post-update work finish, then re-measure** (INT-WAIT-01)
- **Applies to:** Galaxy M15 5G
- **Action:** use the phone normally for **2–3 days**. Update your apps (Play Store > Manage apps > Update all; also Galaxy Store), then **restart the phone once**.
- **What it does:** gives the phone time to finish post-update work such as re-indexing and app optimisation, and brings apps up to date with the new system.
- **Why it may help here:** the drain started the day after the update, and the top item is a background service.
- **Disadvantages:** you wait a few days, and the restart closes open apps.
- **How to reverse:** nothing to reverse.

**Step 2: look at, don't touch, Google Play services** (part of INT-SYS-01)
- **Path:** Settings > Battery > View details > tap **Google Play services**. If it shows a breakdown (e.g. background time), screenshot it. Also check Settings > **Software update** for any follow-up update.
- **What it does:** gathers evidence only; nothing changes.
- **Disadvantages / reverse:** none.

### 6. Re-test instructions
On **day 3 or 4 after the update**, after the restart, repeat the same idle test:
- Write down the % and time at the start and end. Use the same place and home Wi-Fi, with no charging and no use. Aim for 4.5 h or longer (up to about 8 h, e.g. overnight).
- Keep everything else the same: Power saving off, no new settings.
- Before charging, send a screenshot of Settings > Battery > View details.

### 7. Before/after comparison
Round 1, so there's nothing to compare yet.

### 8. Limits of this report
I haven't inspected the phone. This report is based only on the information above. The bands are skill heuristics, not Samsung specifications.
