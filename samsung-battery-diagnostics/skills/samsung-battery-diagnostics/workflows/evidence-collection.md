# Evidence collection and analysis (Steps 4–6)

## Step 4 — Ask only for what the symptom needs
| Tag | Required evidence |
|---|---|
| `rapid_screen_on` | active measurement (start %, end %, screen-on time, workload), battery usage screenshot, display settings, network |
| `overnight` / `idle` | standby measurement (bedtime %/time, morning %/time, no charging), battery usage screenshot before charging, network overnight |
| `after_install` | app name + install/update date, battery usage screenshot, standby measurement |
| `5g` | network icon + signal, standby measurement, battery usage screenshot |
| `weak_signal` | signal bars / location, standby measurement |
| `slow_charging` | adapter/cable/source, charging message, timed charging run, heat, Fast charging toggle, stop % |
| `degradation` | Samsung Members battery status, age, shutdown % and conditions, standby measurement |

Always useful: device temperature impressions (cool / warm / hot) and recent updates.

### Checklist wording (send as one message)
- **Battery usage screenshot:** newer One UI: Settings > Battery > View details; older: Settings > Battery and device care > Battery. Take it **before** charging. [V S10]
- **Screen-on time:** shown on that same screen (Screen on time / Screen off time) [V S10].
- **Start and end %:** write down the % and the clock time at the start and end of the period.
- **Overnight:** % and time at bedtime and on waking; don't charge overnight for this test.
- **Network:** 5G or LTE icon, signal bars, Wi-Fi on/off.
- **Temperature:** cool / warm / hot to the touch (or `dumpsys battery` value, see `adb-evidence.md`).

### When the user sends a screenshot
- Read only what is visible; quote names and % exactly. If text is unreadable, say so and ask.
- Note the period it covers ("since last full charge"/"last 24 hours"/"last 7 days" — depends on One UI version).
- Never infer values that are not on the screenshot.

### When the user can't provide something
State the consequence, e.g. "Without the screen-on time I can't separate screen use from background drain, so I'll treat the cause as unconfirmed."

## Step 5 — Analyse
1. Validate each measurement (see `controlled-testing.md` validity rules).
2. Compute rates (`scripts/battery_diag.py rate` or the formulas in `SKILL.md`), showing arithmetic.
3. Classify with heuristic bands and say they are heuristics.
4. Build two lists:
   - **Observed / Calculated:** facts and arithmetic.
   - **Hypotheses:** possible causes, each with the evidence for and against.

## Step 6 — Rank
Use `scripts/battery_diag.py rank evidence.json` or apply the same scoring by hand:
| Evidence | Cause | Points |
|---|---|---|
| Safety sign | SAFETY_STOP | overrides all |
| App ≥15 % share, mostly background / rarely used, or with elevated standby | APP_BACKGROUND | +3 (else +1) |
| Drain began ≤14 days after install/update | RECENT_INSTALL | +2; +3 more if app ≥10 % share |
| System item ≥20 % | SYSTEM_PROCESS | +2 |
| Update ≤3 days ago | POST_UPDATE_SETTLING | +2 (hypothesis) |
| Weak signal on mobile data | WEAK_SIGNAL | +3; +2 more if standby elevated |
| On 5G | NETWORK_5G | +1; +2 if weak/fluctuating; +1 if user links drain to 5G |
| Hotspot / BT accessories | CONNECTIVITY_EXTRAS | +2 |
| Manual high brightness with elevated screen-on drain | DISPLAY | +2; screen top consumer +1; timeout ≥5 min +1; AOD (M15) with elevated standby +1 |
| Location "all the time" with elevated standby; heavy sync | LOCATION_SYNC | +1 each |
| Members Bad / Weak / Normal | BATTERY_DEGRADATION | +5 / +3 / −2 |
| Shutdown with ≥10 % left; % jumps; age ≥24 months | BATTERY_DEGRADATION | +3; +2; +1 |
| PC port or adapter below device max | CHARGER_UNDERPOWERED | +3 |
| Fast charging off; moisture warning; stop at limit | FAST_CHARGING_OFF / MOISTURE / CHARGE_LIMIT | +4 each |
| Cable/port/interruptions; hot or used while charging | CABLE_PORT / THERMAL_CHARGING | +3 / +2 |
| All measured rates expected, no safety/degradation | WITHIN_EXPECTED | +3 |
| Measured rate elevated/abnormal but no cause reached 3 points | UNEXPLAINED_DRAIN → TEST-AIRPLANE, TEST-SAFE | +2 |

Confidence: **high** ≥5 points with at least one observation; **medium** 3–4; **low** <3.
Present at most the top three causes, each with its points basis and confidence. If required evidence is missing, list it and ask **before** naming a cause.
