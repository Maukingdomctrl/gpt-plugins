Thanks. That points in a clear direction. I can't see your phone, so this is based only on what you sent.

**Device:** Galaxy A14 5G (SM-A146B), One UI Core 7.0 / Android 15, 5,000 mAh typical [V].

**What you reported (Observed)**
- Overnight: 85% → 65% in 9 h. LTE with 1 bar, no Wi-Fi at home.
- The top app is Messages at 5%. You don't need calls at night.

**What I worked out (Calculated)**
- Drop: 85 − 65 = 20 points over 9 h, so **2.22 %/h (±0.11)**.
- 2.22 ÷ 100 × 5,000 = **111 mA-eq**. That's **abnormal** on the skill's standby guide (up to 50 expected, 50–100 elevated, over 100 abnormal). This is a rule of thumb, not a Samsung figure.
- No app explains it. The top one is only 5%.

**Likely causes**
1. **Weak cellular signal.** High confidence. You had 1 bar on mobile data all night, the drain is high, and no app stands out. With a weak signal the modem transmits harder and keeps searching. That's a coverage problem, not a fault in the phone.
- Two things don't apply. You're already on LTE, so switching away from 5G won't help. You have no home Wi-Fi to move data onto.

**One test: Airplane mode overnight (Galaxy A14 5G)**
- **Path [R]:** Quick settings panel > **Airplane mode** on at bedtime.
- **What it does:** turns off the mobile, Wi-Fi and Bluetooth radios.
- **Why it may help here:** if the weak signal is the cause, overnight drain should drop sharply with the radio off. If drain stays high, the cause is something else, and we'll look at that next.
- **Downsides:** no calls, SMS or notifications until you turn it off. You said that's fine at night.
- **To undo:** turn Airplane mode off in the morning.

Change nothing else.

**Re-test**
- Same place, same bedside spot, about 9 h, not charging, not touched.
- Send me the bedtime and wake-up % with times.
- Before you charge, send a screenshot of Settings > Battery > View details.

Quick question for later: do you have a second SIM in the phone? If so, which one carries data?
