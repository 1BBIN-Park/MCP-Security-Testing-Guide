# Test Gateway Allowlist Enforcement for Upstream Tool Destinations

ID: MCPSTG-GW-01

## Summary

Enterprise MCP **gateways** often sit between hosts and MCP servers or between servers and the open internet. A core control is an **allowlist** of upstream destinations that tools may reach (HTTP APIs, internal services, cloud control planes). Misconfigured gateways turn every tool into a generic egress client—amplifying SSRF, data exfiltration, and supply-chain callbacks.

## Scenario

- **Architecture:** MCP server tools call HTTP endpoints; traffic is forced through `<AUTHORIZED_LAB_SERVER>` gateway policies.
- **Attacker position:** Prompt or resource content steers the model to call `https://evil-lab.example` (use only a **non-routable** or **lab-owned** hostname in scope) or an internal service hostname.
- **Potential impact:** Data exfiltration, port scanning via timing, or webhook abuse.

## Test Objectives

- Verify **default deny** for unknown destinations at the gateway.
- Verify allowlist changes are **versioned**, **audited**, and **tested** in CI where possible.
- Verify denied attempts are visible in **SIEM** with enough context to tune rules.

## Preconditions

- Lab gateway policy package and a safe external endpoint you control.
- A tool that accepts a URL or host parameter (`<TEST_TOOL_NAME>_http_fetch` pattern).

## How to Test

### 1. Manual Review

Map every tool that can perform network I/O. Classify destinations (SaaS APIs, internal microservices, object stores).

### 2. Configuration Review

Read allowlist files or policy-as-code modules. Check for wildcards (`*.`) that swallow unintended hosts.

### 3. Runtime Testing

1. Call allowed destination—expect success end-to-end.
2. Call explicitly **disallowed** lab hostname—expect deny at gateway with stable error code.
3. Attempt DNS alias or CNAME that resolves to a disallowed address—expect deny if policy resolves DNS (document behavior if not).

### 4. Abuse Case Testing

- Case and Unicode normalization on hostnames (lab-safe fuzzing only).
- Chained redirects: if redirects are followed, verify redirect targets are re-checked against the allowlist.

### 5. Log and Detection Review

**Detection:** `egress_denied` events include tool id, normalized host, tenant id, and correlation id; no full OAuth tokens in query strings logged.

## Test Data / Example Payloads

```json
{ "url": "https://<AUTHORIZED_LAB_SERVER>/allowed-echo" }
```

```json
{ "url": "https://blocked-lab-host.local/internal" }
```

## Expected Results

- **Secure:** gateway blocks non-allowlisted egress; MCP surfaces a controlled error; alerts can threshold on spikes.
- **Insecure:** requests bypass gateway via alternate interface (direct NIC, DNS tunneling tool); or redirects bypass checks.
- **Evidence:** policy git SHA, redacted deny logs, negative test report.

## Remediation

- Default-deny egress; per-tool destination classes; automated policy tests on PR.
- Disable unsafe redirect following or re-validate each hop.
- Run sensitive tools on network-isolated workers with no generic internet route.

## Tools

Policy test frameworks, egress proxies, DNS logs in lab.

## References

- OWASP API Security Top 10: API7 Server Side Request Forgery (control placement at gateway).
- OWASP ASVS: V13 API and web service.
- CWE-918: Server-Side Request Forgery (SSRF)

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: LLM06 related
- OWASP API Security Top 10: API07
- OWASP ASVS: V13
- MCP specification (versioned): N/A at protocol layer; implementation and deployment
- CWE: CWE-918
- MITRE ATLAS: `N/A`
- Risk level: Critical
- Testing type: Hybrid
