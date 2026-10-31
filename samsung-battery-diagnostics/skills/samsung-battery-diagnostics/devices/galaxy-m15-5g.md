# Samsung Galaxy M15 5G (SM-M156B)

Labels: [V] official Samsung, [R] reliable third party, [U] unverified. Source IDs → `references/samsung-documentation.md`. Specs can vary by region; when in doubt, ask the user to check their phone.

## Identity
| Item | Value | Basis |
|---|---|---|
| Model codes | SM-M156B, SM-M156B/DS, SM-M156B/DSN; retail SKUs e.g. SM-M156BZAVXID, SM-M156BDBVXID | [V] S1; /DS, /DSN suffixes [R] |
| Launch | India 8 April 2024 | [V] S2 |
| RAM / storage | 4 GB + 128 GB and 6 GB + 128 GB in India; 6 GB in Indonesia; microSD up to 1 TB | [V] S2, S1 |

## Battery and charging
| Item | Value | Basis |
|---|---|---|
| Capacity | 6,000 mAh **typical**; **5,880 mAh rated** (IEC 61960) | [V] S1 |
| Wired charging | Up to 25 W "Super Fast Charging"; **25 W adapter sold separately** | [V] S1 |
| India launch offer | Bundled 25 W travel adapter for a limited period (so some users have one, many do not) | [V] S2 |
| Wireless charging | Not listed on Samsung specs | [U] treat as not supported |
| Port | USB Type-C, USB 2.0 | [V] S1 |
| Video playback (Samsung claim) | Up to 25 h | [V] S1 (lab claim, not a diagnostic baseline) |
| Super Fast Charging protocol | Samsung 25 W chargers use USB PD with PPS | [U] not stated on the M15 5G page; a non-PPS charger may show only "Fast charging" or "Charging" |

## Processor and modem
| Item | Value | Basis |
|---|---|---|
| Chipset | MediaTek Dimensity 6100+ | [V] S2 |
| CPU | Octa-core, 2.2 GHz + 2.0 GHz | [V] S1 |
| Modem | Integrated in the Dimensity 6100+ (5G Sub-6 only, no mmWave listed) | [V] bands S1; integration [R] |

## Display
| Item | Value | Basis |
|---|---|---|
| Panel | 6.5" Super AMOLED, 1080 × 2340 (FHD+) | [V] S1 |
| Refresh rate | Up to 90 Hz | [V] S1 |
| Brightness | 800 nits in High Brightness Mode; Vision Booster | [V] S1 |
| Always On Display | AMOLED panel → AOD is expected to be available | [U] confirm menu on the user's phone |

AMOLED: black pixels are off, so **dark mode and dark wallpapers can reduce display power**; this does **not** apply to the A14 5G (LCD).

## Network (Indonesia SM-M156B listing; bands vary by region)
| Item | Value | Basis |
|---|---|---|
| 2G / 3G | GSM 850/900/1800/1900; UMTS B1/2/4/5/8 | [V] S1 |
| 4G FDD | B1, 2, 3, 4, 5, 7, 8, 12, 17, 20, 26, 28, 66 | [V] S1 |
| 4G TDD | B38, 40, 41 | [V] S1 |
| 5G FDD Sub-6 | n1, 3, 5, 7, 8, 20, 28, 66 | [V] S1 |
| 5G TDD Sub-6 | n38, 40, 41, 77, 78 | [V] S1 |
| Wi-Fi | 802.11 a/b/g/n/ac, 2.4 + 5 GHz | [V] S1 |
| Bluetooth | 5.3 | [V] S1 |
| SIM | Dual SIM, Nano; Indonesian unit: SIM 1 + hybrid (SIM or microSD) | [V] S1 |
| NFC | Yes (Indonesia listing) | [V] S1; varies by region [U] |
| GNSS | GPS, GLONASS, BeiDou, Galileo, QZSS | [V] S1 |

## Software
| Item | Value | Basis |
|---|---|---|
| Launch OS | Android 14 with One UI 6.x (sources disagree on 6.0 vs 6.1) | [R] |
| Update promise | Four generations of OS upgrades, five years of security updates | [V] S2 |
| Updates observed | One UI 7 (Android 15) [R]; One UI 8 (Android 16) rolled out from Oct 2025 (first in Korea on the local counterpart, then other regions) [R] S19; Samsung product page lists Android 15 and Android 16 user manuals [V] S1 | |
| Later versions | Reports of One UI 8.5 exist | [U] |

**Always ask the user for their exact One UI version.** Most M15 5G units are on One UI 7 or 8 in late 2026, but some may not have updated.

## Battery management settings (verify the path on the user's One UI version)
| Feature | Expected path | Notes |
|---|---|---|
| Battery usage by app, screen on/off time | Settings > Battery > View details (newer); Settings > Battery and device care > Battery (older) | [V] S10, S9 |
| Background usage limits (sleeping / deep sleeping / never sleeping apps) | Settings > Battery (and device care) > Background usage limits | [V] S8, S9 |
| Optimise battery usage per app | Settings > Apps > ⋮ > Special access > Optimise battery usage | [V] S9; may differ on One UI 7+ (see app's Battery page) [U] |
| Power saving | Settings > Battery > Power saving | [V] S10 |
| Battery protection | Settings > Battery > Battery protection: Basic / Adaptive (or Sleep-time protection) / Maximum; on One UI 7+ Maximum limit selectable 80/85/90/95 % | [V] S11; option names vary [U] |
| Fast charging toggle | Settings > Battery > Charging settings > Fast charging | [V] S15 |
| Motion smoothness | Settings > Display > Motion smoothness | [U] option names on this device |
| Always On Display | Settings > Lock screen (and AOD) > Always On Display | [U] |
| Network mode | Settings > Connections > Mobile networks > Network mode | [V] S17 |
| Battery status check | Samsung Members > Support > Phone diagnostics > Battery status | [V] S13 |

## Known battery-related issues
- **No official Samsung acknowledgement** of a battery fault specific to the M15 5G was found (searched Oct 2026).
- Samsung Community threads contain **isolated user reports** of drain or heat after major updates (One UI 7, Android 16) [anecdotal, S24]. Responses there are community suggestions (re-indexing after updates, deep-sleeping unused apps), not confirmed root causes. **Do not present this as a known issue.** It only supports the general hypothesis "temporary post-update background work", which must be tested by re-measuring after a few days.
