Thanks, that's a clean overnight test. I can't see your phone, so this is based only on what you sent.

**Device:** Galaxy A14 5G (SM-A146B), One UI Core 7.0 / Android 15, 5,000 mAh typical [V].

**What you reported (Observed)**
- 80% at 23:00 → 62% at 07:00, not touched, not charging.
- 5G icon with 1 bar, no Wi-Fi at home.
- Battery usage: Android System 12%, Chrome 8%, WhatsApp 7%.

**What I worked out (Calculated)**
- Drop: 80 − 62 = 18 points over 8 h, so **2.25 %/h (±0.13)**.
- 2.25 ÷ 100 × 5,000 = **112.5 mA-eq**. That's **abnormal** on the skill's standby guide (up to 50 expected, 50–100 elevated, over 100 abnormal). These bands are rules of thumb, not Samsung figures.
- No app stands out. The biggest is 12%, and no single app is anywhere near the share that would point to it.

**Likely causes, most likely first**
1. **Weak cellular signal (1 bar) on mobile data all night.** High confidence. With a weak signal the modem transmits harder and searches more. That fits a high overnight drain with no app dominating.
2. **5G overhead on a weak 5G signal.** Medium confidence. Samsung says 5G can use more power because the phone may use 4G and 5G together, and it suggests switching to LTE where 5G is weak [V S9].
3. Apps and system items: low. Android System 12% isn't high enough on its own, and it often carries work that apps ask it to do. I won't change anything there.

The usual first step for weak signal is to use Wi-Fi where you sleep. You don't have Wi-Fi at home, so the change I can test is the network mode.

**One change to test: switch Network mode from 5G to LTE (Galaxy A14 5G)**
- **Path [V S17]:** Settings > Connections > Mobile networks > **Network mode** > pick the option **without** 5G (e.g. "LTE/3G/2G (auto connect)"). Option names vary by carrier. With two SIMs, change only the SIM used for data.
- **What it does:** stops the phone from using 5G.
- **Why it may help here:** you're on 5G with 1 bar. That's the situation where Samsung suggests LTE.
- **Downsides:** lower peak speed in places where 5G is good.
- **To undo:** choose the option that includes 5G again (e.g. "5G/LTE/3G/2G (auto connect)").

Leave everything else as it is.

**Re-test**
- Same place, same bedside spot, not charging, about 8 h overnight. Note the % and clock time at bedtime and on waking.
- Tell me the network icon and signal bars after the switch. LTE may show a different number of bars.
- Before you charge, send me a screenshot of Settings > Battery > View details.

If this doesn't help, the next step is one night in Airplane mode, to see whether the radio is the cause.
