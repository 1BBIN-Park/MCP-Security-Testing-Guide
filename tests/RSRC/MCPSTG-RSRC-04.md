# Test Secret Leakage Through Resources

ID: MCPSTG-RSRC-04

## Summary

MCP **resources** are a convenient way to expose files, URLs, and database views to models. If resource providers do not enforce **authorization**, **path confinement**, or **redaction**, secrets and customer data can enter the model context and then leak through **tool outputs**, **logs**, or **downstream telemetry**. Resources feel “read-only,” but read access at scale is still exfiltration.

## Scenario

- **MCP server:** Serves `file://` or workspace-backed resources under `<TEST_WORKSPACE>`.
- **Attacker position:** Malicious PR adds a symlink or moves a `.env` file into an indexed folder; or a confused deputy exposes `/secrets/` via a overly broad glob.
- **Potential impact:** Credential disclosure, PII in transcripts, regulatory breach.

## Test Objectives

- Verify resources cannot read **outside** the declared workspace root without explicit policy.
- Verify sensitive filenames and content are **blocked or redacted** before model consumption.
- Verify **logging** does not persist full secret values when resources are fetched.

## Preconditions

- Lab workspace containing **fake** secrets in `secrets/` per [appendix-d-lab-fixtures.md](../../docs/appendix-d-lab-fixtures.md).
- Ability to list resource URIs exposed by the server.

## How to Test

### 1. Manual Review

Enumerate all resource templates in code (glob patterns, SQL views). Look for dynamic path joins.

### 2. Configuration Review

Check read ACLs on directories exposed as resources; verify `.git`, `.ssh`, cloud credential files are excluded by default.

### 3. Runtime Testing

1. Request `<TEST_RESOURCE>` variants that try **path traversal** using benign filenames only (see `MCPSTG-INPV-02`).
2. Attempt to register a resource URI pointing at `secrets/fake.env`—expect **deny** or redaction.

### 4. Abuse Case Testing

- Large file reads that might contain embedded API keys in comments (synthetic files only).

### 5. Log and Detection Review

**Detection:** log lines for resource fetch should include **URI class** and **allow/deny** without echoing secret material.

## Test Data / Example Payloads

Synthetic secret line:

```text
FAKE_API_KEY=mcpstg-lab-deadbeef-0000
```

Resource path attempts (lab):

- `resource://workspace/<TEST_WORKSPACE>/readonly/benign.md` — expect allow.
- `resource://workspace/<TEST_WORKSPACE>/secrets/fake.env` — expect deny.

## Expected Results

- **Secure:** traversal blocked; sensitive paths denied; redaction middleware strips patterns.
- **Insecure:** model receives raw keys; logs store full file body.
- **Evidence:** redacted transcript, policy config, server audit lines.

## Remediation

- Implement **chroot-style** roots for file resources; canonicalize paths; deny symlinks crossing roots.
- Add secret scanners in CI on docs and fixture trees.
- Minimize what hosts **persist** from resource reads into memory (see `MCPSTG-CTX-02`).

## Tools

- Static analysis for path operations, secret scanners (lab repos), structured log review.

## References

- OWASP ASVS: V14 Configuration, V8 Data Protection.
- CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
- CWE-200: Exposure of Sensitive Information to an Unauthorized Actor

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: LLM02 Insecure Output Handling (secondary), LLM06 if model exfiltrates
- OWASP API Security Top 10: API1, API3 (object/property exposure analogs)
- OWASP ASVS: V8, V14
- MCP specification (versioned): resources as implemented
- CWE: CWE-22, CWE-200
- MITRE ATLAS: `N/A`
- Risk level: Critical
- Testing type: Hybrid
