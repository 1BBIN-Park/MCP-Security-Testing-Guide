# Test SSRF Protections for Tool-Mediated HTTP Requests

ID: MCPSTG-GW-02

## Summary

Server-side tools often perform HTTP requests using URLs or hostnames derived from **model-chosen arguments** or **retrieved documents**. Without egress policy, attackers can pivot through the MCP server’s network position to reach **cloud metadata endpoints**, internal health checks, or private lab services. Gateways should enforce **destination allowlists**, DNS controls, and logging on every tool-mediated egress path.

## Scenario

- **MCP host/client:** Managed developer host for `<TEST_USER>`.
- **MCP server:** Lab server with `<TEST_TOOL_NAME>_http_fetch` that retrieves analyst-supplied URLs.
- **Gateway:** Corporate egress proxy intended to restrict destinations.
- **Attacker position:** Prompt attacker or poisoned `<TEST_RESOURCE>` steering the model toward disallowed hosts.
- **Potential impact:** Confidentiality (internal metadata), lateral probing, or abuse of internal webhooks.

## Test Objectives

- Confirm disallowed destinations are **blocked before connect** (not only after TLS failure).
- Confirm logs attribute attempts to **tool id**, **principal**, and **resolved IP** (where permitted).
- Define **secure** behavior: only `<AUTHORIZED_LAB_SERVER>` and explicit allowlist entries succeed.

## Preconditions

- Lab-controlled internal dummy service and an **authorized** external echo endpoint you operate.
- Gateway policy UI or infrastructure-as-code repo access.
- No scanning of third-party networks; all targets must be lab-owned.

## How to Test

### 1. Manual Review

Read gateway policy: are rules based on hostname only, or also **ports** and **URL paths**? Check for DNS rebinding gaps and allowlisting of raw IPs.

### 2. Configuration Review

Verify separate policies for **MCP transport** traffic versus **tool egress** traffic. Confirm metadata IP ranges are denied if applicable to your cloud.

### 3. Runtime Testing

1. Invoke `<TEST_TOOL_NAME>_http_fetch` with `https://<AUTHORIZED_LAB_SERVER>/ok` — expect **allow**.
2. Invoke with an **internal lab-only** URL you are authorized to probe (for example `http://127.0.0.1:<lab-port>/`) — expect **deny** at gateway unless explicitly in scope.
3. Invoke with a **non-lab** public URL outside allowlist — expect **deny**.

### 4. Abuse Case Testing

- URL parsing tricks: mixed case schemes, userinfo prefixes, IPv6 literals—**only** if your lab harness safely supports parsing tests without hitting the open internet.
- Chain: resource suggests a URL → model passes to tool; repeat under different models/prompts.

### 5. Log and Detection Review

**Detection (secure):** deny events include standardized `egress_denied`, tool name, normalized URL class (not necessarily full secret-bearing query strings), and correlation id across MCP steps.

## Test Data / Example Payloads

```json
{ "url": "https://<AUTHORIZED_LAB_SERVER>/echo?tag=mcpstg-lab" }
```

```json
{ "url": "http://169.254.169.254/" }
```

Expect the second to be **blocked** in cloud-adjacent labs when policy forbids metadata endpoints.

## Expected Results

- **Secure:** gateway blocks; MCP server surfaces a safe error; no partial response leakage from internal services.
- **Insecure:** internal HTTP succeeds; errors leak stack traces with internal hostnames.
- **Evidence:** redacted gateway logs, policy version hash, HAR or proxy capture (lab only).

## Remediation

- Default-deny egress with allowlisted destinations per tool class.
- Resolve and validate hosts in a **hardened resolver** context; block link-local and metadata ranges where appropriate.
- Split **read-only** fetch tools from **authenticated API** tools with different policies.

## Tools

- Corporate HTTP forward proxy in lab, mitmproxy or similar in controlled setups, DNS logs, IaC policy tests.

## References

- OWASP Web Security Testing Guide (structure inspiration only).
- OWASP API Security Top 10: API7 Server Side Request Forgery.
- OWASP ASVS: V13 API and web service (SSRF-related verification).
- CWE-918: Server-Side Request Forgery (SSRF).

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: LLM06 related (agent-initiated network actions)
- OWASP API Security Top 10: API07
- OWASP ASVS: V13
- MCP specification (versioned): tool behavior is implementation-defined—cite your server version
- CWE: CWE-918
- MITRE ATLAS: `N/A` unless mapped to a specific exfil technique in your threat model
- Risk level: Critical
- Testing type: Hybrid
