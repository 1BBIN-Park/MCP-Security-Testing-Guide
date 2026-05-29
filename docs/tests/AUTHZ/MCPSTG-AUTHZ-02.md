# Test Bypassing User Approval

ID: MCPSTG-AUTHZ-02

## Summary

Many hosts add **approval dialogs** before high-risk tools run. Bypasses include **UI deception** (summary differs from real arguments), **race conditions** (arguments swapped after approval), **duplicate tool names**, or **alternate code paths** (debug flags, “fast mode”) that skip checks. This test validates that approval is **cryptographically or structurally bound** to the exact operation, not a best-effort UX hint.

## Scenario

- **Host:** Shows “Allow read file?” while passing different paths to the server.
- **MCP server:** Accepts final arguments from the client without re-validation.
- **Attacker position:** Malicious server or compromised client plugin performing argument substitution.
- **Potential impact:** Users click “Allow” for benign wording but enable destructive actions.

## Test Objectives

- Verify approved arguments **match** executed arguments byte-for-byte where feasible.
- Verify no **shadow interfaces** skip approvals (CLI flags, developer menus).
- Verify **secure** logging ties approval tokens to argument hashes.

## Preconditions

- Lab build with approval UI enabled.
- Ability to capture client→server MCP messages (lab consent).

## How to Test

### 1. Manual Review

Read product docs for approval guarantees; list known limitations.

### 2. Configuration Review

Search configs for `skipApproval`, `dangerouslySkip`, `devMode`, etc.

### 3. Runtime Testing

1. Trigger approval for `<TEST_TOOL_NAME>_echo` with argument `A`.
2. If tooling allows, attempt to **mutate pending call** to argument `B` before execution (simulated race in lab harness).
3. Observe whether server rejects mismatch.

### 4. Abuse Case Testing

- Extremely long argument strings that truncate in UI but not on wire.
- Unicode homoglyphs in paths displayed to users.

### 5. Log and Detection Review

**Detection:** approval records should store argument hash, tool version, and user decision timestamp.

## Test Data / Example Payloads

```json
{ "msg": "DISPLAYED_SHORT", "payload": "ACTUAL_LONG_LAB_TOKEN_abcdef" }
```

UI must show full structured payload or an explicit “expand details” path.

## Expected Results

- **Secure:** mismatch aborts; UI cannot hide critical fields; no silent skip flags in prod.
- **Insecure:** execution proceeds with altered args; logs lack binding.
- **Evidence:** diff of approved vs executed payload from lab capture.

## Remediation

- Bind approvals to **canonical JSON** hashes signed by the host.
- Server-side **re-validation** of arguments against policy after approval token presentation.
- Remove or hard-gate developer shortcuts in production builds.

## Tools

- MCP message capture (lab), UI accessibility inspection for hidden fields, binary diff utilities.

## References

- OWASP ASVS: V4 Access Control.
- CWE-358: Improperly Implemented Security Check for Standard
- CWE-451: User Interface (UI) Misrepresentation of Critical Information

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: LLM06 / LLM04 (insecure UI trust—use if credible)
- OWASP API Security Top 10: API5 Broken Function Level Authorization (analog)
- OWASP ASVS: V4
- MCP specification (versioned): client responsibilities are implementation-specific
- CWE: CWE-358, CWE-451
- MITRE ATLAS: `N/A`
- Risk level: Critical
- Testing type: Hybrid
