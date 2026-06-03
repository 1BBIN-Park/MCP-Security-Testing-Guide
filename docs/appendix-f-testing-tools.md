# Appendix F: Testing Tools Resource

Tools commonly useful for MCP security testing in **authorized labs**. This is not an endorsement list; validate fit for your environment and license terms.

## Protocol and API inspection

- **HTTP proxy** (Burp Suite, OWASP ZAP) — remote MCP transports, gateway paths, OAuth flows.
- **TLS analyzers** — certificate validation, cipher suites (`MCPSTG-TRNS-*`).
- **JSON / JSON-RPC helpers** — schema validation, replay of tool calls with mutated arguments.

## Host and local process review

- **Process monitor** — which MCP servers a host spawns, command lines, environment leakage.
- **Filesystem tools** — permissions on workspaces, config stores, token caches (`MCPSTG-CONF-*`, `MCPSTG-SECR-*`).
- **Static analysis** — server and tool source for injection, path handling, subprocess use.

## Logging and detection validation

- **Log aggregation queries** — correlate host, gateway, and server events (`MCPSTG-LOG-*`).
- **SIEM content testing** — dry-run rules against redacted lab transcripts.

## Supply chain

- **Dependency scanners** (OSV, Snyk, etc.) — server packages and container images (`MCPSTG-SUPP-02`).
- **Signature / provenance verification** — align with organizational policy (`MCPSTG-SUPP-01`, `MCPSTG-GOV-02`).

## Lab harness (recommended)

Build or use a minimal MCP server with synthetic tools and resources. See [Appendix D — Safe Lab Fixtures](appendix-d-lab-fixtures.md) and framework guidance in [Chapter 3](03-mcp-security-testing-framework.md).

## Repository tooling

- [`index.json`](../index.json) — machine-readable catalog of all 79 MCPSTG tests (section file, anchor, risk, type).
- [`schemas/test-case.schema.json`](../schemas/test-case.schema.json) — optional structured metadata for tests.
