# Test Redaction of Secrets in Logs and Traces

ID: MCPSTG-SECR-03

## Summary

Structured logging for MCP is essential for detection, but **raw tool arguments**, **resource bodies**, and **HTTP headers** often contain secrets, tokens, and PII. Without **redaction pipelines**, SIEM ingestion becomes a **secondary data breach**. This test validates both **static** redaction rules and **dynamic** patterns (Bearer tokens, `Authorization`, query params named `token=`).

## Scenario

- **Gateway** logs full HTTP request lines including query strings.
- **MCP server** logs JSON-RPC `params` verbatim for debugging.
- **Potential impact:** Secrets replicated to many systems with weaker retention controls than production databases.

## Test Objectives

- Verify sensitive fields are **removed or tokenized** before persistence.
- Verify **debug** logging cannot be enabled in production builds without privileged break-glass.
- Verify distributed traces (OpenTelemetry, vendor APM) scrub MCP spans.

## Preconditions

- Lab sink for logs/traces (or staging project) where synthetic secrets can be injected safely.
- Representative log pipeline (agent → forwarder → SIEM).

## How to Test

### 1. Manual Review

Read logging config: field allowlists, regex redactors, sampling rules that might skip redaction under load.

### 2. Configuration Review

Identify processors that mutate log records; confirm ordering so parsers see redacted output.

### 3. Runtime Testing

1. Call `<TEST_TOOL_NAME>_echo` with argument containing a **fake** API key string (`FAKE_KEY_mcpstg_...`).
2. Search logs/traces for that substring—expect **zero hits** outside intentionally isolated debug vaults (should be none in prod-like env).

### 4. Abuse Case Testing

- Nested JSON: secret inside `metadata.callbackUrl=https://...?token=...`
- Multiline PEM blocks in tool arguments (synthetic certificates marked lab-only).

### 5. Log and Detection Review

**Detection:** pipeline self-checks that alert when redaction rules fail (canary secret in lab).

## Test Data / Example Payloads

```json
{
  "note": "lab-only",
  "token": "FAKE_BEARER_mcpstg_deadbeef",
  "nested": { "Authorization": "Bearer FAKE_BEARER_mcpstg_deadbeef" }
}
```

## Expected Results

- **Secure:** redacted or hashed representations only; debug gated.
- **Insecure:** full secret visible in stdout, log index, or trace UI.
- **Evidence:** search query results (counts), pipeline version id.

## Remediation

- Default-deny logging of `params`; structured allowlist per tool.
- Central redaction service; tests in CI that fail builds on sample leaks.
- Short retention for high-cardinality debug channels.

## Tools

- Log search (lab project), trace UI, regex-based linters on sample exports.

## References

- OWASP ASVS: V7 Error Handling and Logging (sensitive data in logs).
- CWE-532: Insertion of Sensitive Information into Log File

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: `N/A`
- OWASP API Security Top 10: API08 Related (sensitive data exposure via logs)
- OWASP ASVS: V7
- MCP specification (versioned): N/A; observability practice
- CWE: CWE-532
- MITRE ATLAS: `N/A`
- Risk level: High
- Testing type: Hybrid
