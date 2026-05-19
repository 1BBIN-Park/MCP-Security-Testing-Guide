# Map MCP Trust Boundaries

ID: MCPSTG-INFO-04

## Summary

Trust boundary mapping is the **foundation** for MCP assessments. Without an explicit diagram of where **identity is established**, where **authorization is enforced**, and where **data changes trust level** (for example from “user typed” to “retrieved from repo”), testers duplicate work and miss composition risks. This test produces a **living artifact** the team can diff as servers and tools change.

## Scenario

- Organization runs multiple MCP servers (internal data, HR, build/deploy) behind one gateway.
- Teams disagree whether the **model** or the **host** is responsible for a given control.
- **Potential impact:** Gaps go untested because ownership is unclear; incidents are slow to triage.

## Test Objectives

- Produce a boundary map covering **host UI**, **MCP client**, **transport**, **MCP server**, **tool runtime**, **filesystem**, **IdP**, **gateway**, **upstream APIs**, and **logs**.
- Label each hop with **authenticator**, **authorizer**, and **sensitive data classes** crossing it.
- Highlight **unauthenticated** segments (for example local stdio) and justify accepted risk.

## Preconditions

- Architecture docs or access to engineers from host, server, and platform teams.
- Inventory from `MCPSTG-INFO-01` through `MCPSTG-INFO-03` partially complete.

## How to Test

### 1. Manual Review

Interview-style checklist:

- Who installs MCP servers? Who can update tool code?
- Where are OAuth tokens stored? Who can read them?
- Which tools call which upstream APIs with which credentials?

### 2. Configuration Review

Collect sanitized diagrams from IaC: security groups, service mesh routes, gateway policies.

### 3. Runtime Testing

Trace one **golden path** read-only workflow and one **high-risk** workflow (mutating tool) with logging enabled; annotate the trace onto the boundary map.

### 4. Abuse Case Testing

For each boundary, ask: “If this hop is malicious, what is still protected upstream?” Document **assumptions** explicitly (for example “we assume laptop disk is trusted”).

### 5. Log and Detection Review

Confirm logs exist at each control point needed for **after-the-fact** reconstruction (`MCPSTG-LOG-05`).

## Test Data / Example Payloads

Use architecture placeholders:

- `TrustZone_UserDevice`, `TrustZone_CorpNet`, `TrustZone_CloudTenantA`.

## Expected Results

- **Secure process output:** a reviewed diagram with owners per boundary and linked test IDs.
- **Insecure process:** no shared artifact; contradictory verbal models; missing controls on unnamed hops.
- **Evidence:** version-controlled diagram file, meeting notes with sign-off (no secrets).

## Remediation

- Publish the map in the internal wiki; gate new tools on boundary updates.
- Automate drift detection when new outbound domains or tools appear (`MCPSTG-GOV-01`).

## Tools

Diagramming (draw.io, Mermaid), CMDB or service catalog links, architecture review templates.

## References

- OWASP ASVS: V1 Architecture, design, and threat modeling.
- NIST SP 800-53 RA family (risk assessment) as organizational context—not a test script.

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: `N/A`
- OWASP API Security Top 10: `N/A`
- OWASP ASVS: V1
- MCP specification (versioned): high-level reference only
- CWE: `N/A` (process control)
- MITRE ATLAS: `N/A`
- Risk level: High
- Testing type: Manual
