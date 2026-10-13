# Contributing to MCPSTG

## Goals

- Practical, repeatable security tests for MCP clients, servers, tools, resources, transports, and agentic workflows.
- **Vendor-neutral** language: describe control patterns, not product marketing.
- **Do not copy** text from the OWASP Web Security Testing Guide; follow its structural ideas only.

## Test case files

- **Canonical location:** tests live in [Chapter 3 section pages](03. MCP Threats and Attack Patterns/README.md) (`3.01`–`3.19`), embedded under **Test cases**.
- Use the template in [03. MCP Threats and Attack Patterns/test-case-format.md](03. MCP Threats and Attack Patterns/test-case-format.md)
- Use placeholders only: `<TEST_TOOL_NAME>`, `<TEST_RESOURCE>`, `<TEST_WORKSPACE>`, `<TEST_USER>`, `<AUTHORIZED_LAB_SERVER>`, etc.
- **Never** document steps that target real organizations, customers, or non-lab endpoints.

## Adding or renaming a test

1. Add or update the test block in the matching section file (`3.01`–`3.19`).
2. Update the **Test cases** summary table in that section.

## Reviews

Pull requests should state:

- Scope of systems the change applies to (for example stdio servers vs remote HTTP transports).
- Whether examples were exercised in a **lab** only.

