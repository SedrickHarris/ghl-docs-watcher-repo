# Source Verification — Batch 03

## Batch 03 purpose

This batch verifies the AI, agent, MCP, and knowledge base sources that
affect voice agents, conversation automation, workflow AI, agent
configuration, model context protocol support, and AI knowledge
grounding. This completes Phase 1 source verification planning without
enabling live fetching.

## Scope

Seven Phase 1 sources, in this order:

| # | Source ID | Label |
|---|---|---|
| 1 | `ghl-voice-ai` | HighLevel Help Center — Voice AI |
| 2 | `ghl-conversation-ai` | HighLevel Help Center — Conversation AI |
| 3 | `ghl-workflow-ai` | HighLevel Help Center — Workflow AI |
| 4 | `ghl-ai-studio` | HighLevel Help Center — AI Studio |
| 5 | `ghl-agent-studio` | HighLevel Help Center — Agent Studio |
| 6 | `ghl-mcp-server` | HighLevel MCP Server |
| 7 | `ghl-knowledge-bases` | HighLevel Help Center — Knowledge Bases |

## Cross-cutting rules

These apply to every entry in this batch:

- **Do not enable.** `enabled` stays `false` and `verify_before_enabling`
  stays `true` in `config/watched-pages.json`. Enabling is a separate
  gate, downstream of fetcher implementation.
- **Do not fetch programmatically.** Verification is human-in-browser
  only in this phase. No scripts run, no GitHub Actions are touched.
- **Do not edit `config/watched-pages.json`** as part of this batch.
  Record findings here and in `docs/source-verification-tracker.md`;
  config refinements ship as their own reviewed PR.
- **Section-level, not article-level.** If a section drills down into a
  rich set of articles, that's signal for a future phase — not for this
  batch.
- **The whole AI family is high-churn.** HighLevel's AI products have
  been renamed, re-bundled, and split repeatedly. Expect at least one
  of these seven sources to need URL refinement or deferral. Record
  what you find — don't force a verified URL on a section that no
  longer exists under its current label.
- **`ghl-ai-employee` (Batch 02) is the umbrella.** The six AI-family
  entries in this batch are sibling surfaces under that umbrella.
  Overlap with AI Employee content is expected; separate watch entries
  exist for diff-routing granularity.

---

## 1. HighLevel Help Center — Voice AI

- **Source ID:** `ghl-voice-ai`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Voice AI section landing page (voice agent setup, scripts, voice/persona selection, escalation, voicemail handling)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Voice AI handles inbound and outbound calls autonomously — it can
replace or augment human call handling entirely. **Mistakes here are
heard live by customers**: hallucinations, wrong information, awkward
hand-offs all surface in real-time voice. This is the highest blast-
radius AI surface in the platform.

**Verification steps**
1. From the help center root, navigate to the **Voice AI** section.
2. Confirm a distinct section landing page exists for the voice agent
   product specifically.
3. Skim articles for coverage of: agent setup, scripts/prompts, voice
   and persona selection, escalation to human, voicemail handling,
   call routing, supported telephony backends.
4. Note overlap with `ghl-phone-system` (telephony infra) and
   `ghl-ai-employee` (umbrella).
5. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain
  specifically about Voice AI.
- Content is about the voice agent product — agent configuration,
  speech, escalation — not about phone-system infra or generic AI
  features.

**What should not be changed yet**
- Do not merge with `ghl-phone-system` (covered in Batch 02). Voice AI
  is the agent layer on top of the phone system, not the phone system
  itself.
- Do not merge with `ghl-ai-employee` even if Voice AI is documented as
  an AI Employee capability. Voice AI has its own diff signal.
- Do not break out per-feature articles (voicemail, IVR replacement,
  outbound dialing).

**Risk notes**
- Voice AI is one of the highest-churn surfaces in HighLevel — new
  model releases, latency/cost changes, and provider switches all
  change behavior week-to-week. Once enabled, expect noisy diffs;
  a tight `content_selector` will help.
- Pricing changes here affect client cost models directly and can
  invalidate a delivered build.
- If Voice AI has been folded into Agent Studio or rebranded, mark
  **Needs URL refinement** and propose a config update for a future
  reviewed PR.

---

## 2. HighLevel Help Center — Conversation AI

- **Source ID:** `ghl-conversation-ai`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Conversation AI section landing page (text-based AI in the Conversations inbox — SMS, chat, email replies; intents, training, escalation)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Conversation AI handles asynchronous, text-based AI conversation across
all channels that land in the Conversations inbox (SMS, web chat,
email). It is the foundation for most "AI agent" patterns documented
in the consuming `ghl-workflows` repo (qualification, booking
assistance, FAQ, follow-up).

**Verification steps**
1. From the help center root, navigate to the **Conversation AI**
   section.
2. Confirm a distinct section landing page exists.
3. Skim articles for coverage of: agent setup, intents / topics,
   training data, escalation rules, suppression / opt-out, channel
   scoping (SMS vs. chat vs. email).
4. Note the relationship to `ghl-conversations` (inbox surface, Batch
   01) and `ghl-ai-employee` (umbrella, Batch 02).
5. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain.
- Content is about AI handling of inbox conversations, not about the
  inbox UI itself.

**What should not be changed yet**
- Do not merge with `ghl-conversations`. Conversations is the inbox
  *view*; Conversation AI is the autonomous *responder* operating in
  that inbox. Different audiences, different change profiles.
- Do not merge with `ghl-ai-employee` or any other AI sibling.
- Do not break out per-channel articles (chat-AI vs. SMS-AI).

**Risk notes**
- Prompt-engineering / model-behavior changes are usually silent in
  changelogs but loud in production. The help-center section may
  understate the volatility of the underlying agent.
- Suppression and opt-out rules here intersect with compliance
  (`ghl-a2p-registration`, `ghl-email-deliverability`); a change to
  Conversation AI suppression behavior can have downstream compliance
  consequences. Flag any change to suppression / opt-out in particular.

---

## 3. HighLevel Help Center — Workflow AI

- **Source ID:** `ghl-workflow-ai`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Workflow AI section landing page (AI steps used inside workflows — classify, summarize, decide, generate; their inputs, outputs, cost/usage)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Workflow AI covers the AI building-blocks available **inside** the
workflow builder — classification, summarization, decision, generation
steps. Every workflow that uses an AI step depends on these contracts:
input shape, output shape, cost per call, latency, model behavior. A
change here ripples across every workflow with an AI step.

**Verification steps**
1. From the help center root, navigate to the **Workflow AI** (or
   "AI Workflow Steps" / "AI Actions") section.
2. Confirm a distinct section landing page exists, or confirm whether
   AI step documentation lives under `ghl-workflow-actions` instead.
3. Skim articles for coverage of: available AI step types, inputs and
   outputs per step, model selection, cost / usage, error handling.
4. Record the verified URL or flag for refinement / consolidation.

**What counts as verified**
- Distinct section landing page (or clear sub-section) on an official
  HighLevel domain about AI capabilities **inside** workflows
  specifically.
- Content covers per-step contracts (inputs/outputs), not general AI
  product overviews.

**What should not be changed yet**
- Do not merge with `ghl-workflow-actions` (Batch 01) even if AI steps
  are documented there. Workflow AI has a distinct diff audience
  (AI-aware workflow designers) and a different change profile.
- Do not merge with `ghl-ai-employee` or other AI siblings.
- Do not break out per-step articles (Classify, Summarize, Generate as
  individual entries).

**Risk notes**
- If "Workflow AI" doesn't exist as its own section and AI steps are
  intermixed with regular workflow actions, mark **Needs URL
  refinement** and propose either: (a) point this entry at the AI-step
  sub-section if there is one, or (b) collapse into `ghl-workflow-actions`
  in a future config update.
- AI step contracts (inputs/outputs) are the most fragile dependency
  point in any workflow with an AI step. A change to an existing step's
  output schema can break downstream branches silently. Treat any diff
  touching step I/O as a potential breaking change.

---

## 4. HighLevel Help Center — AI Studio

- **Source ID:** `ghl-ai-studio`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** AI Studio section landing page (configuration surface for AI agents — prompts, personas, tools, model selection)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
AI Studio appears to be the configuration / admin surface where AI
agent prompts, personas, tools, and model selection are defined. If so,
it is the operating manual for everything `ghl-conversation-ai`,
`ghl-voice-ai`, and `ghl-ai-employee` consume at runtime. Changes here
affect how every AI agent gets built.

**Verification steps**
1. From the help center root, navigate to the **AI Studio** section.
2. Confirm a distinct section landing page exists.
3. Skim articles for coverage of: prompt configuration, persona /
   voice setup, tool definition, model selection, testing/preview,
   versioning.
4. Clearly distinguish from `ghl-agent-studio` (the next entry).
5. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain
  specifically about AI Studio.
- Content is about Studio as a configuration UI, not about a specific
  AI product (Voice, Conversation, etc.).

**What should not be changed yet**
- Do not merge with `ghl-agent-studio` even though the names are
  confusingly similar. Verification is exactly the work of confirming
  whether they are distinct products or the same product under two
  names.
- Do not merge with `ghl-ai-employee`.
- Do not break out per-capability articles.

**Risk notes**
- "AI Studio" vs. "Agent Studio" is the most likely overlap or rename
  collision in the entire watch list. Verification may reveal these
  are the same product, one is a sub-area of the other, or one has
  been deprecated. Whatever you find, record it in Notes — do **not**
  silently merge entries in this batch.
- HighLevel's Studio products are evolving quickly; if AI Studio has
  been absorbed into Agent Studio (or vice versa), mark **Needs URL
  refinement** and propose a config consolidation in a future reviewed
  PR.

---

## 5. HighLevel Help Center — Agent Studio

- **Source ID:** `ghl-agent-studio`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Agent Studio section landing page (agent definition surface — capabilities, tools, scope, deployment targets)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Agent Studio appears to be the surface where complete AI agents are
defined and deployed to product surfaces (voice, chat, workflow). If
AI Studio is the prompt/persona layer, Agent Studio is the
agent-composition layer above it. Together they form the build pipeline
for every AI capability shipped to clients.

**Verification steps**
1. From the help center root, navigate to the **Agent Studio** section.
2. Confirm a distinct section landing page exists.
3. Skim articles for coverage of: agent definition, capability /
   tool wiring, scope, deployment to Voice / Conversation / Workflow
   surfaces, lifecycle (draft, publish, version).
4. Compare against AI Studio findings — is Agent Studio a superset,
   subset, peer, or replacement?
5. Record the verified URL and the relationship to AI Studio in Notes.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain
  specifically about Agent Studio.
- Content is about defining and deploying agents, not just configuring
  prompts.

**What should not be changed yet**
- Do not merge with `ghl-ai-studio` — see the AI Studio risk notes.
- Do not merge with `ghl-ai-employee`.
- Do not break out per-deployment-target articles (deploying to voice,
  deploying to chat, etc.).

**Risk notes**
- Same AI-product churn risk as AI Studio. If verification reveals AI
  Studio and Agent Studio are the same product, propose collapsing in
  a future reviewed PR — but record both URLs in this tracker first.
- If only one Studio actually exists today, mark the other as
  **Deferred** and note the rebrand history (if known).
- HighLevel has shifted naming for these surfaces multiple times; do
  not assume the current name is the final name when planning fetcher
  work downstream.

---

## 6. HighLevel MCP Server

- **Source ID:** `ghl-mcp-server`
- **Current URL (from config):** `https://highlevel.stoplight.io/`
- **Target section to verify:** MCP Server section on Stoplight or the developer portal (Model Context Protocol implementation — endpoints, auth, resource exposure)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
The MCP Server lets external AI clients (Claude, ChatGPT, custom
agents) access HighLevel resources through the Model Context Protocol.
For external integrations and custom agent builds, this is the
authoritative API surface. Changes to MCP resource exposure, auth, or
schemas directly affect every external agent connected to a HighLevel
sub-account.

**Verification steps**
1. Open `https://highlevel.stoplight.io/`.
2. Look in the Stoplight navigation for an **MCP Server**, **MCP**, or
   **Model Context Protocol** section.
3. If found: confirm it covers the MCP implementation (endpoints,
   auth flow, exposed resources, tool / prompt / resource primitives).
4. If not found in Stoplight: check whether MCP docs live elsewhere
   (developer portal, blog post, GitHub readme). Record what you find.
5. Record the verified URL or flag for deferral.

**What counts as verified**
- Distinct MCP-specific section on an official HighLevel domain
  (`stoplight.io`, `gohighlevel.com`, etc.).
- Content covers the MCP implementation, not generic API docs and
  not "what is MCP" educational material from third parties.

**What should not be changed yet**
- Do not change `source_type` from `developer_portal` even if MCP docs
  end up on Stoplight (which is api_docs in this schema). MCP is a
  developer surface; the `source_type` reflects audience, not domain.
- Do not merge with `ghl-api-docs-root`.
- Do not break out per-resource articles (Contacts MCP, Conversations
  MCP).

**Risk notes**
- MCP as a standard is recent (late 2024 / early 2025). HighLevel's
  implementation may not have public docs yet — the section may not
  exist. If so, mark **Deferred** and revisit when documentation
  ships. Do **not** invent a URL.
- The MCP spec itself is also evolving; HighLevel's docs may lag or
  lead the spec. Once enabled, expect higher-than-usual diff frequency
  in the first six months of any published MCP docs.
- This is the highest-impact source for external AI integrations. If
  you build custom agents against HighLevel, treat any diff here as a
  top-priority alert.

---

## 7. HighLevel Help Center — Knowledge Bases

- **Source ID:** `ghl-knowledge-bases`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Knowledge Bases section landing page (KB creation, ingestion, supported file types, chunking, retrieval, integration with AI agents)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Knowledge Bases are how AI agents get grounded in client-specific
content (product info, policies, FAQ). **Quality of the KB =
quality of the AI answers.** Changes to ingestion limits, supported
file types, chunking strategy, or retrieval semantics silently affect
every grounded AI agent's answer quality — clients won't see "KB
behavior changed", they'll see "the AI started giving worse answers".

**Verification steps**
1. From the help center root, navigate to the **Knowledge Bases** (or
   "Knowledge Base" / "AI Knowledge") section.
2. Confirm a distinct section landing page exists.
3. Skim articles for coverage of: KB creation, file upload / URL
   ingestion, supported source types, size / chunking limits,
   retrieval configuration, integration with Voice AI / Conversation
   AI / Workflow AI / AI Employee.
4. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain.
- Content covers KB lifecycle (creation, ingestion, retrieval), not
  generic "what is RAG" educational content.

**What should not be changed yet**
- Do not merge with `ghl-ai-employee` or any specific AI product
  entry. KBs are a shared resource consumed by multiple AI surfaces;
  the separate entry is intentional.
- Do not break out per-source-type articles (PDF ingestion, URL
  ingestion as individual entries).

**Risk notes**
- Ingestion limits and supported file types change quietly. A client
  whose KB suddenly stops accepting a previously-supported source type
  will have a degraded AI experience with no obvious cause until you
  trace it back to a KB change.
- Retrieval semantics (top-k, similarity threshold, chunk size) drive
  AI answer quality more than the prompt does in most cases. Treat
  changes to retrieval config as high-priority diffs.
- If KBs are tightly coupled to one product (e.g. only Conversation
  AI), the section may live as a sub-section under that product rather
  than as a top-level section. If so, mark **Needs URL refinement**.

---

## Closing checklist for the verifier

Before declaring this batch complete:

- [ ] Every source above has an owner (replace `Unassigned`).
- [ ] Every source above has a status set on the tracker (`Verified`,
      `Needs URL refinement`, or `Deferred`).
- [ ] Findings (verified URL, candidate alternatives, structural notes,
      AI Studio / Agent Studio relationship) are recorded in
      `docs/source-verification-tracker.md` — not in
      `config/watched-pages.json`.
- [ ] `config/watched-pages.json` has been **left unchanged** by this
      batch.
- [ ] No source has been `enabled: true`.
- [ ] No script and no GitHub Action has been touched.

## Phase 1 verification planning — complete

This batch completes Phase 1 source verification **planning** (not
execution). With batches 01, 02, and 03 in place, all 27 Phase 1
sources have a written verification plan:

| Batch | Sources | Scope |
|---|---|---|
| 01 | 10 | API root, Help Center root, Platform Updates, Workflows family (5), Calendars, Conversations |
| 02 | 10 | Phone, Messaging, A2P, Email family (3), Forms, Surveys, Chat Widget, AI Employee |
| 03 | 7 | AI siblings (Voice / Conversation / Workflow), Studios (AI / Agent), MCP Server, Knowledge Bases |

The execution of these plans — human-in-browser verification, owner
assignment, status updates in the tracker — is the next phase. Phase 2
batches (the 25 expansion sources) come after Phase 1 verification has
actually been performed, not just planned.

No live fetching is enabled at the end of this batch. No source is
enabled. The watcher remains a configuration-and-planning artifact.
