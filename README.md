# OWASP MCP Security Testing Guide

The Model Context Protocol (MCP) is an open protocol that lets LLM applications connect to external data sources, tools, prompts, workflows, and services. This guide treats MCP as a security boundary: the chain from the user, through the model and MCP client, to the MCP server, the connected tool, and the target system.

It is a living collection of MCP security knowledge for developers, AppSec, red teams, and SOC teams. It covers threats, secure development, client and host controls, supply chain, enterprise gateways, detection, incident response, taxonomy, public incidents, case studies, and review checklists.

This work is licensed under [GPL-3.0](LICENSE).

## Chapters

1. [Project Overview](<1. Project_Overview.md>)
2. [MCP Fundamentals](<2. MCP Fundamentals.md>)
3. [MCP Threats and Attack Patterns](mcp-threats-and-attack-patterns.md) — pattern index; the write-ups live in [MCP Security Testing](<3. MCP Threats and Attack Patterns/README.md>) sections 4.1–4.19
4. [Secure MCP Development](<4. Secure MCP Development.md>)
5. [MCP Client and Host Security](<5. MCP Client and Host Security.md>)
6. [MCP Supply Chain Security](<6. MCP Supply Chain Security.md>)
7. [MCP Gateways, Registries, and Enterprise Governance](<7. MCP Gateways, Registries, and Enterprise Governance.md>)
8. [Detection, Monitoring, and SOC Content](<8. Detection, Monitoring, and SOC Content.md>)
9. [MCP Incident Response](<9. MCP Incident Response.md>)
10. [MCP Security Taxonomy](<10. MCP Security Taxonomy.md>)
11. [Hacks, News, and Public Incidents](<11. Hacks, News, and Public Incidents.md>)
12. [Case Studies](<12. Case Studies.md>)
13. [Checklists](<13. Checklists.md>)
14. [Glossary](<14. Glossary.md>)

## MCP security testing

The test catalog is in [Chapter 4](<3. MCP Threats and Attack Patterns/README.md>). It uses an OWASP Web Security Testing Guide–style layout: numbered narrative chapters and **79 tests** in sections 4.1–4.19.

| # | Chapter | What it contains |
| --- | --- | --- |
| 1 | [Frontispiece](01-frontispiece.md) | Title, version, how to read the guide |
| 2 | [MCP Fundamentals](<2. MCP Fundamentals.md>) | What MCP is, scope, audience, safe testing rules |
| 3 | [The MCP Security Testing Framework](03-mcp-security-testing-framework.md) | Principles, methodology, threat modeling, SDLC |
| 4 | [MCP Security Testing](<3. MCP Threats and Attack Patterns/README.md>) | Tests explained in sections 4.1–4.19 |
| 5 | [Reporting](05-reporting.md) | Finding format, evidence, severity |
| — | [MCP Threats and Attack Patterns](mcp-threats-and-attack-patterns.md) | Index of attack patterns, public samples, and defenses in sections 4.1–4.19 |

[Contributing](CONTRIBUTING.md) describes how to edit section pages. [index.json](index.json) is the machine-readable catalog of test cases. Test IDs use the form `MCPSTG-<CATEGORY>-<NUMBER>`.

This guide is educational material. Do not use it to test systems without explicit written authorization. Use synthetic lab environments and placeholders.

## Related OWASP projects

- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)
