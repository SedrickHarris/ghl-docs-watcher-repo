# Phase 1 Verification — Execution Guide

> Sibling docs: planning lives in
> [`source-verification-batch-01.md`](source-verification-batch-01.md),
> [`source-verification-batch-02.md`](source-verification-batch-02.md),
> and [`source-verification-batch-03.md`](source-verification-batch-03.md).
> Running status lives in
> [`source-verification-tracker.md`](source-verification-tracker.md).

## 1. Purpose

Phase 1 **planning** is complete: all 27 Phase 1 sources have a written
verification plan across batches 01, 02, and 03. This document controls
the **manual verification process** — the human-in-browser work of
confirming each URL — that comes between planning and any fetcher,
snapshot, or alerting work.

Verification is a configuration and documentation exercise. Nothing is
enabled, no fetcher runs, no GitHub Action is touched. The output of
verification is a set of small, reviewable commits that record what
was confirmed, by whom, and to where each source actually points.

## 2. Required order

Verify sources in this order:

1. **Batch 01 first** — official source roots (API docs, Help Center,
   changelog) plus the Workflows family, Calendars, Conversations.
   These are the foundations everything else hangs off of. Verifying
   them first surfaces help-center URL pattern issues before they
   propagate through 40+ section entries.
2. **Batch 02 second** — Phone, Messaging, A2P, Email family, Forms,
   Surveys, Chat Widget, AI Employee. These are the communication
   and lead-capture surfaces — the bulk of day-to-day client work
   depends on these.
3. **Batch 03 third** — Voice AI, Conversation AI, Workflow AI, AI
   Studio, Agent Studio, MCP Server, Knowledge Bases. These are the
   highest-churn surfaces; doing them last means the verifier has
   already calibrated on stable sections first.

Within each batch, follow the numerical order in the batch document.
Do not cherry-pick sources out of order — the batches are sequenced
deliberately for cross-source context (e.g. verify Workflows before
Workflow Builder, verify AI Studio before Agent Studio).

## 3. Manual verification rules

These rules apply to every source verified under this guide.

- **Open URLs manually in a browser.** No `curl`, no `wget`, no
  Python `requests`, no Claude WebFetch. The fetcher phase has not
  shipped; verification is a human task only.
- **Confirm the domain is official.** It must resolve on an official
  HighLevel domain: `gohighlevel.com`, `help.gohighlevel.com`,
  `highlevel.stoplight.io`, `marketplace.gohighlevel.com`.
- **Prefer section-level URLs over root URLs.** If you can navigate
  from a root to the specific section the entry represents, record
  that section URL as the verified URL — the section URL is the right
  target for diffing.
- **Do not use third-party mirrors.** No community sites, no scraped
  archives, no Stack Overflow answers, no marketplace re-listings.
  An official HighLevel surface is the only acceptable verified URL.
- **Do not enable any source yet.** `enabled` stays `false` in
  `config/watched-pages.json` regardless of how complete verification
  is. Enabling is a separate gate — see section 7.
- **Do not change scripts.** `scripts/fetch_ghl_docs.py`,
  `scripts/parse_and_diff.py`, and `scripts/write_updates.py` are
  out of scope for this guide.
- **Do not change GitHub Actions.** `.github/workflows/daily-docs-watch.yml`
  is out of scope.
- **Keep `verify_before_enabling: true`** in the config until the
  fetcher phase is built and reviewed. A verified URL is not a
  signal to flip this flag.
- **Only update `config/watched-pages.json`** after a verified URL is
  known. Specifically: only edit the `url`, `owner`, and `notes`
  fields, and only for sources whose verification is complete.
- **Only update tracker rows** after the verified URL is confirmed.
  Don't speculatively mark anything `Verified` — the tracker's
  status column is the ground truth other reviewers will rely on.

## 4. What to update after each verified source

After a source is manually verified (a real human opened it in a
browser and confirmed the section URL is correct), make the following
updates — and **only** these updates — in a single small commit.

**In `config/watched-pages.json`, for the verified source entry:**

- `url` — replace the placeholder root URL with the verified
  section-level URL, if one was found.
- `owner` — set to the verifier's GitHub username (no leading `@`).
- `notes` — append a short line recording what was verified (e.g.
  "Verified section URL on 2026-05-24; section TOC lists 14 articles").

**In `docs/source-verification-tracker.md`, for the same source's row:**

- **Verified URL** — fill in the same URL that was written to the
  config (or leave blank if the status is `Needs URL refinement` /
  `Deferred`).
- **Owner** — set to the verifier's GitHub username.
- **Verification status** — set to one of the four values defined
  in section 5.

**Do not touch:**

- `enabled` — stays `false`.
- `verify_before_enabling` — stays `true`.
- `source_type`, `expected_content_type`, `priority`, `phase`,
  `surfaces`, `content_selector` — these were set during planning;
  changing them is a separate, reviewed decision.
- Any other source's row in the tracker — one verified source per
  pass.

## 5. Allowed tracker status changes

The tracker's `Verification status` column accepts exactly four values:

| Status | Meaning | When to use |
|---|---|---|
| **Not started** | No verification work begun. | Initial state. Don't set this back from another status — use one of the others if you've looked at the source at all. |
| **Needs URL refinement** | The root URL is official, but a more specific section URL still needs to be found (or the section was found but the URL was not yet recorded). | When the source exists on an official HighLevel domain but the placeholder URL is too broad. Record the candidate section URL in **Verified URL** so the next pass can confirm it. |
| **Verified** | The section URL has been confirmed: official domain, correct section, renders meaningful content, right level of granularity. | When both the URL and the `notes` line have been written, and the entry is ready for the fetcher phase (whenever that ships). |
| **Deferred** | The source should not be verified in this round. The section does not exist yet, has been deprecated, or is a lower priority than originally scoped. | When verification is intentionally postponed. Record the reason in the row's **Notes** column. Do not delete the row — `Deferred` is a tracked state. |

## 6. Commit pattern

**Verify and commit in small batches, preferably 3 to 5 sources at a
time.**

Why:

- Small commits are easier to review — a reviewer can re-walk each
  source against its `url` change and tracker update in minutes.
- Smaller commits limit blast radius: if a verified URL turns out to
  be wrong, reverting a 3-source commit is cheaper than unwinding a
  whole-batch commit.
- It surfaces help-center pattern issues early — if the first 3
  Workflows-family sources all turn out to need refinement, that
  signals a section-URL-pattern problem worth pausing to discuss
  before working through the next 10.

Commit message convention:

```
docs: verify sources <id1>, <id2>, <id3>
```

For example:

```
docs: verify sources ghl-api-docs-root, ghl-help-center-root, ghl-platform-updates
```

Each commit should touch exactly two files: `config/watched-pages.json`
and `docs/source-verification-tracker.md`. Anything else in the diff
is a sign the change has expanded beyond this guide's scope.

## 7. Do not enable rule

> **A verified source is not the same as an enabled source.**

No source should be set to `enabled: true` until **all** of the
following are true:

- The fetcher (`scripts/fetch_ghl_docs.py`) is implemented and reviewed.
- The diff pipeline (`scripts/parse_and_diff.py`) is implemented and
  reviewed.
- The write-back (`scripts/write_updates.py`) is implemented and reviewed.
- A baseline snapshot has been captured for the source.
- The source's `verify_before_enabling` has been deliberately flipped
  to `false` in its own reviewed change — not as a side effect of
  verification.

Verification establishes that the URL is correct. Enabling is a
separate, downstream decision about whether to start actively
fetching. The two stay decoupled so that verification can complete in
the absence of fetcher work, and so that fetcher work doesn't get
blocked on verification dragging out.

## 8. Next recommended execution batch

Start verification with the first three sources from Batch 01:

| # | Source ID | Label |
|---|---|---|
| 1 | `ghl-api-docs-root` | HighLevel API Documentation (Stoplight) — root |
| 2 | `ghl-help-center-root` | HighLevel Help Center — root |
| 3 | `ghl-platform-updates` | HighLevel Platform Updates / What's Changed |

These three are deliberately chosen as the first execution batch:

- **`ghl-api-docs-root`** confirms the Stoplight workspace is the
  correct API surface and identifies whether the OpenAPI JSON is
  available (which is a far better fetcher target than HTML).
- **`ghl-help-center-root`** identifies the section URL pattern that
  ~46 other entries will inherit. Getting this right early prevents
  cascading rework.
- **`ghl-platform-updates`** finds the actual changelog URL —
  currently a placeholder pointing at the help center root. This is
  the single highest-signal source in the watch list; locating it
  unblocks the most useful alerting once the fetcher ships.

Follow the workflow from sections 3–6 for these three sources, commit
as one small batch (per section 6's pattern), and then continue
through the rest of Batch 01 in order.
