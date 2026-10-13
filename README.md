# OWASP MCP Security Testing Guide

The Model Context Protocol (MCP) is an open protocol that lets LLM applications connect to external data sources, tools, prompts, workflows, and services. This guide treats MCP as a security boundary: the chain from the user, through the model and MCP client, to the MCP server, the connected tool, and the target system.

It is a living collection of MCP security knowledge for developers, AppSec, red teams, and SOC teams. It covers threats, secure development, client and host controls, supply chain, enterprise gateways, detection, incident response, taxonomy, public incidents, case studies, and review checklists.

This work is licensed under [GPL-3.0](LICENSE).

## Chapters

Read the guide in this order. Chapter 3 holds the threat write-ups and **79 tests** in sections 3.1–3.19. Supply chain is [section 3.13](<03. MCP Threats and Attack Patterns/3.13-supply-chain.md>). Detection and SOC content is [section 3.12](<03. MCP Threats and Attack Patterns/3.12-logging-detection.md#detection-monitoring-and-soc-content>).

1. [Project Overview](<01. Project_Overview.md>)
2. [MCP Fundamentals](<02. MCP Fundamentals.md>)
3. [MCP Threats and Attack Patterns](<03. MCP Threats and Attack Patterns/README.md>)
4. [Secure MCP Development](<04. Secure MCP Development.md>)
5. [MCP Client and Host Security](<05. MCP Client and Host Security.md>)
6. [MCP Gateways, Registries, and Enterprise Governance](<06. MCP Gateways, Registries, and Enterprise Governance.md>)
7. [MCP Incident Response](<07. MCP Incident Response.md>)
8. [MCP Security Taxonomy](<08. MCP Security Taxonomy.md>)
9. [Hacks, News, and Public Incidents](<09. Hacks, News, and Public Incidents.md>)
10. [Appendix A — Glossary](<10. Appendix A - Glossary.md>)
11. [Appendix B — Suggested Reading](<11. Appendix B - Suggested Reading.md>)
12. [Appendix C — Security Review](<12. Appendix C - Security Review.md>)

Do not use it to test systems without explicit written authorization. Use synthetic lab environments and placeholders.

## Related OWASP projects

- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)

