# Prompt 02 — Classify Impact

**Goal:** assign each detected change a label from
`config/label-definitions.md` and decide which surfaces it affects.

## Inputs

- A single diff entry (output of prompt 01 or a raw diff hunk).
- `config/label-definitions.md` (canonical label list).

## Instructions

1. Pick exactly one label from the canonical list. If unsure, use
   `unknown`. Do not invent new labels.
2. Decide which surfaces this change touches. Choose any subset of:
   `workflows`, `ai-agents`, `api`. If none apply, return an empty list.
3. Justify the label in one sentence, citing the diff or source URL.

## Output format (JSON)

```json
{
  "label": "<one of: breaking | planned | new | deprecation | clarification | informational | unknown>",
  "surfaces": ["workflows" | "ai-agents" | "api"],
  "justification": "<one sentence, cite the source>"
}
```

Return only the JSON object.
