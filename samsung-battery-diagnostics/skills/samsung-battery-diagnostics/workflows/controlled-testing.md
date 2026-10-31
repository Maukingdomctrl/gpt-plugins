# Controlled testing (Steps 7–8)

## Principle
Change **one thing** (at most two closely related things) between a **before** run and an **after** run, and keep everything else the same. Otherwise the result cannot be attributed.

## Measurement types
| Type | When | How |
|---|---|---|
| `standby` | overnight / idle complaints | Note % and time at bedtime; don't touch or charge; note % and time on waking. ≥6 h ideal (≥4 h minimum). |
| `active` | screen-on complaints | Note % and time; use the phone for a typical 1–2 h block of one workload type; note % and screen-on time (battery screen) at the end. |
| `mixed` | normal day | Full day with screen-on time from the battery screen; needs a standby baseline from a separate night to split screen-on from idle. |
| `charging` | slow charging | Start 20–40 %, screen off, idle, room temperature; 20–30 min; note start %, end %, minutes, adapter, cable. |

## Validity rules (apply before analysing)
1. Not charged during a drain window.
2. Drop (or gain) **≥3 percentage points**; the 1 % display step causes ±1 point uncertainty.
3. Standby: screen-on time under 5 % of the window.
4. Same device, same measurement type.
5. Power saving mode either off in both runs or on in both.

## Comparable conditions (record for both runs)
- Network mode (5G/LTE), Wi-Fi connected or not, signal bars, location (home/office/travel).
- Workload type (for active runs).
- Temperature (cool/warm/hot environment).
- Connected accessories, hotspot.
- Number of changes made since the before run (should be 1–2).

## Step 7 → 8 message pattern
"Here's the one change to test: **[intervention, device, path]**. It does X; it may help because Y; the downside is Z; to undo it, W.
Please repeat **exactly the same test** as before: [type], [duration], same place and network, not charging. Send me the start/end % and times (and the battery usage screenshot)."

## Logging
Offer `templates/measurement-log.csv` (one row per run). The assistant fills in the calculated columns.
