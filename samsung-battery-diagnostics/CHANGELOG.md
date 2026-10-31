# Changelog

## 0.1.0 (2026-10-31)

First release.

### Added
- `samsung-battery-diagnostics` skill for the Galaxy M15 5G (SM-M156B) and Galaxy A14 5G (SM-A146) only.
- Device profiles with verification labels ([V] official Samsung, [R] reliable third party, [U] unverified), including model-code identification and rejection of look-alikes (A14 4G SM-A145, M14 5G, F14/F15 5G, A15 5G).
- Seven diagnostic modules (consumption, standby, network, display, apps, battery health, charging) with decision trees.
- Ten-step workflow files: initial assessment, evidence collection, controlled testing, verification, optional read-only adb evidence.
- Intervention catalogue: every change lists device, path with verification label, what it does, why, disadvantages and how to reverse; a gated last-resort section for factory reset.
- Deterministic engine `scripts/battery_diag.py` (identify, rate, rank, compare) with uncertainty-aware verdicts.
- Report template and measurement log.
- References with title, URL, applicable device, Android/One UI version and access date, plus a list of research gaps.
- Tests: 16 device-specific scenario fixtures, unit tests, static validator, conversation-test rubric, and recorded conversation-test results with transcripts (`tests/behaviour-results.md`, `tests/transcripts/`).
- SKILL.md rules 10–11 (target the top-ranked cause first; label outside claims) added after conversation testing.
- Manifests for ChatGPT (`plugin.json`, `.codex-plugin/`) and Claude Code (`.claude-plugin/`).
