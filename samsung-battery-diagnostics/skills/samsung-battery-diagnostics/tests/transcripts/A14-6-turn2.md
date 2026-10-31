Thanks, that's a clean overnight test. I can't see your phone, so this is based only on what you sent.

**Device:** Galaxy A14 5G (SM-A146B), One UI Core 7.0 / Android 15, 5,000 mAh typical [V].

**What you reported (Observed)**
- Overnight: 80% → 64% in 8 h, on home Wi-Fi with good LTE signal.
- Battery usage: Android System 11%, Chrome 9%.
- Samsung Members battery status: **Normal**. Phone is 30 months old.
- No hotspot, no watch.

**What I worked out (Calculated)**
- Drop: 80 − 64 = 16 points over 8 h, so **2.0 %/h (±0.13)**.
- 2.0 ÷ 100 × 5,000 = **100 mA-eq**. That's **elevated**, right at the top of the 50–100 band on the skill's standby guide (up to 50 is expected). This is a rule of thumb, not a Samsung figure.

**What the evidence does and doesn't show**
- **No single app or system item stands out.** Android System 11% and Chrome 9% are both far below the level where I'd suspect them.
- **Network is unlikely.** You were on Wi-Fi with good LTE, and nothing like a hotspot or watch was connected.
- **Battery wear is not supported.** Members says Normal and you've had no shutdowns. The phone's age alone is only a weak hint, and I wouldn't recommend a new battery on that basis.
- So the cause is **not identified yet**. Something may be keeping the phone awake overnight, but that's a guess and I can't see it without more evidence.

**Next step: a diagnostic test, not a fix (Galaxy A14 5G)**
**Airplane-mode night**
- **Path [R]:** Quick settings panel > **Airplane mode** at bedtime.
- **What it does:** turns off the mobile, Wi-Fi and Bluetooth radios for the night.
- **Why:** it tells us where the drain comes from. If the drain falls a lot, something that uses the network (the radio or an app syncing) is involved. If it stays around 2 %/h, the next night we try Safe mode, which tells us whether a downloaded app is involved.
- **Downsides:** no calls, messages or notifications overnight.
- **To undo:** turn Airplane mode off in the morning.

**Re-test**
- Same place and charge level if possible, about 8 h, not charging, not touched.
- Send me the bedtime and wake-up % with times.
- Before you charge, send a screenshot of Settings > Battery > View details.
- Also, roughly when was your last software update?
