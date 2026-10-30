# gpt-plugins

## Digital Product Earning Assistant (private ChatGPT plugin)

| Path | What it is |
|---|---|
| `digital-product-earning-assistant/` | **Current plugin source, v0.2.0.** Upload this through ChatGPT Plugin Creator. |
| `dist/digital-product-earning-assistant-0.2.0.zip` | The same files zipped, with `plugin.json`, `.codex-plugin/` and `skills/` at the root of the ZIP (same layout as the original archive). |
| `digital-product-earning-assistant.tar.gz` | Original v0.1.0 archive, kept unchanged for reference. |
| `examples/` | Test outputs: a Grade 3 math pack, a science sheet + planner, and a sales-tracker report. Not part of the plugin. |

The plugin ID (`digital-product-earning-assistant`), display name and author are unchanged. Visibility is set in Plugin Creator, not in these files; keep it private there.

### Skills
- `first-sale-workflow`: coach and router; one next step at a time.
- `marketplace-research`: Indian seller eligibility, GST, payouts and fees, with dated sources.
- `product-creation`: builds worksheets, answer keys, covers, previews and listing copy (`scripts/build_printable.py`, needs `reportlab`).
- `sales-tracking`: CSV tracker plus `scripts/analyze_sales.py` (standard library only).

See `digital-product-earning-assistant/CHANGELOG.md` for details.

### Rebuild the ZIP
```bash
cd digital-product-earning-assistant && zip -r ../dist/digital-product-earning-assistant-0.2.0.zip . -x '*__pycache__*' '.DS_Store'
```

Marketplace and tax facts were checked on 2026-10-30. Re-check them before relying on them.
