#!/usr/bin/env python3
"""Static validation of the samsung-battery-diagnostics skill files.

Checks: frontmatter, required files, internal file references, intervention
completeness (six fields), intervention IDs used by the engine exist, source IDs
cited are defined, device separation (no AOD/dark-mode advice in the A14 5G
profile), and banned recommendations.

Run:  python3 tests/validate_skill.py
"""
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PLUGIN = os.path.abspath(os.path.join(ROOT, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import battery_diag as bd  # noqa: E402

REQUIRED = [
    "SKILL.md",
    "devices/device-identification.md", "devices/galaxy-m15-5g.md", "devices/galaxy-a14-5g.md",
    "diagnostics/battery-drain.md", "diagnostics/standby-drain.md", "diagnostics/network-drain.md",
    "diagnostics/display-drain.md", "diagnostics/app-drain.md", "diagnostics/battery-health.md",
    "diagnostics/charging.md",
    "workflows/initial-assessment.md", "workflows/evidence-collection.md",
    "workflows/controlled-testing.md", "workflows/verification.md", "workflows/adb-evidence.md",
    "procedures/interventions.md",
    "templates/diagnostic-report.md", "templates/measurement-log.csv",
    "references/samsung-documentation.md",
    "scripts/battery_diag.py",
    "tests/diagnostic-tests.md", "tests/test_battery_diag.py", "tests/fixtures/scenarios.json",
]

errors: list[str] = []
checks = 0


def check(cond: bool, msg: str) -> None:
    global checks
    checks += 1
    if not cond:
        errors.append(msg)


def read(rel: str) -> str:
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


# 1. required files
for rel in REQUIRED:
    check(os.path.isfile(os.path.join(ROOT, rel)), f"missing file: {rel}")

# 2. frontmatter
skill = read("SKILL.md")
m = re.match(r"^---\nname: ([a-z0-9-]+)\ndescription: (.+?)\n---\n", skill, re.S)
check(bool(m), "SKILL.md frontmatter must start with name and description")
if m:
    check(m.group(1) == "samsung-battery-diagnostics", "frontmatter name must match folder name")
    desc = m.group(2)
    check(len(desc) <= 1024, f"description too long ({len(desc)} > 1024)")
    for word in ("M15 5G", "A14 5G", "SM-M156B", "SM-A146"):
        check(word in desc, f"description should mention {word}")

# 3. internal references in all markdown files resolve
md_files = []
for dp, _, fns in os.walk(ROOT):
    for fn in fns:
        if fn.endswith(".md"):
            md_files.append(os.path.relpath(os.path.join(dp, fn), ROOT))
ref_re = re.compile(r"`((?:devices|diagnostics|workflows|procedures|templates|references|scripts|tests)/[A-Za-z0-9_./-]+\.(?:md|py|csv|json))")
for rel in md_files:
    for ref in ref_re.findall(read(rel)):
        check(os.path.isfile(os.path.join(ROOT, ref)), f"{rel}: broken reference {ref}")

# 4. intervention catalogue completeness
inter = read("procedures/interventions.md")
blocks = re.split(r"\n### ", inter)
ids = {}
for b in blocks[1:]:
    head = b.split("\n", 1)[0]
    iid = head.split(" ")[0]
    ids[iid] = b
for iid, body in ids.items():
    if iid.startswith("INT-"):
        check("**Device" in body, f"{iid}: missing Device")
        check("**Disadvantages:**" in body or "Disadvantages" in body, f"{iid}: missing Disadvantages")
        if iid not in ("INT-NONE-01", "INT-WAIT-01", "INT-HEALTH-01", "INT-HEALTH-02", "INT-SYS-01"):
            check("**Path" in body or "**Action" in body, f"{iid}: missing Path/Action")
        if iid.startswith(("INT-APP", "INT-NET", "INT-DISP", "INT-PWR", "INT-CHG-02", "INT-HEALTH-03", "INT-CHG-06")):
            check("**Reverse" in body or "Reverse:" in body, f"{iid}: missing how to reverse")
        if iid.startswith(("INT-APP", "INT-NET", "INT-DISP", "INT-PWR")):
            check("**What it does:**" in body, f"{iid}: missing What it does")
            check("**Why" in body, f"{iid}: missing Why")
        if "**Path" in body:
            path_line = body.split("**Path", 1)[1].split("\n", 1)[0]
            check(bool(re.search(r"\[(V|R|U)", path_line)), f"{iid}: path has no verification label")
check("LAST-RESORT" in inter, "LAST-RESORT section missing")

# 5. every intervention the engine can emit exists in the catalogue
for cause, lst in bd.INTERVENTIONS.items():
    for iid in lst:
        check(iid in ids or f"### {iid}" in inter, f"engine intervention {iid} ({cause}) not in interventions.md")
for cause, (_, module) in bd.CAUSES.items():
    check(os.path.isfile(os.path.join(ROOT, module)), f"cause {cause} module {module} missing")

# 6. every cited source ID is defined in references
refs = read("references/samsung-documentation.md")
defined = set(re.findall(r"^\| (S\d+) \|", refs, re.M))
for rel in md_files + ["scripts/battery_diag.py"]:
    for sid in set(re.findall(r"\bS(\d{1,2})\b", read(rel))):
        if rel.startswith("tests/"):
            continue
        check(f"S{sid}" in defined, f"{rel}: cites S{sid} which is not defined in references")
check("Date accessed" in refs or "accessed" in refs, "references must state access date")

# 7. device separation
a14 = read("devices/galaxy-a14-5g.md")
check("Not available" in a14 and "Always On Display" in a14, "A14 5G profile must state AOD not available")
check("25 W" not in a14 or "25 W adapter will not" in read("diagnostics/charging.md"), "A14 5G profile must not claim 25 W")
check("15 W" in a14, "A14 5G profile must state 15 W")
m15 = read("devices/galaxy-m15-5g.md")
check("25 W" in m15 and "5,880" in m15 and "6,000" in m15, "M15 5G profile must give 25 W and capacities")
check("SM-A145" in read("devices/device-identification.md"), "identification must exclude SM-A145 (A14 4G)")
check("2022" in read("devices/device-identification.md") and "January 2023" in read("devices/device-identification.md"),
      "identification must address the 2022/2023 release confusion")

# 8. banned recommendations: may only appear in a prohibitive context
banned = [r"calibrat", r"factory (data )?reset", r"battery optimi[sz]er", r"task killer", r"RAM booster"]
neg = re.compile(r"(never|not|no |don't|do not|avoid|only|last resort|LAST-RESORT|forbidden|unless|without)", re.I)
for rel in md_files:
    if rel.startswith("tests/"):
        continue
    for i, line in enumerate(read(rel).splitlines(), 1):
        for pat in banned:
            if re.search(pat, line, re.I):
                check(bool(neg.search(line)) or line.startswith("#") or "General management > Reset" in line,
                      f"{rel}:{i}: '{pat}' appears without a prohibitive/last-resort context")

# 9. plugin manifests
for mf in ("plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
    p = os.path.join(PLUGIN, mf)
    check(os.path.isfile(p), f"missing manifest {mf}")
    if os.path.isfile(p):
        with open(p, encoding="utf-8") as fh:
            data = json.load(fh)
        check(data.get("name") == "samsung-battery-diagnostics", f"{mf}: wrong name")
        check(bool(re.match(r"^\d+\.\d+\.\d+$", data.get("version", ""))), f"{mf}: bad version")

# 10. scenario fixtures cover both devices x 8 required scenarios
with open(os.path.join(ROOT, "tests/fixtures/scenarios.json"), encoding="utf-8") as fh:
    sc = json.load(fh)
for dev in ("M15", "A14"):
    check(len([s for s in sc if s["id"].startswith(dev)]) == 8, f"{dev}: need 8 scenarios")

print(f"{checks} checks, {len(errors)} failures")
for e in errors:
    print("FAIL:", e)
sys.exit(1 if errors else 0)
