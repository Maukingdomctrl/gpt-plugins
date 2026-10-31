# Module G — Charging diagnosis

Slow charging, charging interruptions, cable/adapter problems, excessive heat while charging.

## Device charging specs (do not mix them)
| | Galaxy M15 5G | Galaxy A14 5G |
|---|---|---|
| Max wired | **25 W** Super Fast Charging [V S1] | **15 W** Fast Charging [V S6] |
| Adapter | Sold separately [V S1] (India launch offer bundled one for a limited period [V S2]) | Varies by region [U] |
| Wireless | Not listed [U] | Not listed [U] |
| Port | USB-C, USB 2.0 [V S1] | USB-C, USB 2.0 [V S4] |

Samsung does not publish an official 0–100 % charging time for either model on the pages consulted. **Do not quote charge times.** Compare the user's own timed runs.

## Evidence to request
1. Adapter: brand, wattage printed on it, USB-C or USB-A; or PC/TV/car port.
2. Cable: original? damaged? tried another?
3. What the phone says while charging (lock screen or Battery screen): e.g. "Super fast charging", "Fast charging", "Charging", "Charging slowly" [U exact labels by version].
4. Timed run: start %, end %, minutes, starting below 50 %, screen off, room temperature.
5. Was the phone used (games/video) or hot while charging?
6. Does charging start/stop repeatedly? Any **moisture detected** warning?
7. Does charging stop at 80/85/90/95 %? (Battery protection.)
8. Settings > Battery > Charging settings: Fast charging on? [V S15]

## Decision tree
```
G1. Safety sign (swelling, burning smell, too hot to hold)? → SAFE-01.
G2. Moisture warning? → INT-CHG-04 (MOISTURE). Stop other tests until dry.
G3. Stops at 80/85/90/95 %? → CHARGE_LIMIT. INT-CHG-06 (by design).
G4. Charging from PC/TV/car port or adapter below device max? → CHARGER_UNDERPOWERED. INT-CHG-01.
      M15 5G with 15 W adapter: "Fast charging" (not "Super fast") is expected [U label].
      A14 5G: 15 W is the maximum; a 25 W adapter will not make it faster than 15 W.
G5. Fast charging toggle off? → FAST_CHARGING_OFF. INT-CHG-02.
G6. Interruptions, loose plug, lint, damaged cable? → CABLE_PORT. INT-CHG-03.
G7. Hot or in heavy use while charging, or hot environment? → THERMAL_CHARGING. INT-CHG-05.
G8. Correct adapter, toggle on, clean port, cool, idle — still slow (no improvement in a
    comparable timed run with a second known-good cable and adapter)?
    → Members battery status (Module F) and service-centre inspection [V S15: persistent issues may be hardware].
```

## Controlled charging test
- Start between 20 % and 40 %, phone at room temperature, screen off, not in use, same adapter/cable/socket.
- Record start %, end % and minutes (20–30 min is enough). Use `battery_diag.py rate` with `kind: "charging"`.
- Change one thing (adapter or cable or setting), repeat from a similar start %. Compare with `compare`.
- Charging naturally slows near full; never compare a 20 % start with a 70 % start.

## Do not
- Recommend cheap uncertified adapters, or say any USB-C PD adapter will "Super fast charge" the M15 5G (protocol requirement is [U] on official pages).
- Promise faster than 15 W charging on the A14 5G.
