# Prompt 03 — Draft Update

**Goal:** turn a classified change into a ready-to-paste entry for the
appropriate `alerts/` or `docs/` file.

## Inputs

- The classification JSON from prompt 02.
- The original diff and source URL.
- The target file's template (see `alerts/*.md` and `docs/*.md`).

## Instructions

1. Pick the target file based on the label:
   - `breaking` or `deprecation` → `alerts/breaking-changes.md`
   - `planned` → `alerts/planned-updates.md`
   - Any label with non-empty `surfaces` → also draft an entry for each
     matching `docs/<surface>-implications.md`.
2. Match the target file's entry template exactly — headings, field
   order, date format.
3. Use `YYYY-MM-DD` (UTC) for the date.
4. Do not assert anything not present in the diff or the source URL.
   Use "unknown" rather than guessing.

## Output format

Return one fenced block per target file:

```
### TARGET: <relative path>
<entry matching that file's template>
```

No extra commentary.
