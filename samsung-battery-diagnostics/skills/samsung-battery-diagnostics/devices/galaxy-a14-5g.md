# Samsung Galaxy A14 5G (SM-A146)

Labels: [V] official Samsung, [R] reliable third party, [U] unverified. Source IDs → `references/samsung-documentation.md`.

**Not the Galaxy A14 (4G/LTE, SM-A145…)**, which is a different phone. **Announced January 2023, not 2022** (see `device-identification.md`).

## Identity and variants
| Item | Value | Basis |
|---|---|---|
| Model codes | SM-A146B, SM-A146P, plus regional codes (SM-A146U/U1, SM-A146W, SM-A146M, …) | SM-A146P [V] S4; others [R] S20, S21 |
| Announcement | January 2023 (NL 10-01-2023, IN 16-01-2023, ID 19-01-2023) | [V] S5, S6, S7 |
| RAM / storage | 4/6/8 GB + 64/128 GB by region; microSD up to 1 TB | [V] S4 (6 + 128 PH); others [R] |

## Two chipset variants (do not mix them up)
| Variant | Chipset | CPU | Basis |
|---|---|---|---|
| SM-A146B (e.g. India, Europe) | Samsung Exynos 1330 | Octa-core | [V] S5 names Exynos 1330 for India; code mapping [R] S21 |
| SM-A146P (e.g. Philippines, Indonesia) | MediaTek Dimensity 700 | Octa-core 2.2 GHz + 2.0 GHz | [V] S6, S4 |
| Other suffixes | **[U]** | | third-party only |

Both variants share the same battery and charging specs below [V].

## Battery and charging
| Item | Value | Basis |
|---|---|---|
| Capacity | 5,000 mAh **typical**; **4,900 mAh rated** (IEC 61960) | [V] S4 |
| Wired charging | 15 W Fast Charging | [V] S6 |
| Adapter in box | Varies by region; Philippine buyers report cable only | [U] ask the user |
| Wireless charging | Not listed | [U] treat as not supported |
| Port | USB Type-C, USB 2.0 | [V] S4 |
| Samsung battery-life claim | "Up to 2 days", Strategy Analytics usage profile, pre-release units | [V] S4 (lab claim, not a diagnostic baseline) |

## Display
| Item | Value | Basis |
|---|---|---|
| Panel | 6.6" **PLS LCD**, 1080 × 2408 (FHD+) | [V] S4, S6 |
| Refresh rate | Up to 90 Hz | [V] S4, S6, S7 |
| Motion smoothness | Options reported as Adaptive and Standard | [R] S22 |
| Always On Display | **Not available** (LCD backlight cannot light individual pixels) | [R] S23 community + panel type [V]; if the user sees an AOD menu, ask for a screenshot |
| Inconsistency | Samsung India's release says "6.6" HD+"; Samsung NL, ID and the product page say FHD+ | Treat FHD+ as correct [V] majority; note the conflict |

LCD: **dark mode does not meaningfully reduce display power** (the backlight stays on). Brightness and screen-on time are the main display levers. Do not give AMOLED-only advice to A14 5G users.

## Network (SM-A146P Philippines listing; bands vary by region)
| Item | Value | Basis |
|---|---|---|
| 2G / 3G | GSM 850/900/1800/1900; UMTS B1/2/4/5/8 | [V] S4 |
| 4G FDD | B1, 2, 3, 4, 5, 7, 8, 12, 17, 20, 26, 28, 66 | [V] S4 |
| 4G TDD | B38, 40, 41 | [V] S4 |
| 5G FDD Sub-6 | n1, 3, 5, 7, 8, 20, 28 (no n66 on this listing) | [V] S4 |
| 5G TDD Sub-6 | n38, 40, 41, 77, 78 | [V] S4 |
| Wi-Fi | 802.11 a/b/g/n/ac, 2.4 + 5 GHz | [V] S4 |
| Bluetooth | 5.2 | [V] S4 |
| SIM | Dual SIM, Nano; SIM 1 + SIM 2 + dedicated microSD (PH listing) | [V] S4 |
| NFC | Yes (PH listing); varies by region | [V] S4, [U] elsewhere |

## Software
| Item | Value | Basis |
|---|---|---|
| Launch OS | Android 13, **One UI Core 5.0** | [V] S6 |
| Update promise | Two OS upgrades, four years of security updates | [V] S5, S7 |
| Final major update | Android 15 / One UI (Core) 7 (e.g. India, from mid-2025); not eligible for One UI 8 | [R] S18; Samsung product page lists Android 14 and 15 manuals [V] S4 |

**"One UI Core"** is a reduced feature set. Some features found on M15 5G may be missing or renamed. **Never assume a menu exists; ask the user to confirm or use Settings search.**

## Battery management settings (verify on device)
| Feature | Expected path | Notes |
|---|---|---|
| Battery usage by app, screen on/off time | Settings > Battery > View details (newer One UI, e.g. 7); Settings > Battery and device care > Battery (older, e.g. One UI 5) | [V] S10, S9 |
| Background usage limits | Settings > Battery (and device care) > Background usage limits | [V] S8, S9 |
| Power saving | Settings > Battery > Power saving | [V] S10 |
| Battery protection | Settings > Battery > Battery protection (modes vary by One UI version; older versions: a single 85 % limit toggle) | [V] S11, S12; availability on One UI Core [U] |
| Fast charging toggle | Settings > Battery > Charging settings > Fast charging (older: Battery and device care > Battery > More battery settings) | [V] S15, S16 |
| Motion smoothness | Settings > Display > Motion smoothness | [R] S22 |
| Network mode | Settings > Connections > Mobile networks > Network mode | [V] S17 |
| Battery status check | Samsung Members > Support > Phone diagnostics > Battery status | [V] S13 |

## Known battery-related issues
- **No official Samsung acknowledgement** of an A14 5G-specific battery fault was found (searched Oct 2026).
- Samsung Community has **isolated user reports** of heat and drain, some after One UI 5.1 or 7 updates [anecdotal, S25]; several posts do not identify the model clearly. **Not a known issue.** Treat only as support for the testable hypothesis "temporary post-update background work".
- Phones from early 2023 are now 2.5–3.5 years old; **age makes battery wear plausible**, but it must be confirmed with evidence (`diagnostics/battery-health.md`), not assumed.
