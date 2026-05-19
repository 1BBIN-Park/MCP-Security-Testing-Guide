# Test Rate Limiting and Abuse Throttling at the Gateway

ID: MCPSTG-GW-03

## Summary

Gateways should absorb **abuse-shaped traffic** before it reaches MCP servers and tool runways: burst `tools/call` storms, runaway agent loops, credential stuffing on OAuth endpoints, and oversized upload attempts. Without **rate limits**, **quotas**, and **priority shedding**, a single noisy tenant can degrade others on shared infrastructure.

## Scenario

- **Shared gateway** fronts many developer hosts for the same enterprise.
- **Attacker or buggy agent** issues high-frequency MCP requests or opens many parallel streams.
- **Potential impact:** availability loss, cost spikes on metered model APIs, incident noise masking real attacks.

## Test Objectives

- Verify per-identity and per-tenant limits exist (not only global IP limits).
- Verify **429/503**-style behavior is consistent and includes **Retry-After** or typed backoff hints where applicable.
- Verify **allowlists** for break-glass admin paths cannot be abused anonymously.

## Preconditions

- Written approval for **bounded** load tests; start far below production SLO ceilings.
- Metrics dashboards for gateway and MCP server latency/error rates.

## How to Test

### 1. Manual Review

Read rate-limit policy: dimensions (user id, API key, workspace id), burst vs sustained, and exemptions.

### 2. Configuration Review

Confirm limits apply to **MCP JSON-RPC methods** separately from static asset routes if co-hosted.

### 3. Runtime Testing

1. Send steady low-rate traffic—baseline success.
2. Gradually increase **within agreed cap** until throttling triggers—record threshold versus documentation.
3. Back off and confirm recovery without manual restart (circuit closes).

### 4. Abuse Case Testing

- Parallel identical `tools/call` with tiny arguments—identify fan-out amplification.
- Slowloris-style slow uploads **only** if explicitly in scope and isolated to lab listeners.

### 5. Log and Detection Review

**Detection:** throttled events include principal, rule id, and remaining quota if safe to expose internally.

## Test Data / Example Payloads

Use synthetic tool names and constant small payloads to isolate rate effects from payload size (`MCPSTG-TRNS-03`).

## Expected Results

- **Secure:** fair throttling; no unbounded queues; alerts on sustained limit breaches.
- **Insecure:** single client can OOM workers; limits only by IP missing user dimension; errors leak stack traces.
- **Evidence:** metrics screenshots, rule identifiers, before/after latency samples.

## Remediation

- Multi-dimensional quotas; adaptive throttling; per-tool cost weights.
- Host-side planner caps on steps per minute (`MCPSTG-ABUS-01`).
- Chaos tests for gateway failure modes.

## Tools

Load testing utilities (lab), gateway metrics, log-based anomaly detection.

## References

- OWASP API Security Top 10: API04 Lack of Resources & Rate Limiting.
- CWE-770: Allocation of Resources Without Limits or Throttling

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: LLM10 Unbounded Consumption (when abuse drives model/API cost)
- OWASP API Security Top 10: API04
- OWASP ASVS: V11
- MCP specification (versioned): N/A; deployment control
- CWE: CWE-770
- MITRE ATLAS: `N/A`
- Risk level: Medium
- Testing type: Hybrid
