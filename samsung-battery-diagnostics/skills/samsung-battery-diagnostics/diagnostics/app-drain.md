# Module E — Application diagnosis

Excessive background activity, poorly optimised apps, recently installed apps, location access, notifications and sync.

## Evidence to request
1. Battery usage screenshot (Module A) and, for the top 1–3 apps, the app detail screen (tap the app) showing foreground vs background use if available.
2. Apps installed or updated just before the drain started, with dates.
3. How often the user actually opens the top apps.
4. Location permission of the suspect app: Settings > Apps > *app* > Permissions > Location [U path].
5. Number of accounts syncing (Settings > Accounts and backup > Manage accounts) [R].
6. Notification volume: does the app send many notifications?

## Decision tree
```
E1. Is one app ≥15 % of usage?
    no → app cause is unlikely; go back to Module A/B/C.
E2. Was the user actively using it for most of that share? (e.g. 2 h of video app = expected)
    yes → expected; offer display/network levers instead.
E3. Mostly background, or the user rarely opens it?
    yes → APP_BACKGROUND.
          First: update the app (INT-APP-03 update part).
          Then: INT-APP-02 (optimise/restrict) if the user needs its notifications,
                INT-APP-01 (deep sleep) if they don't.
E4. Drain began within ~14 days after installing/updating it?
    yes → RECENT_INSTALL. Update; if still high, uninstall for one test period (INT-APP-03).
E5. App has location "Allow all the time" with no clear need?
    yes → INT-APP-04.
E6. Heavy sync / many accounts?
    yes → INT-APP-05 for unneeded accounts.
E7. Unsure which app? → TEST-SAFE for one comparable period.
```

## Messaging, alarm, health and work apps
If the top app is one the user relies on for timely notifications (WhatsApp, email, alarm, banking OTP, medical/health monitoring, work MDM), **do not** deep-sleep it. Prefer INT-APP-02, and explain the delay risk explicitly.

## Device notes
Paths are the same pattern on both devices but **One UI Core (A14 5G)** and older One UI versions may show different labels. Use Settings search ("sleeping", "background", "optimise").

## Do not
- Do not recommend "task killer", "cleaner", "booster" or "battery saver" apps.
- Do not tell users to swipe away all recent apps routinely; it can increase drain from app restarts (present as a hypothesis if raised; no official source found).
- Do not name an app as malicious without evidence.
