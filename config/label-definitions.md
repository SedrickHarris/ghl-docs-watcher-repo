# Label Definitions

Labels applied to detected changes by `scripts/parse_and_diff.py` and the
Claude prompts in `prompts/`. Do not add labels outside this list without
updating the prompts and the writer script.

| Label           | When to apply                                                                 |
|-----------------|-------------------------------------------------------------------------------|
| `breaking`      | A change removes, renames, or alters the behavior of an existing capability.  |
| `planned`       | An announced change that has not yet shipped.                                  |
| `new`           | A net-new capability added without removing anything.                          |
| `deprecation`   | A capability is marked deprecated but still functions.                         |
| `clarification` | Wording or structural edits that do not change behavior.                       |
| `informational` | Anything else worth recording but not actionable.                              |
| `unknown`       | The change was detected but its nature could not be determined from the diff. |

## Routing

- `breaking` and `deprecation` → `alerts/breaking-changes.md`.
- `planned` → `alerts/planned-updates.md`.
- All labels → considered for inclusion in `docs/changelog-summary.md`.
- Impact docs (`docs/{workflow,ai-agent,api}-implications.md`) are updated
  only when the change is non-trivial for that surface.
