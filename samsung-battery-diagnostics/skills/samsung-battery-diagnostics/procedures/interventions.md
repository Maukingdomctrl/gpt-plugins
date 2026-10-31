# Intervention catalogue

Every recommendation the assistant makes must come from this file and must keep all six fields: **Device**, **Path**, **What it does**, **Why it may help**, **Disadvantages**, **How to reverse**. Add the verification label for the path.

Path labels: **[V]** path quoted from an official Samsung page (source ID), **[R]** path reported by a reliable source, **[U]** expected path, not verified for this device/One UI version. For [U] paths, tell the user: *"Menu names vary by One UI version; if you can't find it, use the search icon in Settings and type `<keyword>`."*

**Path variants.** Samsung moved battery settings between versions. Give the user both forms when you do not know which they have:
- *Newer form* (e.g. One UI 7/8): `Settings > Battery > …`
- *Older form* (e.g. One UI 5/6): `Settings > Battery and device care > Battery > …`
The exact One UI version where the change happened is **[U]**; do not state it.

**Rule:** apply at most **two** interventions per round, then re-measure (`workflows/controlled-testing.md`).

---

## Safety

### SAFE-01 — Stop and get the battery inspected
- **Device:** M15 5G and A14 5G.
- **Trigger:** swelling (screen or back lifting, gaps), burning/chemical smell, phone too hot to hold, liquid damage, smoke.
- **Action:** stop charging, unplug, power off if safe, keep away from flammable items, do not puncture or press the battery, and contact an authorised Samsung service centre.
- **Why:** these are physical-hazard signs, not software drain.
- **Disadvantages:** phone unavailable until inspected.
- **Reverse:** n/a.

---

## Diagnostic tests (change nothing permanently)

### TEST-SAFE — Safe mode comparison
- **Device:** both.
- **Path [R]:** press and hold the Side key (or open the power menu from Quick settings) > touch and hold **Power off** > tap **Safe mode**. Restart normally to exit.
- **What it does:** starts the phone with downloaded apps disabled for that session.
- **Why:** if a standby test in Safe mode shows much lower drain than a comparable normal test, a downloaded app is the likely cause, so a factory reset is not needed.
- **Disadvantages:** downloaded apps and their notifications do not work during the test; home-screen widgets may need re-adding afterwards.
- **Reverse:** restart the phone.

### TEST-AIRPLANE — Airplane-mode standby comparison
- **Device:** both.
- **Path [R]:** Quick settings panel > **Airplane mode**.
- **What it does:** turns off cellular, Wi-Fi and Bluetooth radios.
- **Why:** if overnight drain falls sharply in airplane mode under otherwise identical conditions, the network (signal, 5G, data apps) is implicated. If drain stays high with radios off and no apps running, suspect battery health or a stuck process.
- **Disadvantages:** no calls, SMS or notifications during the test. Do not use when the user must be reachable.
- **Reverse:** toggle Airplane mode off.

---

## Applications

### INT-APP-01 — Put a specific app into "Deep sleeping apps"
- **Device:** both.
- **Path [V S8, S9]:** Settings > Battery (and device care) > Battery > **Background usage limits** > **Deep sleeping apps** > **+** > select the app > Add.
- **What it does:** the app never runs in the background; it works only when opened.
- **Why:** the evidence shows this app using a large share of battery while the user rarely has it open.
- **Disadvantages:** notifications, sync and background tasks for that app may stop (Samsung: may not receive updates or notifications). **Do not** deep-sleep messaging, calendar, alarm, health, banking-OTP, or work apps the user relies on.
- **Reverse:** same screen > ⋮ > Remove > select the app.

### INT-APP-02 — Restrict or optimise the app's battery use
- **Device:** both.
- **Path [V S9]:** Settings > Apps > ⋮ (More options) > Special access > **Optimise battery usage** > select the app. **Newer One UI [U]:** Settings > Apps > *app* > Battery > **Optimised** / **Restricted**.
- **What it does:** limits some background functions of that app.
- **Why:** a milder alternative to deep sleep for an app the user needs but which uses too much in the background.
- **Disadvantages:** delayed notifications or background sync for that app.
- **Reverse:** set it back to Unrestricted/Not optimised on the same screen.

### INT-APP-03 — Update, then (if needed) temporarily uninstall the suspect new app
- **Device:** both.
- **Path [R]:** Play Store/Galaxy Store > Manage apps > Update. To remove: Settings > Apps > *app* > Uninstall.
- **What it does:** removes the suspected cause for one test period.
- **Why:** the drain started after this app was installed/updated, and it appears in battery usage.
- **Disadvantages:** loss of the app's local data unless it is backed up or synced; reinstall needed.
- **Reverse:** reinstall from the store and sign back in.

### INT-APP-04 — Change an app's location permission to "Allow only while using the app"
- **Device:** both.
- **Path [U]:** Settings > Location > **App permissions** > *app* > Allow only while using the app (or Settings > Apps > *app* > Permissions > Location).
- **What it does:** stops background GPS/location requests by that app.
- **Why:** apps allowed location "all the time" can wake the phone and GPS while idle.
- **Disadvantages:** features like background trip tracking, geofenced reminders or family location sharing stop working for that app.
- **Reverse:** set it back to "Allow all the time".

### INT-APP-05 — Turn off auto-sync for unneeded accounts
- **Device:** both.
- **Path [R]:** Settings > Accounts and backup > Manage accounts > select account > **Sync account** (turn off individual items) or turn off **Auto sync data**.
- **What it does:** stops periodic background synchronisation for that account/data type.
- **Why:** frequent sync of many accounts adds wake-ups during standby.
- **Disadvantages:** email, contacts, calendar or photos stop updating automatically for that account. Never turn off sync the user depends on without telling them.
- **Reverse:** turn sync back on.

---

## Temporary / system

### INT-WAIT-01 — Let post-update work finish, then re-measure
- **Device:** both.
- **Action:** after a major update or new setup, keep using the phone normally for **2–3 days**, make sure apps are updated, restart once, then repeat the same measurement.
- **Why:** Samsung says battery life on a new phone "typically improves after a few days of regular use" [V S9]; similar background work after a major update is a **hypothesis**, tested by re-measuring.
- **Disadvantages:** the user waits a few days.
- **Reverse:** n/a.

### INT-SYS-01 — Investigate a high "system" entry without disabling anything
- **Device:** both.
- **Action:** (1) tap the system entry in battery usage to see details, if available; (2) restart the phone once; (3) check Settings > Software update; (4) run **TEST-SAFE** to see whether a downloaded app is driving it.
- **Why:** entries like Android System, Google Play services or Samsung services often carry work requested by apps, sync or location.
- **Disadvantages:** time; restart closes open apps.
- **Reverse:** n/a. **Never** disable, force-stop or "freeze" system/Google/Samsung services, or use ADB to uninstall them.

### INT-OPT-01 — Device care "Optimise now"
- **Device:** both.
- **Path [V S9]:** Settings > Battery and device care (newer: Device care) > **Optimise now**.
- **What it does:** closes background apps, manages abnormal battery usage, scans for crashed apps and malware.
- **Why:** low-risk one-off clean-up when an app is stuck in the background.
- **Disadvantages:** closes open apps; not a lasting fix and not a diagnosis.
- **Reverse:** n/a.

---

## Network

### INT-NET-01 — Prefer Wi-Fi where cellular signal is weak (and the radio test)
- **Device:** both.
- **Path [R]:** Settings > Connections > Wi-Fi.
- **What it does:** moves data traffic to Wi-Fi.
- **Why:** with weak cellular signal the modem transmits at higher power and searches more often.
- **Disadvantages:** needs a trusted Wi-Fi network; the phone still stays registered on cellular for calls, so drain is reduced but not removed.
- **Reverse:** turn Wi-Fi off.

### INT-NET-02 — Switch Network mode from 5G to LTE (4G)
- **Device:** both (5G Sub-6 only on both).
- **Path [V S17]:** Settings > Connections > Mobile networks > **Network mode** > choose the option **without** 5G, e.g. "LTE/3G/2G (auto connect)". Option names vary by carrier/region [U].
- **What it does:** prevents the phone from using 5G.
- **Why:** Samsung says 5G can use more power because the phone may use 4G and 5G at the same time, and suggests switching to LTE in weak 5G areas [V S9].
- **Disadvantages:** lower peak data speed where 5G is good; some carriers' plans or features may expect 5G.
- **Reverse:** choose the option that includes 5G again (e.g. "5G/LTE/3G/2G (auto connect)").
- **Per-SIM note:** on dual-SIM phones the setting is per SIM; change only the SIM used for data.

### INT-NET-03 — Turn off hotspot / unused Bluetooth, review scanning
- **Device:** both.
- **Path [R / U]:** Quick settings > Mobile Hotspot, Bluetooth. Scanning [U]: Settings > Location > Location services > Wi-Fi scanning / Bluetooth scanning.
- **What it does:** stops radios and scans the user is not using.
- **Why:** hotspot is a heavy continuous load; scanning wakes radios even when Wi-Fi/Bluetooth are "off".
- **Disadvantages:** turning off scanning can reduce location accuracy and Nearby device discovery.
- **Reverse:** turn them back on.

### INT-NET-04 — SIM checks
- **Device:** both.
- **Path [U]:** Settings > Connections > **SIM manager** > toggle the unused SIM off.
- **What it does:** stops that SIM's network registration and searching.
- **Why:** each active SIM keeps its own radio registration; a SIM in poor coverage keeps searching.
- **Disadvantages:** no calls/SMS on that SIM while off.
- **Reverse:** toggle the SIM back on.

---

## Display

### INT-DISP-01 — Use Adaptive brightness or lower brightness
- **Device:** both.
- **Path [V S10]:** Settings > Display > **Adaptive brightness**; brightness slider in Quick settings.
- **What it does:** adjusts brightness to ambient light / lowers backlight (A14 5G) or pixel power (M15 5G).
- **Why:** the display is a major screen-on load; manual high brightness indoors wastes power.
- **Disadvantages:** screen may look dimmer; outdoor readability lower.
- **Reverse:** turn Adaptive brightness off / raise the slider.

### INT-DISP-02 — Shorter screen timeout
- **Device:** both.
- **Path [V S10]:** Settings > Display > **Screen timeout** > 30 seconds (Samsung default) or 15 seconds (most saving).
- **What it does:** screen turns off sooner when untouched.
- **Why:** long timeouts keep the screen lit while unused.
- **Disadvantages:** screen turns off while reading; the user must tap more.
- **Reverse:** choose the previous timeout.

### INT-DISP-03 — Motion smoothness to Standard (60 Hz)
- **Device:** both (both have up to 90 Hz panels [V]).
- **Path [R S22 for A14 5G; U for M15 5G]:** Settings > Display > **Motion smoothness** > Standard.
- **What it does:** caps refresh at 60 Hz instead of up to 90 Hz.
- **Why:** higher refresh rates use more power during screen-on time.
- **Disadvantages:** scrolling and animations look less smooth.
- **Reverse:** choose Adaptive/High again.

### INT-DISP-04 — Always On Display off or "Tap to show" (M15 5G only)
- **Device:** **Galaxy M15 5G only.** The A14 5G has no AOD.
- **Path [U]:** Settings > Lock screen (and AOD) > **Always On Display** > off, or set "Tap to show" / "Show as scheduled".
- **What it does:** the screen stays dark while the phone is idle.
- **Why:** AOD keeps part of the display and processor active during standby.
- **Disadvantages:** you can't glance at time and notifications without waking the phone.
- **Reverse:** turn AOD back on.

### INT-DISP-05 — Dark mode (M15 5G only)
- **Device:** **Galaxy M15 5G only** (AMOLED). Not useful on the A14 5G LCD.
- **Path [U]:** Settings > Display > **Dark**.
- **What it does:** dark backgrounds; AMOLED pixels showing black use little power.
- **Why:** on AMOLED, display power depends on content brightness; dark content lowers screen-on drain (amount not published for this model — measure it).
- **Disadvantages:** personal preference; some content is harder to read.
- **Reverse:** Settings > Display > Light.

---

## Power saving (not a diagnosis)

### INT-PWR-01 — Power saving
- **Device:** both.
- **Path [V S10]:** Settings > Battery > **Power saving** (options vary).
- **What it does:** restricts background network use, may turn off AOD, limit CPU and refresh rate.
- **Why:** extends runtime when needed. **It hides the cause rather than fixing it**, so do not use it as the fix during diagnosis and never during a measurement unless both runs use it.
- **Disadvantages:** delayed notifications/sync, lower performance.
- **Reverse:** turn Power saving off.

---

## Battery health

### INT-HEALTH-01 — Samsung Members battery diagnostic
- **Device:** both.
- **Path [V S13, S14]:** Samsung Members > **Support** > Phone diagnostics > **Get started** > **Battery status**. Results: Normal / Weak / Bad.
- **What it does:** Samsung's own battery check.
- **Why:** gives objective evidence before talking about replacement.
- **Disadvantages:** none; it is a rough status, not a capacity measurement.
- **Reverse:** n/a.

### INT-HEALTH-02 — Service-centre battery inspection
- **Device:** both.
- **Trigger (needs evidence):** Members status Weak/Bad **and** symptoms, or unexpected shutdowns with charge remaining, or swelling (→ SAFE-01).
- **Why:** Samsung advises a service-centre visit for Bad status or persistent symptoms [V S13, S14].
- **Disadvantages:** cost, time without phone; back up first.
- **Reverse:** n/a.

### INT-HEALTH-03 — Battery protection (long-term wear, not a drain fix)
- **Device:** both (availability and modes depend on One UI version [U] for A14 5G One UI Core).
- **Path [V S11, S15]:** Settings > Battery > **Battery protection**: Basic (stops at 100 %, resumes at 95 %), Adaptive / Sleep-time protection (holds ~80 % overnight), Maximum (fixed limit; on One UI 7+ choose 80/85/90/95 %). Older versions: a single "Protect battery" toggle limiting to 85 % [V S12].
- **What it does:** limits time spent at full charge.
- **Why:** may slow long-term wear; it does **not** reduce drain.
- **Disadvantages:** less runtime per charge with Maximum.
- **Reverse:** choose Basic or turn the toggle off.

---

## Charging

### INT-CHG-01 — Use an adapter that matches the phone
- **Device:** both, with different limits: **M15 5G up to 25 W** Super Fast Charging, adapter sold separately [V S1]; **A14 5G up to 15 W** Fast Charging [V S6]. Don't promise the M15's 25 W speed to an A14 5G user.
- **Action:** use a Samsung or certified USB-C adapter of the right class (a 25 W Samsung adapter for the M15 5G; a 25 W Samsung adapter also charges the A14 5G, but only at up to 15 W [R]), plugged into a wall socket, not a PC or TV USB port.
- **What it does:** lets the phone negotiate its fast-charging mode.
- **Why:** PC ports and low-power adapters cannot fast-charge [V S15, S16].
- **Disadvantages:** cost of a new adapter; slightly more heat during fast charging.
- **Reverse:** go back to the previous adapter.

### INT-CHG-02 — Turn on Fast charging
- **Device:** both.
- **Path [V S15]:** Settings > Battery > **Charging settings** > Fast charging (older [V S16]: Battery and device care > Battery > More battery settings > Fast charging / Super fast charging).
- **What it does:** enables the phone's fast-charging mode with a compatible adapter.
- **Why:** if the toggle is off, the phone charges at the slower standard rate on any adapter.
- **Disadvantages:** slightly more heat while charging.
- **Reverse:** turn the toggle off.

### INT-CHG-03 — Inspect port, swap cable
- **Device:** both.
- **Action [V S15]:** turn the phone off, shine a flashlight into the USB-C port, remove lint **without metal objects or liquids**; reconnect firmly; try another compatible cable and adapter.
- **What it does:** removes a poor electrical connection as a cause.
- **Why:** debris and worn cables cause slow or interrupted charging and heat [V S15, S16].
- **Disadvantages:** risk of damaging the port if forced; if unsure, ask a service centre.
- **Reverse:** n/a (nothing on the phone is changed).

### INT-CHG-04 — Moisture detected
- **Device:** both.
- **Action [V S15]:** unplug; gently shake out water; wipe; dry in a well-ventilated place with cool air; charge only when the port is completely dry.
- **What it does:** clears the condition the phone is protecting against.
- **Why:** charging stops while moisture is detected, and charging a wet port risks corrosion [V S15].
- **Disadvantages:** waiting time. Never use heat (hair dryer on hot) or insert objects.
- **Reverse:** n/a.

### INT-CHG-05 — Charge cool and idle
- **Device:** both.
- **Action [V S15, S16]:** charge at room temperature, out of direct sun/car dashboards; avoid gaming/video while charging; let a hot phone cool first; remove a thick case if the phone gets hot.
- **What it does:** keeps the phone below the temperature at which it slows or pauses charging.
- **Why:** the phone slows or pauses charging when hot; heavy use while charging also uses power that would otherwise go into the battery [V S16].
- **Disadvantages:** can't use the phone heavily while charging.
- **Reverse:** n/a.

### INT-CHG-06 — Explain Battery protection
- **Device:** both (option names depend on One UI version; availability on A14 5G One UI Core [U]).
- **Path [V S11, S15]:** Settings > Battery > **Battery protection**.
- **What it does:** shows whether a charge limit (80/85/90/95 % or the older 85 % toggle) is active.
- **Why:** charging that "stops" at those levels is by design, not a fault.
- **Disadvantages:** turning the limit off gives more runtime per charge but loses its long-term wear benefit.
- **Reverse:** choose Basic / turn off when a full charge is needed; turn it back on afterwards.

---

## No change

### INT-NONE-01 — Consumption is within the expected range
- **Device:** both.
- **Disadvantages:** none; no setting is changed.
- **Action:** explain the measurement and the heuristic range; suggest no setting change. If the user wants more runtime anyway, offer INT-DISP-01/02 or INT-PWR-01 with trade-offs.

---

## LAST-RESORT — Factory data reset (never an early step)
Only discuss when **all** are true: two or more rounds of targeted changes failed with comparable measurements; TEST-SAFE was done and drain persists in Safe mode; software is up to date; Members battery status is Normal (else battery first); the user has a full backup.
- **Path [R]:** Settings > General management > Reset > Factory data reset.
- **Disadvantages:** erases all data; hours of setup; restoring the same apps can bring the problem back.
- **Reverse:** cannot be undone; restore from backup.
Recommend a service-centre software check as an alternative first.
