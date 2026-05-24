# ghl-docs-watcher

Starter scaffold for a HighLevel (GoHighLevel / GHL) documentation watcher.

> **Status:** scaffold only. Scripts are stubs and **do not fetch live pages**.
> Verify every URL in `config/watched-pages.json` against an official HighLevel
> source before enabling any watcher.

## Current readiness status

- **Repo initialized.** Directory layout, templates, and the Claude
  Project instruction prompt are in place.
- **Scripts are stubs.** `scripts/fetch_ghl_docs.py`,
  `scripts/parse_and_diff.py`, and `scripts/write_updates.py` are safe
  skeletons; they raise `NotImplementedError` for any real work and
  only support `--dry-run`.
- **Sources are disabled.** Every entry in `config/watched-pages.json`
  has `enabled: false` and `verify_before_enabling: true`. No URL has
  been confirmed as the correct watch target yet.
- **Claude Project connection allowed.** After this readiness patch,
  the repo can be wired into a Claude Project as source-of-truth. The
  Project will see uploaded files only — there is no live watcher data
  to consume yet, so analyses will be limited to whatever diffs or
  snapshots a user pastes in manually.
- **Live watcher implementation comes later.** Implementing real
  fetching, diffing, and write-back is an explicit, reviewed next step
  — not part of this readiness patch.

## What this repo is for

Track changes to official HighLevel documentation over time, classify the
impact (breaking / planned / informational), and produce structured outputs
that downstream tools (a Claude project, alerting, etc.) can consume.

## Layout

```
.
├── README.md
├── .gitignore
├── .github/workflows/daily-docs-watch.yml   # scheduled run (skeleton)
├── alerts/                                  # human-facing alert logs
│   ├── breaking-changes.md
│   └── planned-updates.md
├── config/                                  # what to watch and how to label it
│   ├── watched-pages.json
│   └── label-definitions.md
├── docs/                                    # analysis outputs (templates)
│   ├── changelog-summary.md
│   ├── workflow-implications.md
│   ├── ai-agent-implications.md
│   ├── api-implications.md
│   └── implementation-guide.md
├── prompts/                                 # prompts for the Claude project
│   ├── claude-project-instructions.md
│   ├── 01-summarize-changelog.md
│   ├── 02-classify-impact.md
│   └── 03-draft-update.md
├── scripts/                                 # Python pipeline (skeletons)
│   ├── fetch_ghl_docs.py
│   ├── parse_and_diff.py
│   └── write_updates.py
└── sources/                                 # raw inputs and intermediate state
    ├── last-checked.txt
    ├── snapshots/   (gitkeep)
    └── diffs/       (gitkeep)
```

## Ground rules for contributors

1. Do not invent HighLevel features, endpoints, or behaviors. Cite an
   official source URL for every factual claim.
2. Only official HighLevel domains belong in `config/watched-pages.json`.
3. Scripts must remain safe starter skeletons until reviewed — no surprise
   network calls, no writes outside the repo.
4. Live fetching is disabled. Implement `fetch_page()` deliberately, with
   review, before enabling any watched page.

## Watched-source expansion strategy

This repo does **not** attempt to watch every HighLevel URL. The watch list
in `config/watched-pages.json` is built up in deliberate phases:

- **Phase 1 (critical):** the official source *roots* (API docs, Help Center,
  changelog) plus the high-impact product surfaces — workflows, AI agents,
  calendars, conversations, phone, messaging, email, forms, knowledge bases,
  MCP Server.
- **Phase 2 (expansion):** broader surfaces — contacts, opportunities, sites,
  payments, settings, reporting, integrations, reputation, custom objects,
  marketplace, SaaS / agency tooling, memberships, e-commerce, and others.

Both phases follow the same rules:

- Every source starts with `enabled: false` and `verify_before_enabling: true`.
- A source is only enabled after a human has confirmed the URL is official,
  current, and the right level of granularity for diffing.
- **Section-level watching first, article-level later.** The watch list
  targets section landing pages (or, where the section URL isn't yet known,
  the relevant domain root). Article-level watching is a later phase, gated
  on the fetcher being implemented and on a section showing signal worth
  drilling into.
- **Live fetching remains disabled.** No scripts and no GitHub Actions are
  modified in this phase. The watch list is configuration only; the fetcher
  is implemented in a separate, reviewed phase.

## Source verification tracker

The watch list in `config/watched-pages.json` contains **52 configured
sources** across Phase 1 (critical) and Phase 2 (expansion). Every source
must be verified before it can be enabled — see the per-source rules
under [Watched-source expansion strategy](#watched-source-expansion-strategy).

Verification progress is tracked at
[`docs/source-verification-tracker.md`](docs/source-verification-tracker.md),
one row per source.

## Next steps (suggested, not done yet)

- Confirm the exact HighLevel sources to watch and add them to
  `config/watched-pages.json` with `enabled: true`.
- Replace the `NotImplementedError` blocks in `scripts/` with a real
  fetcher, parser, and writer.
- Decide whether snapshots/diffs are committed to the repo or stored
  elsewhere (e.g., an artifact bucket).
- Wire the GitHub Actions workflow to real secrets if/when needed.
