Thanks, that's enough to work with. I can't see your phone, so this is based only on what you've sent.

**Device:** Galaxy A14 5G (SM-A146B, Exynos 1330 [V]), One UI Core 7.0 / Android 15, battery 5,000 mAh typical [V].

**What you reported (Observed)**
- 90% → 50% in 3 h, screen-on 2 h 40 min, browsing on Wi-Fi (light use).
- Battery usage: Facebook 35% (mostly background, you rarely open it), Screen 20%.
- Adaptive brightness on, screen timeout 30 s, Motion smoothness Adaptive.

**What I worked out (Calculated)**
- Drop: 90 − 50 = 40 points.
- Screen-on rate: 40 ÷ 2.67 h = **15 %/h (±0.4)**. Only 20 min of the 3 h were screen-off, so I've counted the whole drop against screen-on time.
- 15 %/h × 5,000 mAh ÷ 100 = **750 mA-eq**. That's **elevated** for light use. The skill's rough guide for light use is: up to 600 expected, 600–900 elevated. These bands are rules of thumb, not Samsung figures.
- Facebook's 35% is a share of what the battery used, not 35% of the battery. If that list covers this same period, 35% of 40 points is about **14 points** going to an app you barely opened. If the list goes back to an earlier full charge, the number is different, but the share is still large.

**Likely causes, most likely first**
1. **Facebook running in the background.** Medium confidence. For: it has the biggest share (35%), mostly background, and you rarely open it. Against: this is one session's data.
2. Display: low. Brightness is automatic and the timeout is already short, and Screen is only 20%. So I'm not changing display settings this round.
Not supported: battery wear (nothing points to it) and network (you were on Wi-Fi).

**One change to test (Galaxy A14 5G, One UI Core 7.0)**
First, update Facebook in the Play Store (Manage apps > Update). Then do **one** of these, depending on whether you need Facebook notifications:
- **If you don't need Facebook notifications, put Facebook into Deep sleeping apps.**
  - **Path [V]:** Settings > Battery > Background usage limits > Deep sleeping apps > **+** > Facebook > Add. One UI Core may label this differently. If you can't find it, use the search icon in Settings and type `sleeping`.
  - **What it does:** Facebook only runs while you have it open.
  - **Why it may help here:** most of its use was in the background, even though you barely use it.
  - **Downsides:** no Facebook notifications or background refresh until you open the app.
  - **To undo:** same screen > ⋮ > Remove > Facebook.
- **If you want to keep its notifications, set Facebook's battery use to Restricted instead.**
  - **Path [U]:** Settings > Apps > Facebook > Battery > Restricted (older form: Settings > Apps > ⋮ > Special access > Optimise battery usage).
  - **What it does:** limits Facebook's background activity but doesn't stop it completely.
  - **Downsides:** notifications may arrive late.
  - **To undo:** set it back to Unrestricted or Optimised.

Don't change anything else this round, so we can tell whether this change made the difference.

**Re-test (keep it the same as last time)**
- Start around 90%, not charging. Browse on the same Wi-Fi for about 2½–3 h with the same display settings.
- Before you charge, send me:
  - the start and end % and the clock times,
  - the screen-on time,
  - a screenshot of Settings > Battery > View details.
