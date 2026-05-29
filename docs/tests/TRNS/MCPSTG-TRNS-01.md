# Test TLS Configuration and Certificate Validation

ID: MCPSTG-TRNS-01

## Summary

Remote MCP transports rely on TLS for confidentiality and integrity between **client** and **server**. Weak cipher suites, missing certificate validation, or mis-terminated TLS at an untrusted hop exposes tokens, tool arguments, and resource payloads. MCP deployments often sit behind reverse proxies; misconfiguration there becomes part of the MCP trust boundary.

## Scenario

- **MCP host/client:** Connects to a remote MCP endpoint over HTTPS.
- **Infrastructure:** TLS terminates at a load balancer; backend may be plaintext on a private network.
- **Attacker position:** Network observer on untrusted Wi‑Fi path to public endpoint; or compromised proxy in a misconfigured enterprise path.
- **Potential impact:** Credential theft, session hijack, undetected tampering with tool definitions in transit.

## Test Objectives

- Verify **TLS versions**, **cipher strength**, and **certificate chain validation** meet organizational baselines.
- Verify **SNI** and **hostname** validation align with the MCP server identity.
- Identify **insecure** patterns: cert pinning disabled globally, `insecureSkipVerify`-style flags, mixed content downgrades.

## Preconditions

- Authorized test against **lab** MCP HTTPS endpoint (not customer production).
- Permission to run TLS assessment tooling from an approved scanner host.
- Access to proxy/load balancer configuration (redacted).

## How to Test

### 1. Manual Review

Read deployment docs for TLS termination points and which component validates client certificates (if mTLS is claimed).

### 2. Configuration Review

Inspect server and proxy configs for deprecated protocols (TLS 1.0/1.1), weak DH parameters, and permissive trust stores shipping private roots without justification.

### 3. Runtime Testing

1. Connect with a known-good client and capture negotiated TLS version/cipher via approved SSL scanning (lab scope).
2. Attempt **hostname mismatch** using a valid certificate for a different name—expect **failure**.
3. If mTLS is required, attempt connection **without** client cert—expect **failure**.

### 4. Abuse Case Testing

- Certificate expiry near-miss: deploy short-lived lab cert and verify renewal alarms (process test).
- Revocation behavior: document whether stapled OCSP/CRL checks are enforced (design documentation acceptable if live revocation tests are disallowed).

### 5. Log and Detection Review

**Detection:** TLS handshake failures, cert validation errors, and proxy anomalies should be logged with client identity where available.

## Test Data / Example Payloads

Use scanner profiles restricted to `<AUTHORIZED_LAB_SERVER>` hostnames only.

## Expected Results

- **Secure:** TLS 1.2+ with modern ciphers; strict hostname validation; no silent bypass flags in production paths.
- **Insecure:** handshake succeeds with obsolete ciphers; tool traffic readable on the wire in lab capture.
- **Evidence:** redacted scan summary, config snippets with secrets removed.

## Remediation

- Enforce TLS 1.2+ and modern cipher suites at the edge; automate cert lifecycle.
- Avoid `insecureSkipVerify` in production builds; isolate debug builds.
- Document trust store ownership and change control.

## Tools

- Approved TLS scanners, `openssl s_client` in lab, cloud provider TLS policy dashboards.

## References

- OWASP Web Security Testing Guide (structure inspiration only).
- OWASP ASVS: V9 Communications (TLS-related verification).
- CWE-295: Improper Certificate Validation
- CWE-326: Inadequate Encryption Strength

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: `N/A` (transport layer)
- OWASP API Security Top 10: API2 Authentication Failures (when tokens ride the channel)
- OWASP ASVS: V9
- MCP specification (versioned): remote transport security as implemented by your stack
- CWE: CWE-295, CWE-326
- MITRE ATLAS: `N/A`
- Risk level: High
- Testing type: Hybrid
