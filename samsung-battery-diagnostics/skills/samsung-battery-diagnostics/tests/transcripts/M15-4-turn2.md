Thanks. That's a useful baseline. I can't see your phone, so everything below comes from what you sent. Each line is labelled **Observed** (what you told me), **Calculated** (my arithmetic on it) or **Hypothesis** (still to be tested).

## Battery diagnostic report: Galaxy M15 5G
**Round:** 1  **Date:** 2026-10-31

### 1. Device
| Item | Value | Source |
|---|---|---|
| Model number | SM-M156B | Observed |
| Chipset / modem | MediaTek Dimensity 6100+ (5G Sub-6 only) | [V] |
| One UI / Android | 7.0 / 15 | Observed |
| Battery (typical / rated) | 6,000 / 5,880 mAh | [V] |
| Last update installed | not provided | — |

### 2. Problem as reported
"Drains more since using 5G." Tags: `5g`, `overnight`

### 3. Evidence received
| Evidence | Value | Label |
|---|---|---|
| Overnight standby | 80 % → 66 %, so 14 points in 8 h, on mobile data, no Wi-Fi | Observed |
| Standby rate | 14 ÷ 8 = **1.75 %/h ± 0.13** (±1 point ÷ 8 h) | Calculated |
| mA-equivalent | 1.75 ÷ 100 × 6,000 = **105 mA-eq (±7.5, so about 98–113)** | Calculated |
| Class (heuristic) | The skill's rough standby bands are ≤50 expected, 50–100 elevated, >100 abnormal. You're **on the elevated/abnormal line**, well above expected either way. | Calculated |
| Network | Status-bar icon keeps switching between 5G and LTE; no Wi-Fi at home | Observed |
| Battery screen | Android System 14 %, Gmail 6 %, nothing above 15 % | Observed |

**Missing evidence and its impact:** I don't have your **signal bars** or the **number of active SIMs**. Without the bars, I can't tell whether the extra drain is about 5G specifically or about weak coverage in general. Weak coverage would also cost battery on LTE. Please note the bars in the re-test.

### 4. Ranked causes
| # | Cause | Evidence for | Evidence against | Confidence |
|---|---|---|---|---|
| 1 | **Unstable 5G connection** (constant switching between 5G and LTE) | The icon flips 5G↔LTE; you're on mobile data only; standby is high; you link the drain to 5G. Samsung notes that 5G can use more power because the phone may run 4G and 5G together, and suggests LTE where 5G is weak. | Not yet tested; signal strength unknown | **Medium** |
| 2 | Weak signal in general | Possible (Hypothesis) | No bars reported | Low, needs the bars |
| — | A specific app | — | No app above 15 %; Android System at 14 % is not unusual | Not supported |

### 5. Recommended change: one setting, one night

**Switch the data SIM from 5G to LTE** (INT-NET-02)
- **Applies to:** Galaxy M15 5G
- **Path:** Settings > **Connections** > **Mobile networks** > **Network mode** > choose the option **without 5G**, e.g. "LTE/3G/2G (auto connect)". [V] Samsung support. Option names vary by carrier and region. With two SIMs, the setting is per SIM: change only the SIM you use for mobile data.
- **What it does:** stops the phone using 5G, so it stays on LTE.
- **Why it may help here:** your phone keeps flipping between 5G and LTE at home. Each switch and the dual 4G/5G connection keep the modem busier.
- **Disadvantages:** lower peak data speed where 5G is good. Some carrier plans or features may expect 5G.
- **How to reverse:** same screen > choose the option that includes 5G again (e.g. "5G/LTE/3G/2G (auto connect)").

Nothing else needs changing this round.

### 6. Re-test instructions
Repeat the same overnight test:
- At bedtime and on waking, write down the % and time. Aim for about 8 h at home, on mobile data (no Wi-Fi, same as before), with no charging and no use.
- Note the **signal bars** at bedtime and in the morning, and whether the icon shows LTE steadily.
- Keep everything else the same: Power saving off, no hotspot or other new connections.
- Before charging, send a **morning screenshot** of Settings > Battery > View details.

### 7. Before/after comparison
Round 1, so there's nothing to compare yet.

### 8. Limits of this report
I haven't inspected the phone. This report is based only on the information above. The bands are skill heuristics, not Samsung specifications. Whether 5G costs you battery depends on your coverage, and your before/after nights will show it.
