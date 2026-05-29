# 4. MCP Security Testing

This chapter is the **MCP equivalent of OWASP WSTG Chapter 4 (Web Application Security Testing)**. It defines **79** security test cases for MCP hosts, clients, servers, tools, resources, transports, gateways, and agentic workflows.

**Executable procedures** live in [`docs/tests/`](tests/)—one markdown file per test ID. **Category guides** (this chapter’s subpages) explain *why* each test family matters and link to those procedures. The machine-readable catalog is [`index.json`](../index.json).

---

## How this chapter is organized

| Layer | Location | What you get |
|-------|----------|--------------|
| **Chapter hub** | This file | Navigation, quick reference, links to all subpages |
| **Chapter guides** | [`04-mcp-security-testing/`](04-mcp-security-testing/about-docs-tests.md) | Full explanations of taxonomy, workflow, and each test category |
| **Procedures** | [`docs/tests/<CATEGORY>/`](tests/) | Step-by-step lab tests (`MCPSTG-*-*.md`) |

Start with [About `docs/tests/`](04-mcp-security-testing/about-docs-tests.md) if you are new to the repository layout.

---

## Chapter 4 guides

### Getting started

| Guide | Description |
|-------|-------------|
| [About `docs/tests/`](04-mcp-security-testing/about-docs-tests.md) | What the procedure directory is, how it relates to this chapter, skeleton vs. curated tests |
| [How to run tests](04-mcp-security-testing/how-to-run.md) | Assessment workflow from inventory to evidence and reporting |
| [Test ID taxonomy](04-mcp-security-testing/taxonomy.md) | Prefix meanings, numbering rules, ID matrix |
| [Test case format](04-mcp-security-testing/test-case-format.md) | Required sections, placeholders, maintainer notes |

### Test categories (4.1 – 4.19)

Each guide includes scope, priority guidance, related categories, common test chains, and a table linking to procedures in `docs/tests/`.

| Section | Category | Guide | Procedure folder |
|---------|----------|-------|------------------|
| 4.1 | Information Gathering (`INFO`) | [Open guide](04-mcp-security-testing/4.01-information-gathering.md) | [`tests/INFO/`](tests/INFO/) |
| 4.2 | Configuration and Deployment (`CONF`) | [Open guide](04-mcp-security-testing/4.02-configuration-deployment.md) | [`tests/CONF/`](tests/CONF/) |
| 4.3 | Identity and Authentication (`AUTHN`) | [Open guide](04-mcp-security-testing/4.03-identity-authentication.md) | [`tests/AUTHN/`](tests/AUTHN/) |
| 4.4 | Authorization and Permission (`AUTHZ`) | [Open guide](04-mcp-security-testing/4.04-authorization-permission.md) | [`tests/AUTHZ/`](tests/AUTHZ/) |
| 4.5 | Tool Security (`TOOL`) | [Open guide](04-mcp-security-testing/4.05-tool-security.md) | [`tests/TOOL/`](tests/TOOL/) |
| 4.6 | Resource and Data Access (`RSRC`) | [Open guide](04-mcp-security-testing/4.06-resource-data-access.md) | [`tests/RSRC/`](tests/RSRC/) |
| 4.7 | Prompt and Instruction (`PRMT`) | [Open guide](04-mcp-security-testing/4.07-prompt-instruction.md) | [`tests/PRMT/`](tests/PRMT/) |
| 4.8 | Context and Memory (`CTX`) | [Open guide](04-mcp-security-testing/4.08-context-memory.md) | [`tests/CTX/`](tests/CTX/) |
| 4.9 | Agentic Workflow (`AGNT`) | [Open guide](04-mcp-security-testing/4.09-agentic-workflow.md) | [`tests/AGNT/`](tests/AGNT/) |
| 4.10 | Input Validation (`INPV`) | [Open guide](04-mcp-security-testing/4.10-input-validation.md) | [`tests/INPV/`](tests/INPV/) |
| 4.11 | Output Handling (`OUTV`) | [Open guide](04-mcp-security-testing/4.11-output-handling.md) | [`tests/OUTV/`](tests/OUTV/) |
| 4.12 | Logging and Detection (`LOG`) | [Open guide](04-mcp-security-testing/4.12-logging-detection.md) | [`tests/LOG/`](tests/LOG/) |
| 4.13 | Supply Chain (`SUPP`) | [Open guide](04-mcp-security-testing/4.13-supply-chain.md) | [`tests/SUPP/`](tests/SUPP/) |
| 4.14 | Enterprise Governance (`GOV`) | [Open guide](04-mcp-security-testing/4.14-enterprise-governance.md) | [`tests/GOV/`](tests/GOV/) |
| 4.15 | Transport and Channel (`TRNS`) | [Open guide](04-mcp-security-testing/4.15-transport-channel.md) | [`tests/TRNS/`](tests/TRNS/) |
| 4.16 | Gateway and Egress (`GW`) | [Open guide](04-mcp-security-testing/4.16-gateway-egress.md) | [`tests/GW/`](tests/GW/) |
| 4.17 | Secrets and Credentials (`SECR`) | [Open guide](04-mcp-security-testing/4.17-secrets-credentials.md) | [`tests/SECR/`](tests/SECR/) |
| 4.18 | Resilience and Abuse (`ABUS`) | [Open guide](04-mcp-security-testing/4.18-resilience-abuse.md) | [`tests/ABUS/`](tests/ABUS/) |
| 4.19 | Privacy and Retention (`PRVC`) | [Open guide](04-mcp-security-testing/4.19-privacy-retention.md) | [`tests/PRVC/`](tests/PRVC/) |

---

## Quick start

1. Read [About `docs/tests/`](04-mcp-security-testing/about-docs-tests.md) to understand the two-layer structure (guides vs. procedures).
2. Run [4.1 Information Gathering](04-mcp-security-testing/4.01-information-gathering.md) to build inventory.
3. Pick categories by risk using [How to run tests](04-mcp-security-testing/how-to-run.md).
4. Open a procedure under [`docs/tests/`](tests/) and execute in an authorized lab.
5. Report per [Chapter 5 — Reporting](05-reporting.md).

**How to run tests:** follow each procedure’s **How to Test** sections; use synthetic lab placeholders only.

---

## Guide table of contents

1. [Frontispiece](01-frontispiece.md)
2. [Introduction](02-introduction.md)
3. [The MCP Security Testing Framework](03-mcp-security-testing-framework.md)
4. **MCP Security Testing** (this chapter → [`docs/tests/`](tests/))
5. [Reporting](05-reporting.md)

**Appendices:** [A](appendix-a-glossary.md) · [B](appendix-b-scenarios.md) · [C](appendix-c-evidence-checklist.md) · [D](appendix-d-lab-fixtures.md) · [E](appendix-e-suggested-reading.md) · [F](appendix-f-testing-tools.md)

---

## `docs/tests/` at a glance

The [`docs/tests/`](tests/) tree holds **79 procedure files** in **19 category folders**. Each file:

- Uses ID format `MCPSTG-<CATEGORY>-<NN>` (for example `MCPSTG-TOOL-01`)
- Follows the [test case format](04-mcp-security-testing/test-case-format.md)
- Is indexed in [`index.json`](../index.json) with risk level and testing type (Manual, Automated, Hybrid)

**Example path:** [`docs/tests/TOOL/MCPSTG-TOOL-01.md`](tests/TOOL/MCPSTG-TOOL-01.md) — Test Tool Description Poisoning.

For the full explanation of directory layout, naming, skeleton vs. curated content, and navigation, see [About `docs/tests/`](04-mcp-security-testing/about-docs-tests.md).
