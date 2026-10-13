# Contributing to MCPSTG

## Goals

- Practical, repeatable security tests for MCP clients, servers, tools, resources, transports, and agentic workflows.
- **Vendor-neutral** language: describe control patterns, not product marketing.
- **Do not copy** text from the OWASP Web Security Testing Guide; follow its structural ideas only.

## Test case files

- **Canonical location:** tests live in [Chapter 4 section pages](04-mcp-security-testing/README.md) (`4.01`–`4.19`), embedded under **Test cases**.
- Use the template in [04-mcp-security-testing/test-case-format.md](04-mcp-security-testing/test-case-format.md)
- Use placeholders only: `<TEST_TOOL_NAME>`, `<TEST_RESOURCE>`, `<TEST_WORKSPACE>`, `<TEST_USER>`, `<AUTHORIZED_LAB_SERVER>`, etc.
- **Never** document steps that target real organizations, customers, or non-lab endpoints.

## Taxonomy rules

- **One primary prefix per test** (the category code matches the ID prefix).
- **Input validation** tests use `MCPSTG-INPV-*` in [4.10 Input Validation](04-mcp-security-testing/4.10-input-validation.md).
- **Output handling** tests use `MCPSTG-OUTV-*` in [4.11 Output Handling](04-mcp-security-testing/4.11-output-handling.md).
- New categories (`TRNS`, `GW`, `SECR`, `ABUS`, `PRVC`) follow the same numbering pattern.

## Mappings discipline

- Map to **OWASP LLM Top 10**, **OWASP API Security Top 10**, **OWASP ASVS**, **CWE**, and **MITRE ATLAS** only when credible.
- **OWASP MCP Top 10:** include only if your edition cites a specific published or draft list; otherwise use `N/A` with a short note.
- Cite **versioned** MCP specification sections when referencing protocol behavior.

## Index maintenance

When adding or renaming a test:

1. Add or update the test block in the matching section file (`4.01`–`4.19`).
2. Update the **Test cases** summary table in that section.
3. Update [index.json](index.json) with `id`, `title`, `category`, `risk`, `testingType`, `file`, `anchor`, and optional mappings.

## Optional metadata block

You may add YAML front matter at the top of a test block for tooling. If present, it should align with [schemas/test-case.schema.json](schemas/test-case.schema.json).

## Reviews

Pull requests should state:

- Scope of systems the change applies to (for example stdio servers vs remote HTTP transports).
- Whether examples were exercised in a **lab** only.
