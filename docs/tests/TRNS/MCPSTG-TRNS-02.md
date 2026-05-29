# Test Transport Authentication Binding

ID: MCPSTG-TRNS-02

## Summary

**Transport authentication binding** asks whether MCP sessions are tied to the **intended identity, tenant, and origin** for the transport in use. Failures include accepting bearer tokens on the wrong virtual host, missing **origin** checks on browser-originated traffic, confused deputy behavior behind shared reverse proxies, and stdio servers that treat **any local process** on the pipe as trusted.

## Scenario

- **Remote transport:** MCP over HTTPS where the same load balancer serves multiple tenants or environments.
- **Local transport:** stdio MCP server launched by a host; a second local process attempts to attach if file descriptors leak or sockets are world-accessible (misconfiguration).
- **Attacker position:** Network client presenting a stolen token to the wrong MCP base URL; or local malware exploiting permissive IPC.
- **Potential impact:** Cross-tenant tool execution, session fixation, or silent proxy mis-routing of MCP JSON-RPC.

## Test Objectives

- Verify tokens and session handles are **audience-bound** (hostname, path prefix, tenant id) where applicable.
- Verify browser-facing deployments use appropriate **origin**, **CORS**, and **cookie** flags consistent with your threat model—not “wide open because it is internal.”
- Verify stdio/socket transports cannot be reached from unintended OS principals.

## Preconditions

- Lab URLs for at least two logical MCP “tenants” or path prefixes on the same infrastructure (if that matches production topology).
- Two test tokens (or mTLS identities) scoped to different audiences, synthetic only.
- Permission to inspect proxy routing rules (redacted).

## How to Test

### 1. Manual Review

Document the chain: **who authenticates whom** (client→server, server→upstream). Identify whether the MCP endpoint URL is part of the cryptographic or logical binding for tokens.

### 2. Configuration Review

- For HTTPS: check virtual host routing, default backends, and whether a missing `Host` header falls through to a sensitive MCP instance.
- For cookies (if used): `Secure`, `HttpOnly`, `SameSite`, path scope.
- For stdio: process launch arguments, file descriptor inheritance, and socket filesystem permissions.

### 3. Runtime Testing

1. Obtain a **valid** lab token scoped to tenant A.
2. Present it to the MCP endpoint that should only serve tenant B (same LB, different path or host)—expect **reject**.
3. Repeat with correct endpoint—expect **accept**.

### 4. Abuse Case Testing

- Replay captured MCP messages with a rotated nonce or session id if your stack uses such fields—expect strict failure modes, not partial execution.
- If applicable, attempt cross-origin browser calls from an unauthorized lab origin—expect deny.

### 5. Log and Detection Review

**Detection:** authentication failures should log **reason codes** (audience mismatch, unknown client, clock skew) without printing secrets.

## Test Data / Example Payloads

Use synthetic hostnames only, for example `mcp-lab-a.<AUTHORIZED_LAB_SERVER>` vs `mcp-lab-b.<AUTHORIZED_LAB_SERVER>`.

## Expected Results

- **Secure:** wrong audience or origin cannot initialize a session or call tools; stdio server only parent process can communicate.
- **Insecure:** token works on unintended tenant route; world-readable Unix socket accepts connections.
- **Evidence:** redacted proxy rules, auth error logs, minimal PCAP excerpts in lab.

## Remediation

- Bind access tokens to **issuer, audience, and MCP resource identifier**; reject default-backend fallthrough.
- Harden local transports: least-privilege OS users, restricted socket paths, explicit parent–child process relationship checks where feasible.
- Prefer mTLS or signed connection bootstrap for high-risk remote MCP.

## Tools

TLS proxies, JWT debugging utilities (lab tokens only), web browser devtools for origin checks, `lsof` / permission audits for local sockets.

## References

- OWASP ASVS: V2 Authentication, V3 Session Management, V9 Communications.
- OWASP API Security Top 10: API2 Authentication Failures.
- CWE-287: Improper Authentication
- CWE-306: Missing Authentication for Critical Function

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: `N/A` (transport binding)
- OWASP API Security Top 10: API02
- OWASP ASVS: V2, V3, V9
- MCP specification (versioned): transport and security profile you target
- CWE: CWE-287, CWE-306
- MITRE ATLAS: `N/A`
- Risk level: High
- Testing type: Hybrid
