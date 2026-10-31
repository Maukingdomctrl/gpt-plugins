Thanks, that's everything I need for a first round. I can't see your phone, so everything below comes from your numbers. Each line is labelled **Observed** (what you told me), **Calculated** (my arithmetic on it) or **Hypothesis** (still to be tested).

## Battery diagnostic report: Galaxy M15 5G
**Round:** 1  **Date:** 2026-10-31

### 1. Device
| Item | Value | Source |
|---|---|---|
| Model number | SM-M156B | Observed |
| Chipset | MediaTek Dimensity 6100+ | [V] Samsung Newsroom India |
| One UI / Android | 8.0 / 16 | Observed |
| Battery (typical / rated) | 6,000 / 5,880 mAh | [V] Samsung spec |
| Last update installed | not provided | — |

### 2. Problem as reported
"Dies quickly when I'm using it." Tag: `rapid_screen_on`

### 3. Evidence received
| Evidence | Value | Label |
|---|---|---|
| Active run | 100 % at 9:00 → 62 % at 12:00, so 38 points in 3 h; screen-on 2 h 30 min; Instagram + browsing (light use) | Observed |
| Screen-on rate | 38 ÷ 2.5 h = **15.2 %/h ± 0.4** (±1 point ÷ 2.5 h) | Calculated |
| mA-equivalent | 15.2 ÷ 100 × 6,000 = **912 mA-eq (±24, so 888–936)** | Calculated |
| Class (heuristic) | For light use, the skill's rough bands are ≤600 expected, 600–900 elevated, >900 abnormal. You're **right on the elevated/abnormal line**. Either way it's higher than expected. | Calculated |
| What that means for runtime | 100 ÷ 15.2 ≈ **6.6 h of this kind of screen-on use per full charge** | Calculated |
| Battery screen | Screen 40 %, Instagram 25 % (shares of the battery used, not % of capacity) | Observed |
| Display | Brightness manual near max, timeout 10 min, Motion smoothness Adaptive | Observed |
| Network | Home Wi-Fi | Observed |

Notes:
- The 3 h window includes about 30 min with the screen off. I had no separate standby figure to subtract, so the rate above is slightly higher than the pure screen-on rate.
- If the battery list covers only since your 9:00 full charge, the screen took about 0.40 × 38 ≈ 15 points and Instagram about 0.25 × 38 ≈ 9.5 points. **Calculated**, and valid only if the list covers the same window.

**Missing evidence and its impact:** you didn't say whether the phone felt warm. That doesn't block this round, but please note it next time.

### 4. Ranked causes
| # | Cause | Evidence for | Evidence against | Confidence |
|---|---|---|---|---|
| 1 | **Display settings** (brightness, timeout) | Manual brightness near max during elevated screen-on drain; the screen is the biggest consumer at 40 %; a 10-minute timeout keeps the screen lit while you're not looking at it | Not yet tested; the effect has to show up in your re-test | **Medium** (Hypothesis) |
| 2 | Instagram itself | 25 % share | You were actively using it, so a big share is expected; there's no sign of background drain | Low |
| — | Network | — | Home Wi-Fi; nothing points to the network | Not supported |

### 5. Recommended changes (two, both display, tested together)

**Change 1: Adaptive brightness** (INT-DISP-01)
- **Applies to:** Galaxy M15 5G
- **Path:** Settings > Display > **Adaptive brightness** (on). Then adjust the brightness slider in Quick settings if it's too dim. [V] This path is from Samsung's generic Galaxy battery page and isn't confirmed for One UI 8.0 on the M15, so please check it on your phone. If you can't find it, search Settings for "brightness".
- **What it does:** sets brightness to the light around you, instead of keeping it near maximum indoors.
- **Why it may help here:** the screen is your biggest consumer, and near-max brightness on the AMOLED panel uses more power the whole time the screen is on.
- **Disadvantages:** the screen may look dimmer indoors and be harder to read outdoors in sun.
- **How to reverse:** turn Adaptive brightness off and raise the slider again.

**Change 2: shorter screen timeout** (INT-DISP-02)
- **Applies to:** Galaxy M15 5G
- **Path:** Settings > Display > **Screen timeout** > **30 seconds** (Samsung default). [V] Generic Samsung page; please check it on One UI 8.0.
- **What it does:** turns the screen off after 30 seconds without a touch, instead of 10 minutes.
- **Why it may help here:** with 10 minutes, the screen stays lit at near-max brightness every time you put the phone down.
- **Disadvantages:** the screen may go dark while you're reading, so you'll tap more.
- **How to reverse:** set the timeout back to 10 minutes.

**Leave Motion smoothness on Adaptive for now.** If I changed a third thing, we couldn't tell which change helped. Switching to Standard (60 Hz) is the next step if drain is still high after this round.

### 6. Re-test instructions
Repeat the same kind of test:
- Start from a known % (a full charge is fine) and write down the % and time.
- Do the **same thing**: Instagram and browsing on home Wi-Fi, for about 2–3 hours.
- At the end, write down the % and time, and the **screen-on time** from Settings > Battery > View details. Take a screenshot before you charge.
- Keep the same: home Wi-Fi, Motion smoothness Adaptive, Power saving off, no charging during the test.
- Tell me if the phone felt cool, warm or hot.

Your screen-on time may come out shorter for the same activity, because the screen no longer stays lit for 10 minutes. That's expected. I'll compare **% per screen-on hour** before and after.

### 7. Before/after comparison
Round 1, so there's nothing to compare yet.

### 8. Limits of this report
I haven't inspected the phone. This report is based only on the information above. The bands are skill heuristics, not Samsung specifications; your before/after comparison is what decides.
