# Test Token Storage and Rotation Behavior on the Host

ID: MCPSTG-SECR-02

## Summary

MCP hosts often store **OAuth access tokens**, **refresh tokens**, and **API keys** for upstream tools. Weaknesses include **plaintext** OS keychains, shared profiles on multi-user machines, missing **rotation** after scope changes, and tokens persisted in **world-readable** cache files. Attackers with local malware or physical access may exfiltrate these assets without attacking the MCP server at all.

## Scenario

- **Host** caches OAuth tokens for `<TEST_USER>` to call `<AUTHORIZED_LAB_SERVER>` tools.
- **Attacker position:** Malware running as the same user; forensic analyst with disk image; backup system that copies the cache directory.
- **Potential impact:** Long-lived refresh token theft; silent re-authorization to broader scopes.

## Test Objectives

- Verify storage uses **OS-protected** credential APIs where available; verify file permissions on any fallback cache.
- Verify **refresh** and **revocation** events update or invalidate local material.
- Verify **scope changes** require user-visible re-consent, not silent merges.

## Preconditions

- Lab IdP or mock OAuth server supporting revoke endpoint.
- Access to host filesystem or configuration export APIs under authorization.

## How to Test

### 1. Manual Review

Read vendor documentation for token storage location, encryption at rest, and multi-profile isolation.

### 2. Configuration Review

Locate on-disk paths; check POSIX ACLs or Windows DACLs. Confirm backups exclude token stores or encrypt them.

### 3. Runtime Testing

1. Authenticate in lab; record file metadata (not contents) for cache files.
2. Revoke refresh token at IdP; run MCP operations—expect **re-auth** prompt or clean failure, not stale success.
3. Change granted scopes in IdP; verify host detects mismatch and does not silently widen access.

### 4. Abuse Case Testing

- Secondary OS account on shared machine attempts to read another user’s home directory token path—expect OS deny.

### 5. Log and Detection Review

**Detection:** host logs token acquisition and refresh events without printing raw tokens (hash or last-4 only if needed).

## Test Data / Example Payloads

Use IdP test clients with **non-production** tenants and synthetic redirect URIs registered only for lab.

## Expected Results

- **Secure:** least-privilege storage; revocation works; logs redact secrets.
- **Insecure:** tokens in sqlite/plain JSON world-readable; revocation ignored until manual cache delete.
- **Evidence:** permission listings, redacted logs, IdP audit of revoke vs host behavior.

## Remediation

- Prefer OS keychain / secure enclave integrations; encrypt any at-rest cache with user-specific keys.
- Short-lived access tokens; rotate refresh tokens; bind tokens to device posture where enterprise policy requires it.

## Tools

- Filesystem permission audits, IdP admin consoles (lab), host debug APIs if sanctioned.

## References

- OWASP ASVS: V2 Authentication, V3 Session Management, V8 Data Protection.
- OWASP API Security Top 10: API2 Authentication Failures.
- CWE-522: Insufficiently Protected Credentials

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: `N/A`
- OWASP API Security Top 10: API02
- OWASP ASVS: V2, V3, V8
- MCP specification (versioned): authorization extensions you use (cite version)
- CWE: CWE-522
- MITRE ATLAS: `N/A`
- Risk level: High
- Testing type: Manual
