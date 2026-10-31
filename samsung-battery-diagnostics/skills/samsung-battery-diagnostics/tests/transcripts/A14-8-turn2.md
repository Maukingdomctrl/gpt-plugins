Thanks. This helps answer the replacement question. I can't see your phone, so this is based only on what you sent.

**Device:** Galaxy A14 5G (SM-A146B), One UI Core 7.0 / Android 15, 5,000 mAh typical [V].

**What you reported (Observed)**
- Samsung Members battery status: **Normal**. No unexpected shutdowns. Phone is almost 3 years old.
- Overnight on Wi-Fi: 80% → 70% in 8 h.
- WeatherLive uses 20%, mostly in the background. Two apps have location set to "Allow all the time".

**What I worked out (Calculated)**
- Drop: 80 − 70 = 10 points over 8 h, so **1.25 %/h (±0.13)**.
- 1.25 ÷ 100 × 5,000 = **62.5 mA-eq**. That's **elevated** on the skill's standby guide (up to 50 expected, 50–100 elevated). This is a rule of thumb, not a Samsung figure.

**Is the battery dying? The evidence says no.**
- Samsung Members says Normal, and you've had no shutdowns with charge left. Those are the signs that would point to wear.
- Age alone is only a weak hint, so **I don't recommend replacing the battery** on this evidence.
- What the evidence does show is a background app using a large share.

**Likely causes, most likely first**
1. **WeatherLive running in the background.** Medium confidence. It's 20% of use, mostly in the background, and your overnight drain is elevated.
2. **Location set to "all the time".** Low confidence. Two apps have it, but I don't know yet whether WeatherLive is one of them.
3. Battery wear: not supported (Members Normal, no shutdowns).

**One change to test (Galaxy A14 5G, One UI Core 7.0)**
Pick the version that fits how you use WeatherLive:
- **If you don't need WeatherLive alerts or a live widget, put it into Deep sleeping apps.**
  - **Path [V]:** Settings > Battery > Background usage limits > Deep sleeping apps > **+** > WeatherLive > Add. If One UI Core labels it differently, search Settings for `sleeping`.
  - **What it does:** WeatherLive runs only when you open it.
  - **Why it may help here:** most of its 20% was background use.
  - **Downsides:** no weather alerts or background widget updates until you open it.
  - **To undo:** same screen > ⋮ > Remove > WeatherLive.
- **If you rely on its weather alerts, set its battery use to Restricted instead.**
  - **Path [U]:** Settings > Apps > WeatherLive > Battery > Restricted. It limits background activity but doesn't stop it.
  - **Downside:** alerts may be delayed.
  - **To undo:** set it back to Unrestricted or Optimised.

Leave the location settings alone for now, so we can tell whether this change made the difference. Tell me which two apps have "Allow all the time"; that's the next thing to test.

**Re-test**
- One night under the same conditions: Wi-Fi, about 8 h, not charging, not touched.
- Send me the bedtime and wake-up % with times.
- Before you charge, send a screenshot of Settings > Battery > View details.
