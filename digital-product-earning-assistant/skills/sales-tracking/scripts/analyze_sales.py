#!/usr/bin/env python3
"""Summarise a sales-tracker CSV and suggest one action per listing.

Each CSV row holds one period's numbers (not running totals) for one
product on one marketplace. Columns: see assets/sales-tracker-template.csv.
Standard library only.

Usage:
  python3 analyze_sales.py tracker.csv [--today YYYY-MM-DD]
"""
import argparse
import csv
import sys
from collections import OrderedDict
from datetime import date

NUM = ["views", "clicks", "saves", "questions", "orders", "revenue_usd", "fees_usd", "changes_made"]

# Rules of thumb, not platform benchmarks. Kept deliberately cautious so a
# handful of views never produces a confident verdict.
MIN_DAYS = 14          # judge nothing about a listing younger than this
MIN_VIEWS = 100        # minimum views before reading a conversion rate
LOW_VIEWS_PER_DAY = 3  # below this after MIN_DAYS -> visibility problem
STOP_DAYS, STOP_VIEWS, STOP_CHANGES = 60, 300, 2


def num(value, field, line, problems):
    value = (value or "").strip()
    if value == "":
        return 0.0
    try:
        n = float(value)
    except ValueError:
        problems.append("line %d: %s=%r is not a number (counted as 0)" % (line, field, value))
        return 0.0
    if n < 0:
        problems.append("line %d: %s is negative" % (line, field))
    return n


def parse_date(value, field, line, problems):
    try:
        return date.fromisoformat((value or "").strip())
    except ValueError:
        problems.append("line %d: %s=%r should be YYYY-MM-DD" % (line, field, value))
        return None


def pct(part, whole):
    return "%.1f%%" % (100.0 * part / whole) if whole else "n/a"


def verdict(t, days):
    """Return (decision, reason, next step)."""
    v, o = t["views"], t["orders"]
    if days is not None and days < MIN_DAYS:
        return ("WAIT", "listed %d days; too early to judge" % days,
                "Keep sharing it in your one chosen free channel and record numbers weekly.")
    if v < MIN_VIEWS:
        per_day = v / days if days else 0
        if days is not None and per_day < LOW_VIEWS_PER_DAY:
            return ("IMPROVE VISIBILITY", "%.1f views/day after %d days" % (per_day, days),
                    "Rewrite the title so it starts with what buyers search, use all tag slots, "
                    "and post one helpful preview in your chosen channel this week.")
        return ("WAIT", "only %d views; too few to read a conversion rate" % v,
                "Collect at least %d views before changing price or product." % MIN_VIEWS)
    if o == 0:
        if (days or 0) >= STOP_DAYS and v >= STOP_VIEWS and t["changes_made"] >= STOP_CHANGES:
            return ("CONSIDER DISCONTINUING",
                    "%d views, 0 orders, %d changes tried over %d days" % (v, t["changes_made"], days),
                    "Stop putting time into this listing; reuse what you learned for a narrower product.")
        if t["saves"] >= 0.05 * v:
            reason = "%d views and %d saves but no orders: interest without purchase" % (v, t["saves"])
            step = "Test one change: a lower test price OR clearer previews showing inside pages."
        else:
            reason = "%d views, few saves, no orders: the page isn't convincing" % v
            step = ("Test one change: the cover/first image and first two lines of the description "
                    "must say grade, topic, page count and 'answer key included'.")
        if t["questions"]:
            step += " Add answers to buyer questions into the description."
        return ("TEST ONE CHANGE", reason, step)
    if o < 3:
        return ("KEEP AND WATCH", "%d order(s) from %d views; promising but a tiny sample" % (o, v),
                "Don't change what works. Ask buyers for feedback and keep tracking.")
    return ("KEEP; BUILD A RELATED PRODUCT", "%d orders from %d views (%s)" % (o, v, pct(o, v)),
            "Make one closely related product (next grade or next skill) for the same buyers.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--today", help="override today's date (YYYY-MM-DD)")
    args = ap.parse_args()
    today = date.fromisoformat(args.today) if args.today else date.today()

    totals, problems = OrderedDict(), []
    with open(args.csv, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        missing = {"product_name", "marketplace", "listing_date", "views", "orders"} - set(reader.fieldnames or [])
        if missing:
            raise SystemExit("CSV is missing columns: %s" % ", ".join(sorted(missing)))
        for line, row in enumerate(reader, start=2):
            name = (row.get("product_name") or "").strip()
            if not name or name.lower().startswith("example -"):
                continue
            key = (name, (row.get("marketplace") or "").strip())
            t = totals.setdefault(key, dict.fromkeys(NUM + ["net_usd"], 0.0) | {"listed": None})
            vals = {f: num(row.get(f), f, line, problems) for f in NUM}
            for f in NUM:  # changes_made is a running count, everything else is per period
                t[f] = max(t[f], vals[f]) if f == "changes_made" else t[f] + vals[f]
            net = (row.get("net_usd") or "").strip()
            t["net_usd"] += num(net, "net_usd", line, problems) if net else vals["revenue_usd"] - vals["fees_usd"]
            listed = parse_date(row.get("listing_date"), "listing_date", line, problems)
            if listed and (t["listed"] is None or listed < t["listed"]):
                t["listed"] = listed
            if vals["orders"] > vals["views"] > 0:
                problems.append("line %d: more orders than views; check the numbers" % line)
            if vals["orders"] and not vals["revenue_usd"]:
                problems.append("line %d: orders recorded but revenue is 0" % line)

    if not totals:
        print("No data rows yet. Add one row per product per week (delete the example row).")
        return 0

    print("| Product | Marketplace | Days | Views | Clicks | Saves | Qs | Orders | Conv. (orders/views) "
          "| Orders/clicks | Revenue | Fees | Net |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    grand = dict.fromkeys(["revenue_usd", "fees_usd", "net_usd", "orders"], 0.0)
    for (name, market), t in totals.items():
        days = (today - t["listed"]).days if t["listed"] else None
        print("| %s | %s | %s | %d | %d | %d | %d | %d | %s | %s | $%.2f | $%.2f | $%.2f |" % (
            name, market, days if days is not None else "?", t["views"], t["clicks"], t["saves"],
            t["questions"], t["orders"], pct(t["orders"], t["views"]), pct(t["orders"], t["clicks"]),
            t["revenue_usd"], t["fees_usd"], t["net_usd"]))
        for k in grand:
            grand[k] += t[k]
        t["days"] = days
    print("\nTotal: %d orders, revenue $%.2f, fees $%.2f, net $%.2f (before currency conversion "
          "and payout charges unless you entered them as fees)." % (
              grand["orders"], grand["revenue_usd"], grand["fees_usd"], grand["net_usd"]))

    print("\n## Decisions")
    for (name, market), t in totals.items():
        decision, reason, step = verdict(t, t["days"])
        print("- **%s (%s): %s**: %s.\n  Next: %s" % (name, market, decision, reason, step))

    if problems:
        print("\n## Data checks")
        for p in problems:
            print("- " + p)
    print("\nThresholds (%d days, %d views) are cautious rules of thumb, not platform benchmarks."
          % (MIN_DAYS, MIN_VIEWS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
