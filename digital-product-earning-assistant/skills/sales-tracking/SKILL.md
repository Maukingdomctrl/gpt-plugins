---
name: sales-tracking
description: Use when the user shares listing numbers (views, clicks, saves, questions, orders, revenue, fees), wants a sales tracker or spreadsheet, asks why a product isn't selling, or must decide whether to improve, test or discontinue a listing.
---

# Sales tracking and improvement

## Set up (once)
Give the user `assets/sales-tracker-template.csv` (opens in Google Sheets or Excel). One row per product, per marketplace, per week. Each row holds **that week's numbers only**.

| Column | Meaning |
|---|---|
| product_name, marketplace | What and where |
| listing_date | First day the listing went live (YYYY-MM-DD) |
| period_start, period_end | The week the numbers cover |
| views | Listing page views (the marketplace's stats page) |
| clicks | Clicks to the listing from search or your posts/pins, if reported; else 0 |
| saves | Favourites / wishlist adds / pin saves |
| questions | Buyer messages or questions received |
| orders | Paid orders (exclude refunded) |
| revenue_usd | What buyers paid for those orders |
| fees_usd | All platform, processing, listing and payout fees for the week |
| net_usd | Leave blank to auto-calculate revenue − fees |
| changes_made | Total improvements tried on this listing so far (running count) |
| notes | What changed this week, e.g. "new cover" |

Spreadsheet formulas if the user prefers a sheet: Net `=K2-L2`; Conversion `=IF(F2=0,"",J2/F2)`.

## Analyse
If Python is available, run `scripts/analyze_sales.py tracker.csv`. Otherwise calculate the same by hand and show the arithmetic:
- **Conversion rate** = orders ÷ views. Secondary: orders ÷ clicks.
- **Net earnings** = revenue − fees (then note currency conversion and payout costs if not already in fees).

## Decide (cautious rules)
- **Under 14 days or under 100 views → WAIT.** Never judge price or product on a few dozen views. Say so plainly.
- **Low visibility** (under ~3 views/day after 14 days) → fix discoverability: title wording, all tags, cover, one channel post per week.
- **Views but no sales** (100+ views, 0 orders) → **test one change** at a time: cover/first image, first lines of the description, previews, or a test price. Saves without orders usually point to price or unclear previews. Questions point to missing information in the description.
- **1–2 orders** → keep and watch; it's a tiny sample, so don't over-celebrate or change what works.
- **3+ orders** → keep; make one closely related product for the same buyers.
- **Consider discontinuing** only after ~60 days, 300+ views, 0 orders **and** at least two tested changes.

These thresholds are cautious rules of thumb, not marketplace benchmarks. Never quote "typical conversion rates" without a verified source.

## Reply format
One short table, one decision per listing, and **one** next action, with the result to record next week. Remind the user that no outcome is guaranteed and early zeros are normal.
