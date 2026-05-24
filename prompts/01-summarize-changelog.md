# Prompt 01 — Summarize Changelog

**Goal:** turn a set of per-page diffs into a single dated section for
`docs/changelog-summary.md`.

## Inputs

- One or more diff files from `sources/diffs/` (current run).
- The matching entries from `config/watched-pages.json` (for source URLs).

## Instructions

1. Group changes by page (`id` from `watched-pages.json`).
2. For each page, write one bullet per discrete change:
   `- **<label>** — <one-line summary> — <source URL>`
3. Use only labels from `config/label-definitions.md`.
4. Skip pure-formatting diffs (whitespace, anchor reordering) unless
   they alter content.
5. If you cannot determine what changed, use `unknown` and quote the
   diff hunk verbatim in the bullet.

## Output format

```
## YYYY-MM-DD

- **<label>** — <summary> — <url>
- **<label>** — <summary> — <url>
```

Return only the section. Do not include preamble.
