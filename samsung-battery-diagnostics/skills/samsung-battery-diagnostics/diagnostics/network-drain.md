# Module C — Network-related drain

5G versus 4G, weak signal, mobile data, Wi-Fi and Bluetooth, SIM issues.

## What Samsung says (official)
- 5G can use more power because the phone may run 4G and 5G together; this can also cause slight heating. Samsung suggests switching to LTE in weak 5G areas [V S9].
- Network mode path: Settings > Connections > Mobile networks > Network mode [V S17].
- Both phones are **5G Sub-6 only** (no mmWave in Samsung's band lists) [V S1, S4]. Bands differ by region and between the two models (e.g. n66 is listed for the M15 5G Indonesian unit but not for the A14 5G Philippine unit). If the user's carrier 5G band is missing, the phone simply stays on LTE; that is not a fault.

## Evidence to request
- Status-bar network icon during the problem (5G / LTE / 4G+ / 3G) and signal bars.
- Location type: home, office, basement, travelling, rural.
- Wi-Fi on and connected? Mobile data on? Hotspot? Bluetooth devices connected?
- Dual SIM: how many active SIMs, and which has data?
- Any "No service" / "Emergency calls only" periods.

## Decision tree
```
C1. Weak signal (≤1–2 bars, frequent drops) where the drain happens?
    yes, on mobile data → WEAK_SIGNAL. INT-NET-01 (use Wi-Fi there); confirm with TEST-AIRPLANE overnight.
    yes, on Wi-Fi       → weaker effect; still possible (cellular registration remains). Check C4.
C2. On 5G with weak or fluctuating 5G (icon flips 5G↔LTE)?
    yes → NETWORK_5G. INT-NET-02 (switch to LTE) for one comparable test period.
C3. Hotspot used, or Bluetooth accessories connected continuously?
    yes → CONNECTIVITY_EXTRAS. INT-NET-03 if not needed.
C4. Second SIM in a poor-coverage area or unused?
    yes → INT-NET-04.
C5. Mobile data use very high (Settings > Connections > Data usage) by an app?
    yes → Module E for that app.
C6. None → network is not the leading hypothesis; return to Module A/B.
```

## Controlled 5G vs LTE comparison (both devices)
1. Night 1 (or same 3 h idle block): current Network mode with 5G, same place, Wi-Fi as usual. Record % and times.
2. Change only Network mode to the LTE option (INT-NET-02).
3. Night 2: identical conditions. Compare with `battery_diag.py compare`.
4. If improvement > uncertainty and the user does not need 5G speeds there, keep LTE; otherwise revert.

## Do not
- Do not claim 5G "always" drains more; it depends on coverage. Present it as a testable hypothesis unless the comparison shows it.
- Do not recommend carrier-specific hidden menus, dialler codes or band-locking apps.
