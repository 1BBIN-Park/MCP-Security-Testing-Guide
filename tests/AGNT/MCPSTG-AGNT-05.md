# Test Unsafe Retry and Loop Behavior

ID: MCPSTG-AGNT-05

## Summary

Summarize the weakness in practical language for MCP systems (host, server, tools, model routing). Explain why it matters in composed deployments.

## Scenario

Describe a realistic lab scenario using placeholders:

- **MCP host/client:** `<TEST_USER>` on a managed workstation running `<AUTHORIZED_LAB_SERVER>` integrations only.
- **MCP server:** a lab server package under `<TEST_WORKSPACE>`.
- **Tools/resources/prompts involved:** `<TEST_TOOL_NAME>`, `<TEST_RESOURCE>`.
- **Trust boundary:** between host, server, OS, and upstream APIs.
- **Attacker position:** external network attacker, malicious insider, or compromised upstream content (pick what applies).
- **Potential impact:** confidentiality, integrity, availability, or financial abuse.

## Test Objectives

- Verify the specific insecure behavior is absent or mitigated.
- Identify missing controls (authorization, input validation, egress policy, logging).
- Describe what **secure** behavior looks like under the same inputs.

## Preconditions

- Authorized lab environment and written scope.
- Access to host configuration, server configuration, and (if applicable) gateway policy UI.
- Test principal `<TEST_USER>` and non-privileged secondary account if testing cross-user issues.
- Log access for host, gateway, and MCP server.

## How to Test

### 1. Manual Review

Review documentation, tool metadata, and permission manifests for risky defaults.

### 2. Configuration Review

Inspect environment variables, config files, and transport settings with secrets redacted.

### 3. Runtime Testing

Execute safe, bounded calls through the MCP client using synthetic arguments only.

### 4. Abuse Case Testing

Attempt benign mutations of parameters and sequencing (no destructive payloads, no third-party targets).

### 5. Log and Detection Review

Confirm events contain enough structured fields to reconstruct tool name, principal, decision, and outcome without leaking secrets.

## Test Data / Example Payloads

Use only synthetic examples, for example:

- Tool argument: `{"query": "benign-lab-string-123", "workspace": "<TEST_WORKSPACE>"}`
- Resource URI: `<TEST_RESOURCE>`

## Expected Results

- **Secure:** policy blocks unsafe actions; logs show a deny/alert with stable reason codes.
- **Insecure:** sensitive data returned, dangerous side effect occurs, or approvals are bypassed.
- **Evidence:** redacted logs, policy screenshots, hashes of server build artifacts.

## Remediation

Apply least privilege, strong defaults, approvals for high-risk tools, input validation, output filtering, gateway egress controls, and secret hygiene.

## Tools

Generic categories: MCP inspection utilities, HTTP/TLS proxies, static analysis, dependency scanners, structured log queries, policy-as-code test harnesses.

## References

- OWASP Web Security Testing Guide (structure inspiration only).
- OWASP LLM Top 10 for LLM Applications.
- OWASP API Security Top 10.
- OWASP ASVS (verification requirements).
- Model Context Protocol documentation (cite versioned sections when possible).
- CWE and MITRE ATLAS where applicable.

## Mapping

- OWASP MCP Top 10: `N/A` (cite your organizational list if adopted)
- OWASP LLM Top 10: TBD (pick entry if credible, else `N/A`)
- OWASP API Security Top 10: TBD / `N/A`
- OWASP ASVS: TBD / `N/A`
- MCP specification (versioned): TBD
- CWE: TBD / `N/A`
- MITRE ATLAS: TBD / `N/A`
- Risk level: High
- Testing type: Hybrid
