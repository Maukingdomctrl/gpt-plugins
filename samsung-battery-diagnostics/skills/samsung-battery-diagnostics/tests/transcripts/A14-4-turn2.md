Thanks, that's a useful test. I can't see your phone, so this is based only on your numbers.

**Device:** Galaxy A14 5G (SM-A146B), One UI Core 7.0 / Android 15, 5,000 mAh typical [V].

**What you reported (Observed)**
- Overnight on 5G with good signal (4 bars), no Wi-Fi: 80% → 74% in 8 h.
- YouTube 12% on the list since your last full charge. That's from videos you watched before bed, so it's normal use, not background drain.

**What I worked out (Calculated)**
- Drop: 80 − 74 = 6 points over 8 h, so **0.75 %/h (±0.13)**.
- 0.75 ÷ 100 × 5,000 = **37.5 mA-eq**. That's within the **expected** range on the skill's standby guide (up to 50 mA-eq expected). This is a rule of thumb, not a Samsung figure.

**So, does 5G drain your A14 5G?**
- What Samsung says: 5G *can* use more power, because the phone may use 4G and 5G at the same time. It suggests switching to LTE **where 5G is weak** [V S9].
- What your test shows: on a **strong** 5G signal, overnight standby was in the expected range. Nothing here shows 5G draining your battery while the phone sits idle.

**Likely causes**
1. **Usage is within the expected range.** Medium confidence. Your overnight drain is normal.
2. 5G overhead: low confidence. You're on 5G and you feel it's worse, but your signal is strong and the measured rate is normal.

**Recommendation: no setting change needed.** Keeping 5G on costs nothing measurable in this test.

If you still want to know for sure, you can do an optional comparison:
- **Network mode to LTE for one night [V S17]:** Settings > Connections > Mobile networks > Network mode > the option without 5G (e.g. "LTE/3G/2G (auto connect)").
  - **What it does:** stops the phone using 5G.
  - **Downside:** slower peak data where 5G is good.
  - **To undo:** pick the option that includes 5G again.
- Then repeat exactly the same night: same place, no Wi-Fi, not charging, about 8 h. Send the bedtime and wake-up % with times.
- Bear in mind: last night's drop was only 6 points. A difference of about a point either way is within reading error.

If the drain you feel happens **during the day while you use the phone**, the overnight test doesn't cover that. Instead, send me one block of normal use: start and end %, screen-on time from Settings > Battery > View details, what you did, and whether it showed 5G or LTE.
