# Appendix B: Sample Threat Scenarios

These short narratives link multiple test IDs. Use them in threat modeling workshops.

## Scenario B1: Poisoned capability metadata

An attacker contributes a malicious MCP server package to a shared registry. Tool **descriptions** claim benign behavior while parameters enable destructive actions. A host auto-installs the server for employees.

**Relevant tests:** `MCPSTG-TOOL-01`, `MCPSTG-SUPP-03`, `MCPSTG-GOV-02`, `MCPSTG-LOG-01`.

## Scenario B2: Resource-driven takeover

A compromised documentation wiki is exposed to the model as a resource. Pages contain hidden instructions to exfiltrate environment variable names via a tool that echoes arguments to an outbound webhook tool.

**Relevant tests:** `MCPSTG-PRMT-02`, `MCPSTG-GW-02`, `MCPSTG-RSRC-01`, `MCPSTG-SECR-01`.

## Scenario B3: Chain escalation across credentials

Tool A lists cloud resources with read-only credentials. Tool B performs writes using a different credential bundle, but the model chains A→B using inferred identifiers without an explicit human mapping step.

**Relevant tests:** `MCPSTG-AUTHZ-04`, `MCPSTG-TOOL-05`, `MCPSTG-AGNT-02`.

## Scenario B4: Multi-session context confusion

A shared lab host caches conversation context or tool outputs between users. User 2’s session receives fragments of user 1’s prior tool results.

**Relevant tests:** `MCPSTG-CTX-04`, `MCPSTG-AUTHZ-03`, `MCPSTG-PRVC-02`.

## Scenario B5: OAuth token replay across MCP routes

A gateway terminates TLS and forwards to multiple MCP backends using path prefixes. A valid OAuth access token for **environment A** is replayed against the **environment B** route. Weakness appears if the gateway does not bind tokens to audience, tenant, or backend instance.

**Relevant tests:** `MCPSTG-TRNS-02`, `MCPSTG-AUTHN-02`, `MCPSTG-SECR-02`, `MCPSTG-GOV-03`.
