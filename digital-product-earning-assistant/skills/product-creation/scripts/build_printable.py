#!/usr/bin/env python3
"""Build a print-ready worksheet pack from a JSON spec.

Outputs (per paper size): worksheets PDF and a separate answer-key PDF.
Also: a square cover PNG, watermarked preview PNGs and qa_report.txt.

Needs: reportlab. Optional: Pillow (cover/previews), pdftoppm (page
thumbnails). Missing optional tools are reported, never faked.

Usage:
  python3 build_printable.py spec.json --out OUTPUT_DIR
"""
import argparse
import ast
import json
import operator
import os
import random
import re
import shutil
import subprocess
import sys
from datetime import date
from fractions import Fraction

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph,
                                SimpleDocTemplate, Spacer, Table, TableStyle)

PAPER = {"letter": LETTER, "a4": A4}
MARGIN = 0.6 * inch  # inside the 0.25-0.5in unprintable edge of most home printers
INK = colors.HexColor("#1f2933")
ACCENT = colors.HexColor("#2f6f9f")
KEY_INK = colors.HexColor("#b42318")

# ---------------------------------------------------------------- answers

_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod, ast.Pow: operator.pow}


def safe_eval(expr):
    """Evaluate +,-,*,/,//,%,**, brackets on numbers exactly (Fractions)."""
    expr = expr.replace("×", "*").replace("÷", "/").replace("−", "-").replace("^", "**")

    def ev(node):
        if isinstance(node, ast.Expression):
            return ev(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return Fraction(str(node.value))
        if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
            left, right = ev(node.left), ev(node.right)
            if isinstance(node.op, ast.Pow) and (right.denominator != 1 or abs(right) > 12):
                raise ValueError("unsupported exponent")
            return _OPS[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            v = ev(node.operand)
            return -v if isinstance(node.op, ast.USub) else v
        raise ValueError("unsupported expression: %r" % expr)

    return ev(ast.parse(expr, mode="eval"))


def parse_number(text):
    text = str(text).strip().replace(",", "")
    m = re.fullmatch(r"(-?\d+)\s+(\d+)/(\d+)", text)  # mixed number "1 1/2"
    if m:
        whole, num, den = (int(g) for g in m.groups())
        sign = -1 if whole < 0 else 1
        return Fraction(whole) + sign * Fraction(num, den)
    try:
        return Fraction(text)
    except (ValueError, ZeroDivisionError):
        return None


def fmt_number(value):
    if value.denominator == 1:
        return str(value.numerator)
    return "%d/%d" % (value.numerator, value.denominator)


def check_problem(p):
    """Return (status, message). status: verified | mismatch | unchecked."""
    if p.get("choices"):
        letters = [chr(65 + i) for i in range(len(p["choices"]))]
        if str(p.get("a", "")).strip().upper() not in letters:
            return "mismatch", "answer %r is not one of %s" % (p.get("a"), letters)
    if not p.get("check"):
        return "unchecked", "no 'check' expression: review by hand"
    expected = safe_eval(p["check"])
    given = parse_number(p.get("a", ""))
    if given is None or given != expected:
        return "mismatch", "answer %r but %s = %s" % (p.get("a"), p["check"], fmt_number(expected))
    return "verified", ""


# ------------------------------------------------------------- generators

def generate(cfg):
    rng = random.Random(cfg.get("seed", 1))
    op = cfg["op"]
    lo_a, hi_a = cfg.get("a", [1, 10])
    lo_b, hi_b = cfg.get("b", [1, 10])
    count = int(cfg.get("count", 20))
    seen, out, tries = set(), [], 0
    while len(out) < count and tries < count * 200:
        tries += 1
        a, b = rng.randint(lo_a, hi_a), rng.randint(lo_b, hi_b)
        if op == "add":
            q, check = "%d + %d =" % (a, b), "%d+%d" % (a, b)
        elif op == "subtract":
            a, b = max(a, b), min(a, b)  # no negative answers for young learners
            q, check = "%d - %d =" % (a, b), "%d-%d" % (a, b)
        elif op == "multiply":
            q, check = "%d × %d =" % (a, b), "%d*%d" % (a, b)
        elif op == "divide":
            if b == 0:
                continue
            q, check = "%d ÷ %d =" % (a * b, b), "%d/%d" % (a * b, b)  # always exact
        else:
            raise SystemExit("unknown generator op: %s" % op)
        if q in seen:
            continue
        seen.add(q)
        out.append({"q": q, "a": fmt_number(safe_eval(check)), "check": check})
    if len(out) < count:
        raise SystemExit("only %d unique '%s' problems fit the ranges; widen them" % (len(out), op))
    return out


# ------------------------------------------------------------------ layout

def styles():
    base = dict(fontName="Helvetica", textColor=INK)
    return {
        "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=20, leading=24,
                                textColor=ACCENT, alignment=TA_CENTER),
        "sub": ParagraphStyle("sub", fontSize=11, leading=14, alignment=TA_CENTER,
                              textColor=colors.HexColor("#52606d"), fontName="Helvetica"),
        "head": ParagraphStyle("head", fontName="Helvetica-Bold", fontSize=13, leading=16,
                               textColor=INK, spaceBefore=4, spaceAfter=4),
        "instr": ParagraphStyle("instr", fontSize=10.5, leading=14, **base),
        "q": ParagraphStyle("q", fontSize=12, leading=16, **base),
        "key": ParagraphStyle("key", fontName="Helvetica-Bold", fontSize=12, leading=16,
                              textColor=KEY_INK),
    }


def esc(text):
    text = str(text).replace("−", "-")  # U+2212 is missing from the base PDF fonts
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def name_block(st, width):
    t = Table([[Paragraph("Name: ____________________________", st["instr"]),
                Paragraph("Date: ______________", st["instr"])]],
              colWidths=[width * 0.65, width * 0.35])
    t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0)]))
    return t


def answer_line(width):
    t = Table([[""]], colWidths=[width], rowHeights=[22])
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 0.6, colors.HexColor("#9aa5b1"))]))
    return t


def problem_cell(n, p, st, key, width):
    inline = p.get("inline", not p.get("choices") and not p.get("lines"))
    q = esc(p["q"])
    if inline and not key:
        q += " ________"  # short facts: write the answer right after the question
    parts = [Paragraph("<b>%d.</b> %s" % (n, q), st["q"])]
    for i, choice in enumerate(p.get("choices") or []):
        parts.append(Paragraph("&nbsp;&nbsp;&nbsp;%s) %s" % (chr(65 + i), esc(choice)), st["q"]))
    if key:
        parts.append(Paragraph("Answer: %s" % esc(p.get("a", "")), st["key"]))
        if p.get("explain"):
            parts.append(Paragraph(esc(p["explain"]), st["instr"]))
    else:
        for _ in range(0 if inline else int(p.get("lines", 0 if p.get("choices") else 1))):
            parts.append(answer_line(width))
    parts.append(Spacer(1, 8))
    return parts


def build_pdf(spec, sections, paper, path, key):
    page_w, page_h = PAPER[paper]
    width = page_w - 2 * MARGIN
    st = styles()
    brand = spec.get("brand", "")
    year = date.today().year
    footer = spec.get("footer") or (
        "© %d %s. For personal and single-classroom use." % (year, brand) if brand
        else "For personal and single-classroom use.")

    def decorate(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#7b8794"))
        canvas.drawString(MARGIN, MARGIN * 0.5, footer)
        canvas.drawRightString(page_w - MARGIN, MARGIN * 0.5, "Page %d" % doc.page)
        canvas.restoreState()

    doc = SimpleDocTemplate(path, pagesize=(page_w, page_h), leftMargin=MARGIN,
                            rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN,
                            title=spec["title"] + (" - Answer Key" if key else ""),
                            author=brand or "", subject=spec.get("subtitle", ""))
    story = []
    for idx, sec in enumerate(sections):
        if idx:
            story.append(PageBreak())
        story.append(Paragraph(esc(spec["title"]), st["title"]))
        if key:
            story.append(Paragraph("ANSWER KEY", ParagraphStyle(
                "keyhead", parent=st["sub"], fontName="Helvetica-Bold", textColor=KEY_INK)))
        sub = " · ".join(x for x in [spec.get("grade"), spec.get("subtitle")] if x)
        if sub:
            story.append(Paragraph(esc(sub), st["sub"]))
        story.append(Spacer(1, 10))
        if not key:
            story += [name_block(st, width), Spacer(1, 8)]
        story.append(Paragraph(esc(sec.get("heading", "Section %d" % (idx + 1))), st["head"]))
        if sec.get("instructions") and not key:
            story.append(Paragraph(esc(sec["instructions"]), st["instr"]))
        story.append(Spacer(1, 8))
        cols = max(1, int(sec.get("columns", 2)))
        cells = [problem_cell(i + 1, p, st, key, width / cols - 14) for i, p in enumerate(sec["problems"])]
        rows = [cells[i:i + cols] + [""] * (cols - len(cells[i:i + cols]))
                for i in range(0, len(cells), cols)]
        grid = Table(rows, colWidths=[width / cols] * cols, splitByRow=1)
        grid.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                  ("LEFTPADDING", (0, 0), (-1, -1), 2),
                                  ("RIGHTPADDING", (0, 0), (-1, -1), 8)]))
        story.append(grid)
        if sec.get("note") and not key:
            story += [Spacer(1, 8), KeepTogether(Paragraph(esc(sec["note"]), st["instr"]))]
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)


# ------------------------------------------------------- cover and preview

def load_font(size, bold=False):
    from PIL import ImageFont
    names = (["DejaVuSans-Bold.ttf", "Arial Bold.ttf", "LiberationSans-Bold.ttf"] if bold
             else ["DejaVuSans.ttf", "Arial.ttf", "LiberationSans-Regular.ttf"])
    for n in names:
        for d in ["", "/usr/share/fonts/truetype/dejavu/", "/usr/share/fonts/truetype/liberation/",
                  "/Library/Fonts/", "C:/Windows/Fonts/"]:
            try:
                return ImageFont.truetype(d + n, size)
            except OSError:
                continue
    return ImageFont.load_default(size=size)


def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    return lines + ([cur] if cur else [])


def render_pages(pdf, prefix, dpi):
    if not shutil.which("pdftoppm"):
        return []
    subprocess.run(["pdftoppm", "-png", "-r", str(dpi), pdf, prefix], check=True)
    folder, base = os.path.split(prefix)
    return sorted(os.path.join(folder, f) for f in os.listdir(folder or ".")
                  if f.startswith(base + "-") and f.endswith(".png"))


def make_cover(spec, out, slug, page_count, thumb, size):
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (size, size), "#f4f7fb")
    d = ImageDraw.Draw(img)
    s = size / 2000.0
    title_font = load_font(int(120 * s), True)
    lines = wrap(d, spec["title"], title_font, size - int(160 * s))[:3]
    banner = int(90 * s) + len(lines) * int(135 * s) + int(70 * s)
    d.rectangle([0, 0, size, banner], fill="#2f6f9f")
    y = int(90 * s)
    for line in lines:
        d.text((int(80 * s), y), line, font=title_font, fill="white")
        y += int(135 * s)
    tags = [t for t in [spec.get("grade"), "%d pages + answer key" % page_count,
                        " & ".join(p.upper() if p == "a4" else "US Letter"
                                   for p in spec.get("paper", ["letter"]))] if t]
    ty, font = banner + int(60 * s), load_font(int(64 * s), True)
    for t in tags:
        w = d.textlength(t, font=font)
        d.rounded_rectangle([int(80 * s), ty, int(80 * s + w + 60 * s), ty + int(100 * s)],
                            radius=int(40 * s), fill="#ffd166")
        d.text((int(110 * s), ty + int(14 * s)), t, font=font, fill="#1f2933")
        ty += int(125 * s)
    if thumb:
        page = Image.open(thumb).convert("RGB")
        box_h = size - ty - int(120 * s)
        page.thumbnail((size - int(160 * s), box_h))
        x = (size - page.width) // 2
        d.rectangle([x + 18, ty + 58, x + page.width + 18, ty + 40 + page.height + 18], fill="#c7d2de")
        img.paste(page, (x, ty + 40))
    path = os.path.join(out, slug + "_cover.png")
    img.save(path, optimize=True)
    return path


def watermark(src, dst):
    from PIL import Image, ImageDraw
    page = Image.open(src).convert("RGBA")
    layer = Image.new("RGBA", page.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    font = load_font(max(24, page.width // 8), True)
    w = d.textlength("PREVIEW", font=font)
    d.text(((page.width - w) / 2, page.height / 2 - page.width // 16), "PREVIEW",
           font=font, fill=(47, 111, 159, 70))
    layer = layer.rotate(30, center=(page.width / 2, page.height / 2))
    Image.alpha_composite(page, layer).convert("RGB").save(dst, optimize=True)
    return dst


# -------------------------------------------------------------------- main

def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "product"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("--out", default="output")
    ap.add_argument("--cover-size", type=int, default=2000, help="square cover width in px")
    ap.add_argument("--previews", type=int, default=2, help="watermarked preview pages to export")
    args = ap.parse_args()

    with open(args.spec, encoding="utf-8") as fh:
        spec = json.load(fh)
    os.makedirs(args.out, exist_ok=True)
    slug = spec.get("slug") or slugify(spec["title"])
    papers = [p.lower() for p in spec.get("paper", ["letter"])]
    for p in papers:
        if p not in PAPER:
            raise SystemExit("paper must be 'letter' or 'a4', got %r" % p)

    sections, report, problems = [], [], 0
    counts = {"verified": 0, "unchecked": 0, "mismatch": 0, "open": 0}
    seen = {}
    for si, sec in enumerate(spec["sections"]):
        sec = dict(sec)
        sec["problems"] = list(sec.get("problems", [])) + (generate(sec["generate"]) if sec.get("generate") else [])
        if not sec["problems"]:
            raise SystemExit("section %d has no problems" % (si + 1))
        for pi, p in enumerate(sec["problems"]):
            problems += 1
            label = "S%d Q%d" % (si + 1, pi + 1)
            if p.get("open") and str(p.get("q", "")).strip():
                p.setdefault("a", "Answers will vary.")  # planners, reflections
                counts["open"] += 1
                continue
            if not str(p.get("q", "")).strip() or not str(p.get("a", "")).strip():
                counts["mismatch"] += 1
                report.append("ERROR %s: missing question or answer" % label)
                continue
            status, msg = check_problem(p)
            counts[status] += 1
            if status == "mismatch":
                report.append("ERROR %s: %s" % (label, msg))
            elif status == "unchecked":
                report.append("REVIEW %s: %s -> %s" % (label, p["q"], p["a"]))
            if p["q"] in seen:
                report.append("WARN %s duplicates %s: %s" % (label, seen[p["q"]], p["q"]))
            seen.setdefault(p["q"], label)
        sections.append(sec)

    if counts["mismatch"]:
        print("\n".join(report))
        raise SystemExit("Stopped: %d answer error(s). Fix the spec; no files were built." % counts["mismatch"])

    files = []
    for p in papers:
        for key in (False, True):
            path = os.path.join(args.out, "%s_%s_%s.pdf" % (slug, "answer_key" if key else "worksheets", p))
            build_pdf(spec, sections, p, path, key)
            files.append(path)

    page_info = []
    try:
        from pypdf import PdfReader
        for f in files:
            r = PdfReader(f)
            box = r.pages[0].mediabox
            page_info.append("%s: %d page(s), %.2f x %.2f in" % (os.path.basename(f), len(r.pages),
                                                                 float(box.width) / 72, float(box.height) / 72))
        ws_pages = len(PdfReader(files[0]).pages)
        for f in files:
            if len(PdfReader(f).pages) > len(sections):
                report.append("WARN %s: a section runs onto an extra page; reduce problems, "
                              "lines or columns, or split the section" % os.path.basename(f))
    except ImportError:
        page_info.append("pypdf not installed: page sizes not re-read from the files")
        ws_pages = len(sections)

    extras, notes = [], []
    try:
        import PIL  # noqa: F401
        tmp = os.path.join(args.out, "_render")
        os.makedirs(tmp, exist_ok=True)
        pages = render_pages(files[0], os.path.join(tmp, "p"), 110)
        if not pages:
            notes.append("pdftoppm not found: cover has no page thumbnail and no previews were made")
        extras.append(make_cover(spec, args.out, slug, ws_pages, pages[0] if pages else None, args.cover_size))
        for i, pg in enumerate(pages[:args.previews]):
            extras.append(watermark(pg, os.path.join(args.out, "%s_preview_%d.png" % (slug, i + 1))))
        shutil.rmtree(tmp, ignore_errors=True)
    except ImportError:
        notes.append("Pillow not installed: no cover or previews made")

    summary = [
        "QA REPORT: %s" % spec["title"],
        "Problems: %d | verified by calculation: %d | need manual review: %d | open-ended: %d" % (
            problems, counts["verified"], counts["unchecked"], counts["open"]),
        "Margins: %.2f in on all sides" % (MARGIN / inch),
    ] + page_info + notes + ["", "Files:"] + ["  " + os.path.basename(f) for f in files + extras]
    if report:
        summary += ["", "Items to check:"] + ["  " + r for r in report]
    summary += ["", "Before calling this finished: open each PDF, read every 'REVIEW' item, "
                "check spelling, age level and that nothing is copied from a textbook."]
    text = "\n".join(summary)
    with open(os.path.join(args.out, "qa_report.txt"), "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(text)


if __name__ == "__main__":
    sys.exit(main())
