# Initial assessment (Steps 1–3)

## Step 1 — Identify the device
Ask: *"Please open Settings > About phone and tell me the **Model number** (e.g. SM-M156B/DSN or SM-A146B)."*
- Run `devices/device-identification.md` (or `scripts/battery_diag.py identify <code>`).
- Not supported → use the out-of-scope reply and stop.
- If the user only says "A14", **always** confirm it is the 5G model (SM-A146…) and not the A14 4G (SM-A145…).

## Step 2 — Software
Ask for (Settings > About phone > Software information):
- **One UI version** (e.g. 7.0, 8.0; A14 5G shows "One UI Core …").
- **Android version**.
- Optional: security patch level and when the last update was installed (needed for the post-update hypothesis).

Record them in the report. Use them to choose the path variant in `procedures/interventions.md`. If the user cannot find them, continue, but give both path variants.

## Step 3 — Problem description → symptom tags
Ask the user to describe the problem in their own words: *when* it drains, *how fast* (their numbers), *since when*, and *what changed* around then.

Map to tags (more than one is allowed):
| User says | Tag | Primary module |
|---|---|---|
| Drains fast while I use it | `rapid_screen_on` | A, D |
| Loses a lot overnight | `overnight` | B |
| Drains while I'm not using it / in my pocket | `idle` | B |
| Started after I installed / updated an app | `after_install` | E |
| Worse on 5G / since 5G | `5g` | C |
| Bad signal where I am / at home / at work | `weak_signal` | C |
| Charges slowly / stops charging / gets hot charging | `slow_charging` | G |
| Shuts down at X % / battery is old / health | `degradation` | F |

## Opening reply pattern
1. Confirm device and software (or ask).
2. Restate the problem neutrally with the user's own numbers labelled **Observed**.
3. Say what you **cannot** know yet ("I can't see your phone; I'll work from what you send").
4. Ask for the evidence checklist from `workflows/evidence-collection.md` for these tags only.
Do not give a list of generic tips before evidence arrives.
