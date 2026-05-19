# Test Missing Authentication on MCP Server

ID: MCPSTG-AUTHN-01

## Summary

An MCP server exposed on a **network transport** without authentication allows any client that can reach the port to list tools, read resources, and invoke side-effecting capabilities. Even “internal only” networks are often broader than assumed (VPN split tunneling, compromised laptops, mis-routed VPC peering). **Stdio** transports shift risk to **local process** spawning but do not remove authorization requirements if multiple principals share a machine.

## Scenario

- **Remote MCP** listens on `0.0.0.0` in a container with wide security groups “for debugging.”
- **Attacker position:** Any internal host that can route to the port; malware on a developer laptop during off-VPN periods.
- **Potential impact:** Remote code paths via dangerous tools, data exfiltration via resources, lateral movement.

## Test Objectives

- Verify unauthenticated clients cannot complete MCP initialization or tool calls (for deployments that claim authentication).
- Verify **network binding** is loopback-only or behind authenticated mesh where policy requires it.
- Verify stdio servers are **not** accidentally exposed via TCP wrappers or socat tunnels left running.

## Preconditions

- Lab clone of the service topology; no testing against production without explicit scope.
- Secondary machine or network namespace in lab to simulate non-client origin if authorized.

## How to Test

### 1. Manual Review

Read deployment guide: is authentication mandatory or “optional for internal”?

### 2. Configuration Review

- Firewall rules, bind addresses, `docker port` mappings, Kubernetes `Service` types (`LoadBalancer` vs `ClusterIP`).
- Auth middleware order: authentication before capability negotiation.

### 3. Runtime Testing

1. From an **unauthorized** lab client (no token / wrong mTLS cert), call `initialize` and `tools/list`—expect **fail** if auth is required.
2. From authorized client—expect success.
3. For stdio-only servers, verify no auxiliary HTTP admin port is exposed without auth.

### 4. Abuse Case Testing

- Replay a captured `Authorization` header from a different lab session id—expect rejection if session-bound.

### 5. Log and Detection Review

**Detection:** failed auth spikes, connections from unexpected CIDRs, successful anonymous tool calls (should be impossible if policy says otherwise).

## Test Data / Example Payloads

Use synthetic bearer strings: `Authorization: Bearer lab-invalid-token`.

## Expected Results

- **Secure:** anonymous access impossible; bind addresses match policy; auth enforced before tools/resources.
- **Insecure:** anonymous `tools/call` succeeds; server listens on all interfaces without TLS in sensitive zones.
- **Evidence:** redacted tcpdump summaries, config diffs, audit logs.

## Remediation

- Require mutual TLS or OAuth for remote MCP; place behind authenticated gateway by default.
- Bind to localhost for dev; use SSH tunnels instead of wide SGs where possible.
- Add health checks that fail deployment if auth modules are disabled (`MCPSTG-CONF-01`).

## Tools

- `nmap` / `nc` in lab, authenticated curl, service mesh policy debug CLIs.

## References

- OWASP API Security Top 10: API2 Authentication Failures.
- OWASP ASVS: V2 Authentication.
- CWE-306: Missing Authentication for Critical Function

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: `N/A`
- OWASP API Security Top 10: API02
- OWASP ASVS: V2
- MCP specification (versioned): security guidance for HTTP transports you target
- CWE: CWE-306
- MITRE ATLAS: `N/A`
- Risk level: Critical
- Testing type: Hybrid
