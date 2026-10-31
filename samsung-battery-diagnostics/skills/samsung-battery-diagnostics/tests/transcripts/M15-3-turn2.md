Thanks, that's enough to start. I can't see your phone, so everything below comes from what you sent. Each line is labelled **Observed** (what you told me), **Calculated** (my arithmetic on it) or **Hypothesis** (still to be tested).

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
"Worse since I installed a new photo app." Tags: `after_install`, `overnight`

### 3. Evidence received
| Evidence | Value | Label |
|---|---|---|
| New app | PhotoFilter X, installed 3 days ago | Observed |
| Overnight standby | 90 % → 75 %, so 15 points in 7 h | Observed |
| Standby rate | 15 ÷ 7 = **2.14 %/h ± 0.14** (±1 point ÷ 7 h) | Calculated |
| mA-equivalent | 2.143 ÷ 100 × 6,000 = **≈129 mA-eq (±9)** | Calculated |
| Class (heuristic) | The skill's rough standby bands are ≤50 expected, 50–100 elevated, >100 abnormal. **Abnormal**. | Calculated |
| Battery screen | PhotoFilter X 28 %, mostly background | Observed |
| Network | Home Wi-Fi, good LTE signal | Observed |

**Missing evidence and its impact:** I don't know how often you open the app, whether it backs up or syncs photos automatically, or what its location permission is set to. Those would help explain *why* it runs in the background. They don't change what to test first.

### 4. Ranked causes
| # | Cause | Evidence for | Evidence against | Confidence |
|---|---|---|---|---|
| 1 | **PhotoFilter X, recently installed and active in the background** | The drain began 3 days after you installed it; it takes 28 %, mostly in the background; overnight standby is abnormal | Not yet confirmed by a before/after test | **High** (still a hypothesis until the re-test) |
| — | Network | — | Wi-Fi with good signal | Not supported |

I'm not saying the app is malicious. Only its background activity is in question. Some photo apps run in the background to back up, sync or process images.

### 5. Recommended changes: both target the same app

**Change 1: update the app** (first part of INT-APP-03)
- **Applies to:** Galaxy M15 5G
- **Path:** Play Store (or Galaxy Store, if you installed it from there) > Manage apps > **Update** PhotoFilter X, if an update is available. [R]
- **What it does:** installs the developer's latest version.
- **Why it may help here:** a new app's background behaviour sometimes changes between versions. This is a hypothesis.
- **Disadvantages:** none significant.
- **How to reverse:** usually not needed. The app can't simply be rolled back.

**Change 2: put PhotoFilter X into Deep sleeping apps** (INT-APP-01)
- **Applies to:** Galaxy M15 5G
- **Path:** Settings > Battery > **Background usage limits** > **Deep sleeping apps** > **+** > PhotoFilter X > Add. [V] Samsung support. On older layouts it's under Settings > Battery and device care > Battery. If you can't find it, search Settings for "sleeping".
- **What it does:** PhotoFilter X never runs in the background. It works only while you have it open.
- **Why it may help here:** almost all of its 28 % was background use, while you weren't using the phone.
- **Disadvantages:** any automatic photo backup, sync or notifications from that app stop until you open it.
- **How to reverse:** same screen > ⋮ > **Remove** > select PhotoFilter X.

**Don't uninstall it yet.** If deep sleep doesn't bring the overnight drain down, the next step is to uninstall it for one night (back up anything you've edited in it first) and re-measure.

### 6. Re-test instructions
Repeat the same overnight test:
- At bedtime and on waking, write down the % and time. Aim for about 7 h, with no charging and no use.
- Keep the same: home Wi-Fi, same place, Power saving off. Don't change any other setting.
- Before charging, send a **morning screenshot** of Settings > Battery > View details, so I can see PhotoFilter X's share.

### 7. Before/after comparison
Round 1, so there's nothing to compare yet.

### 8. Limits of this report
I haven't inspected the phone. This report is based only on the information above. The bands are skill heuristics, not Samsung specifications.
