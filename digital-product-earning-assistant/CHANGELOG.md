# Changelog

## 0.2.0 (2026-10-30)

Plugin ID `digital-product-earning-assistant`, display name, author, category and manifest structure are unchanged.

### Added
- **marketplace-research** skill: eligibility checklist for Indian sellers (account opening, GST, payment and payout methods, minimum payouts, all fees, conversion, tax/compliance), comparison workflow and table, and a worked fee example.
  - `references/marketplace-facts.md`: dated, sourced findings for Etsy, Payoneer, Gumroad, Payhip, TPT, Lemon Squeezy and PayPal India, each labelled Verified, Partly verified or Unverified.
  - `references/india-tax-compliance.md`: GST threshold, inter-state exemption, LUT, marketplace TDS/TCS, income-tax notes with CBIC/GST portal sources.
- **product-creation** skill: builds real files from a JSON spec.
  - `scripts/build_printable.py`: worksheets PDF plus separate answer-key PDF in US Letter and/or A4, 2000×2000 cover PNG, watermarked previews and `qa_report.txt`. Numeric answers are recalculated; the build stops on any wrong answer. Arithmetic generator: add, subtract (no negatives), multiply, divide (exact).
  - `assets/example-spec.json`: Grade 3 ×/÷ facts and word problems.
  - `references/quality-checklist.md`, `references/listing-copy-template.md`.
- **sales-tracking** skill: column definitions, decision rules that avoid judging small samples, and reply format.
  - `assets/sales-tracker-template.csv`, `scripts/analyze_sales.py` (standard library only).

### Changed
- **first-sale-workflow**: now the coach and router. It adds the user's fixed context (India-based, US buyers, ₹0, digital only), one-step-at-a-time coaching rules, and a stage table pointing to the new skills. Stage 1 and the launch experiment are kept; pricing and listing details moved to the specialised skills.
- Manifests: version 0.1.0 → 0.2.0, updated description, long description, two of three default prompts, and three new keywords.

### Removed
- Chess-related product suggestions (skill description and Stage 1 list).
- Duplicate pricing and marketplace instructions now covered by `marketplace-research`.
