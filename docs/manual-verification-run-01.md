# Manual Verification — Run 01

> Companion docs: this is the execution worksheet for the first three
> sources from
> [`source-verification-batch-01.md`](source-verification-batch-01.md).
> The process this worksheet follows is defined in
> [`phase-1-verification-execution-guide.md`](phase-1-verification-execution-guide.md).
> The running status of record is in
> [`source-verification-tracker.md`](source-verification-tracker.md).

## Manual verification instructions for Sedrick

1. **Open each current URL manually in the browser.** Do not run any
   script, do not use `curl` / `wget`, do not call any fetcher.
2. **Confirm the URL is official HighLevel.** It must resolve on an
   official HighLevel domain: `highlevel.stoplight.io`,
   `help.gohighlevel.com`, `gohighlevel.com`, or
   `marketplace.gohighlevel.com`. No third-party mirrors.
3. **Find the best section-level URL** if the current URL is only a
   root URL. For the help center, drill into the actual section the
   entry represents (or, for sources 1–3, the actual workspace /
   landing / changelog page).
4. **Paste the verified URL back into this document** under
   **Verified URL** for each source below. Use the literal URL,
   no markdown link wrapping.
5. **Do not set `enabled` to `true`** in `config/watched-pages.json`.
   `enabled` stays `false` regardless of what is verified here.
   `verify_before_enabling` stays `true`.
6. **After the verified URLs are added**, the *next* update step
   (a separate, reviewed change) will use this worksheet to update
   `config/watched-pages.json` (`url` / `owner` / `notes`) and
   `docs/source-verification-tracker.md` (Verified URL / Owner /
   Verification status). Do **not** make those edits as part of this
   worksheet pass.

---

## Scope of this run

Three sources from Batch 01, in order:

| # | Source ID | Label |
|---|---|---|
| 1 | `ghl-api-docs-root` | HighLevel API Documentation (Stoplight) — root |
| 2 | `ghl-help-center-root` | HighLevel Help Center — root |
| 3 | `ghl-platform-updates` | HighLevel Platform Updates / What's Changed |

---

## 1. HighLevel API Documentation (Stoplight) — root

- **Source ID:** `ghl-api-docs-root`
- **Current URL (from config):** `https://highlevel.stoplight.io/`
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open `https://highlevel.stoplight.io/` in a normal browser window
   (no login).
2. Confirm the page loads as a HighLevel Stoplight workspace —
   HighLevel branding visible, page title references HighLevel.
3. Confirm the left-hand navigation lists the public API resources
   (Contacts, Conversations, Workflows, Calendars, etc.).
4. Look for an OpenAPI / Swagger JSON link or "Download API spec"
   button anywhere on the page. If you find one, record the URL in
   the verified URL note for follow-up — it's a stronger fetcher
   target than HTML once the fetcher ships.
5. Confirm the public docs are reachable without any login wall.

### Domain that must be confirmed

`highlevel.stoplight.io` (an official HighLevel-hosted Stoplight
workspace).

### Section URL to look for

The Stoplight workspace **root** *is* the appropriate section-level
URL for this entry — there is no deeper "section" to drill into for
this row. The watch target is the workspace itself.

Optionally, record any OpenAPI JSON URL you find for a future
phase — that becomes a separate, structured-content source, not a
replacement for this one.

### What counts as Verified

- URL resolves on `highlevel.stoplight.io`.
- Page renders the HighLevel API workspace with a resource navigation.
- Public docs reachable without login.
- (Nice to have) An OpenAPI spec URL is identified and noted for the
  future.

### What counts as Needs URL refinement

- URL resolves but the workspace appears to be a *different* HighLevel
  workspace (e.g. an old / marketplace / partner workspace) rather
  than the canonical public API.
- URL redirects to a sign-in page only.
- A clearly more canonical "API home" URL exists elsewhere on
  HighLevel-owned property (e.g. a Developer Portal hub) and would be
  a better watch root.

### What should not be changed

- `source_type` stays `api_docs`. Do not change to `developer_portal`
  even if the workspace is also a developer surface.
- `expected_content_type` stays `html` for this entry. The OpenAPI
  JSON, if found, is recorded for a *future* separate entry — not by
  flipping this row to `openapi`.
- `content_selector` stays `null` (per the no-content_selector rule
  for this run).
- `enabled` stays `false`. `verify_before_enabling` stays `true`.

---

## 2. HighLevel Help Center — root

- **Source ID:** `ghl-help-center-root`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open `https://help.gohighlevel.com/` in a normal browser window
   (no login).
2. Confirm the page is the official HighLevel help portal — HighLevel
   branding, official domain.
3. Identify how categories / sections are presented (a category grid,
   a top-nav menu, a sidebar, etc.).
4. **Capture the URL pattern for sub-sections.** Click into any
   one category (e.g. "Workflows") and inspect the URL bar — does the
   sub-section path look like:
   - `/support/solutions/folders/<numeric-id>` (Freshdesk pattern)
   - `/category/<slug>` (Document360 pattern)
   - `/en/category/<slug>` (Document360 with locale)
   - `/articles/<slug>` (Intercom / Helpscout)
   - Something else?
   Note the pattern — this is the single most important output of
   this verification, because ~46 other entries inherit it.
5. Confirm the help center is publicly accessible without login.

### Domain that must be confirmed

`help.gohighlevel.com` (the official HighLevel help portal).

### Section URL to look for

The help portal **root** is the appropriate watch target for this
entry — this row tracks the root index itself, not any sub-section.

The actual *output* of this verification is the **URL pattern** for
sub-sections (recorded in the Verified URL note as a pattern example),
which other tracker rows will use during their own verification.

### What counts as Verified

- URL resolves on `help.gohighlevel.com`.
- Page renders a category index / section list.
- Help center is publicly accessible without login.
- The sub-section URL pattern is identified and recorded (as a
  pattern example, in the verified URL note or alongside).

### What counts as Needs URL refinement

- URL redirects to a marketing page (`gohighlevel.com`) rather than
  the help portal itself.
- The page loads but doesn't expose a browsable section index
  (e.g. only a search box).
- The "canonical" help-center URL turns out to be a different host
  (e.g. `help-center.gohighlevel.com`, `docs.gohighlevel.com`,
  `support.gohighlevel.com`) — record that one instead.

### What should not be changed

- `source_type` stays `help_center`.
- `expected_content_type` stays `html`.
- `content_selector` stays `null`.
- `enabled` stays `false`. `verify_before_enabling` stays `true`.
- **Do not** start refining the ~46 other help-center entries during
  this run — that's a separate, reviewed update once this pattern
  is captured.

---

## 3. HighLevel Platform Updates / What's Changed

- **Source ID:** `ghl-platform-updates`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the current URL (`https://help.gohighlevel.com/`) — note that
   this is a known placeholder, not the actual changelog.
2. Search the help center for "What's New", "What's Changed",
   "Release Notes", "Changelog", or "Product Updates".
3. Alternatively, check directly from the HighLevel app UI — many
   SaaS products surface a "What's New" link in the bell / help
   menu. If so, follow it and record where it lands.
4. Also worth checking: `ideas.gohighlevel.com`,
   `changelog.gohighlevel.com`, `updates.gohighlevel.com`,
   `productupdates.gohighlevel.com` — note whether any of those
   resolve on official HighLevel infrastructure.
5. Confirm the chosen page is a **chronological feed** of platform
   updates (dated entries, most recent first), not a static
   "About" / "Overview" page.
6. Confirm the most recent entry is recent (within the last 30–60
   days). Stale feeds usually mean the URL has moved.

### Domain that must be confirmed

Any official HighLevel-owned domain that hosts the chronological
changelog. Candidates (in rough order of likelihood):

- `help.gohighlevel.com` — sub-section under the help center
- A dedicated subdomain such as `changelog.gohighlevel.com`,
  `updates.gohighlevel.com`, or similar
- `ideas.gohighlevel.com` — usually feature requests, **not** the
  changelog (record but probably wrong target)
- `marketplace.gohighlevel.com` — usually app listings, not the
  changelog (also probably wrong target)

### Section URL to look for

A page (or feed) that lists platform updates **chronologically**,
with dated entries. Examples of acceptable shapes:

- A `/whats-new/` / `/changelog/` / `/release-notes/` path under the
  help center.
- A dedicated subdomain whose index page is the chronological feed.
- An RSS / Atom feed URL (record it as a bonus — same target, more
  stable for diffing once the fetcher exists).

### What counts as Verified

- The verified URL resolves on an official HighLevel domain.
- The page is a dated chronological feed of platform updates.
- The most recent entry is reasonably recent (within ~60 days).
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- An official-looking changelog URL was identified but the page is
  empty / stale / "coming soon" / behind login — record the URL
  anyway, but note the blocker.
- Multiple candidate "updates" feeds were found (e.g. a product
  changelog AND a marketing release-announcement feed) and a
  judgement call is needed about which is canonical — record both,
  flag for a follow-up decision.

### What counts as Deferred (special-case for this source)

- No publicly accessible changelog can be found anywhere on official
  HighLevel infrastructure after a reasonable search. In that case
  mark **Deferred** in the tracker and flag for product-team follow-up
  — **do not invent a URL**.

### What should not be changed

- `source_type` stays `changelog`.
- `expected_content_type` stays `html`.
- `content_selector` stays `null`.
- `enabled` stays `false`. `verify_before_enabling` stays `true`.
- Do not build any RSS subscription, scraper, or alerting on top of
  the verified URL — that is post-fetcher work.

---

## After this worksheet is filled in

When all three Verified URL fields above are populated (or each is
explicitly marked Needs URL refinement / Deferred with reasoning):

1. **Do not** edit `config/watched-pages.json` or
   `docs/source-verification-tracker.md` as part of this worksheet pass.
2. Open a *separate* update step. In that next step:
   - For each verified source, update `config/watched-pages.json`:
     `url` → verified URL, `owner` → GitHub username, `notes`
     → short verification record.
   - For each row in `docs/source-verification-tracker.md`:
     Verified URL → same URL, Owner → GitHub username, Verification
     status → `Verified` / `Needs URL refinement` / `Deferred`.
3. Commit that next step per the
   [`phase-1-verification-execution-guide.md`](phase-1-verification-execution-guide.md)
   convention: one small commit, message
   `docs: verify sources ghl-api-docs-root, ghl-help-center-root, ghl-platform-updates`.
4. **Do not flip `enabled` to `true`** in that step either. Verified
   ≠ enabled. The enable gate is downstream of the fetcher being
   built.
