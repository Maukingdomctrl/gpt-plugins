---
name: product-creation
description: Use when the user wants to actually make a printable digital product (math worksheets, science practice sheets, revision sheets, study planners, educational bundles) including the PDF files, separate answer key, cover, preview images, title, description, tags and listing copy.
---

# Product creation: build the real files

Make the finished product, not instructions for making it. Work on one product at a time.

## 1. Lock the brief (ask at most one question)
Confirm or default: subject and topic, grade/age (US grade levels for US buyers), skill goal, number of pages (default 3–6 practice pages), paper (default **US Letter + A4**), shop/brand name for the footer. Write a one-line promise: "Grade 3 students practise ×/÷ facts 2–10 and apply them in word problems."

## 2. Write original content
- Base the content on general curriculum skills (for example, US Common Core or NGSS skill descriptions, in your own words). Never copy textbook pages, publisher question banks, worksheets from other sellers, or branded characters.
- Keep reading level and numbers age-appropriate; use neutral, inclusive names and everyday contexts.
- Every problem needs an answer. For anything numeric, also give a `check` expression so the answer is calculated, not trusted.
- Science and other text answers: state the answer and a one-line explanation, then re-read them against reliable knowledge. List them as "needs review" if unsure. Never invent facts.

## 3. Build the files
If Python is available, write a spec and run `scripts/build_printable.py` (needs `reportlab`; `Pillow` and `pdftoppm` add the cover and previews). Start from `assets/example-spec.json`.

```
python3 scripts/build_printable.py spec.json --out output
```

Spec essentials: `title`, `subtitle`, `grade`, `brand`, `paper` (`["letter","a4"]`), and `sections`. Each section has `heading`, `instructions`, `columns`, and `problems` and/or `generate`.
- Problem: `{"q": "...", "a": "...", "check": "6*4", "lines": 3, "choices": [...], "explain": "..."}`. Multiple-choice answers are letters (`"B"`). Use `"open": true` (no `a`) for planner or reflection prompts. Short facts get an inline blank automatically; `lines` adds full answer lines for working.
- Generator: `{"op": "add|subtract|multiply|divide", "count": 30, "a": [2,10], "b": [2,10], "seed": 7}`. Subtraction never goes negative; division is always exact.

Output: worksheets PDF and **separate** answer-key PDF per paper size, a 2000×2000 cover PNG, watermarked preview PNGs, and `qa_report.txt`. The script refuses to build if any calculated answer is wrong.

If you cannot run code, give the complete content in a copy-ready layout with page breaks marked, and say plainly that you could not produce the files.

Other printables (study planners, revision sheets, trackers) can also be built with the script by using sections with `lines` and no `check`. Otherwise, use reportlab directly with the same margins (0.6 in), fonts and footer.

## 4. Check before calling it finished
Go through `references/quality-checklist.md`. Read `qa_report.txt`. Resolve every ERROR, WARN and REVIEW line, and look at the rendered pages if you can. Only then say "finished", and list anything still unverified.

## 5. Listing package
Use `references/listing-copy-template.md` to write the title, description, tags and preview plan. Base keywords on the words buyers use; don't invent search-volume figures. Never claim the product is uploaded or live unless a tool actually did it.
