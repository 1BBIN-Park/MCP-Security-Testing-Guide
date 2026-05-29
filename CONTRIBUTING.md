# Contributing to MCPSTG

## Goals

- Practical, repeatable security tests for MCP clients, servers, tools, resources, transports, and agentic workflows.
- **Vendor-neutral** language: describe control patterns, not product marketing.
- **Do not copy** text from the OWASP Web Security Testing Guide; follow its structural ideas only.

## Test case files

- One file per test: `docs/tests/<CATEGORY>/MCPSTG-<CATEGORY>-NN.md`.
- Use the template sections defined in [docs/04-mcp-security-testing/test-case-format.md](docs/04-mcp-security-testing/test-case-format.md) (Individual Test Case Format).
- Use placeholders only: `<TEST_TOOL_NAME>`, `<TEST_RESOURCE>`, `<TEST_WORKSPACE>`, `<TEST_USER>`, `<AUTHORIZED_LAB_SERVER>`, etc.
- **Never** document steps that target real organizations, customers, or non-lab endpoints.

## Taxonomy rules

- **One primary prefix per file** (the folder name matches the ID prefix).
- **Input validation** tests use `MCPSTG-INPV-*` under `docs/tests/INPV/`.
- **Output handling** tests use `MCPSTG-OUTV-*` under `docs/tests/OUTV/`.
- New categories (`TRNS`, `GW`, `SECR`, `ABUS`, `PRVC`) follow the same numbering pattern.

## Mappings discipline

- Map to **OWASP LLM Top 10**, **OWASP API Security Top 10**, **OWASP ASVS**, **CWE**, and **MITRE ATLAS** only when credible.
- **OWASP MCP Top 10:** include only if your edition cites a specific published or draft list; otherwise use `N/A` with a short note.
- Cite **versioned** MCP specification sections when referencing protocol behavior.

## Index maintenance

When adding or renaming a test:

1. Add or update `docs/tests/<CATEGORY>/MCPSTG-<CATEGORY>-NN.md`.
2. Update [index.json](index.json) with `id`, `title`, `category`, `risk`, `testingType`, `file`, and optional mappings.

## Regenerating skeletons (`scripts/bootstrap_tests.py`)

- `python3 scripts/bootstrap_tests.py` — refreshes `index.json` and writes **skeleton** markdown for any test not listed in `HAND_AUTHORED`, or for curated IDs whose files are **missing**.
- Curated tests (expanded prose) are **skipped** when the file already exists, so normal runs do not erase hand-written content.
- `python3 scripts/bootstrap_tests.py --force` — overwrites **all** test markdown from the skeleton template. Use only when you intend to reset prose; back up or commit first.

When you fully author a new test, add `(CATEGORY, N)` to `HAND_AUTHORED` in the script (or accept that the next non-force run may overwrite a file you meant to keep—if it is not in the preserve set).

## Optional metadata block

You may add YAML front matter at the top of a test file for tooling. If present, it should align with [schemas/test-case.schema.json](schemas/test-case.schema.json).

## Reviews

Pull requests should state:

- Scope of systems the change applies to (for example stdio servers vs remote HTTP transports).
- Whether examples were exercised in a **lab** only.
