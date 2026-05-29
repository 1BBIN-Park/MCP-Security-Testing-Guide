# MCP Security Testing Guide (MCPSTG)

Vendor-neutral security testing guidance for systems built around the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). This repository follows an **OWASP Web Security Testing Guide–style** layout: numbered narrative chapters, a dedicated **MCP Security Testing** chapter (test procedures), and appendices.

## Audience

Developers, security testers, red teams, application security engineers, AI security reviewers, **platform engineers**, and **MCP server maintainers**.

## Guide structure (read in order)

| # | Chapter | What it contains |
|---|---------|------------------|
| 1 | [**Frontispiece**](docs/01-frontispiece.md) | Title, version, how to read the guide |
| 2 | [**Introduction**](docs/02-introduction.md) | MCP scope, audience, safe testing rules |
| 3 | [**The MCP Security Testing Framework**](docs/03-mcp-security-testing-framework.md) | Principles, methodology, threat modeling, SDLC |
| 4 | [**MCP Security Testing**](docs/04-mcp-security-testing.md) | **Index of all tests** → procedures in [`tests/`](tests/) |
| 5 | [**Reporting**](docs/05-reporting.md) | Finding format, evidence, severity |

### Where is the MCP security testing?

**Chapter 4** is the table of contents for every test. Each test is a markdown file under **`tests/<CATEGORY>/`**, for example [`tests/TOOL/MCPSTG-TOOL-01.md`](tests/TOOL/MCPSTG-TOOL-01.md). Start at [docs/04-mcp-security-testing.md](docs/04-mcp-security-testing.md) or browse [`tests/`](tests/) directly.

### Appendices

| Appendix | File |
|----------|------|
| A — Glossary | [docs/appendix-a-glossary.md](docs/appendix-a-glossary.md) |
| B — Sample Threat Scenarios | [docs/appendix-b-scenarios.md](docs/appendix-b-scenarios.md) |
| C — Evidence Checklist | [docs/appendix-c-evidence-checklist.md](docs/appendix-c-evidence-checklist.md) |
| D — Safe Lab Fixtures | [docs/appendix-d-lab-fixtures.md](docs/appendix-d-lab-fixtures.md) |
| E — Suggested Reading | [docs/appendix-e-suggested-reading.md](docs/appendix-e-suggested-reading.md) |
| F — Testing Tools Resource | [docs/appendix-f-testing-tools.md](docs/appendix-f-testing-tools.md) |

## Repository layout

### Project root

| Name | Role |
|------|------|
| [Overview](README.md) | Project summary, layout, legal notice |
| [Contributing](CONTRIBUTING.md) | Contribution rules, tone, bootstrap usage |
| [Test index](index.json) | Machine-readable catalog of all test cases |

### Test cases (`tests/`)

| Name | Role |
|------|------|
| [Category folders](tests/) | One subdirectory per four-letter category (`TOOL/`, `AUTHN/`, …) |
| [Example test case](tests/TOOL/MCPSTG-TOOL-01.md) | Pattern: `tests/<CATEGORY>/MCPSTG-<CATEGORY>-NN.md` |

Category titles and the full test list are in [docs/04-mcp-security-testing.md](docs/04-mcp-security-testing.md).

### Tooling (`scripts/`, `schemas/`)

| Name | Role |
|------|------|
| [Bootstrap tests](scripts/bootstrap_tests.py) | Create or refresh test stubs from the taxonomy |
| [Test case schema](schemas/test-case.schema.json) | Optional JSON Schema for structured test metadata |

## Test ID format

`MCPSTG-<CATEGORY>-<NUMBER>` (for example `MCPSTG-TOOL-01`).

## Important notice

This guide is educational material. **Do not** use it to test systems without explicit written authorization. Use synthetic lab environments and placeholders—not production data or real third-party targets.

## Regenerating tests

See [CONTRIBUTING.md](CONTRIBUTING.md) for `scripts/bootstrap_tests.py` (preserves hand-authored tests unless `--force`).

## License

Specify your license in a `LICENSE` file when publishing (for example CC BY-SA 4.0 for documentation-only projects).
# mcp-security-testing-guide
