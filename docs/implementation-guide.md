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
