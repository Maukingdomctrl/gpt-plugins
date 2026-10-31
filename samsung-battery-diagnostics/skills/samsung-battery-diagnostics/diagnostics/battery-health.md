# Module F — Battery health

Battery ageing, charging behaviour, temperature, capacity-degradation indicators, and separating software drain from physical wear.

## Safety first
Swelling, screen or back lifting, burning or chemical smell, smoke, phone too hot to hold, or liquid damage → **SAFE-01** immediately. Do not continue diagnostics.

## Evidence to request
1. **Samsung Members** > Support > Phone diagnostics > **Battery status**: Normal / Weak / Bad [V S13, S14].
2. Phone age (purchase month) and how it is usually charged (overnight, many short charges, hot environments).
3. Unexpected shutdowns: at what % shown? In cold conditions? [V S14 lists sudden shutdowns, especially in cold, as a sign].
4. Does the % jump (e.g. 30 % → 5 %) or freeze?
5. Temperature: does the phone get hot when idle or charging? Optional: `dumpsys battery` temperature (`workflows/adb-evidence.md`).
6. A clean standby measurement (Module B) and, if possible, a TEST-AIRPLANE night.

## Software drain vs battery wear
| Indicator | Points to software/usage | Points to battery wear |
|---|---|---|
| Battery usage screen | One app/system item dominates | Normal-looking distribution, just runs out sooner |
| Airplane-mode standby | Much lower than normal standby | Still high (only if nothing else is running) |
| Safe-mode standby | Much lower | Unchanged |
| Samsung Members | Normal | Weak or Bad |
| Shutdowns | No | Shuts down with charge remaining, esp. in cold |
| % behaviour | Smooth | Sudden jumps/drops |
| Onset | After an install/update/setting change | Gradual over months/years |

## Decision tree
```
F1. Safety sign? → SAFE-01. Stop.
F2. Members status Bad → BATTERY_DEGRADATION (high). INT-HEALTH-02.
F3. Members status Weak + (shutdowns with charge left OR % jumps) → BATTERY_DEGRADATION (high). INT-HEALTH-02.
F4. Members status Weak, no other sign → medium. Also check software causes (Modules A–E); re-measure.
F5. Members Normal + shutdowns at ≥10 % → conflicting; ask for a second diagnostic run and a service-centre test.
F6. Members Normal, no shutdowns/jumps → wear is NOT supported; pursue software causes.
F7. Age ≥ 24 months alone → only a weak hypothesis; never recommend replacement on age alone.
```

## Temperature
- Samsung: charge at room temperature; very high or low temperatures slow charging; the phone may stop charging when hot [V S15, S16].
- Heat when idle is a symptom of background activity or poor signal, not proof of a bad battery.
- With `dumpsys battery`, temperature is in tenths of °C (e.g. `temperature: 352` = 35.2 °C). Do not cite a "safe limit" number; none is published for these models. Describe readings relative to the room temperature and the user's other readings.

## Not allowed
- **No battery calibration** advice (full discharge to 0 %, "calibration apps", deleting batterystats). Samsung's guidance does not ask for it.
- No replacement recommendation without F2/F3 evidence or a service-centre result.
- No capacity % estimate (e.g. "your battery is at 78 %") unless the user's phone reports one; Samsung Members gives a status, not a capacity figure [V S13 describes three statuses only].

## Device notes
- **A14 5G** (2023 launch): more units are now at an age where wear is plausible, but it still needs evidence.
- **M15 5G** (2024 launch): younger; wear is less likely as a first explanation.
- Battery protection (INT-HEALTH-03) may slow future wear; it does not fix drain.
