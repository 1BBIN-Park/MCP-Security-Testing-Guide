# How to Run MCPSTG Tests

[← Chapter 4 overview](README.md) · [About test procedures](about-docs-tests.md)

This page describes a practical workflow for running tests explained in **sections 4.1–4.19** during an authorized MCP security assessment.

## Before you start

1. **Confirm scope** — Which hosts, servers, transports, and tenants are in scope? Document out-of-scope systems explicitly.
2. **Read Chapter 3** — Apply [framework principles](../03-mcp-security-testing-framework.md): assume composition, test chains, validate detection.
3. **Prepare a lab** — Use synthetic tools/resources; see [Appendix D](../appendix-d-lab-fixtures.md).
4. **Enable logging** — Host, gateway, and MCP server logs should be available for `MCPSTG-LOG-*` validation.

## Step 1: Reconnaissance (`MCPSTG-INFO-*`)

Start with [4.1 Information Gathering](4.01-information-gathering.md). You cannot prioritize tests without knowing:

- Which MCP servers and clients exist
- Which tools and resources are exposed
- Where trust boundaries sit (host ↔ server ↔ OS ↔ upstream API)
- Which context flows carry sensitive data

Output: an inventory table mapping servers → tools → data classes → identities.

## Step 2: Pick categories by risk

Use the chapter hub risk signals:

| If your deployment has… | Prioritize |
|-------------------------|------------|
| Remote MCP or HTTP transport | `TRNS`, `AUTHN`, `GW` |
| Powerful tools (write, exec, network) | `TOOL`, `AUTHZ`, `INPV`, `GW` |
| Multi-user or multi-tenant hosts | `AUTHZ`, `CTX`, `PRVC`, `RSRC` |
| Agentic planners with retries | `AGNT`, `AUTHZ`, `ABUS` |
| Third-party or registry-installed servers | `SUPP`, `GOV`, `SECR` |
| Resources fed from untrusted content | `PRMT`, `RSRC`, `CTX` |

Each [category guide](4.01-information-gathering.md) explains when that family of tests matters most.

## Step 3: Work through the test in its section

Open the category guide (for example [4.4 Authorization](4.04-authorization-permission.md)), use the **View** link in the table or scroll to **Test cases**, and follow the explained steps for that ID (for example [MCPSTG-AUTHZ-02](4.04-authorization-permission.md#mcpstg-authz-02)).

Work through sections in order:

1. **Preconditions** — Stop if scope or access is insufficient; note as “not tested” with reason.
2. **Manual / configuration review** — Often finds issues before runtime abuse.
3. **Runtime testing** — Bounded calls with synthetic arguments only.
4. **Abuse case testing** — Mutations and sequencing within lab limits.
5. **Log and detection review** — Confirm events are alertable.

## Step 4: Record evidence

Capture per [Appendix C — Evidence Checklist](../appendix-c-evidence-checklist.md):

- Test ID and title (from procedure header)
- Host/server versions (hashes if possible)
- Redacted logs, policy screenshots, before/after capability lists
- Explicit **secure** vs. **insecure** observation tied to expected results

Report using [Chapter 5 — Reporting](../05-reporting.md).

## Step 5: Chain tests deliberately

MCP failures often appear in **composition**:

```
untrusted resource → model context → tool call → upstream API
```

When a single test passes in isolation but the deployment feels risky, chain adjacent IDs—for example:

- `MCPSTG-PRMT-02` + `MCPSTG-TOOL-05` (indirect injection leading to dangerous chaining)
- `MCPSTG-RSRC-04` + `MCPSTG-OUTV-02` (secrets in resources echoed in tool output)
- `MCPSTG-AUTHZ-02` + `MCPSTG-AGNT-03` (approval bypass in multi-step workflows)

Category guides call out common chains in **Related categories** sections.

## Testing types

| Type | Meaning |
|------|---------|
| **Manual** | Human-driven review and lab steps |
| **Automated** | Suitable for scanners or scripted checks (for example dependency CVEs) |
| **Hybrid** | Combines review, runtime testing, and log validation |

The **Type** column in each category table comes from [`index.json`](../../index.json).

## Tooling

See [Appendix F — Testing Tools](../appendix-f-testing-tools.md) and [`index.json`](../../index.json) for the machine-readable test catalog.
