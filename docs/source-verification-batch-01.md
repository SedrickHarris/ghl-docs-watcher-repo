# Source Verification — Batch 01

## Batch 01 purpose

This batch verifies the highest-impact HighLevel sources before any live
fetching or automation is enabled. The goal is to confirm official URLs
and section-level targets only — no source is enabled, no script is
changed, no fetcher runs.

## Scope

Ten Phase 1 sources, in this order:

| # | Source ID | Label |
|---|---|---|
| 1 | `ghl-api-docs-root` | HighLevel API Documentation (Stoplight) — root |
| 2 | `ghl-help-center-root` | HighLevel Help Center — root |
| 3 | `ghl-platform-updates` | HighLevel Platform Updates / What's Changed |
| 4 | `ghl-workflows` | HighLevel Help Center — Workflows |
| 5 | `ghl-workflow-builder` | HighLevel Help Center — Workflow Builder |
| 6 | `ghl-workflow-triggers` | HighLevel Help Center — Workflow Triggers |
| 7 | `ghl-workflow-actions` | HighLevel Help Center — Workflow Actions |
| 8 | `ghl-workflow-developer-resources` | HighLevel Workflow Developer Resources |
| 9 | `ghl-calendars-appointments` | HighLevel Help Center — Calendars & Appointments |
| 10 | `ghl-conversations` | HighLevel Help Center — Conversations |

## Cross-cutting rules

These apply to every entry in this batch:

- **Do not enable.** `enabled` stays `false` and `verify_before_enabling`
  stays `true` in `config/watched-pages.json`. Enabling is a separate
  gate, downstream of fetcher implementation.
- **Do not fetch programmatically.** Verification is human-in-browser only
  in this phase. No scripts run, no GitHub Actions are touched.
- **Do not edit `config/watched-pages.json`** as part of this batch.
  Record findings here and in `docs/source-verification-tracker.md`;
  config refinements ship as their own reviewed PR.
- **Section-level, not article-level.** If a section drills down into a
  rich set of articles, that's signal for a future phase — not for this
  batch.

---

## 1. HighLevel API Documentation (Stoplight) — root

- **Source ID:** `ghl-api-docs-root`
- **Current URL (from config):** `https://highlevel.stoplight.io/`
- **Target section to verify:** Stoplight workspace root / API resource index
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
This is the foundation for every API-driven workflow and integration.
If the API surface, endpoint paths, auth, or rate-limit semantics change,
every consuming workflow is potentially affected. It's also the cleanest
candidate for structured (OpenAPI JSON) diffing in a future phase.

**Verification steps**
1. Open `https://highlevel.stoplight.io/` in a browser.
2. Confirm the page is the official HighLevel Stoplight workspace (HighLevel
   branding, no third-party hosting).
3. Confirm the left-hand navigation lists the public API resources
   (Contacts, Conversations, Workflows, Calendars, etc.).
4. Note whether an OpenAPI/Swagger JSON spec is linked from this page
   (record the URL in the tracker's Notes column if so — it's a stronger
   future watch target than HTML).
5. Confirm no auth wall blocks public documentation pages.

**What counts as verified**
- URL resolves on `highlevel.stoplight.io` (official subdomain).
- Page shows the HighLevel API resource navigation.
- Public docs are reachable without login.
- If an OpenAPI spec URL is exposed, it is recorded for a future phase.

**What should not be changed yet**
- Do not switch the entry to per-resource URLs (e.g. `…/contacts`,
  `…/workflows`) — that's article-level work, deferred.
- Do not change `source_type` from `api_docs` even if Stoplight is also a
  developer portal in spirit.
- Do not switch `expected_content_type` to `openapi` yet — that requires
  the fetcher to support JSON diffing.

**Risk notes**
- Stoplight occasionally A/B tests layouts; whole-page HTML diffing will
  be noisy. The OpenAPI spec, if available, is a far more stable target.
- Stoplight's CSS class structure changes more often than the API itself —
  a `content_selector` may help once we move to active fetching.

---

## 2. HighLevel Help Center — root

- **Source ID:** `ghl-help-center-root`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Help center root / category landing index
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
This URL is the anchor for ~46 other section-level entries that currently
point at the same root as a placeholder. If the help center is migrated
or rebranded, every help-center entry needs to be re-pointed in one
coordinated sweep.

**Verification steps**
1. Open `https://help.gohighlevel.com/` in a browser.
2. Confirm the page is the official HighLevel help portal (HighLevel
   branding, official domain).
3. Identify the structural pattern for sections/categories (is it a
   Freshdesk-style `/support/solutions/folders/...`, a Document360-style
   `/category/...`, or something else?). Record the pattern in Notes.
4. Confirm the help center is publicly accessible without login.

**What counts as verified**
- URL resolves on `help.gohighlevel.com` (official subdomain).
- Page renders a category index, not a 404 or a redirect to a marketing
  page.
- The URL pattern for sub-sections is identified and recorded in Notes,
  for later per-section URL refinement.

**What should not be changed yet**
- Do not enumerate sub-section URLs from this verification — each
  sub-section is its own tracker row and gets its own verification.
- Do not change `source_type` from `help_center`.
- Do not enable.

**Risk notes**
- Help portals (Freshdesk, Document360, Zendesk, etc.) change URL schemes
  during platform migrations more often than the underlying content
  changes. The URL pattern is part of what's being verified, not just the
  domain.
- If the help center sits behind any geo-redirect or A/B test, root
  verification may not surface the issue — flag it for a per-section
  check later.

---

## 3. HighLevel Platform Updates / What's Changed

- **Source ID:** `ghl-platform-updates`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Official platform changelog / "What's Changed" / "What's New" feed
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
This is the **highest-signal source in the entire watch list**. It is the
canary for breaking changes, feature deprecations, and platform-wide
rollouts. If anything is enabled first once the fetcher exists, this
should be it.

**Verification steps**
1. From the HighLevel help center (or product UI, if a public link
   exists), locate the official changelog / "What's Changed" / "What's
   New" / "Release Notes" page.
2. Confirm it is on an official HighLevel domain.
3. Confirm it is a chronological feed of updates (dated entries, most
   recent first), not a static "About" page.
4. Confirm the most recent entry is recent (days or weeks, not months) —
   stale feeds are a signal that the URL has moved.
5. Record the verified URL in the tracker. **Do not edit the config
   itself in this batch.**

**What counts as verified**
- URL resolves on an official HighLevel domain.
- Page shows a dated list of platform updates.
- Most recent entry is reasonably current (within the last 30–60 days).
- The page is publicly accessible.

**What should not be changed yet**
- Do not build any alerting or RSS subscription on top of this URL — that
  is post-fetcher work.
- Do not change `source_type` from `changelog`.
- Do not enable.

**Risk notes**
- Changelogs are often the **first** thing to move during platform
  redesigns. The current placeholder URL (`https://help.gohighlevel.com/`)
  is intentionally a root — the real URL needs finding.
- HighLevel may have multiple "updates" feeds (product changelog vs.
  marketing release announcements vs. blog). Pick the one closest to a
  technical change log; record other candidates in Notes for later
  consideration.
- If no public changelog exists, mark this source **Deferred** and flag
  it for product-team follow-up — do not invent a URL.

---

## 4. HighLevel Help Center — Workflows

- **Source ID:** `ghl-workflows`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Workflows section landing page (overview, distinct from Builder/Triggers/Actions sub-sections)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Workflows are the central automation primitive in HighLevel and the
foundation for the consuming `ghl-workflows` repo. Changes to the
Workflows section affect how every client engagement is designed and
built.

**Verification steps**
1. From the help center root, navigate to the **Workflows** category /
   section.
2. Confirm a distinct Workflows landing page exists (separate URL from
   Workflow Builder, Workflow Triggers, Workflow Actions).
3. Skim the article titles under this section to confirm the section is
   genuinely about workflows-as-a-concept, not just a sub-feature.
4. Record the verified URL in the tracker.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain.
- URL is distinct from the Builder / Triggers / Actions URLs.
- Article list is non-trivial and recognizably about workflows.

**What should not be changed yet**
- Do not merge this entry with `ghl-workflow-builder` even if the help
  center groups them — keeping them separate gives finer-grained diff
  signal once the fetcher exists.
- Do not track individual articles from this section yet.

**Risk notes**
- HighLevel reorganizes the workflows area periodically (the surface
  itself is high-churn). Section may have been split, renamed, or folded
  into a broader "Automations" parent.
- If "Workflows" only exists as a parent that aggregates Builder /
  Triggers / Actions with no own landing page, mark **Needs URL
  refinement** and propose collapsing this entry into the parent during
  a future config update.

---

## 5. HighLevel Help Center — Workflow Builder

- **Source ID:** `ghl-workflow-builder`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Workflow Builder section landing page (canvas, drag-and-drop, save/publish semantics)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
The builder is the surface every client-build touches. UI changes
(save/publish semantics, node grouping, version history) propagate
directly into the `clients/{client}/checklists/` build steps in the
consuming workflows repo.

**Verification steps**
1. From the Workflows section (verified above), navigate to the **Workflow
   Builder** sub-section.
2. Confirm a distinct landing page exists. If it does not, this entry may
   not survive verification.
3. Look for articles about: building, saving, publishing, version history,
   testing/preview, draft vs. live.
4. Record the verified URL — or flag for refinement / consolidation.

**What counts as verified**
- Distinct landing page covering builder UI semantics on an official
  domain.
- Articles relate to building/publishing, not to triggers or actions
  specifically.

**What should not be changed yet**
- Do not track per-article URLs (e.g. "How to publish a workflow") — that
  is article-level work, deferred.
- Do not merge with `ghl-workflows` even if tempting.

**Risk notes**
- The builder may not have its own dedicated section in the help center;
  builder content may be intermixed with workflow content. If so, mark
  this entry **Needs URL refinement** or **Deferred** rather than
  pointing it at the same URL as `ghl-workflows`.

---

## 6. HighLevel Help Center — Workflow Triggers

- **Source ID:** `ghl-workflow-triggers`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Workflow Triggers reference / catalog landing page
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Triggers determine workflow entry. A change here — a new trigger type, a
deprecated trigger, a behavior change in an existing trigger — is a
**re-architecture risk** for every client workflow that uses it. This is
one of the most sensitive sources in the entire watch list.

**Verification steps**
1. From the Workflows section, navigate to the **Workflow Triggers**
   sub-section.
2. Confirm a distinct landing page or trigger catalog exists.
3. Skim the trigger list — is it a comprehensive reference, or sparse?
4. Record the verified URL.

**What counts as verified**
- Distinct landing page on an official domain that catalogs trigger
  types.
- Articles cover trigger configuration patterns, filters, entry
  conditions.

**What should not be changed yet**
- Do not break this into per-trigger entries — that's article-level work,
  deferred.
- Do not change `priority` from `high` even if the section looks sparse.

**Risk notes**
- HighLevel ships new trigger types frequently, especially as new product
  surfaces (AI, e-commerce, communities) come online. This section will
  churn. Once enabled, expect noisy diffs — a tight `content_selector`
  may be needed.
- Triggers and actions are sometimes co-documented; if the section
  doesn't exist as a standalone, propose merging Triggers + Actions in a
  future config update.

---

## 7. HighLevel Help Center — Workflow Actions

- **Source ID:** `ghl-workflow-actions`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Workflow Actions reference / catalog landing page
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Actions are the steps inside every workflow. Changes here affect every
workflow's behavior — new actions enable new patterns; changed actions
can silently break existing flows. Like Triggers, this is a sensitive
source.

**Verification steps**
1. From the Workflows section, navigate to the **Workflow Actions**
   sub-section.
2. Confirm a distinct landing page or actions catalog exists.
3. Skim the actions list (Send Email, Send SMS, AI step, Wait, Branch,
   etc.).
4. Record the verified URL.

**What counts as verified**
- Distinct landing page on an official domain cataloging action types.
- Articles cover action configuration, including AI-related actions if
  they exist as their own section.

**What should not be changed yet**
- Do not break into per-action entries — article-level work, deferred.
- Do not split out AI actions into a separate entry — `ghl-workflow-ai`
  already covers that surface.

**Risk notes**
- Actions expand the most often of any workflows sub-section, especially
  with AI features being added quarterly.
- If "AI workflow steps" are documented inside this section instead of
  under `ghl-workflow-ai`, note the overlap in Notes; do not change the
  config yet.

---

## 8. HighLevel Workflow Developer Resources

- **Source ID:** `ghl-workflow-developer-resources`
- **Current URL (from config):** `https://highlevel.stoplight.io/`
- **Target section to verify:** Developer-facing workflow material on Stoplight (custom actions, webhooks, workflow API)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
This covers the developer-facing workflow surface — custom workflow
actions, webhook contracts, the workflow API. Integrations, marketplace
apps, and any custom-built automation depend on these contracts being
stable.

**Verification steps**
1. Open `https://highlevel.stoplight.io/`.
2. Look in the Stoplight navigation for a Workflows-specific resource,
   webhook documentation, or a "Workflow Actions" / "Custom Actions" API
   reference.
3. Confirm the section is distinct from the general API docs.
4. Record the verified URL or note its absence.

**What counts as verified**
- A distinct workflows-related developer section exists on an official
  HighLevel domain.
- Webhook contracts, custom-action schemas, or workflow API endpoints are
  documented.

**What should not be changed yet**
- Do not change `source_type` from `developer_portal` to `api_docs` even
  if the section lives inside Stoplight — the *intent* of this entry is
  workflow-specific developer material, not the whole API surface.
- Do not collapse into `ghl-api-docs-root` — separate entries give better
  diff routing.

**Risk notes**
- This section may not exist as a distinct entity. If workflow developer
  material is scattered across general API docs rather than collected,
  mark **Deferred** and revisit when (a) the fetcher exists and per-page
  watching becomes practical, or (b) HighLevel publishes a dedicated
  workflow developer section.
- Custom workflow actions are a relatively new HighLevel feature;
  documentation may still be marketplace-focused rather than developer-
  focused.

---

## 9. HighLevel Help Center — Calendars & Appointments

- **Source ID:** `ghl-calendars-appointments`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Calendars & Appointments section landing page
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Calendar events and appointment statuses are the trigger source for many
of the most common GHL workflows: confirmations, reminders, no-show
recovery, review requests. Changes to appointment status semantics or
calendar event shapes cascade into every appointment-driven workflow.

**Verification steps**
1. From the help center root, navigate to **Calendars** (and/or
   **Appointments**).
2. Determine whether Calendars and Appointments are one combined section,
   two adjacent sections, or one parent with sub-sections.
3. Record the structure in Notes; record the verified URL for the
   landing page that best represents both.

**What counts as verified**
- Section landing page (or pages) exist on an official domain covering
  calendar setup, availability, booking, and appointment status
  semantics.

**What should not be changed yet**
- Do not split this single entry into separate `ghl-calendars` and
  `ghl-appointments` entries yet — defer to a future config update if
  the help center clearly separates them.
- Do not track per-calendar-type articles (Round Robin, Class, etc.).

**Risk notes**
- Calendars and Appointments may live under different parent sections
  (e.g. Calendars under "Calendars" and Appointments under "CRM"). If so,
  mark **Needs URL refinement** and propose splitting in a future config
  update.
- Calendar event payloads on webhooks have changed in the past — a
  related but separate watch target (developer resources) may be more
  useful for that risk.

---

## 10. HighLevel Help Center — Conversations

- **Source ID:** `ghl-conversations`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Conversations (unified inbox) section landing page
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Conversations is the messaging surface where most live customer
interaction happens — SMS replies, email threads, chat-widget messages,
AI agent transcripts all flow here. AI agents and reply-driven
workflows depend on Conversations behavior being stable.

**Verification steps**
1. From the help center root, navigate to the **Conversations** section.
2. Confirm a distinct landing page exists for the unified inbox.
3. Note whether per-channel articles (SMS, email, chat, voice) live
   inside Conversations or under their own top-level sections
   (`ghl-messaging`, `ghl-email`, `ghl-chat-widget`, `ghl-phone-system`).
4. Record the verified URL and the relationship to neighboring sections
   in Notes.

**What counts as verified**
- Distinct Conversations section landing page on an official domain.
- Section is about the inbox/unified-conversation surface, not about a
  specific channel.

**What should not be changed yet**
- Do not collapse this into `ghl-messaging`, `ghl-email`, or
  `ghl-chat-widget` even if there is heavy overlap. Overlap is expected
  and the separate entries give better surface-level routing for
  downstream implication docs.
- Do not drill into per-channel articles (they are owned by other
  entries).

**Risk notes**
- Conversations content overlaps with Messaging, Phone System, Email, and
  Chat Widget. Once enabled, the same content change may show up in
  multiple diffs — that's a feature (multiple surface views), not a bug.
- The "Conversation AI" feature is documented under `ghl-conversation-ai`,
  not here. If you see AI content mixed into this section, note it but
  don't change the config.

---

## Closing checklist for the verifier

Before declaring this batch complete:

- [ ] Every source above has an owner (replace `Unassigned`).
- [ ] Every source above has a status set on the tracker (`Verified`,
      `Needs URL refinement`, or `Deferred`).
- [ ] Findings (verified URL, candidate alternatives, structural notes)
      are recorded in `docs/source-verification-tracker.md` — not in
      `config/watched-pages.json`.
- [ ] `config/watched-pages.json` has been **left unchanged** by this
      batch.
- [ ] No source has been `enabled: true`.
- [ ] No script and no GitHub Action has been touched.
- [ ] Batch 02 is queued for the next 10 Phase 1 sources
      (Phone System through MCP Server).
