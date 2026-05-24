# Manual Verification — Run 03

> Companion docs: this is the execution worksheet for the seven AI /
> agent / MCP / knowledge-base sources in
> [`source-verification-batch-03.md`](source-verification-batch-03.md).
> The process this worksheet follows is defined in
> [`phase-1-verification-execution-guide.md`](phase-1-verification-execution-guide.md).
> The running status of record is in
> [`source-verification-tracker.md`](source-verification-tracker.md).
> Prior worksheet:
> [`manual-verification-run-01.md`](manual-verification-run-01.md).

## Manual verification instructions for Sedrick

1. **Open each current URL manually in the browser.** Do not run any
   script, do not use `curl` / `wget`, do not call any fetcher.
2. **Use the candidate title as the search target inside the official
   HighLevel support portal.** The current URLs are placeholders; the
   candidate title is the phrase to search for inside
   `help.gohighlevel.com` or the relevant developer surface.
3. **Confirm the page is on an official HighLevel domain.** Acceptable
   domains: `help.gohighlevel.com`, `gohighlevel.com`,
   `marketplace.gohighlevel.com`, `highlevel.stoplight.io`,
   `developers.gohighlevel.com`. No third-party mirrors, no community
   sites.
4. **Prefer exact article or folder URLs over the broad support portal
   root.** When the candidate maps to multiple plausible articles, pick
   the most authoritative *section* URL and record any sibling articles
   in the verification note rather than splitting into multiple entries.
5. **Paste the verified URL back into this worksheet under
   `Verified URL`** for each source below. Use the literal URL, no
   markdown link wrapping.
6. **Do not set `enabled` to `true`** in `config/watched-pages.json`.
   `enabled` stays `false` regardless of what is verified here.
   `verify_before_enabling` stays `true`.
7. **Do not change scripts.** `scripts/fetch_ghl_docs.py`,
   `scripts/parse_and_diff.py`, and `scripts/write_updates.py` are out
   of scope for this worksheet.
8. **Do not change GitHub Actions.** `.github/workflows/daily-docs-watch.yml`
   is out of scope.
9. **After the verified URLs are added**, the *next* update step
   (a separate, reviewed change) will use this worksheet to update
   `config/watched-pages.json` (`url` / `owner` / `notes`) and
   `docs/source-verification-tracker.md` (Verified URL / Owner /
   Verification status). Do **not** make those edits as part of this
   worksheet pass.

---

## Batch 3 verification priority

Recommend verifying in this order:

1. **AI Studio** (`ghl-ai-studio`)
2. **Agent Studio** (`ghl-agent-studio`)
3. **Conversation AI** (`ghl-conversation-ai`)
4. **Voice AI** (`ghl-voice-ai`)
5. **Knowledge Bases** (`ghl-knowledge-bases`)
6. **Workflow AI** (`ghl-workflow-ai`)
7. **MCP Server** (`ghl-mcp-server`)

**Why this order:** AI Studio and Agent Studio are verified first
because several Batch 3 sources overlap around AI agents, agent
configuration, Ask AI routing, and knowledge grounding. Resolving the
Studio-vs-Studio relationship up front anchors the verification of the
sibling AI surfaces (Conversation AI, Voice AI) and clarifies whether
Knowledge Bases is documented as a standalone surface or as part of
agent setup. MCP Server is verified last because it may require
developer-portal URL refinement (a separate domain space from the help
center) and is the most likely entry in this batch to end up
**Deferred** if no public MCP documentation exists yet.

---

## Scope of this run

Seven sources from Batch 03, listed in their config order:

| # | Source ID | Label |
|---|---|---|
| 1 | `ghl-voice-ai` | HighLevel Help Center — Voice AI |
| 2 | `ghl-conversation-ai` | HighLevel Help Center — Conversation AI |
| 3 | `ghl-workflow-ai` | HighLevel Help Center — Workflow AI |
| 4 | `ghl-ai-studio` | HighLevel Help Center — AI Studio |
| 5 | `ghl-agent-studio` | HighLevel Help Center — Agent Studio |
| 6 | `ghl-mcp-server` | HighLevel MCP Server |
| 7 | `ghl-knowledge-bases` | HighLevel Help Center — Knowledge Bases |

(Verification *execution* order is the priority list above, not this
config order.)

---

## 1. HighLevel Help Center — Voice AI

- **Source label:** HighLevel Help Center — Voice AI
- **Source ID:** `ghl-voice-ai`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** AI Tools in HighLevel
- **Candidate status:** Needs exact URL
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the support portal root and search for "AI Tools in HighLevel".
2. From the results, look specifically for the official HighLevel
   overview of **Voice AI** — Voice AI overview, Voice AI agents,
   AI Employee voice surface, or a dedicated voice-agent article or
   folder.
3. Drill into the most authoritative landing page or folder (prefer a
   folder index over a single article when both exist).
4. Skim the article / folder contents for coverage of: voice agent
   setup, scripts / prompts, voice and persona selection, escalation
   to human, voicemail handling, supported telephony backends.
5. Note any overlap with **AI Employee** (umbrella) and **Phone
   System** (telephony infra) but do not collapse this entry into
   either.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).
Alternate official domains (`gohighlevel.com` product page) are
acceptable if the help center has no dedicated Voice AI surface.

### Section or article URL to look for

The official HighLevel AI Tools overview, Voice AI overview, Voice AI
agents, AI Employee, or voice-agent support article or folder.

### What counts as Verified

- Verified URL resolves on an official HighLevel domain.
- The page is specifically about the Voice AI product (voice agent
  configuration, speech, escalation), not about phone-system infra or
  generic AI features.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- Voice AI exists as a surface but is only documented inside a broader
  "AI Tools" or "AI Employee" article without its own landing — record
  the broader page as the candidate and flag for follow-up.
- Multiple plausible Voice AI articles exist (overview, setup,
  configuration) and a judgement call is needed on the canonical
  one — record all candidates.
- Voice AI has been rebranded or folded into Agent Studio.

### What should not be changed

- `source_type` stays `help_center`. Do not change to `developer_portal`.
- `content_selector` stays `null` (no changes in this run).
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge this entry with `ghl-phone-system` or `ghl-ai-employee`
  during this worksheet — overlap is expected; separate entries give
  better diff signal.

---

## 2. HighLevel Help Center — Conversation AI

- **Source label:** HighLevel Help Center — Conversation AI
- **Source ID:** `ghl-conversation-ai`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** AI Tools in HighLevel
- **Candidate status:** Needs exact URL
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the support portal root and search for "AI Tools in HighLevel"
   and "Conversation AI".
2. From the results, identify the official Conversation AI surface —
   Conversation AI, AI Employee text/inbox surface, bot response mode,
   conversation automation, or AI chat article or folder.
3. Drill into the most authoritative landing page or folder.
4. Skim the article / folder contents for coverage of: agent setup,
   intents / topics, training data, escalation rules, suppression /
   opt-out, channel scoping (SMS vs. chat vs. email), bot response
   mode toggling.
5. Note the relationship to `ghl-conversations` (inbox UI surface) and
   `ghl-ai-employee` (umbrella). Conversation AI is the *responder*
   operating *in* the inbox, not the inbox itself.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

The official Conversation AI, AI Employee, AI Tools, bot response
mode, conversation automation, or AI chat support article or folder.

### What counts as Verified

- Verified URL resolves on an official HighLevel domain.
- The page is specifically about AI handling of inbox conversations
  (text / chat / email), not about the inbox UI itself or about voice.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- Conversation AI exists only as a sub-topic inside a general "AI
  Tools" / "AI Employee" article without its own landing.
- Suppression / opt-out behavior is documented separately from the
  agent overview and needs a second linked entry (record both).
- Conversation AI has been rebranded (e.g. merged into AI Employee
  inbox features) — record the new landing and flag for follow-up.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge with `ghl-conversations` (Batch 01) — Conversations is
  the inbox view, Conversation AI is the autonomous responder.
- Do not merge with `ghl-ai-employee` or any other AI sibling during
  this worksheet.

---

## 3. HighLevel Help Center — Workflow AI

- **Source label:** HighLevel Help Center — Workflow AI
- **Source ID:** `ghl-workflow-ai`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** A List of Workflow Actions
- **Candidate status:** Needs exact URL
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the support portal root and search for "A List of Workflow
   Actions".
2. From that article (and any sibling articles in the same folder),
   identify any **Workflow AI action**, **AI action**, **generated
   content**, **AI assistant**, **GPT action**, or **custom code
   action** references.
3. If the workflow actions article catalogs AI steps inline (mixed
   with non-AI steps), record the article URL and note that AI steps
   are not separately landing-paged. If a dedicated "Workflow AI" /
   "AI Workflow Steps" sub-section exists, prefer that.
4. Skim for coverage of: per-AI-step inputs / outputs, model
   selection, cost / usage, error handling, deprecated AI steps.
5. Decide: distinct Workflow AI landing exists → **Verified** with
   that URL; AI steps only documented inside the broader actions
   article → **Needs URL refinement** with the actions article URL
   recorded and a config-consolidation proposal flagged.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

The workflow actions article and any Workflow AI action, AI action,
generated content, AI assistant, or custom code action references.

### What counts as Verified

- Verified URL resolves on an official HighLevel domain.
- The page (or clear sub-section) is specifically about AI capabilities
  **inside** workflows — per-step contracts (inputs / outputs), not
  generic AI product overviews.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- "Workflow AI" does not exist as its own section and AI steps are
  intermixed with regular workflow actions — record the actions
  article URL and note the merge candidate
  (`ghl-workflow-actions`).
- AI steps are documented only via per-step articles (Classify,
  Summarize, Generate, etc.) with no overview — record the most
  authoritative single article and note the article-level expansion
  is deferred.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge with `ghl-workflow-actions` (Batch 01) during this
  worksheet — even if findings argue for consolidation, the merge is a
  separate config decision.
- Do not break per-AI-step articles into their own entries.

---

## 4. HighLevel Help Center — AI Studio

- **Source label:** HighLevel Help Center — AI Studio
- **Source ID:** `ghl-ai-studio`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** How to Use AI Agent Studio in HighLevel
- **Candidate status:** Exact URL provided
- **Candidate exact URL:** `https://help.gohighlevel.com/support/solutions/articles/155000006058-how-to-use-the-ai-agent-studio-in-highlevel`
- **Also compare against:** `https://help.gohighlevel.com/support/solutions/articles/155000007393-agent-studio-overview`
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the candidate exact URL in the browser. Confirm the article
   loads on `help.gohighlevel.com/support/solutions/articles/...`
   without login.
2. Confirm the article is current (recent updated-date, no "deprecated"
   notice).
3. Read the article and decide whether it is the best primary surface
   for **AI Studio** specifically (prompts, personas, tools, model
   selection — the *configuration UI* layer).
4. Open the "Also compare against" Agent Studio overview URL in a
   second tab. Compare: does the AI Studio article and the Agent
   Studio overview describe the **same product under two names**, two
   **distinct products** (configuration layer vs. agent-composition
   layer), or one **subset of the other**?
5. Record the relationship in the verification note. The relationship
   is the most important output of this verification, even more than
   the URL itself.
6. If AI Studio is genuinely a distinct surface, record the candidate
   exact URL as **Verified URL**. If AI Studio has been folded into
   Agent Studio, mark **Needs URL refinement** and propose collapsing
   this entry in a follow-up config update.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

Confirm this article is official, current, and relevant to AI Studio
setup and agent creation.

### What counts as Verified

- The candidate URL resolves on `help.gohighlevel.com`.
- The article is current and primarily about AI Studio as a
  configuration surface (not a redirect to a different product).
- The relationship between AI Studio and Agent Studio is recorded in
  the verification note.
- The article is publicly accessible without login.

### What counts as Needs URL refinement

- The article exists but is primarily *Agent Studio* content with AI
  Studio mentioned only in passing — record both URLs, flag the merge
  question for follow-up.
- "AI Studio" has been deprecated / renamed to "Agent Studio" — record
  the Agent Studio URL as the candidate and flag for consolidation.
- A more specific AI Studio folder index exists at a higher level than
  this article — record the folder URL instead.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge with `ghl-agent-studio` during this worksheet, even if
  findings suggest they are the same product. Verification records the
  finding; the merge is a separate reviewed config decision.

---

## 5. HighLevel Help Center — Agent Studio

- **Source label:** HighLevel Help Center — Agent Studio
- **Source ID:** `ghl-agent-studio`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** Agent Studio Overview
- **Candidate status:** Exact URL provided
- **Candidate exact URL:** `https://help.gohighlevel.com/support/solutions/articles/155000007393-agent-studio-overview`
- **Also compare against:** `https://help.gohighlevel.com/support/solutions/articles/155000006677-ask-ai-agent-studio-integration`
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the candidate exact URL in the browser. Confirm the article
   loads on `help.gohighlevel.com/support/solutions/articles/...`
   without login.
2. Confirm the article is current and is the primary overview for
   Agent Studio (agent definition, capability / tool wiring, scope,
   deployment to Voice / Conversation / Workflow surfaces).
3. Open the "Also compare against" Ask AI / Agent Studio integration
   URL in a second tab. Decide whether **Ask AI** is part of Agent
   Studio, a sibling product that *uses* Agent Studio, or a separate
   surface that should be tracked on its own at some future point.
4. Cross-reference with the AI Studio verification above — confirm or
   contradict the relationship recorded there.
5. Record the candidate exact URL as **Verified URL** if the overview
   is the right primary surface. If a folder index above the article
   exists (e.g. an "Agent Studio" Freshdesk folder), prefer the folder
   URL.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

Confirm this article is official, current, and the best primary Agent
Studio overview page.

### What counts as Verified

- The candidate URL resolves on `help.gohighlevel.com`.
- The article is current and is the canonical Agent Studio overview
  (or a folder index that supersedes it is recorded instead).
- The relationship to AI Studio and to Ask AI is recorded in the
  verification note.
- The article is publicly accessible without login.

### What counts as Needs URL refinement

- The overview article exists but is shallow (a stub) and a richer
  Agent Studio folder / setup guide is the real canonical surface —
  record the richer URL.
- Ask AI integration is documented as a peer surface that arguably
  deserves its own watch entry — note the proposal but do not add an
  entry in this worksheet.
- Agent Studio has been rebranded or absorbed into a broader "AI
  Agents" surface — record the new landing.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge with `ghl-ai-studio` during this worksheet, even if
  findings argue for consolidation.
- Do not add an `ask-ai` entry to the config as part of this run.

---

## 6. HighLevel MCP Server

- **Source label:** HighLevel MCP Server
- **Source ID:** `ghl-mcp-server`
- **Current URL (from config):** `https://highlevel.stoplight.io/`
- **Candidate URL or title:** GoHighLevel Developers
- **Candidate status:** Needs URL refinement
- **Candidate URL:** `https://developers.gohighlevel.com`
- **Also compare against:** `https://marketplace.gohighlevel.com/docs/`
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open `https://developers.gohighlevel.com` in the browser. Confirm
   the domain resolves on official HighLevel infrastructure and is not
   a third-party developer aggregator.
2. Look in the navigation for **MCP Server**, **MCP**, **Model Context
   Protocol**, developer tools, integrations, API, automation,
   marketplace, or protocol-related pages.
3. Open the also-compare URL `https://marketplace.gohighlevel.com/docs/`
   in a second tab. Look for the same MCP / protocol references there.
   Decide which of the two surfaces is the canonical developer home
   for MCP.
4. Also check `https://highlevel.stoplight.io/` (the current URL) for
   an MCP section — record whether MCP material lives in Stoplight,
   the developer portal, the marketplace docs, or nowhere yet.
5. If a dedicated MCP page exists on any official surface: record that
   URL as **Verified URL**.
6. If no MCP-specific documentation exists publicly anywhere on
   HighLevel infrastructure: mark the source **Deferred** and flag for
   revisit once HighLevel publishes MCP docs. **Do not invent a URL.**

### Domain that should be confirmed

Any official HighLevel-owned developer surface. Candidates (in rough
order of likelihood):

- `developers.gohighlevel.com` — primary developer hub if it exists
- `marketplace.gohighlevel.com/docs/` — marketplace developer docs
- `highlevel.stoplight.io` — Stoplight workspace (current URL)
- A dedicated MCP subdomain or GitHub repo readme on an official
  HighLevel-owned account

### Section or article URL to look for

An official MCP Server, developer tools, integrations, API,
automation, marketplace, or protocol-related page.

### What counts as Verified

- The verified URL resolves on an official HighLevel domain.
- The page covers the HighLevel **MCP Server implementation**
  specifically — endpoints, auth, exposed resources, tool / prompt /
  resource primitives.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- A developer portal exists at `developers.gohighlevel.com` but its
  MCP coverage is shallow or buried — record the developer portal
  root and note the gap.
- MCP is mentioned across multiple surfaces (Stoplight, marketplace
  docs, developer portal) and the canonical home is ambiguous —
  record the strongest candidate and flag for follow-up.
- MCP docs exist only behind a marketplace-app install flow — record
  the install-flow URL and note the gating.

### What counts as Deferred (special-case for this source)

- No publicly accessible MCP documentation can be found anywhere on
  official HighLevel infrastructure after a reasonable search across
  the developer portal, marketplace docs, Stoplight, and any
  HighLevel-owned GitHub readme. Mark **Deferred** and flag for revisit
  once MCP docs ship. **Do not invent a URL.**

### What should not be changed

- `source_type` stays `developer_portal` even if MCP docs end up on
  Stoplight (which is `api_docs` in the schema). `source_type`
  reflects audience, not domain.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge with `ghl-api-docs-root` even if MCP docs live alongside
  the API docs.

---

## 7. HighLevel Help Center — Knowledge Bases

- **Source label:** HighLevel Help Center — Knowledge Bases
- **Source ID:** `ghl-knowledge-bases`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** How to Use AI Agent Studio in HighLevel
- **Candidate status:** Exact URL provided as supporting source
- **Candidate exact URL:** `https://help.gohighlevel.com/support/solutions/articles/155000006058-how-to-use-the-ai-agent-studio-in-highlevel`
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the candidate exact URL in the browser. Confirm the article
   loads on `help.gohighlevel.com/support/solutions/articles/...`
   without login.
2. Read the article specifically for **Knowledge Base** content: KB
   creation, file / URL ingestion, supported source types, chunking
   limits, retrieval configuration, integration with AI agents.
3. Decide:
   - The article has *substantive* Knowledge Base setup content
     (creation, ingestion, retrieval) → record this URL as a candidate
     but keep looking for a stronger dedicated Knowledge Bases article
     or folder.
   - The article only mentions Knowledge Bases as a step inside agent
     setup → this is a **supporting source only**; the canonical
     Knowledge Bases article is elsewhere.
4. Search the support portal for "Knowledge Base", "Knowledge Bases",
   "AI Knowledge", "RAG", "Grounding". Record any dedicated Knowledge
   Bases article or folder you find.
5. If a stronger dedicated Knowledge Bases surface exists, record
   *that* as **Verified URL** and keep the AI Agent Studio article URL
   in the verification note as a cross-reference.
6. If no dedicated Knowledge Bases surface exists and KB content lives
   only inside agent-setup articles, mark **Needs URL refinement**,
   record the AI Agent Studio article URL as the best available
   supporting source, and flag the sub-section gap for follow-up.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

Confirm whether the candidate article contains knowledge base setup or
grounding references. If it only mentions knowledge bases as part of
agent setup, mark it as a supporting source and keep looking for a
stronger Knowledge Bases article or folder.

### What counts as Verified

- The verified URL resolves on `help.gohighlevel.com`.
- The page is specifically about Knowledge Base lifecycle (creation,
  ingestion, retrieval), not generic "what is RAG" content and not
  only an agent-setup walkthrough.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- The candidate exact URL contains Knowledge Base content only as a
  step inside agent setup — record the URL as a **supporting source**
  with a note, and flag the dedicated Knowledge Bases article as
  still to be located.
- A dedicated Knowledge Bases article exists but is buried under a
  specific AI product (e.g. Conversation AI) rather than as a shared
  resource — record the URL but note the structural issue.
- KB content is split across multiple articles (ingestion in one,
  retrieval in another) with no overview — record the most
  authoritative single article and flag the gap.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge with `ghl-ai-employee`, `ghl-conversation-ai`,
  `ghl-voice-ai`, or any other AI product entry during this worksheet,
  even if findings show KBs are tightly coupled to one product.

---

## After this worksheet is filled in

When all seven Verified URL fields above are populated (or each is
explicitly marked Needs URL refinement / Deferred with reasoning):

1. **Do not** edit `config/watched-pages.json` or
   `docs/source-verification-tracker.md` as part of this worksheet pass.
2. Open a *separate* update step. In that next step:
   - For each verified source, update `config/watched-pages.json`:
     `url` → verified URL, `owner` → username, `notes`
     → short verification record.
   - For each row in `docs/source-verification-tracker.md`:
     Verified URL → same URL, Owner → username, Verification status
     → `Verified` / `Needs URL refinement` / `Deferred`.
3. Commit that next step per the
   [`phase-1-verification-execution-guide.md`](phase-1-verification-execution-guide.md)
   convention: one small commit per 3–5 sources, message
   `docs: verify sources <id1>, <id2>, <id3>`.
4. **Do not flip `enabled` to `true`** in that step either. Verified
   ≠ enabled. The enable gate is downstream of the fetcher being
   built.
