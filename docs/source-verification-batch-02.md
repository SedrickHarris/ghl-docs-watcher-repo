# Source Verification — Batch 02

## Batch 02 purpose

This batch verifies the communication, compliance, email, form, survey,
chat, and AI Employee sources that directly affect lead capture,
messaging, client communication, and automation safety.

## Scope

Ten Phase 1 sources, in this order:

| # | Source ID | Label |
|---|---|---|
| 1 | `ghl-phone-system` | HighLevel Help Center — Phone System |
| 2 | `ghl-messaging` | HighLevel Help Center — Messaging |
| 3 | `ghl-a2p-registration` | HighLevel Help Center — A2P 10DLC Registration |
| 4 | `ghl-email` | HighLevel Help Center — Email |
| 5 | `ghl-email-deliverability` | HighLevel Help Center — Email Deliverability |
| 6 | `ghl-lc-email` | HighLevel Help Center — LC Email |
| 7 | `ghl-forms` | HighLevel Help Center — Forms |
| 8 | `ghl-surveys` | HighLevel Help Center — Surveys |
| 9 | `ghl-chat-widget` | HighLevel Help Center — Chat Widget |
| 10 | `ghl-ai-employee` | HighLevel Help Center — AI Employee |

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
- **Heavy overlap is expected.** This batch's surfaces (Phone /
  Messaging / Conversations / Chat Widget; Email / Email Deliverability /
  LC Email; Forms / Surveys) sit on shared infrastructure. Overlap in
  help-center content is not a defect — keeping separate watch entries
  gives finer-grained diff routing.

---

## 1. HighLevel Help Center — Phone System

- **Source ID:** `ghl-phone-system`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Phone System section landing page (number management, IVR, voicemail, call routing)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
This is the voice infrastructure surface — number provisioning, IVR,
voicemail, call recording, routing. Every voice workflow (missed-call
text-back, voicemail-drop, voice AI handoff) depends on it. Changes to
voice provider behavior or pricing cascade into client engagements
quickly.

**Verification steps**
1. From the help center root, navigate to the **Phone System** (or "Phone
   Numbers" / "Calling") section.
2. Confirm a distinct section landing page exists.
3. Skim articles for coverage of: number management, IVR, voicemail,
   call recording, call forwarding/routing.
4. Note whether telephony-provider-specific docs (LC Phone vs. Twilio)
   are mixed in or live elsewhere.
5. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain covering
  the voice surface.
- Articles relate to phone/call setup and operation, not to SMS sending
  or AI agents.

**What should not be changed yet**
- Do not merge with `ghl-messaging` even though both involve "phone".
  Phone here means voice; Messaging is SMS/MMS.
- Do not merge with `ghl-voice-ai` (covered in Batch 03) — voice AI is a
  layer on top of the phone system, documented separately.
- Do not break out per-feature articles (IVR, voicemail, recording).

**Risk notes**
- HighLevel's phone backend has shifted (LC Phone vs. Twilio integration);
  the help-center section may be reorganized to reflect the current
  primary backend. If LC Phone has its own dedicated section, propose
  splitting in a future config update.
- A2P / 10DLC compliance content sometimes lives under Phone System
  instead of Messaging. If you find it here, note the overlap.
- Throughput and pricing change frequently — once enabled, expect
  noticeable but legitimate diffs around carrier rate updates.

---

## 2. HighLevel Help Center — Messaging

- **Source ID:** `ghl-messaging`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Messaging section landing page (SMS / MMS configuration, sending, replies, opt-outs)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
SMS is the highest-volume outbound channel in most GHL workflows
(missed-call text-back, reminders, nurture, review requests). Changes
to send behavior, opt-out handling, throughput, or rate limits affect
every messaging-driven workflow.

**Verification steps**
1. From the help center root, navigate to the **Messaging** (or "SMS /
   MMS" / "Text Messaging") section.
2. Confirm a distinct section landing page exists.
3. Skim articles for coverage of: SMS sending, MMS, templates, replies,
   opt-out handling, STOP/HELP keywords.
4. Confirm it is distinct from A2P Registration (compliance), Phone
   System (voice), and Conversations (inbox view).
5. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain covering
  SMS/MMS as a sending channel.
- Articles cover sending mechanics, not compliance registration or
  inbox-display behavior.

**What should not be changed yet**
- Do not collapse into `ghl-a2p-registration` even though both involve
  SMS — compliance churns separately and on a different cadence.
- Do not collapse into `ghl-conversations` even though messages render
  in the inbox. Conversations is the *view*; Messaging is the *channel*.
- Do not break out per-template-type articles.

**Risk notes**
- "Messaging" is sometimes used as an umbrella for all channels (SMS,
  email, chat) in HighLevel marketing materials. The help-center section
  is usually narrower (SMS/MMS only) — confirm scope at verification.
- The boundary between Messaging and Conversations is the most common
  source of overlap noise in this batch.

---

## 3. HighLevel Help Center — A2P 10DLC Registration

- **Source ID:** `ghl-a2p-registration`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** A2P 10DLC Registration section landing page (brand registration, campaign approval, throughput tiers, compliance)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
This is a **legal/compliance gate** for US SMS sending. Non-compliance
means messages are blocked at the carrier — silent failure with no
delivery. From a project-shipping standpoint, this is one of the highest-
risk sections in the entire watch list: a rule change here can ground
an entire client's outbound SMS.

**Verification steps**
1. From the help center root, navigate to the **A2P 10DLC** (or
   "Registration" / "SMS Compliance" / "TCR") section.
2. Confirm a distinct section landing page exists.
3. Skim articles for coverage of: brand registration, campaign
   submission, vetting, throughput tiers (T1/T2/T3), rejection handling.
4. Note whether content also covers Toll-Free verification (separate but
   adjacent compliance regime).
5. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain.
- Content covers 10DLC brand + campaign registration mechanics, not just
  generic "what is A2P" marketing copy.

**What should not be changed yet**
- Do not collapse into `ghl-messaging` even though it sits adjacent.
  Compliance has its own cadence and risk profile.
- Do not expand to Toll-Free verification as its own entry yet (defer to
  a Phase 2 expansion if it becomes load-bearing).
- Do not break out per-tier or per-vertical articles.

**Risk notes**
- A2P rules are set externally (TCR, carrier policy, CTIA guidelines)
  and change **frequently**. Expect this section to churn. Once enabled,
  a tight `content_selector` will help reduce noise.
- A regulation-driven change is the highest-priority alert profile in
  the entire watch list — anything that changes registration
  requirements, throughput limits, or vetting criteria should be flagged
  to clients within 24h.
- If the section is sparse (just a "contact support" page), mark
  **Deferred** — HighLevel may handle A2P registration as a
  human-mediated process without rich self-serve docs.

---

## 4. HighLevel Help Center — Email

- **Source ID:** `ghl-email`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Email section landing page (composition, templates, sending, the broader email surface)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Email is the second-highest volume channel after SMS. Changes to
composition, template behavior, or sending mechanics affect every
email-bearing workflow (welcome, nurture, reminders, receipts, review
requests).

**Verification steps**
1. From the help center root, navigate to the **Email** section.
2. Confirm a distinct section landing page exists.
3. Skim articles for coverage of: email composition, templates,
   sending, scheduling, segmentation.
4. Clearly distinguish from Email Deliverability (auth/warmup) and LC
   Email (managed sending infrastructure).
5. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain.
- Content covers email composition and sending, not deliverability auth
  or LC-Email-specific infrastructure.

**What should not be changed yet**
- Do not collapse `ghl-email-deliverability` or `ghl-lc-email` into this
  entry. Separate watch targets exist precisely because each has its own
  diff signal and audience.
- Do not break out Email Marketing campaigns vs. transactional email as
  separate entries unless the help center clearly distinguishes them.

**Risk notes**
- HighLevel has multiple email surfaces (Email, Email Marketing, LC
  Email, transactional). Section boundaries in the help center may not
  be crisp. If "Email" is just a parent that aggregates the others,
  mark **Needs URL refinement** and propose collapsing into a more
  specific entry in a future config update.
- Email template engines change occasionally (block-based vs. HTML);
  template-related diffs are usually low-impact but high-volume.

---

## 5. HighLevel Help Center — Email Deliverability

- **Source ID:** `ghl-email-deliverability`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Email Deliverability section landing page (SPF, DKIM, DMARC, domain warmup, sender reputation, Google/Yahoo bulk-sender rules)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Deliverability determines whether emails reach the inbox. Ignored, it's
a silent failure mode — campaigns "send" but never land. This is the
email equivalent of A2P: a compliance/configuration regime where
changes by external parties (Google, Yahoo, Microsoft) directly affect
client outcomes.

**Verification steps**
1. From the help center root, navigate to the **Email Deliverability**
   (or "Domain Setup" / "Sender Authentication") section.
2. Confirm a distinct section landing page exists.
3. Skim articles for coverage of: SPF, DKIM, DMARC, BIMI, domain
   warmup, sender reputation, list hygiene.
4. Note whether the section addresses the 2024+ Google/Yahoo bulk-
   sender requirements explicitly.
5. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain.
- Content covers email authentication and deliverability mechanics,
  not generic "how to send email" material.

**What should not be changed yet**
- Do not merge with `ghl-email` even though both involve email.
  Deliverability is a separate operational concern with a different
  audience (admins and IT, not marketers).
- Do not break out per-record-type articles (SPF, DKIM, DMARC as
  individual entries).

**Risk notes**
- Mailbox-provider policy changes (Google/Yahoo bulk-sender thresholds,
  spam-rate caps, DMARC enforcement) are some of the highest-impact
  external changes in this entire watch list. Treat any change to this
  section as a potential cross-client alert.
- Help-center sections on deliverability can lag behind the actual
  product behavior. If content looks stale, that's worth flagging
  separately — it doesn't mean the URL is wrong.

---

## 6. HighLevel Help Center — LC Email

- **Source ID:** `ghl-lc-email`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** LC Email section landing page (HighLevel-managed email sending infrastructure, pricing tier, sending limits, included vs. add-on capacity)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
LC Email is HighLevel's first-party managed email sending — distinct
from BYO-SMTP / Mailgun integrations. Pricing, included volume, and
behavior differ. Clients on LC Email vs. BYO-SMTP have different
deliverability and cost profiles, and changes here directly affect
billing and capacity planning.

**Verification steps**
1. From the help center root, navigate to **LC Email** (or
   "HighLevel Email" / "Email Service").
2. Confirm a distinct section landing page exists for the managed
   sending product specifically.
3. Skim articles for coverage of: setup, sending limits, pricing tiers,
   included vs. add-on volume, differences from BYO-SMTP.
4. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain
  specifically about LC Email.
- Content is product-specific (not generic email-channel content).

**What should not be changed yet**
- Do not merge with `ghl-email` even though LC Email is the default
  email channel for most sub-accounts.
- Do not merge with `ghl-email-deliverability` even though LC Email
  comes with HighLevel-managed sender reputation.
- Do not track LC Email pricing as its own entry — pricing pages live
  elsewhere and are not in the section-level watch scope.

**Risk notes**
- LC Email is a relatively newer / evolving HighLevel product. Section
  may be sparse, may have been renamed, or may not yet exist as a
  standalone section in the help center.
- If the section is absent or only consists of a single "what is LC
  Email" article, mark **Deferred** and revisit once HighLevel publishes
  dedicated documentation.
- Sending limit / pricing changes can break client cost models; treat
  any diff here with elevated priority once the fetcher is live.

---

## 7. HighLevel Help Center — Forms

- **Source ID:** `ghl-forms`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Forms section landing page (form builder, embed, submission handling, conditional logic)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Forms are the primary lead-capture surface for most GHL clients. Every
lead-source workflow starts with form submission. Changes to form
behavior, embed mechanics, or submission webhooks affect every funnel
the client has live.

**Verification steps**
1. From the help center root, navigate to the **Forms** section.
2. Confirm a distinct section landing page exists.
3. Skim articles for coverage of: form builder, field types, embed,
   submission handling, conditional logic, custom field mapping.
4. Note whether forms and surveys share a parent section in the help
   center.
5. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain.
- Content covers form building and submission mechanics.

**What should not be changed yet**
- Do not merge with `ghl-surveys` even though they share infrastructure.
  Forms and surveys have different use cases and different downstream
  workflow patterns.
- Do not break out per-field-type or per-embed-method articles.

**Risk notes**
- HighLevel forms and surveys share the same underlying builder
  infrastructure; help-center sections may blur the line. If the
  section landing page is genuinely shared with surveys, mark **Needs
  URL refinement** and propose collapsing both entries in a future
  config update.
- Form embed mechanics (iframe, JS snippet, redirect URLs) change
  occasionally; these changes are silent for the agency but loud for
  the client whose site embed suddenly breaks.

---

## 8. HighLevel Help Center — Surveys

- **Source ID:** `ghl-surveys`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Surveys section landing page (survey builder, branching/conditional logic, scoring, post-submission routing)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
Surveys collect qualification data and post-interaction feedback. Their
output drives branching in nurture and review-request workflows
(e.g. the 4-or-5-star branch in the review-request pattern is usually a
survey response). Changes to survey scoring or routing affect every
sentiment-aware workflow.

**Verification steps**
1. From the help center root, navigate to the **Surveys** section.
2. Confirm a distinct section landing page exists.
3. Skim articles for coverage of: survey builder, branching logic,
   scoring, post-submission routing, integration with workflows.
4. Note whether the section is distinct from Forms or shared.
5. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain.
- Content covers survey-specific mechanics (branching, scoring), not
  just generic form-building.

**What should not be changed yet**
- Do not merge with `ghl-forms` unless verification shows the help
  center treats them as one section with no separable URL.
- Do not break out individual question-type articles.

**Risk notes**
- Same shared-infrastructure overlap as Forms. If the section
  effectively redirects to or is identical to Forms, mark **Needs URL
  refinement**.
- Survey branching is one of the most-used features in
  qualification-driven workflows; changes here are higher-impact than
  the section's apparent visibility suggests.

---

## 9. HighLevel Help Center — Chat Widget

- **Source ID:** `ghl-chat-widget`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** Chat Widget section landing page (widget installation, behavior, routing, AI handoff)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
The chat widget is the real-time on-site entry point — visitor lands on
the client's website, hits chat, conversation lands in the Conversations
inbox (often through Conversation AI first). It's an increasingly common
trigger source for AI-driven workflows.

**Verification steps**
1. From the help center root, navigate to the **Chat Widget** (or
   "Web Chat" / "Live Chat") section.
2. Confirm a distinct section landing page exists.
3. Skim articles for coverage of: install/embed, widget appearance,
   routing rules, business-hours behavior, AI handoff.
4. Note whether Chat Widget content lives under Conversations, Sites,
   or its own top-level section.
5. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain.
- Content covers widget-specific mechanics (embed, routing,
  appearance), not just generic Conversations behavior.

**What should not be changed yet**
- Do not merge with `ghl-conversations` even though chat messages flow
  into the same inbox. The widget itself is a separate surface with
  its own configuration concerns (embed, appearance, on-page behavior).
- Do not merge with `ghl-messaging` — chat is web-based, not
  SMS-based.
- Do not couple to `ghl-conversation-ai` (covered in Batch 03) — the
  widget can run with or without an AI agent attached.

**Risk notes**
- The Chat Widget is often grouped under "Conversations" or "Websites"
  in the help center depending on the current information architecture.
  Section may have moved without a redirect.
- Widget embed code changes are silently breaking for clients whose
  sites still have older snippets. Once enabled, this is a high-priority
  diff target.

---

## 10. HighLevel Help Center — AI Employee

- **Source ID:** `ghl-ai-employee`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Target section to verify:** AI Employee section landing page (umbrella AI agent product, capabilities, scope, safety/escalation)
- **Owner:** Unassigned
- **Status:** Not started

**Why this source matters**
AI Employee is HighLevel's umbrella branding for its AI agent products.
Behavior changes here affect every AI-driven workflow's safety,
escalation, and tone. Together with `ghl-platform-updates`, this is one
of the highest-signal sources for AI-related breaking changes — and one
of the most likely to be renamed or restructured.

**Verification steps**
1. From the help center root, navigate to the **AI Employee** section.
2. Confirm a distinct section landing page exists for the AI Employee
   product specifically.
3. Skim articles for coverage of: AI Employee capabilities, scope,
   guardrails, escalation rules, billing/usage.
4. Note the relationship to neighboring AI entries — Voice AI,
   Conversation AI, Workflow AI, AI Studio, Agent Studio (all covered
   in Batch 03).
5. Record the verified URL.

**What counts as verified**
- Distinct section landing page on an official HighLevel domain.
- Content is specifically about AI Employee, not generic AI features
  available elsewhere in the product.

**What should not be changed yet**
- Do not merge with any of the AI siblings in Batch 03 (Voice AI,
  Conversation AI, Workflow AI, AI Studio, Agent Studio) — separate
  entries exist because each surface has its own diff signal and
  audience even if they share underlying tech.
- Do not break out per-capability articles (intent classification,
  sentiment, tool use).

**Risk notes**
- HighLevel's AI products are renamed and re-bundled **frequently**
  (the lineage AI Employee → Voice AI → Conversation AI → Agent Studio
  has shifted multiple times). Section may have been renamed, split, or
  consolidated.
- If AI Employee has been deprecated or absorbed into another product
  (e.g. Agent Studio), mark **Needs URL refinement** and propose a
  config update — but do not change the config in this batch.
- Pricing/usage changes for AI products affect client cost models
  directly. Once enabled, this is high-priority diff territory.

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
- [ ] Batch 03 is queued for the remaining 7 Phase 1 sources: Voice AI,
      Conversation AI, Workflow AI, AI Studio, Agent Studio, MCP Server,
      Knowledge Bases.
