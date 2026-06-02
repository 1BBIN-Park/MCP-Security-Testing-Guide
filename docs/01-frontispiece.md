# 1. Frontispiece

## MCP Security Testing Guide (MCPSTG)

**Version:** 1.0 (draft)  
**Status:** Community guidance — not an official OWASP project document  
**Structure:** Modeled on the [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) chapter layout, adapted for Model Context Protocol (MCP) systems.

## About this guide

MCPSTG is vendor-neutral security testing guidance for **hosts**, **clients**, **MCP servers**, **tools**, **resources**, **prompts**, **transports**, **gateways**, and **agentic workflows** built on MCP.

This repository separates:

| Part | Location |
|------|----------|
| Narrative chapters | [`docs/`](.) |
| Executable test procedures | [`docs/tests/`](tests/) |
| Machine-readable catalog | [`index.json`](../index.json) |

## How to read this guide

1. [Frontispiece](01-frontispiece.md) (this page)
2. [Introduction](02-introduction.md)
3. [The MCP Security Testing Framework](03-mcp-security-testing-framework.md)
4. [MCP Security Testing](04-mcp-security-testing/README.md) — **all test cases live under** [`docs/tests/`](tests/)
5. [Reporting](05-reporting.md)

**Appendices**

- [Appendix A — Glossary](appendix-a-glossary.md)
- [Appendix B — Sample Threat Scenarios](appendix-b-scenarios.md)
- [Appendix C — Evidence Checklist](appendix-c-evidence-checklist.md)
- [Appendix D — Safe Lab Fixtures](appendix-d-lab-fixtures.md)
- [Appendix E — Suggested Reading](appendix-e-suggested-reading.md)
- [Appendix F — Testing Tools Resource](appendix-f-testing-tools.md)

## Important notice

This guide is **educational material**. Do not use it against systems without **explicit written authorization**. Use synthetic lab environments and placeholders—not production data or third-party targets without engagement.

## License

Specify your license in a `LICENSE` file when publishing (for example CC BY-SA 4.0 for documentation-only projects).
