# Samsung Battery Diagnostics (plugin + skill)

An evidence-based battery diagnostic assistant for **exactly two phones**:

| Device | Model codes | Battery (typical / rated) | Max wired charging | Display |
|---|---|---|---|---|
| Galaxy M15 5G | SM-M156B (…/DS, …/DSN) | 6,000 / 5,880 mAh | 25 W (adapter sold separately) | 6.5" Super AMOLED, 90 Hz |
| Galaxy A14 5G | SM-A146B (Exynos 1330), SM-A146P (Dimensity 700), other SM-A146 codes | 5,000 / 4,900 mAh | 15 W | 6.6" PLS LCD, 90 Hz |

It is not a battery-tips bot. It identifies the device, collects measurements, ranks causes, recommends at most two targeted changes with exact One UI paths, trade-offs and reversal steps, and verifies the effect with a before/after test.

## Layout
```
samsung-battery-diagnostics/
  plugin.json                  ChatGPT plugin manifest (same schema as the repo's other plugin)
  .codex-plugin/plugin.json    Codex / ChatGPT Plugin Creator manifest
  .claude-plugin/plugin.json   Claude Code plugin manifest
  skills/samsung-battery-diagnostics/
    SKILL.md                   entry point: scope gate, 10-step workflow, rules
    devices/                   device-identification, galaxy-m15-5g, galaxy-a14-5g
    diagnostics/               modules A–G (drain, standby, network, display, apps, health, charging)
    workflows/                 initial assessment, evidence collection, controlled testing, verification, adb (optional)
    procedures/interventions.md every allowed change with device, path, effect, reason, downside, reversal
    templates/                 diagnostic report, measurement log CSV
    references/                sources (title, URL, device, version, access date) and research gaps
    scripts/battery_diag.py    deterministic engine: identify, rate, rank, compare (stdlib only)
    tests/                     scenario spec, fixtures, unit tests, static validator
```

## Install and invoke

**Claude Code**
- As a plugin from a local clone:
```bash
claude --plugin-dir ./samsung-battery-diagnostics
```
- Or copy just the skill into your personal skills folder:
```bash
cp -r samsung-battery-diagnostics/skills/samsung-battery-diagnostics ~/.claude/skills/
```
- Invoke by describing the problem ("My Galaxy A14 5G loses 18 % overnight") or with `/samsung-battery-diagnostics`.

**ChatGPT (Plugin Creator)**
Upload the `samsung-battery-diagnostics/` folder (or a ZIP with `plugin.json`, `.codex-plugin/` and `skills/` at the root). Keep visibility private in Plugin Creator. Start with one of the default prompts.

**Claude.ai / other skill hosts**
Zip `skills/samsung-battery-diagnostics/` (with `SKILL.md` at the top level of the folder) and upload it as a skill.

## Using the engine directly
```bash
cd skills/samsung-battery-diagnostics
python3 scripts/battery_diag.py identify SM-A146B
python3 scripts/battery_diag.py rate measurement.json
python3 scripts/battery_diag.py rank evidence.json
python3 scripts/battery_diag.py compare before.json after.json
```
Field formats are shown in `tests/fixtures/scenarios.json`.

## Tests
```bash
cd skills/samsung-battery-diagnostics
python3 tests/test_battery_diag.py -v
python3 tests/validate_skill.py
```

## Limitations
- The assistant cannot see the phone; everything depends on what the user reports.
- Menu paths vary across One UI versions; unverified paths are labelled and paired with "use Settings search".
- Thresholds are triage heuristics, not Samsung specifications; the decisive test is the before/after comparison.
- See `skills/samsung-battery-diagnostics/references/samsung-documentation.md` for sources and open research gaps. Facts were checked on 2026-10-31.
