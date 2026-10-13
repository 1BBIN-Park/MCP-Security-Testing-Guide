# 4. MCP Security Testing

This chapter is the **MCP equivalent of OWASP WSTG Chapter 4**. It defines **79** security test cases for MCP hosts, clients, servers, tools, resources, transports, gateways, and agentic workflows.

**Every test is explained in sections 4.1–4.19 on this chapter’s pages**—including summary, scenario, steps, **MCP code snippets** (JSON-RPC, host config, lab scripts), expected results, and remediation. All test documentation lives in this folder; there is no separate reader-facing test section elsewhere in the guide.

---

## How this chapter is organized

| Layer | Location | What you get |
|-------|----------|--------------|
| **Chapter hub** | This file | Navigation and links to sections 4.1–4.19 |
| **Sections 4.1–4.19** | `4.01-*.md` … `4.19-*.md` | Category context, **published threats with sources**, and **all tests explained with code snippets** |

---

## Chapter 4 guides

### Getting started

| Guide | Description |
|-------|-------------|
| [About test procedures](about-docs-tests.md) | How tests are organized in sections 4.1–4.19 |
| [How to run tests](how-to-run.md) | Assessment workflow from inventory to evidence |
| [Test ID taxonomy](taxonomy.md) | Prefix meanings and ID matrix |
| [Test case format](test-case-format.md) | Template for authors (maintainers) |
| [Red team checklist](test-case-format.md#mcp-red-team-checklist) | Rules of engagement, safe tests, and the finding template |
| [Attack pattern index](4.01-information-gathering.md#documented-public-samples) | Public samples that the patterns in this chapter come from |
| [Attack surface and pattern catalog](4.01-information-gathering.md#attack-surface-and-pattern-catalog) | Attack-surface model, pattern summary, and public-sample catalog |

### Test categories — sections 4.1 to 4.19

| Section | Category | Open guide |
|---------|----------|------------|
| 4.1 | Information Gathering (`INFO`) | [4.1](4.01-information-gathering.md) |
| 4.2 | Configuration and Deployment (`CONF`) | [4.2](4.02-configuration-deployment.md) |
| 4.3 | Identity and Authentication (`AUTHN`) | [4.3](4.03-identity-authentication.md) |
| 4.4 | Authorization and Permission (`AUTHZ`) | [4.4](4.04-authorization-permission.md) |
| 4.5 | Tool Security (`TOOL`) | [4.5](4.05-tool-security.md) |
| 4.6 | Resource and Data Access (`RSRC`) | [4.6](4.06-resource-data-access.md) |
| 4.7 | Prompt and Instruction (`PRMT`) | [4.7](4.07-prompt-instruction.md) |
| 4.8 | Context and Memory (`CTX`) | [4.8](4.08-context-memory.md) |
| 4.9 | Agentic Workflow (`AGNT`) | [4.9](4.09-agentic-workflow.md) |
| 4.10 | Input Validation (`INPV`) | [4.10](4.10-input-validation.md) |
| 4.11 | Output Handling (`OUTV`) | [4.11](4.11-output-handling.md) |
| 4.12 | Logging and Detection (`LOG`) | [4.12](4.12-logging-detection.md) |
| 4.13 | Supply Chain (`SUPP`) | [4.13](4.13-supply-chain.md) |
| 4.14 | Enterprise Governance (`GOV`) | [4.14](4.14-enterprise-governance.md) |
| 4.15 | Transport and Channel (`TRNS`) | [4.15](4.15-transport-channel.md) |
| 4.16 | Gateway and Egress (`GW`) | [4.16](4.16-gateway-egress.md) |
| 4.17 | Secrets and Credentials (`SECR`) | [4.17](4.17-secrets-credentials.md) |
| 4.18 | Resilience and Abuse (`ABUS`) | [4.18](4.18-resilience-abuse.md) |
| 4.19 | Privacy and Retention (`PRVC`) | [4.19](4.19-privacy-retention.md) |

---

## Quick start

1. Open [4.1 Information Gathering](4.01-information-gathering.md) and work through **Test cases**.
2. Use **Example snippets** in each test—replace `<TEST_*>` placeholders with [Appendix D](../appendix-d-lab-fixtures.md) fixtures.
3. Report per [Chapter 5 — Reporting](../05-reporting.md).

---

## Guide table of contents

1. [Project Overview](<../01. Project_Overview.md>)
2. [MCP Fundamentals](<../02. MCP Fundamentals.md>)
3. **MCP Threats and Attack Patterns** (this chapter)
4. [Secure MCP Development](<../04. Secure MCP Development.md>)
5. [MCP Client and Host Security](<../05. MCP Client and Host Security.md>)
6. [MCP Supply Chain Security](4.13-supply-chain.md)
7. [MCP Gateways, Registries, and Enterprise Governance](<../07. MCP Gateways, Registries, and Enterprise Governance.md>)
8. [Detection, Monitoring, and SOC Content](4.12-logging-detection.md#detection-monitoring-and-soc-content)
9. [MCP Incident Response](<../09. MCP Incident Response.md>)
10. [MCP Security Taxonomy](<../10. MCP Security Taxonomy.md>)
11. [Hacks, News, and Public Incidents](<../11. Hacks, News, and Public Incidents.md>)
14. [Appendix A — Glossary](<../14. Appendix A - Glossary.md>)
15. [Appendix B — Sample Threat Scenarios](<../15. Appendix B - Sample Threat Scenarios.md>)
16. [Appendix C — Suggested Reading](<../16. Appendix C - Suggested Reading.md>)
17. [Appendix G — Security Review](<../17. Appendix G - Security Review.md>)

Review rows for servers, clients, governance, incident response, and authorized red-team tests sit in those chapters. [Appendix G](<../17. Appendix G - Security Review.md>) holds the status values, review flow, scorecard, and copy-paste review template.

---

## Maintainers

Edit tests directly in the matching section file (`4.01`–`4.19`) under **Test cases** when adding or renaming tests.

See [About test procedures](about-docs-tests.md) and [CONTRIBUTING.md](../CONTRIBUTING.md).
