# MCP Security Testing Guide (MCPSTG)

Vendor-neutral security testing guidance for systems built around the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). This repository follows an **OWASP Web Security Testing Guide–style** layout: numbered narrative chapters, a dedicated **MCP Security Testing** chapter (sections 4.1–4.19), and appendices.

## Audience

Developers, security testers, red teams, application security engineers, AI security reviewers, **platform engineers**, and **MCP server maintainers**.

## Guide structure (read in order)


| #   | Chapter                                                                             | What it contains                                                     |
| --- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 1   | **[Frontispiece](docs/01-frontispiece.md)**                                         | Title, version, how to read the guide                                |
| 2   | **[Introduction](docs/02-introduction.md)**                                         | MCP scope, audience, safe testing rules                              |
| 3   | **[The MCP Security Testing Framework](docs/03-mcp-security-testing-framework.md)** | Principles, methodology, threat modeling, SDLC                       |
| 4   | **[MCP Security Testing](docs/04-mcp-security-testing/README.md)**                  | **79 tests explained in sections 4.1–4.19** (with MCP code snippets) |
| 5   | **[Reporting](docs/05-reporting.md)**                                               | Finding format, evidence, severity                                   |
| —   | **[MCP Threats and Attack Patterns](docs/mcp-threats-and-attack-patterns.md)**     | Canonical attack patterns, public samples, and defenses              |


### Where is the MCP security testing?

Open **[Chapter 4](docs/04-mcp-security-testing/README.md)** and pick a section **4.1 through 4.19**. Each page explains that category’s tests on the same page—summary, steps, **example JSON/YAML/code snippets**, and expected results. Example: [4.18 Resilience and Abuse](docs/04-mcp-security-testing/4.18-resilience-abuse.md).

### Appendices


| Appendix                    | File                                                                           |
| --------------------------- | ------------------------------------------------------------------------------ |
| A — Glossary                | [docs/appendix-a-glossary.md](docs/appendix-a-glossary.md)                     |
| B — Sample Threat Scenarios | [docs/appendix-b-scenarios.md](docs/appendix-b-scenarios.md)                   |
| C — Evidence Checklist      | [docs/appendix-c-evidence-checklist.md](docs/appendix-c-evidence-checklist.md) |
| D — Safe Lab Fixtures       | [docs/appendix-d-lab-fixtures.md](docs/appendix-d-lab-fixtures.md)             |
| E — Suggested Reading       | [docs/appendix-e-suggested-reading.md](docs/appendix-e-suggested-reading.md)   |
| F — Testing Tools Resource  | [docs/appendix-f-testing-tools.md](docs/appendix-f-testing-tools.md)           |


## Repository layout

### Project root


| Name                            | Role                                       |
| ------------------------------- | ------------------------------------------ |
| [Overview](README.md)           | Project summary, layout, legal notice      |
| [Contributing](CONTRIBUTING.md) | Contribution rules, tone, bootstrap usage  |
| [Test index](index.json)        | Machine-readable catalog of all test cases |


### Chapter 4 test sections


| Section    | Category              | Guide                                                   |
| ---------- | --------------------- | ------------------------------------------------------- |
| 4.1 – 4.19 | All MCPSTG categories | [Chapter 4 hub](docs/04-mcp-security-testing/README.md) |


Tests are **not** maintained as a separate reader-facing documentation tree. Section pages under `docs/04-mcp-security-testing/` are the canonical reading path.

### Tooling (`schemas/`)


| Name                                              | Role                                              |
| ------------------------------------------------- | ------------------------------------------------- |
| [Test case schema](schemas/test-case.schema.json) | Optional JSON Schema for structured test metadata |


## Test ID format

`MCPSTG-<CATEGORY>-<NUMBER>` (for example `MCPSTG-TOOL-01`).

## Important notice

This guide is educational material. **Do not** use it to test systems without explicit written authorization. Use synthetic lab environments and placeholders—not production data or real third-party targets.

## Maintaining tests

See [CONTRIBUTING.md](CONTRIBUTING.md) for editing section pages and updating [index.json](index.json).

## License

Specify your license in a `LICENSE` file when publishing (for example CC BY-SA 4.0 for documentation-only projects).