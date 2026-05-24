# Implementation Guide

How to operate the docs watcher once the script stubs are implemented.

## 1. Setup

- Python 3.11+ recommended.
- Create a virtualenv: `python -m venv .venv` and activate it.
- Install dependencies (none yet — add a `requirements.txt` when the real
  fetcher is written).

## 2. Configure watched pages

- Edit `config/watched-pages.json`.
- Each entry needs an official HighLevel URL and a stable `id`.
- Leave `verify_before_enabling: true` until the URL has been confirmed.
- Set `enabled: true` only after verification.

## 3. Run the pipeline locally

```
python scripts/fetch_ghl_docs.py --dry-run
python scripts/parse_and_diff.py --dry-run
python scripts/write_updates.py --dry-run
```

All three scripts are skeletons. Removing `--dry-run` will raise
`NotImplementedError` until the real logic is added.

## 4. Run via GitHub Actions

The workflow at `.github/workflows/daily-docs-watch.yml` runs the three
scripts daily in `--dry-run` mode. Update the workflow once the scripts
do real work.

## 5. Interpret outputs

- `sources/snapshots/` — raw captured pages (one file per page per run).
- `sources/diffs/` — per-run diffs against the previous snapshot.
- `docs/changelog-summary.md` — rolling human-readable summary.
- `docs/{workflow,ai-agent,api}-implications.md` — surface-specific
  analyses, only when applicable.
- `alerts/breaking-changes.md` and `alerts/planned-updates.md` —
  high-signal alerts for action.

## 6. Add a new watched page

1. Add an entry to `config/watched-pages.json` with `enabled: false`.
2. Confirm the URL is official and stable.
3. Set `enabled: true`.
4. Run the pipeline once manually to seed a baseline snapshot.

## 7. Phase 2: Watched-source expansion

Phase 2 broadens `config/watched-pages.json` from the two example entries
to the full set of HighLevel product surfaces we expect to track over
time. No code, scripts, or CI workflows are touched in this phase — only
the configuration and supporting documentation.

### How sources are grouped

- **`phase: "1-critical"`** — official source roots and the high-impact
  product surfaces (workflows, AI agents, calendars, conversations, phone,
  messaging, email, forms, knowledge bases, MCP). These get verified and
  enabled first.
- **`phase: "2-expansion"`** — broader surfaces (CRM, sites, payments,
  reporting, integrations, SaaS / agency tooling, marketplace, etc.).
- **`surfaces: [...]`** on each entry tags the high-level product areas
  the source feeds into (e.g. `workflows`, `ai-agents`, `crm`). This is
  the field downstream tooling uses to route diffs into the right
  surface-specific implication doc.

### Why section-level before article-level

- Section landing pages are stable; individual article URLs change more
  often and proliferate fast — a watch list of articles becomes stale
  faster than it provides value.
- A section-level diff is a useful early-warning signal: when a section's
  table of contents changes, it points the human reviewer at *which*
  article to drill into next.
- Article-level URLs cannot be enumerated reliably without fetching, and
  live fetching is disabled in this phase. Section-level entries let us
  populate the watch list now without violating the no-fetch rule.
  Specific URLs are refined during the verification step.

### How to verify a URL

For each entry with `verify_before_enabling: true`:

1. Open the `url` in a browser.
2. Confirm the domain is an official HighLevel domain
   (`gohighlevel.com`, `highlevel.stoplight.io`). No third-party mirrors,
   no community sites.
3. Confirm the page is the intended *section* landing page, not the site
   root and not an individual article. Update the `url` to the more
   specific section URL when one exists.
4. Confirm the page renders meaningful content (not a 404, a login wall,
   or a redirect to a different surface).
5. Decide on a `content_selector` if a section's wrapper page contains
   a lot of navigation churn. `null` is fine for sources where whole-page
   diffing is acceptable.
6. Record the verifier as `owner` (GitHub username).

### Rules before setting `enabled: true`

- The URL has been verified per the steps above.
- `verify_before_enabling` is flipped to `false`.
- The fetcher implementation supports the source's `expected_content_type`.
- A baseline snapshot has been captured (see section 6).

### Why no fetcher scripts change in this phase

Phase 2 is configuration only. Implementing real fetching, diffing, and
write-back is a separate, reviewed phase. Keeping these phases apart lets
the watch list be reviewed on its own merits — URLs, granularity,
ownership — without entangling that review with code changes that would
also need their own safety review.
