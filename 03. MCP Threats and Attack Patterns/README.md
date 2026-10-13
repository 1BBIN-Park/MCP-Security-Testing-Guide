# 3. MCP Threats and Attack Patterns

This chapter is the **MCP equivalent of OWASP WSTG Chapter 4**. It defines **79** security test cases for MCP hosts, clients, servers, tools, resources, transports, gateways, and agentic workflows.

**Every test is explained in sections 3.1–3.19 on this chapter’s pages**—including summary, scenario, steps, **MCP code snippets** (JSON-RPC, host config, lab scripts), expected results, and remediation. All test documentation lives in this folder; there is no separate reader-facing test section elsewhere in the guide.

---

## How this chapter is organized

| Layer | Location | What you get |
|-------|----------|--------------|
| **Chapter hub** | This file | Navigation and links to sections 3.1–3.19 |
| **Sections 3.1–3.19** | `3.01-*.md` … `3.19-*.md` | Category context, **published threats with sources**, and **all tests explained with code snippets** |

---

## Chapter 3 guides

### Getting started

| Guide | Description |
|-------|-------------|
| [About test procedures](about-docs-tests.md) | How tests are organized in sections 3.1–3.19 |
| [How to run tests](how-to-run.md) | Assessment workflow from inventory to evidence |
| [Test ID taxonomy](taxonomy.md) | Prefix meanings and ID matrix |
| [Test case format](test-case-format.md) | Template for authors (maintainers) |
| [Red team checklist](test-case-format.md#mcp-red-team-checklist) | Rules of engagement, safe tests, and the finding template |
| [Attack pattern index](3.01-information-gathering.md#documented-public-samples) | Public samples that the patterns in this chapter come from |
| [Attack surface and pattern catalog](3.01-information-gathering.md#attack-surface-and-pattern-catalog) | Attack-surface model, pattern summary, and public-sample catalog |

### Test categories — sections 3.1 to 3.19

| Section | Category | Open guide |
|---------|----------|------------|
| 3.1 | Information Gathering (`INFO`) | [3.1](3.01-information-gathering.md) |
| 3.2 | Configuration and Deployment (`CONF`) | [3.2](3.02-configuration-deployment.md) |
| 3.3 | Identity and Authentication (`AUTHN`) | [3.3](3.03-identity-authentication.md) |
| 3.4 | Authorization and Permission (`AUTHZ`) | [3.4](3.04-authorization-permission.md) |
| 3.5 | Tool Security (`TOOL`) | [3.5](3.05-tool-security.md) |
| 3.6 | Resource and Data Access (`RSRC`) | [3.6](3.06-resource-data-access.md) |
| 3.7 | Prompt and Instruction (`PRMT`) | [3.7](3.07-prompt-instruction.md) |
| 3.8 | Context and Memory (`CTX`) | [3.8](3.08-context-memory.md) |
| 3.9 | Agentic Workflow (`AGNT`) | [3.9](3.09-agentic-workflow.md) |
| 3.10 | Input Validation (`INPV`) | [3.10](3.10-input-validation.md) |
| 3.11 | Output Handling (`OUTV`) | [3.11](3.11-output-handling.md) |
| 3.12 | Logging and Detection (`LOG`) | [3.12](3.12-logging-detection.md) |
| 3.13 | Supply Chain (`SUPP`) | [3.13](3.13-supply-chain.md) |
| 3.14 | Enterprise Governance (`GOV`) | [3.14](3.14-enterprise-governance.md) |
| 3.15 | Transport and Channel (`TRNS`) | [3.15](3.15-transport-channel.md) |
| 3.16 | Gateway and Egress (`GW`) | [3.16](3.16-gateway-egress.md) |
| 3.17 | Secrets and Credentials (`SECR`) | [3.17](3.17-secrets-credentials.md) |
| 3.18 | Resilience and Abuse (`ABUS`) | [3.18](3.18-resilience-abuse.md) |
| 3.19 | Privacy and Retention (`PRVC`) | [3.19](3.19-privacy-retention.md) |

---

## Quick start

1. Open [3.1 Information Gathering](3.01-information-gathering.md) and work through **Test cases**.
2. Use **Example snippets** in each test—replace `<TEST_*>` placeholders with [Appendix D](../appendix-d-lab-fixtures.md) fixtures.
3. Report per [Chapter 5 — Reporting](../05-reporting.md).

---

## Guide table of contents

1. [Project Overview](<../01. Project_Overview.md>)
2. [MCP Fundamentals](<../02. MCP Fundamentals.md>)
3. **MCP Threats and Attack Patterns** (this chapter). Supply chain is [section 3.13](3.13-supply-chain.md). Detection and SOC content is [section 3.12](3.12-logging-detection.md#detection-monitoring-and-soc-content).
4. [Secure MCP Development](<../04. Secure MCP Development.md>)
5. [MCP Client and Host Security](<../05. MCP Client and Host Security.md>)
6. [MCP Gateways, Registries, and Enterprise Governance](<../06. MCP Gateways, Registries, and Enterprise Governance.md>)
7. [MCP Incident Response](<../07. MCP Incident Response.md>)
8. [MCP Security Taxonomy](<../08. MCP Security Taxonomy.md>)
9. [Hacks, News, and Public Incidents](<../09. Hacks, News, and Public Incidents.md>)
10. [Appendix A — Glossary](<../10. Appendix A - Glossary.md>)
11. [Appendix B — Suggested Reading](<../11. Appendix B - Suggested Reading.md>)
12. [Appendix C — Security Review](<../12. Appendix C - Security Review.md>)

Review rows for servers, clients, governance, incident response, and authorized red-team tests sit in those chapters. [Appendix C](<../12. Appendix C - Security Review.md>) holds the status values, review flow, scorecard, and copy-paste review template.

---

## Maintainers

Edit tests directly in the matching section file (`3.01`–`3.19`) under **Test cases** when adding or renaming tests.

See [About test procedures](about-docs-tests.md) and [CONTRIBUTING.md](../CONTRIBUTING.md).
