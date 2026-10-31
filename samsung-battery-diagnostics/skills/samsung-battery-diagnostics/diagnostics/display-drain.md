# Module D — Display-related drain

Brightness, screen timeout, refresh rate (Motion smoothness), Always On Display (M15 5G only).

## Device differences (critical)
| | Galaxy M15 5G | Galaxy A14 5G |
|---|---|---|
| Panel | Super AMOLED [V S1] | PLS LCD [V S4] |
| Max refresh | 90 Hz [V S1] | 90 Hz [V S4] |
| Always On Display | Expected available (AMOLED) [U menu] | **Not available** [R S23] |
| Dark mode saves power | Yes, meaningfully on dark content (AMOLED) | Not meaningfully (backlight stays on) |
| Peak brightness | 800 nits HBM [V S1] | Not stated on product page |

## Evidence to request
- Brightness: auto (Adaptive brightness) or manual; roughly how high.
- Screen timeout value.
- Motion smoothness setting.
- M15 5G only: AOD on/off and mode (always / tap to show / scheduled).
- Screen-on time and % used in that time; outdoor use?

## Decision tree
```
D1. Is screen-on drain elevated/abnormal for light or moderate use (Module A)?
    no → display changes are optional comfort trade-offs; say so.
D2. Manual brightness high indoors, or outdoors in sun for long periods?
    yes → INT-DISP-01.
D3. Screen timeout ≥ 2 min?  (≥5 min is a strong signal)
    yes → INT-DISP-02.
D4. Motion smoothness on Adaptive/High and drain still elevated after D2/D3?
    yes → INT-DISP-03 (one test round).
D5. M15 5G and standby elevated with AOD always on?
    yes → INT-DISP-04 (one night test).
D6. M15 5G user wants more saving and uses light themes → INT-DISP-05 (optional).
```
Apply no more than two of these per round.

## Do not
- Do not give AOD or dark-mode advice to A14 5G users.
- Do not state numeric power savings for any of these settings; none are published by Samsung for these models. Measure instead.
