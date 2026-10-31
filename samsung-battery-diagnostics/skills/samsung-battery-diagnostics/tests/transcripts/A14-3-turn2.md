Thanks. I can't see your phone, so this is based only on what you've told me.

**Device:** Galaxy A14 5G (SM-A146B), One UI Core 7.0 / Android 15, 5,000 mAh typical [V].

**What you reported (Observed)**
- GameHub installed 5 days ago, and the battery has been worse since.
- Overnight: 70% → 58% in 8 h, on home Wi-Fi, with good LTE signal.
- GameHub shows 18% of battery use, mostly in the background, and you rarely play it.

**What I worked out (Calculated)**
- Drop: 70 − 58 = 12 points over 8 h, so **1.5 %/h (±0.13)**.
- 1.5 ÷ 100 × 5,000 = **75 mA-eq**. That's **elevated** on the skill's standby guide (up to 50 expected, 50–100 elevated). This is a rule of thumb, not a Samsung figure.
- 18% is GameHub's share of what the battery used. If the list covers this night, that's 18% of 12 points, or about 2 points. If it covers a longer period, the exact figure differs, but the share is still the largest.

**Likely causes, most likely first**
1. **The new GameHub install.** High confidence. The drain started within 5 days of installing it, it's among the top users at 18%, and that use is mostly in the background.
2. **GameHub running in the background** in general. Medium confidence. This is the same app, just viewed as a background-activity problem.
Network doesn't fit: you were on Wi-Fi with good LTE. Nothing points to battery wear.

**Changes to test. Both affect only GameHub, so we can still tell whether it's the cause.**

1. **Update GameHub.** Play Store or Galaxy Store > Manage apps > Update [R]. Newer versions sometimes fix background behaviour. Nothing to undo.
2. **Put GameHub into Deep sleeping apps.**
   - **Path [V]:** Settings > Battery > Background usage limits > Deep sleeping apps > **+** > GameHub > Add. One UI Core may name it slightly differently. If so, search Settings for `sleeping`.
   - **What it does:** GameHub runs only while you have it open.
   - **Why it may help here:** most of its use was in the background, and you rarely play.
   - **Downsides:** no GameHub notifications or background downloads and updates until you open it.
   - **To undo:** same screen > ⋮ > Remove > GameHub.

Don't change anything else.

**Re-test**
- One night under the same conditions: home Wi-Fi, not charging, about 8 h, phone not touched.
- Send me the bedtime and wake-up % with clock times.
- Before you charge, send a screenshot of Settings > Battery > View details.

If GameHub still uses a lot even in deep sleep, the next test is to uninstall it for one night. That loses any local game data unless it's synced.
