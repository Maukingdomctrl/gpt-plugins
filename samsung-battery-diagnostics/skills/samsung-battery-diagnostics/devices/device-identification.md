# Device identification

Verification labels used in all device files:
- **[V]** Verified on an official Samsung page (product page, Samsung Newsroom or Samsung support). Source ID in brackets, see `references/samsung-documentation.md`.
- **[R]** Reported by a reliable third-party source (e.g. GSMArena, SamMobile) but not found on an official Samsung page.
- **[U]** Unverified or conflicting. Ask the user to check on their phone.

## How the user finds the model number
Settings > About phone. The **Model number** line shows the code, e.g. `SM-M156B/DSN`. (Present on both devices; the exact layout may differ by One UI version.) The box label and the phone's SIM tray area may also show it.

Ask for the **model number**, not only the name. Names are reused across regions and generations.

## Supported codes
| Model code | Device | Chipset | Basis |
|---|---|---|---|
| `SM-M156B`, `SM-M156B/DS`, `SM-M156B/DSN`, retail SKUs like `SM-M156BZAVXID` | Galaxy M15 5G | MediaTek Dimensity 6100+ | [V] S2 (chipset), S1 (code, specs) |
| `SM-A146B` (+ `/DS`, `/DSN`) | Galaxy A14 5G | Samsung Exynos 1330 | [V] S5 (India launch names Exynos 1330); code-to-chip mapping [R] S21 |
| `SM-A146P` (+ retail SKUs like `SM-A146PDRHPHL`) | Galaxy A14 5G | MediaTek Dimensity 700 | [V] S6 (Indonesia launch names Dimensity 700), S4 (product page with this code) |
| `SM-A146U` (US) | Galaxy A14 5G | MediaTek Dimensity 700 | [R] S22 (review of the US unit); not confirmed on a Samsung page |
| `SM-A146U1`, `SM-A146W`, `SM-A146M`, `SM-S146VL` (US prepaid) and other listed codes | Galaxy A14 5G | **[U]** | codes listed by S20 [R] without a chipset; not confirmed on Samsung pages |

The chipset matters only for interpreting heat and performance; the diagnostic method is the same. If the chipset is [U], do not state it as fact.

## Codes that are NOT supported (common confusions)
| Code | Phone | Why it matters |
|---|---|---|
| `SM-A145…` | Galaxy A14 (4G/LTE) | Different phone and chipset, no 5G. **Do not treat it as the A14 5G.** |
| `SM-M146B` | Galaxy M14 5G | Different phone (shares a chipset family with some A14 5G units, but not supported). |
| `SM-E146B` | Galaxy F14 5G | Different phone. |
| `SM-E156B` | Galaxy F15 5G | Sibling of the M15 5G; different product, not supported. |
| `SM-A156…` | Galaxy A15 5G | Different phone. |
| `SM-M156` + anything other than `B` | Regional variants (e.g. Korean models sold under other names) | Not verified; not supported. |

## Release timing (avoid common mistakes)
- **Galaxy A14 5G** was announced in **January 2023** (GSMArena lists 4 January 2023 [R] S20; Samsung Newsroom Netherlands 10-01-2023 [V] S7; India 16-01-2023 [V] S5; Indonesia 19-01-2023 [V] S6). Do **not** say it was released in 2022. Samsung's battery-life claim cites testing of pre-release units in Dec 2022 – Jan 2023 [V] S4.
- **Galaxy M15 5G** launched in India on **8 April 2024** [V] S2. Other markets had earlier or later dates [R].

## Out-of-scope reply (template)
"Thanks. Your model number `<code>` is a `<phone>`. This assistant only covers the Galaxy M15 5G (SM-M156B) and Galaxy A14 5G (SM-A146). Its settings, battery and charging specs differ, so device-specific advice from here could mislead you. Samsung's support site or Samsung Members > Support can help with your model."
