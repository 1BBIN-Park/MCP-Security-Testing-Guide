# 5. Reporting

## 5.1 Purpose

MCP assessments produce findings that span **hosts**, **servers**, **gateways**, **tools**, and **upstream APIs**. Consistent reporting helps owners remediate quickly and supports detection engineering.

## 5.2 Minimum finding fields

Each finding should include:

- **Test ID** (for example `MCPSTG-AUTHZ-04`) and test title from [Chapter 4](04-mcp-security-testing/README.md).
- **Affected component** (host, server, gateway, specific tool, transport).
- **Prerequisites** and **reproduction steps** using lab placeholders only.
- **Impact** (confidentiality, integrity, availability, financial abuse, safety).
- **Evidence** (redacted logs, config hashes, screenshots of approval dialogs).
- **Remediation** mapped to accountable owners (host team vs server team vs platform).
- **Residual risk** after fixes and any accepted compensating controls.

## 5.3 Evidence packaging

Use [Appendix C — Evidence Checklist](appendix-c-evidence-checklist.md). At minimum, capture:

- Correlation IDs across host, gateway, and server logs (when applicable).
- Tool name, redacted arguments, approval decision, and user principal.
- Transport metadata relevant to the finding (for example TLS version, binding mode).

## 5.4 Severity and risk rating

Rate findings using your organization's standard (CVSS, DREAD, or qualitative scales). For MCP, explicitly note:

- Whether exploitation requires **model cooperation** or works with **direct protocol abuse**.
- Whether **human approval** was bypassed, misleading, or absent.
- **Blast radius** (single user, tenant, fleet-wide host policy).

## 5.5 Reporting to different audiences

| Audience | Emphasis |
|----------|----------|
| Engineering | Reproduction, config diffs, code locations, patch guidance |
| Platform / SRE | Gateway rules, fleet policy, logging gaps, rollout risk |
| Leadership | Business impact, regulatory exposure, timeline, residual risk |
| Detection | Observable events, suggested rules, false-positive notes |

## 5.6 Operational reporting obligations

Beyond technical content:

- Confirm **vendor terms** for SaaS in the chain (host, model API, registry).
- Provide **emergency contacts** and an agreed **stop condition** if tests destabilize shared environments.
- Record **authorization scope** (systems, dates, techniques allowed).

## 5.7 Mapping to standards

In each test file's **Mapping** section, cite **OWASP LLM Top 10**, **OWASP API Security Top 10**, **ASVS**, **CWE**, and **MITRE ATLAS** only when credible. For organization-specific MCP risk lists, cite the named document and version; otherwise use `N/A` (see governance note in [Chapter 4 — taxonomy](04-mcp-security-testing/taxonomy.md)).
