# Source verification tracker

Tracks per-source verification status for every entry in
[`../config/watched-pages.json`](../config/watched-pages.json). One row
per source.

## Verification rules

- **Do not enable a source during verification.** `enabled` stays `false`
  and `verify_before_enabling` stays `true` regardless of how this tracker
  is filled in. Enabling is a separate gate, downstream of fetcher
  implementation.
- **Confirm the URL is official.** It must resolve on an official
  HighLevel domain (`gohighlevel.com`, `highlevel.stoplight.io`,
  `marketplace.gohighlevel.com`). No third-party mirrors, no community
  sites.
- **Prefer section-level URLs over root URLs.** If a more specific
  section URL is known, record it in **Verified URL** — leave the actual
  config change for a separate, reviewed update.
- **Only move to article-level URLs later.** Article-level watching is a
  later phase, gated on the fetcher being implemented and on a section
  showing signal worth drilling into.
- **Record the verifier as Owner** (GitHub username).
- **Keep `verify_before_enabling: true`** in `config/watched-pages.json`
  until the fetcher implementation is ready, even after a URL is verified.

## Status legend

| Status | Meaning |
|---|---|
| Not started | No verification work begun. |
| Needs URL refinement | Reviewed; a better section-level URL is known. Record it in **Verified URL**; do not edit the config in this tracker. |
| Verified | URL confirmed official, current, and at the right granularity. Still not enabled. |
| Deferred | Verification intentionally postponed (section doesn't exist yet, lower priority than expected, etc.). |

## Sources

| Phase | Source ID | Label | Current URL | Target section to verify | Surface | Priority | Verified URL | Owner | Verification status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1-critical | ghl-api-docs-root | HighLevel API Documentation (Stoplight) — root | https://highlevel.stoplight.io/ | Stoplight root index | api, general | high | https://marketplace.gohighlevel.com/docs/ | Sedrick Harris | Verified | Verified official HighLevel API Documentation / Developer Portal URL. |
| 1-critical | ghl-help-center-root | HighLevel Help Center — root | https://help.gohighlevel.com/ | Help center root index | general | high | https://help.gohighlevel.com/support/solutions | Sedrick Harris | Verified | Verified official HighLevel Support Portal knowledge base root. |
| 1-critical | ghl-platform-updates | HighLevel Platform Updates / What's Changed | https://help.gohighlevel.com/ | Platform changelog / What's Changed | general | high | https://ideas.gohighlevel.com/changelog | Sedrick Harris | Verified | Verified official HighLevel public changelog URL for platform updates. |
| 1-critical | ghl-workflows | HighLevel Help Center — Workflows | https://help.gohighlevel.com/ | Workflows section landing page | workflows | high |  | Unassigned | Not started |  |
| 1-critical | ghl-workflow-builder | HighLevel Help Center — Workflow Builder | https://help.gohighlevel.com/ | Workflow Builder section landing page | workflows | high |  | Unassigned | Not started |  |
| 1-critical | ghl-workflow-triggers | HighLevel Help Center — Workflow Triggers | https://help.gohighlevel.com/ | Workflow Triggers section landing page | workflows | high |  | Unassigned | Not started |  |
| 1-critical | ghl-workflow-actions | HighLevel Help Center — Workflow Actions | https://help.gohighlevel.com/ | Workflow Actions section landing page | workflows | high |  | Unassigned | Not started |  |
| 1-critical | ghl-workflow-developer-resources | HighLevel Workflow Developer Resources | https://highlevel.stoplight.io/ | Workflow developer section on Stoplight | workflows, api | high |  | Unassigned | Not started |  |
| 1-critical | ghl-calendars-appointments | HighLevel Help Center — Calendars & Appointments | https://help.gohighlevel.com/ | Calendars & Appointments section landing page | calendars | high |  | Unassigned | Not started |  |
| 1-critical | ghl-conversations | HighLevel Help Center — Conversations | https://help.gohighlevel.com/ | Conversations section landing page | conversations | high |  | Unassigned | Not started |  |
| 1-critical | ghl-phone-system | HighLevel Help Center — Phone System | https://help.gohighlevel.com/ | Phone System section landing page | phone | high |  | Unassigned | Not started |  |
| 1-critical | ghl-messaging | HighLevel Help Center — Messaging | https://help.gohighlevel.com/ | Messaging section landing page | messaging | high |  | Unassigned | Not started |  |
| 1-critical | ghl-a2p-registration | HighLevel Help Center — A2P 10DLC Registration | https://help.gohighlevel.com/ | A2P 10DLC Registration section landing page | messaging | high |  | Unassigned | Not started |  |
| 1-critical | ghl-email | HighLevel Help Center — Email | https://help.gohighlevel.com/ | Email section landing page | email | high | https://help.gohighlevel.com/support/solutions/articles/155000005552-how-to-access-the-all-in-one-dashboard-for-email-marketing | Sedrick Harris | Verified | All-in-One Email Dashboard article (primary). Supporting: Workflow Action - Send Email (`https://help.gohighlevel.com/support/solutions/articles/155000002472-workflow-action-send-email`). |
| 1-critical | ghl-email-deliverability | HighLevel Help Center — Email Deliverability | https://help.gohighlevel.com/ | Email Deliverability section landing page | email | high |  | Unassigned | Not started |  |
| 1-critical | ghl-lc-email | HighLevel Help Center — LC Email | https://help.gohighlevel.com/ | LC Email section landing page | email | high |  | Unassigned | Not started |  |
| 1-critical | ghl-forms | HighLevel Help Center — Forms | https://help.gohighlevel.com/ | Forms section landing page | forms | high |  | Unassigned | Not started |  |
| 1-critical | ghl-surveys | HighLevel Help Center — Surveys | https://help.gohighlevel.com/ | Surveys section landing page | forms | high |  | Unassigned | Not started |  |
| 1-critical | ghl-chat-widget | HighLevel Help Center — Chat Widget | https://help.gohighlevel.com/ | Chat Widget section landing page | messaging, conversations | high |  | Unassigned | Not started |  |
| 1-critical | ghl-ai-employee | HighLevel Help Center — AI Employee | https://help.gohighlevel.com/ | AI Employee section landing page | ai-agents | high | https://help.gohighlevel.com/support/solutions/articles/155000003906-ai-employee-overview | Sedrick Harris | Verified | AI Employee Overview article (primary; slug `ai-employee-overview`). Supporting: AI Tools in HighLevel (`https://help.gohighlevel.com/support/solutions/articles/155000002166-ai-tools-in-highlevel`). |
| 1-critical | ghl-voice-ai | HighLevel Help Center — Voice AI | https://help.gohighlevel.com/ | Voice AI section landing page | ai-agents, phone | high |  | Unassigned | Not started |  |
| 1-critical | ghl-conversation-ai | HighLevel Help Center — Conversation AI | https://help.gohighlevel.com/ | Conversation AI section landing page | ai-agents, conversations | high |  | Unassigned | Not started |  |
| 1-critical | ghl-workflow-ai | HighLevel Help Center — Workflow AI | https://help.gohighlevel.com/ | Workflow AI section landing page | ai-agents, workflows | high |  | Unassigned | Not started |  |
| 1-critical | ghl-ai-studio | HighLevel Help Center — AI Studio | https://help.gohighlevel.com/ | AI Studio section landing page | ai-agents | high |  | Unassigned | Not started |  |
| 1-critical | ghl-agent-studio | HighLevel Help Center — Agent Studio | https://help.gohighlevel.com/ | Agent Studio section landing page | ai-agents | high |  | Unassigned | Not started |  |
| 1-critical | ghl-mcp-server | HighLevel MCP Server | https://highlevel.stoplight.io/ | MCP Server section on Stoplight | ai-agents, api | high |  | Unassigned | Not started |  |
| 1-critical | ghl-knowledge-bases | HighLevel Help Center — Knowledge Bases | https://help.gohighlevel.com/ | Knowledge Bases section landing page | ai-agents | high |  | Unassigned | Not started |  |
| 2-expansion | ghl-developer-resources | HighLevel Developer Resources | https://highlevel.stoplight.io/ | Developer resources index on Stoplight | api | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-contacts | HighLevel Help Center — Contacts | https://help.gohighlevel.com/ | Contacts section landing page | crm | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-opportunities-pipelines | HighLevel Help Center — Opportunities & Pipelines | https://help.gohighlevel.com/ | Opportunities & Pipelines section landing page | crm | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-sites | HighLevel Help Center — Sites (Websites & Funnels) | https://help.gohighlevel.com/ | Sites section landing page | sites | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-payments | HighLevel Help Center — Payments | https://help.gohighlevel.com/ | Payments section landing page | payments | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-settings | HighLevel Help Center — Settings | https://help.gohighlevel.com/ | Settings section landing page | settings | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-documents-contracts | HighLevel Help Center — Documents & Contracts | https://help.gohighlevel.com/ | Documents & Contracts section landing page | payments | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-dashboards | HighLevel Help Center — Dashboards | https://help.gohighlevel.com/ | Dashboards section landing page | reporting | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-reporting | HighLevel Help Center — Reporting | https://help.gohighlevel.com/ | Reporting section landing page | reporting | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-integrations | HighLevel Help Center — Integrations | https://help.gohighlevel.com/ | Integrations section landing page | integrations | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-reputation-management-reviews | HighLevel Help Center — Reputation Management & Reviews | https://help.gohighlevel.com/ | Reputation Management & Reviews section landing page | reputation | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-custom-objects | HighLevel Help Center — Custom Objects | https://help.gohighlevel.com/ | Custom Objects section landing page | crm | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-companies | HighLevel Help Center — Companies | https://help.gohighlevel.com/ | Companies section landing page | crm | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-crm | HighLevel Help Center — CRM (overview) | https://help.gohighlevel.com/ | CRM overview section landing page | crm | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-tasks | HighLevel Help Center — Tasks | https://help.gohighlevel.com/ | Tasks section landing page | crm | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-media-storage | HighLevel Help Center — Media Storage | https://help.gohighlevel.com/ | Media Storage section landing page | general | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-saas-configurator | HighLevel Help Center — SaaS Configurator | https://help.gohighlevel.com/ | SaaS Configurator section landing page | saas | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-agency-view | HighLevel Help Center — Agency View | https://help.gohighlevel.com/ | Agency View section landing page | saas | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-account-snapshots | HighLevel Help Center — Account Snapshots | https://help.gohighlevel.com/ | Account Snapshots section landing page | saas | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-memberships-communities | HighLevel Help Center — Memberships & Communities | https://help.gohighlevel.com/ | Memberships & Communities section landing page | sites | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-client-portal | HighLevel Help Center — Client Portal | https://help.gohighlevel.com/ | Client Portal section landing page | sites, crm | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-app-marketplace | HighLevel App Marketplace | https://marketplace.gohighlevel.com/ | App Marketplace root index | integrations | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-ecommerce-store | HighLevel Help Center — E-commerce Store | https://help.gohighlevel.com/ | E-commerce Store section landing page | sites, payments | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-certificates | HighLevel Help Center — Certificates | https://help.gohighlevel.com/ | Certificates section landing page | sites | medium |  | Unassigned | Not started |  |
| 2-expansion | ghl-merge-fields-custom-variables | HighLevel Help Center — Merge Fields & Custom Variables | https://help.gohighlevel.com/ | Merge Fields & Custom Variables section landing page | general, workflows | medium |  | Unassigned | Not started |  |
