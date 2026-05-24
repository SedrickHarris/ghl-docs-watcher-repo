# Candidate HighLevel Source URL Map

This document captures candidate HighLevel URLs, exact URLs, article
titles, section targets, and source mapping notes before
`config/watched-pages.json` or `docs/source-verification-tracker.md`
are updated.

## 1. Purpose

This file is the central research layer for HighLevel source
verification. It is used to collect likely official URLs and
title-based targets before they are promoted into
`config/watched-pages.json`. A URL should not be marked verified in
the tracker until it is manually opened in a browser and confirmed on
an official HighLevel domain.

The map is structured so a verifier can walk top-to-bottom: confirmed
URLs first (section 3), then per-batch / per-phase candidate tables
(sections 4–8), then the outstanding collection queue (section 9),
then the promotion gate (section 10) that must be cleared before any
candidate is written into the config.

## 2. Source classification rules

Every candidate row in this document uses one of the following
classifications. The classification is a hint about how to use the URL
during verification — it is not the final verified status (that lives
in `docs/source-verification-tracker.md`).

- **Canonical source** — the best primary URL for a watch area. If
  confirmed in a browser, this is the URL that should be promoted to
  the watch entry's `url` field.
- **Supporting source** — a useful secondary URL that supports the
  watch area but may not be the main source. Worth recording, but
  should not displace a stronger canonical URL when one is found.
- **Shared source** — one URL used by multiple watch areas. Promote
  with care: the same URL may end up referenced from several entries.
- **Needs exact URL** — the target title is known, but the exact
  official URL still needs to be copied from the browser. Verifier
  finds it by searching the support portal for the title.
- **Needs URL refinement** — a broad URL is known, but a better
  section-level or article-level URL should be found before the URL
  is promoted to the config.

## 3. Confirmed exact URLs already supplied

These are URLs whose exact path has already been supplied. They still
need browser confirmation before being marked verified in the tracker,
but they do not need further URL hunting.

| Label | URL | Classification | Notes |
|---|---|---|---|
| HighLevel API Documentation | https://marketplace.gohighlevel.com/docs/ | Canonical source | Current API documentation and developer portal source. |
| HighLevel Support Portal Root | https://help.gohighlevel.com/support/solutions | Canonical root source | Broad support portal index. Use only as a root until exact folders or articles are found. |
| HighLevel Changelog | https://ideas.gohighlevel.com/changelog | Canonical source | Primary public changelog for platform updates. |
| GoHighLevel Developers | https://developers.gohighlevel.com | Supporting source | Developer hub and ecosystem entry point. |
| Agent Studio Overview | https://help.gohighlevel.com/support/solutions/articles/155000007393-agent-studio-overview | Canonical or supporting source | Candidate for Agent Studio overview. |
| How to Use AI Agent Studio in HighLevel | https://help.gohighlevel.com/support/solutions/articles/155000006058-how-to-use-the-ai-agent-studio-in-highlevel | Canonical or supporting source | Candidate for AI Studio setup and knowledge base references. |
| Ask AI + Agent Studio Integration | https://help.gohighlevel.com/support/solutions/articles/155000006677-ask-ai-agent-studio-integration | Supporting source | Candidate for Agent Studio, Ask AI, and routing integration. |
| Documents & Contracts Public APIs | https://help.gohighlevel.com/support/solutions/articles/155000006323-documents-contracts-public-apis | Supporting source | Candidate for documents, contracts, API, and automation references. |
| HighLevel API Documentation Support Article | https://help.gohighlevel.com/support/solutions/articles/48001060529-highlevel-api-documentation | Supporting source | Support article pointing users to the current API documentation. |
| New Release Updates Folder | https://help.gohighlevel.com/support/solutions/folders/48000666449 | Supporting source | Candidate support portal source for release updates. |

## 4. Phase 1 Batch 01 mapping

| Watch Area | Candidate URL or Title | URL Type | Recommended Use | Related Source IDs | Status Notes |
|---|---|---|---|---|---|
| HighLevel API Docs | https://marketplace.gohighlevel.com/docs/ | Canonical source | API changes, webhooks, endpoints, auth, and integrations | `ghl-api-docs-root` | Ready for manual verification or already verified if opened in browser. |
| Help Center Root | https://help.gohighlevel.com/support/solutions | Canonical root source | Broad support portal index | `ghl-help-center-root` | Use as root only before narrowing sections. |
| Platform Updates | https://ideas.gohighlevel.com/changelog | Canonical source | Public platform changelog | `ghl-platform-updates` | Ready for manual verification or already verified if opened in browser. |
| Developer Resources | https://developers.gohighlevel.com | Supporting source | Developer hub and platform development resources | `ghl-developer-resources` | Useful secondary developer source. |
| Developer Resources | https://marketplace.gohighlevel.com/docs/ | Canonical source | Current API reference and developer portal | `ghl-developer-resources`, `ghl-api-docs-root` | Shared with API Docs. |
| Workflow Triggers | A List of Workflow Triggers | Needs exact URL | Trigger changes can break automations | `ghl-workflow-triggers`, `ghl-workflows` | Exact article URL needed. |
| Workflow Actions | A List of Workflow Actions | Needs exact URL | Action changes can break automations and delivery flows | `ghl-workflow-actions`, `ghl-workflows` | Exact article URL needed. |
| Workflows | A List of Workflow Triggers / A List of Workflow Actions | Shared source, needs exact URL | Workflow builder behavior | `ghl-workflows` | Exact article URLs needed. |
| Calendars & Appointments | https://help.gohighlevel.com/support/solutions | Needs URL refinement | Calendar and appointment documentation | `ghl-calendars-appointments` | Find exact folder or article. |
| Conversations | https://help.gohighlevel.com/support/solutions/articles/155000006677-ask-ai-agent-studio-integration | Supporting source | Inbox, assistant routing, and conversation automation | `ghl-conversations` | May need stronger canonical Conversations URL. |

## 5. Phase 1 Batch 02 mapping

| Watch Area | Candidate URL or Title | URL Type | Recommended Use | Related Source IDs | Status Notes |
|---|---|---|---|---|---|
| Phone System | https://help.gohighlevel.com/support/solutions | Needs URL refinement | Phone, calling, phone numbers, LC Phone, and messaging docs | `ghl-phone-system` | Find exact Phone System or LC Phone folder. |
| Messaging | A List of Workflow Actions | Needs exact URL | SMS, email, call, WhatsApp, live chat, and delivery actions | `ghl-messaging` | Exact workflow actions URL needed. |
| A2P Registration | https://help.gohighlevel.com/support/solutions | Needs URL refinement | A2P, 10DLC, SMS compliance, messaging approval | `ghl-a2p-registration` | Find exact A2P article or folder. |
| Email | A List of Workflow Actions | Needs exact URL | Email sending behavior and workflow delivery actions | `ghl-email` | Exact workflow actions URL needed. |
| Email Deliverability | https://help.gohighlevel.com/support/solutions | Needs URL refinement | Email deliverability, sending domains, LC Email, authentication | `ghl-email-deliverability` | Find exact deliverability folder or article. |
| LC Email | https://help.gohighlevel.com/support/solutions | Needs URL refinement | LC Email setup and sending domain behavior | `ghl-lc-email` | Find exact LC Email article or folder. |
| Forms | Workflow Trigger - Form Submitted | Needs exact URL | Form submission trigger behavior | `ghl-forms` | Exact trigger article URL needed. |
| Surveys | A List of Workflow Triggers | Needs exact URL | Survey submission trigger behavior | `ghl-surveys` | Exact workflow triggers URL needed. |
| Chat Widget | A List of Workflow Actions | Needs exact URL | Live chat actions and message routing | `ghl-chat-widget` | Exact workflow actions URL needed. |
| AI Employee | AI Tools in HighLevel | Needs exact URL | Main AI feature overview | `ghl-ai-employee` | Exact AI tools article or folder needed. |

## 6. Phase 1 Batch 03 mapping

| Watch Area | Candidate URL or Title | URL Type | Recommended Use | Related Source IDs | Status Notes |
|---|---|---|---|---|---|
| Voice AI | AI Tools in HighLevel | Needs exact URL | Voice AI and AI Employee behavior | `ghl-voice-ai` | Find exact Voice AI or AI Tools source. |
| Conversation AI | AI Tools in HighLevel | Needs exact URL | Conversation AI behavior and feature updates | `ghl-conversation-ai` | Find exact Conversation AI or AI Tools source. |
| Workflow AI | A List of Workflow Actions | Needs exact URL | Workflow AI action behavior | `ghl-workflow-ai` | Exact workflow actions URL needed. |
| AI Studio | https://help.gohighlevel.com/support/solutions/articles/155000006058-how-to-use-the-ai-agent-studio-in-highlevel | Exact URL supplied | AI Studio setup and agent creation | `ghl-ai-studio` | Confirm in browser before tracker verification. |
| AI Studio | https://help.gohighlevel.com/support/solutions/articles/155000007393-agent-studio-overview | Supporting source | Agent Studio overview and beginner guidance | `ghl-ai-studio`, `ghl-agent-studio` | Compare during verification. |
| Agent Studio | https://help.gohighlevel.com/support/solutions/articles/155000007393-agent-studio-overview | Exact URL supplied | Agent Studio overview | `ghl-agent-studio` | Confirm in browser before tracker verification. |
| Agent Studio | https://help.gohighlevel.com/support/solutions/articles/155000006677-ask-ai-agent-studio-integration | Supporting source | Ask AI routing into custom agents | `ghl-agent-studio` | Use as supporting source. |
| MCP Server | https://developers.gohighlevel.com | Needs URL refinement | Developer tooling and integration-related changes | `ghl-mcp-server` | Find exact MCP Server source if available. |
| Knowledge Bases | https://help.gohighlevel.com/support/solutions/articles/155000006058-how-to-use-the-ai-agent-studio-in-highlevel | Supporting source | Knowledge base references inside agent setup | `ghl-knowledge-bases` | Find stronger canonical Knowledge Bases source if available. |

## 7. Phase 2 expansion candidate mappings

| Watch Area | Candidate URL or Title | URL Type | Recommended Use | Related Source IDs | Status Notes |
|---|---|---|---|---|---|
| Getting Started w/ HighLevel | Solutions portal | Needs exact URL | Foundational setup docs | `ghl-getting-started` | Find exact Getting Started section. |
| Agency View | Agency Company Settings | Needs exact URL | Agency dashboard, branding, global settings, sub-account controls | `ghl-agency-view` | Exact article needed. |
| SaaS Configurator | HighLevel SaaS Mode Setup Guide for Agencies | Needs exact URL | SaaS mode, Stripe, plans, rebilling, snapshots, onboarding | `ghl-saas-configurator` | Exact article needed. |
| Contacts | Solutions portal | Needs URL refinement | Contact-related docs | `ghl-contacts` | Find exact Contacts section. |
| Opportunities & Pipelines | Solutions portal | Needs URL refinement | Pipeline and opportunity docs | `ghl-opportunities-pipelines` | Find exact CRM or pipeline section. |
| Sites | Solutions portal | Needs URL refinement | Funnels, websites, blogs, WordPress, SEO, QR code docs | `ghl-sites` | Find exact Sites section. |
| Payments | HighLevel Pricing & Billing: Wallets, Charges, Rebilling | Needs exact URL | Payments, charges, rebilling, billing behavior | `ghl-payments` | Exact article needed. |
| Settings | Agency Company Settings | Needs exact URL | Agency settings and platform configuration | `ghl-settings` | Shared with Agency View. |
| Documents & Contracts | How to use Documents & Contracts? | Needs exact URL | Contracts, templates, notifications, agreement workflows | `ghl-documents-contracts` | Compare with public APIs URL. |
| Dashboards | Solutions portal | Needs URL refinement | Dashboard widgets, themes, templates, permissions | `ghl-dashboards` | Find exact section. |
| Account Snapshots | HighLevel SaaS Mode Setup Guide for Agencies | Needs exact URL | Snapshot use in SaaS setup and deployment | `ghl-account-snapshots` | Shared with SaaS Configurator. |
| Reporting | Getting Started with Custom Objects | Needs exact URL | Reporting relationships with objects and dashboards | `ghl-reporting` | May be supporting only. |
| Logic & Fulfillment | https://marketplace.gohighlevel.com/docs/ | Canonical source | Webhook, custom value, and integration behavior | `ghl-logic-fulfillment`, `ghl-api-docs-root` | API docs likely canonical. |
| Mobile & Desktop App | Solutions portal | Needs URL refinement | Mobile app and desktop app documentation | `ghl-mobile-desktop-app` | Find exact app section. |
| Agency Reporting | Solutions portal | Needs URL refinement | Agency-level reporting and scheduler docs | `ghl-agency-reporting` | Find exact section. |
| Memberships & Communities | Solutions portal | Needs URL refinement | Membership and community docs | `ghl-memberships-communities` | Find exact section. |
| Client Portal | Solutions portal | Needs URL refinement | Client portal setup and dashboard docs | `ghl-client-portal` | Find exact section. |
| Custom Objects | Getting Started with Custom Objects | Needs exact URL | Custom objects overview and automation uses | `ghl-custom-objects` | Exact article needed. |
| Companies | Getting Started with Custom Objects | Supporting source | Companies and associations | `ghl-companies` | May need stronger canonical Companies source. |
| CRM | Solutions portal | Needs URL refinement | CRM notes, tasks, contacts, associations, pipeline docs | `ghl-crm` | Find exact section. |
| Tasks | Solutions portal | Needs URL refinement | Unified task management and recurring tasks | `ghl-tasks` | Find exact section. |
| Media Storage | Solutions portal | Needs URL refinement | Media library, file handling, Canva integration | `ghl-media-storage` | Find exact section. |

## 8. Phase 3 optional/later candidate mappings

| Watch Area | Candidate URL or Title | URL Type | Recommended Use | Related Source IDs | Status Notes |
|---|---|---|---|---|---|
| Customer Support | 24/7 Customer Support Options | Needs exact URL | Support options, billing support, migration help, login recovery | `ghl-customer-support` | Exact article needed. |
| HighLevel Affiliates Program | HighLevel Affiliate Program - Affiliate Portal | Needs exact URL | Affiliate docs, portal access, link setup, payout tracking | `ghl-affiliates-program` | Exact article needed. |
| Notifications | Solutions portal | Needs URL refinement | User and sub-account notifications | `ghl-notifications` | Find exact section. |
| Add-ons & Sales Trainings | Solutions portal | Needs URL refinement | Add-ons, sales materials, training content | `ghl-add-ons-sales-trainings` | Optional/later. |
| University | Solutions portal | Needs URL refinement | Training and prospecting lessons | `ghl-university` | Optional/later. |
| Miscellaneous | Solutions portal | Needs URL refinement | General platform notes and UX issue articles | `ghl-miscellaneous` | Low priority, avoid noisy source. |
| Reselling Products | Prerequisite to Launch Your First Affiliate Campaign | Needs exact URL | Product listing, external website support, affiliate commerce | `ghl-reselling-products` | Exact article needed. |
| Internationalization | 24/7 Customer Support Options | Supporting source | International support numbers and regional support | `ghl-internationalization` | Supporting source only. |
| Compliance | AI Tools in HighLevel | Supporting source | AI behavior and compliance-adjacent platform grouping | `ghl-compliance` | Need stronger canonical compliance source. |
| Industry Guides | Solutions portal | Needs URL refinement | Industry playbooks and guides | `ghl-industry-guides` | Exact section needed. |
| App Marketplace | https://marketplace.gohighlevel.com/docs/ | Supporting source | App integration and developer ecosystem | `ghl-app-marketplace` | API docs support marketplace behavior. |
| E-commerce Store | HighLevel Pricing & Billing: Wallets, Charges, Rebilling | Supporting source | Store checkout, charges, payment behavior | `ghl-ecommerce-store` | May need stronger e-commerce source. |
| Certificates | https://help.gohighlevel.com/support/solutions/articles/155000006323-documents-contracts-public-apis | Supporting source | Certificates, badges, issuance workflow automation anchors | `ghl-certificates` | Supporting only unless certificates are clearly covered. |
| Merge Fields & Custom Variables | Custom Values For Courses | Needs exact URL | Dynamic values, templating, personalization behavior | `ghl-merge-fields-custom-variables` | Find stronger canonical merge fields or custom values source. |
| GoKollab | Solutions portal | Needs URL refinement | GoKollab group, course, and community docs | `ghl-gokollab` | Exact section needed. |

## 9. Exact URL collection queue

This is the running queue of title-based targets that still need an
exact official URL copied from the browser. Verifiers should work
through these by searching the HighLevel support portal for each
title and pasting the resulting article / folder URL back into the
corresponding row in sections 4–8.

### Phase 1 still needs exact URLs

- A List of Workflow Triggers
- A List of Workflow Actions
- Workflow Triggers folder
- Workflow Trigger - Form Submitted
- AI Tools in HighLevel
- Voice AI source
- Conversation AI source
- MCP Server source
- Knowledge Bases source

### Phase 2 still needs exact URLs

- Agency Company Settings
- HighLevel SaaS Mode Setup Guide for Agencies
- HighLevel Pricing & Billing: Wallets, Charges, Rebilling
- How to use Documents & Contracts?
- Getting Started with Custom Objects
- Mobile & Desktop App support section
- Agency Reporting support section
- Memberships & Communities support section
- Client Portal support section
- CRM support section
- Tasks support section
- Media Storage support section

### Phase 3 still needs exact URLs

- 24/7 Customer Support Options
- HighLevel Affiliate Program - Affiliate Portal
- Notifications support section
- Add-ons & Sales Trainings support section
- University support section
- Miscellaneous support section
- Prerequisite to Launch Your First Affiliate Campaign
- Industry Guides support section
- HighLevel Pricing & Billing: Wallets, Charges, Rebilling
- Custom Values For Courses
- GoKollab support section

## 10. Promotion rules

A candidate URL recorded in this document can only be promoted to
`config/watched-pages.json` after **all** of the following are true:

1. It is manually opened in a browser.
2. It resolves successfully.
3. It is confirmed to be on an official HighLevel domain.
4. It is the best available article, folder, or canonical page for
   that watch area.
5. The tracker (`docs/source-verification-tracker.md`) is updated in
   the same commit.
6. `enabled` remains `false`.
7. `verify_before_enabling` remains `true`.
8. `content_selector` remains `null` until selector testing is done.

Promotion is a separate, reviewed change — never a side effect of
adding a row to this map. The map is the research layer; the config
and tracker are the source of truth.
