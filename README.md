# OWASP MCP Security Testing Guide

The Model Context Protocol (MCP) is an open protocol that lets LLM applications connect to external data sources, tools, prompts, workflows, and services. This guide treats MCP as a security boundary: the chain from the user, through the model and MCP client, to the MCP server, the connected tool, and the target system.

It is a living collection of MCP security knowledge for developers, AppSec, red teams, and SOC teams. It covers threats, secure development, client and host controls, supply chain, enterprise gateways, detection, incident response, taxonomy, public incidents, case studies, and review checklists.

This work is licensed under [GPL-3.0](LICENSE).

## Chapters

Read the guide in this order. Chapter 3 holds the threat write-ups and **79 tests** in sections 4.1–4.19.

1. [Project Overview](<01. Project_Overview.md>)
2. [MCP Fundamentals](<02. MCP Fundamentals.md>)
3. [MCP Threats and Attack Patterns](<03. MCP Threats and Attack Patterns/README.md>)
4. [Secure MCP Development](<04. Secure MCP Development.md>)
5. [MCP Client and Host Security](<05. MCP Client and Host Security.md>)
6. [MCP Supply Chain Security](<03. MCP Threats and Attack Patterns/4.13-supply-chain.md>)
7. [MCP Gateways, Registries, and Enterprise Governance](<07. MCP Gateways, Registries, and Enterprise Governance.md>)
8. [Detection, Monitoring, and SOC Content](<03. MCP Threats and Attack Patterns/4.12-logging-detection.md#detection-monitoring-and-soc-content>)
9. [MCP Incident Response](<09. MCP Incident Response.md>)
10. [MCP Security Taxonomy](<10. MCP Security Taxonomy.md>)
11. [Hacks, News, and Public Incidents](<11. Hacks, News, and Public Incidents.md>)
14. [Appendix A — Glossary](<14. Appendix A - Glossary.md>)
15. [Appendix B — Sample Threat Scenarios](<15. Appendix B - Sample Threat Scenarios.md>)
16. [Appendix C — Suggested Reading](<16. Appendix C - Suggested Reading.md>)
17. [Appendix G — Security Review](<17. Appendix G - Security Review.md>)

Review rows for servers, clients, governance, incident response, and authorized red-team tests sit in those chapters. [Appendix G](<17. Appendix G - Security Review.md>) holds the status values, review flow, scorecard, and copy-paste review template.

[Contributing](CONTRIBUTING.md) describes how to edit section pages. Test IDs use the form `MCPSTG-<CATEGORY>-<NUMBER>`.

This guide is educational material. Do not use it to test systems without explicit written authorization. Use synthetic lab environments and placeholders.

## Related OWASP projects

- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)
