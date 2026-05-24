# Manual Verification — Run 02

> Companion docs: this is the execution worksheet for the ten
> communication, compliance, email, form, survey, chat, and AI
> Employee sources in
> [`source-verification-batch-02.md`](source-verification-batch-02.md).
> The process this worksheet follows is defined in
> [`phase-1-verification-execution-guide.md`](phase-1-verification-execution-guide.md).
> The running status of record is in
> [`source-verification-tracker.md`](source-verification-tracker.md).
> Prior worksheets:
> [`manual-verification-run-01.md`](manual-verification-run-01.md),
> [`manual-verification-run-03.md`](manual-verification-run-03.md).

## Manual verification instructions for Sedrick

1. **Open each current URL manually in the browser.** Do not run any
   script, do not use `curl` / `wget`, do not call any fetcher.
2. **Use the candidate title as the search target inside the official
   HighLevel support portal.** The current URLs are placeholders; the
   candidate title is the phrase to search for inside
   `help.gohighlevel.com` or the relevant adjacent surface.
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

## Batch 2 verification priority

Recommend verifying in this order:

1. **Phone System** (`ghl-phone-system`)
2. **A2P Registration** (`ghl-a2p-registration`)
3. **Messaging** (`ghl-messaging`)
4. **Email** (`ghl-email`)
5. **Email Deliverability** (`ghl-email-deliverability`)
6. **LC Email** (`ghl-lc-email`)
7. **Forms** (`ghl-forms`)
8. **Surveys** (`ghl-surveys`)
9. **Chat Widget** (`ghl-chat-widget`)
10. **AI Employee** (`ghl-ai-employee`)

**Why this order:** Phone, A2P, Messaging, and Email should be
verified first because they directly affect lead communication,
compliance, reminders, missed-call text-back, and automation
deliverability — the surfaces with the highest blast radius for client
engagements already in production. Email Deliverability and LC Email
follow because they govern whether email actually reaches the inbox.
Forms and Surveys come next as lead-capture surfaces, then Chat
Widget as the on-site real-time entry point. AI Employee is verified
last because it is the most likely to have been renamed, re-bundled,
or folded into Agent Studio (the AI-family naming and structure has
shifted multiple times) and the rest of the batch is more stable.

---

## Scope of this run

Ten sources from Batch 02, listed in their config order:

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

(Verification *execution* order is the priority list above, not this
config order.)

---

## 1. HighLevel Help Center — Phone System

- **Source label:** HighLevel Help Center — Phone System
- **Source ID:** `ghl-phone-system`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** `https://help.gohighlevel.com/support/solutions`
- **Candidate status:** Needs URL refinement
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the support portal root and search for "Phone System". Also
   search for the related terms: "Phone Numbers", "Calling", "LC
   Phone", "IVR", "voicemail", "call routing".
2. From the results, navigate into the distinct Phone System folder
   or landing page (prefer a folder index over a single article when
   both exist).
3. Skim articles for coverage of: number provisioning / porting,
   IVR, voicemail, call recording, call forwarding / routing,
   business-hours handling.
4. Note whether telephony-provider-specific docs (LC Phone vs.
   Twilio) are mixed in or live in a sibling folder.
5. Note any A2P / 10DLC content that lives under Phone System rather
   than under Messaging (overlap is expected).

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

The Phone System folder or section landing — distinct from Messaging
(SMS surface), Conversations (inbox view), and Voice AI (Batch 03,
the agent layer above the phone system).

### What counts as Verified

- Verified URL resolves on `help.gohighlevel.com`.
- The page is specifically about the voice / telephony surface
  (number management, IVR, voicemail, call routing), not about SMS
  or AI agents.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- LC Phone has its own dedicated folder and is the more authoritative
  primary surface than a generic "Phone System" page — record both,
  flag for follow-up.
- Phone System exists only as scattered articles under Settings or
  Conversations with no dedicated folder — record the strongest
  candidate and flag the structural gap.
- A2P / 10DLC content lives under Phone System rather than under a
  dedicated A2P folder — note the overlap.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge this entry with `ghl-messaging`, `ghl-voice-ai`, or
  `ghl-conversations` during this worksheet — overlap is expected;
  separate entries give better diff routing.

---

## 2. HighLevel Help Center — Messaging

- **Source label:** HighLevel Help Center — Messaging
- **Source ID:** `ghl-messaging`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** A List of Workflow Actions
- **Candidate status:** Needs exact URL
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the support portal root and search for "A List of Workflow
   Actions" — find the canonical actions reference article and
   confirm it covers SMS / MMS send actions.
2. Also search the portal for "Messaging", "SMS", "MMS", "Text
   Messaging" and navigate into the Messaging folder or landing page
   if one exists.
3. Decide: is the canonical surface (a) a Messaging-specific folder /
   landing, or (b) the workflow actions article (because SMS sending
   is documented as a workflow action rather than as a standalone
   channel article)?
4. Skim for coverage of: SMS / MMS sending, templates, replies,
   STOP / HELP / opt-out handling, throughput / rate limits.
5. Record the strongest single URL as **Verified URL**, with the
   alternate URL noted in the verification record.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

The Messaging folder or section landing — OR the "A List of Workflow
Actions" article if SMS sending is only documented as a workflow
action. Distinct from A2P Registration (compliance), Phone System
(voice), and Conversations (inbox).

### What counts as Verified

- Verified URL resolves on `help.gohighlevel.com`.
- The page covers SMS / MMS as a sending channel (sending mechanics,
  templates, opt-out), not compliance registration or inbox display.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- "Messaging" exists only as an umbrella term used in marketing copy
  and has no dedicated help-center surface — record the workflow
  actions article and flag the structural gap.
- Messaging content is split between a workflow-actions reference and
  a separate inbox article with no clear primary — record both and
  flag for follow-up.
- The candidate workflow-actions article catalogs many non-messaging
  actions inline — record it but note that the Messaging-specific
  signal will be noisy until a tighter section is found.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not collapse into `ghl-a2p-registration` (compliance churns on a
  different cadence) or `ghl-conversations` (inbox view, not channel).

---

## 3. HighLevel Help Center — A2P 10DLC Registration

- **Source label:** HighLevel Help Center — A2P 10DLC Registration
- **Source ID:** `ghl-a2p-registration`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** `https://help.gohighlevel.com/support/solutions`
- **Candidate status:** Needs URL refinement
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the support portal root and search for "A2P". Also search for
   "10DLC", "TCR", "SMS Compliance", "Registration", "campaign
   approval".
2. Navigate into the distinct A2P 10DLC folder or article (brand
   registration, campaign submission, throughput tiers, vetting).
3. Skim articles for coverage of: brand registration, campaign
   submission, throughput tiers (T1/T2/T3), rejection handling,
   timeline expectations.
4. Note whether Toll-Free verification is documented alongside or as
   a separate regime (record but do not substitute).
5. Confirm the section is non-trivial (not just a "contact support"
   stub) — if it is a stub, mark **Deferred** in the verification
   note.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

The A2P 10DLC folder or registration article — distinct from generic
Messaging content, distinct from any Toll-Free verification surface.

### What counts as Verified

- Verified URL resolves on `help.gohighlevel.com`.
- The page covers 10DLC brand and campaign registration mechanics
  (registration steps, vetting, throughput, rejection handling), not
  generic "what is A2P" marketing copy.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- A2P content lives under the Phone System folder rather than as a
  dedicated A2P folder — record the strongest candidate, flag the
  overlap.
- Multiple A2P articles exist (overview vs. registration walkthrough
  vs. troubleshooting) and the canonical landing is ambiguous —
  record the most authoritative one and flag.
- The page exists but is sparse / mostly a "contact support" stub —
  mark **Deferred** in the verification note rather than promoting
  a thin URL.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not add a Toll-Free verification entry to the config during this
  worksheet, even if a strong Toll-Free article is found.

---

## 4. HighLevel Help Center — Email

- **Source label:** HighLevel Help Center — Email
- **Source ID:** `ghl-email`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** A List of Workflow Actions
- **Candidate status:** Needs exact URL
- **Owner:** Sedrick Harris
- **Status:** Verified
- **Verified URL:** https://help.gohighlevel.com/support/solutions/articles/155000005552-how-to-access-the-all-in-one-dashboard-for-email-marketing
- **Verification record:** Primary is the All-in-One Email Dashboard article (access & reports landing). Supporting URL: `https://help.gohighlevel.com/support/solutions/articles/155000002472-workflow-action-send-email` (Workflow Action - Send Email reference). Both resolve on `help.gohighlevel.com` and are publicly accessible without login.

### Browser verification steps

1. Open the support portal root and search for "A List of Workflow
   Actions" and confirm whether the article covers Send Email actions.
2. Also search for "Email", "Send Email", "workflow email action" and
   identify any dedicated Email folder or landing page.
3. Decide: is the canonical surface a (a) general Email folder, (b)
   the workflow actions article (where Send Email is one of many), or
   (c) a redirect into LC Email or Email Marketing?
4. Skim for coverage of: email composition, templates, sending,
   scheduling, segmentation — content that belongs to the Email
   surface broadly (not to deliverability auth or LC-Email-specific
   infrastructure).
5. Record the strongest single URL as **Verified URL**, with any
   alternates noted in the verification record.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

The Email folder or section landing — OR the "A List of Workflow
Actions" article if Send Email is only documented as a workflow
action. Distinct from Email Deliverability (auth / warmup) and LC
Email (managed sending infrastructure).

### What counts as Verified

- Verified URL resolves on `help.gohighlevel.com`.
- The page covers email composition and sending (not deliverability
  auth, not LC-Email-specific infrastructure).
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- "Email" only exists as a parent that aggregates Email Marketing,
  LC Email, and transactional — record the parent URL and flag the
  collapse decision for a future config update.
- Send Email is documented only inside the workflow actions article
  with no standalone Email surface — record the actions article and
  flag the gap.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not collapse `ghl-email-deliverability` or `ghl-lc-email` into
  this entry during this worksheet, even if the help-center structure
  suggests they could merge.

---

## 5. HighLevel Help Center — Email Deliverability

- **Source label:** HighLevel Help Center — Email Deliverability
- **Source ID:** `ghl-email-deliverability`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** `https://help.gohighlevel.com/support/solutions`
- **Candidate status:** Needs URL refinement
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the support portal root and search for "Email Deliverability".
   Also search for "SPF", "DKIM", "DMARC", "domain setup", "sender
   authentication".
2. Navigate into the distinct Email Deliverability folder or landing
   page.
3. Skim articles for coverage of: SPF, DKIM, DMARC, BIMI, domain
   warmup, sender reputation, list hygiene, bounce / complaint
   handling.
4. **Specifically confirm:** does the section address the 2024+
   Google / Yahoo / Microsoft bulk-sender requirements (one-click
   unsubscribe header, spam-rate caps, DMARC enforcement)?
5. Record the strongest single URL as **Verified URL**.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

The Email Deliverability folder or section landing — distinct from
generic Email content, distinct from LC-Email-specific infrastructure.

### What counts as Verified

- Verified URL resolves on `help.gohighlevel.com`.
- The page covers email authentication and deliverability mechanics
  (SPF / DKIM / DMARC, warmup, reputation), not generic "how to send
  email" material.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- Deliverability content lives only under LC Email rather than as a
  dedicated section — record the LC Email URL and flag the overlap.
- The section exists but does not address 2024+ Google / Yahoo bulk-
  sender rules — record the URL and flag the staleness in the
  verification note.
- Authentication articles (SPF / DKIM / DMARC) are split into separate
  unconnected pages with no overview — record the most authoritative
  single article and flag.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge with `ghl-email` or `ghl-lc-email` during this
  worksheet, even if findings suggest consolidation.

---

## 6. HighLevel Help Center — LC Email

- **Source label:** HighLevel Help Center — LC Email
- **Source ID:** `ghl-lc-email`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** `https://help.gohighlevel.com/support/solutions`
- **Candidate status:** Needs URL refinement
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the support portal root and search for "LC Email". Also
   search for "HighLevel Email", "Email Service", "sending domain",
   "dedicated domain".
2. Navigate into the distinct LC Email folder or landing page if one
   exists.
3. Skim articles for coverage of: setup, sending limits, pricing
   tiers, included vs. add-on volume, differences from BYO-SMTP /
   Mailgun, dedicated domain configuration.
4. Decide: a distinct LC Email surface exists → **Verified URL** with
   that URL; LC Email is only mentioned inside a broader Email
   article → **Needs URL refinement** with the broader URL recorded.
5. If only a single "what is LC Email" article exists and there is
   no surrounding content, mark **Deferred** in the verification
   note.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

The LC Email folder or section landing — content specifically about
HighLevel-managed email sending infrastructure, distinct from generic
Email content and distinct from deliverability auth.

### What counts as Verified

- Verified URL resolves on `help.gohighlevel.com`.
- The page is product-specific to LC Email (setup, limits, pricing
  tiers, dedicated domain).
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- LC Email is documented only inside a broader Email article with no
  dedicated landing — record the broader article URL and flag.
- LC Email content is scattered (setup in one article, pricing in
  another, limits in a third) with no overview — record the most
  authoritative single article and flag.
- LC Email has been renamed or rebundled (e.g. into a generic "Email
  Service" or merged with Email Marketing) — record the new landing
  and flag for follow-up.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not collapse this entry into `ghl-email` or
  `ghl-email-deliverability` during this worksheet.

---

## 7. HighLevel Help Center — Forms

- **Source label:** HighLevel Help Center — Forms
- **Source ID:** `ghl-forms`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** Workflow Trigger - Form Submitted
- **Candidate status:** Needs exact URL
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the support portal root and search for "Workflow Trigger -
   Form Submitted" — confirm the exact article exists.
2. Also search for "Forms", "Form Submitted", "form builder",
   "embed" — identify the Forms folder or section landing page.
3. Decide: is the canonical surface (a) a dedicated Forms folder
   landing, or (b) the Form Submitted trigger article (because forms
   are documented primarily as a trigger source)? Prefer the folder
   landing when one exists.
4. Skim for coverage of: form builder, field types, embed (iframe /
   JS snippet), submission handling, conditional logic, custom field
   mapping.
5. Note whether Forms and Surveys share a parent section in the help
   center.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

The Forms folder or section landing — OR the Form Submitted trigger
article if no dedicated Forms folder exists. Distinct from Surveys
even if they share underlying infrastructure.

### What counts as Verified

- Verified URL resolves on `help.gohighlevel.com`.
- The page covers form building and submission mechanics
  specifically.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- Forms shares a section landing with Surveys with no separable URL —
  record the shared URL and flag the merge candidate.
- The Form Submitted trigger article is the only Forms-related
  surface and there is no Forms folder — record the trigger article
  and flag.
- Forms are documented inside Sites / Funnels rather than as their
  own surface — record the new location and flag.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge with `ghl-surveys` during this worksheet, even if the
  help center shares a parent section.

---

## 8. HighLevel Help Center — Surveys

- **Source label:** HighLevel Help Center — Surveys
- **Source ID:** `ghl-surveys`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** A List of Workflow Triggers
- **Candidate status:** Needs exact URL
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the support portal root and search for "A List of Workflow
   Triggers" — confirm whether the article covers Survey Submitted
   triggers.
2. Also search for "Surveys", "Survey Submitted", "survey builder" —
   identify the Surveys folder or section landing page.
3. Decide: is the canonical surface (a) a dedicated Surveys folder,
   (b) the workflow triggers article (where Survey Submitted is one
   trigger), or (c) only a Forms sub-page?
4. Skim for coverage of: survey builder, branching / conditional
   logic, scoring, post-submission routing, integration with
   workflows.
5. Note whether Surveys is genuinely distinct from Forms.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

The Surveys folder or section landing — OR the workflow triggers
article if Survey Submitted is documented only as a trigger. Distinct
from Forms (separate use cases and downstream patterns) even if they
share underlying infrastructure.

### What counts as Verified

- Verified URL resolves on `help.gohighlevel.com`.
- The page covers survey-specific mechanics (branching, scoring,
  routing), not just generic form-building.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- Surveys only render as a sub-page or tab inside the Forms folder
  with no separable URL — record the shared URL and flag the merge
  candidate.
- Survey Submitted is only documented inside the broader triggers
  article — record the triggers article and flag.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge with `ghl-forms` during this worksheet.

---

## 9. HighLevel Help Center — Chat Widget

- **Source label:** HighLevel Help Center — Chat Widget
- **Source ID:** `ghl-chat-widget`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** A List of Workflow Actions
- **Candidate status:** Needs exact URL
- **Owner:** Unassigned
- **Status:** Not started
- **Verified URL:** *(paste here after browser verification — leave blank if status ends up Needs URL refinement or Deferred)*

### Browser verification steps

1. Open the support portal root and search for "A List of Workflow
   Actions" — confirm whether the article covers chat actions / live
   chat routing.
2. Also search for "Chat Widget", "Web Chat", "Live Chat",
   "conversations", "AI handoff" — identify the Chat Widget folder
   or section landing page.
3. Note whether Chat Widget content lives under Conversations, Sites,
   or its own top-level section.
4. Skim for coverage of: install / embed code, widget appearance,
   routing rules, business-hours behavior, AI handoff, mobile vs.
   desktop behavior.
5. Record the strongest single URL as **Verified URL**, with any
   alternates noted in the verification record.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

The Chat Widget folder or section landing — content specifically
about widget install / behavior / routing. Distinct from
Conversations (the inbox view) and Messaging (SMS channel).

### What counts as Verified

- Verified URL resolves on `help.gohighlevel.com`.
- The page covers widget-specific mechanics (embed, routing,
  appearance), not just generic Conversations behavior or generic
  workflow actions.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- Chat Widget content lives under Conversations or Sites with no
  dedicated folder — record the strongest candidate URL and flag the
  structural placement.
- Widget install / embed docs are split from widget routing /
  appearance docs with no overview — record the most authoritative
  single article and flag.
- The widget has been renamed (e.g. to "Web Chat" or rolled into a
  broader "Site Tools" surface) — record the new landing and flag
  for follow-up.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge with `ghl-conversations`, `ghl-messaging`, or
  `ghl-conversation-ai` during this worksheet.

---

## 10. HighLevel Help Center — AI Employee

- **Source label:** HighLevel Help Center — AI Employee
- **Source ID:** `ghl-ai-employee`
- **Current URL (from config):** `https://help.gohighlevel.com/`
- **Candidate URL or title:** AI Tools in HighLevel
- **Candidate status:** Needs exact URL
- **Owner:** Sedrick Harris
- **Status:** Verified
- **Verified URL:** https://help.gohighlevel.com/support/solutions/articles/155000003906-ai-employee-overview
- **Verification record:** Primary is the AI Employee overview article (slug literally `ai-employee-overview`; covers Automate Calls, Chats & Workflows). Supporting URL: `https://help.gohighlevel.com/support/solutions/articles/155000002166-ai-tools-in-highlevel` (AI Tools in HighLevel umbrella article — the original Batch 02 candidate). Both resolve on `help.gohighlevel.com` and are publicly accessible without login.

### Browser verification steps

1. Open the support portal root and search for "AI Tools in
   HighLevel". Also search for "AI Employee", "AI tools", "Agent
   Studio", "Conversation AI".
2. Navigate into the most authoritative AI Employee landing or
   folder. If the surface has been rebranded or absorbed (the
   AI-family naming has shifted multiple times), record the
   *current* canonical landing for the umbrella AI product even if
   it is no longer labeled "AI Employee".
3. Skim for coverage of: AI Employee capabilities, scope, guardrails,
   escalation rules, billing / usage, pricing changes.
4. Note the relationship to the Batch 03 AI siblings — Voice AI,
   Conversation AI, Workflow AI, AI Studio, Agent Studio. These are
   all separate watch entries; do not collapse during this worksheet.
5. Record the strongest single URL as **Verified URL**.

### Domain that should be confirmed

`help.gohighlevel.com` (the official HighLevel support portal).

### Section or article URL to look for

The AI Employee folder or section landing — OR the "AI Tools in
HighLevel" umbrella article if AI Employee no longer has its own
distinct surface. Distinct from each of the specific AI products
(Voice AI, Conversation AI, Workflow AI, AI Studio, Agent Studio)
covered in Batch 03.

### What counts as Verified

- Verified URL resolves on `help.gohighlevel.com`.
- The page is specifically about the umbrella AI Employee product
  (capabilities, scope, guardrails, billing), not about a single
  AI sibling.
- The page is publicly accessible without login.

### What counts as Needs URL refinement

- AI Employee has been renamed to "AI Tools" or absorbed into
  Agent Studio — record the new landing and flag the rebrand in the
  verification note. The watch entry name in config stays
  `ghl-ai-employee` until a separate reviewed config update.
- AI Employee content is split across multiple AI sibling articles
  with no umbrella — record the most authoritative single article
  and flag the structural change.
- Pricing / usage docs for AI Employee live in a separate Pricing
  section rather than under the product landing — record the
  product-landing URL and note the split.

### What should not be changed

- `source_type` stays `help_center`.
- `content_selector` stays `null`.
- `verify_before_enabling` stays `true`.
- `enabled` stays `false`.
- Do not merge with any of the Batch 03 AI siblings (`ghl-voice-ai`,
  `ghl-conversation-ai`, `ghl-workflow-ai`, `ghl-ai-studio`,
  `ghl-agent-studio`) during this worksheet.

---

## After this worksheet is filled in

When all ten Verified URL fields above are populated (or each is
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
