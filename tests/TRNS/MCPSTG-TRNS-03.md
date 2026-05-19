# Test Message Size Limits and Timeouts Under Load

ID: MCPSTG-TRNS-03

## Summary

MCP sessions can carry **large tool results**, **big resource reads**, or **verbose logging** embedded in JSON-RPC payloads. Without **maximum message size**, **stream backpressure**, and **timeouts**, servers become fragile under abuse or accidental “runaway” model outputs. This is availability and sometimes confidentiality (crash-induced error pages, partial writes).

## Scenario

- **Host + model** return a multi-megabyte tool payload (logs, file dumps) in a single response.
- **Attacker or buggy tool** sends an oversized argument blob or floods parallel `tools/call` requests.
- **Potential impact:** process OOM, thread pool exhaustion, cascading failures in shared gateways, inflated egress costs.

## Test Objectives

- Verify hard and soft limits on **request and response** sizes at client, server, and gateway.
- Verify **timeouts** for idle streams, slow clients, and hung tool executions.
- Verify **graceful** rejection (typed error) rather than opaque crashes.

## Preconditions

- Lab-only load driver permitted in scope (low concurrency first).
- Monitoring for CPU, memory, and open connections on MCP server and gateway.

## How to Test

### 1. Manual Review

Read limits documentation: defaults, overrides, and whether limits differ for stdio vs HTTP.

### 2. Configuration Review

Inspect gateway `max_body_size`, server read buffers, client timeouts, and tool-specific caps (for example “max bytes read from file tool”).

### 3. Runtime Testing

1. Send a **just-below-limit** synthetic payload and confirm success.
2. Send a **just-above-limit** payload—expect HTTP 413 or protocol-specific error without server crash.
3. Open a connection and **stall** sending mid-message beyond idle timeout—expect disconnect and cleanup.

### 4. Abuse Case Testing

- Bounded parallel tool calls (N small calls), stepping N upward until latency budgets break—stop before harming shared infrastructure.
- Very long-lived SSE/WebSocket streams: verify heartbeat and max duration.

### 5. Log and Detection Review

**Detection:** rate-limit hits, timeout reasons, and payload size rejections should appear in metrics with MCP method names.

## Test Data / Example Payloads

Generate in-lab random base64 blobs of known sizes (for example 512 KiB, 2 MiB, 8 MiB) **without** compressing secrets into them.

## Expected Results

- **Secure:** limits enforced with clear errors; no sustained memory growth; connections closed cleanly.
- **Insecure:** worker crash, gateway 502s to unrelated tenants, or silent truncation that corrupts JSON framing.
- **Evidence:** metric charts, redacted error payloads, versioned config snippets.

## Remediation

- Enforce layered limits: edge, MCP server, tool runtime.
- Stream large artifacts to object storage with signed URLs instead of inline MCP messages where appropriate.
- Add circuit breakers and per-principal concurrency caps (`MCPSTG-ABUS-01`).

## Tools

Load generators in lab, observability stacks, `curl`/`h2load` with size-controlled bodies where permitted.

## References

- OWASP ASVS: V11 Denial of Service (verification concepts).
- CWE-400: Uncontrolled Resource Consumption
- CWE-770: Allocation of Resources Without Limits or Throttling

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: `N/A` unless framed as availability for agent loops
- OWASP API Security Top 10: API04 (lack of resources / rate limiting analog)
- OWASP ASVS: V11
- MCP specification (versioned): framing and streaming behavior as implemented
- CWE: CWE-400, CWE-770
- MITRE ATLAS: `N/A`
- Risk level: Medium
- Testing type: Hybrid
