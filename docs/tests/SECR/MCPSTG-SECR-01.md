# Test Secrets in Server Configuration and Environment Exposure

ID: MCPSTG-SECR-01

## Summary

MCP servers frequently read **API keys, client secrets, and database URLs** from environment variables or flat config files. Those values can leak through **process listings**, **core dumps**, **error pages**, **telemetry**, or **exported diagnostics** bundles. Because tools often echo arguments or environment for “debugging,” secret hygiene is a first-class MCP test—not only a traditional server hardening afterthought.

## Scenario

- **MCP server** loads `DATABASE_URL` and a SaaS API key from `.env` next to the workspace.
- **Tool** `<TEST_TOOL_NAME>_debug_env` (if present) or verbose logging prints effective configuration on failure.
- **Attacker position:** Local user on shared CI runner; compromised backup; insider with read access to repo + env files.
- **Potential impact:** Credential theft enabling data exfiltration or lateral movement.

## Test Objectives

- Verify secrets are **not** in repository-tracked files; verify secret injection via vault or host-managed secret store where required.
- Verify tools cannot read arbitrary environment unless explicitly scoped.
- Verify crash paths and `--help` output do not print secrets.

## Preconditions

- **Fake** secrets only (see [appendix-d-lab-fixtures.md](../../docs/appendix-d-lab-fixtures.md)).
- Permission to scan repo and container image layers in lab.

## How to Test

### 1. Manual Review

Inventory all secret-bearing variables. Map which tools and resource providers read them.

### 2. Configuration Review

- Search for `.env` in VCS history (use `git log -- .env` patterns in a **copy** of the repo).
- Inspect container `ENV` directives and Kubernetes secrets mounting modes (tmpfs vs world-readable volumes).

### 3. Runtime Testing

1. Trigger a **controlled** error path (invalid but non-prod dependency) and capture stderr—verify no secret substrings.
2. Invoke any diagnostic tool with benign flags—verify no full environment dump.

### 4. Abuse Case Testing

- Attempt to read `/proc/self/environ` via a file-reading tool if such a tool exists—expect deny outside explicit debug profiles.

### 5. Log and Detection Review

**Detection:** secret scanners on CI; alerts on high-entropy strings in application logs; policy denying `export` style debug endpoints in production.

## Test Data / Example Payloads

Synthetic only:

```text
FAKE_DATABASE_URL=postgres://lab:fake@localhost:5432/mcpstg
```

## Expected Results

- **Secure:** secrets sourced from managed stores; redacted logs; tools lack ambient env read.
- **Insecure:** secrets in git, world-readable `.env`, or log lines containing API key material.
- **Evidence:** scanner report hashes, redacted log excerpts, config diff.

## Remediation

- Remove secrets from repos; use short-lived credentials; rotate on exposure.
- Drop environment inheritance for tool subprocesses; pass explicit minimal env maps.
- Add regression tests for error formatting (`MCPSTG-CONF-03`).

## Tools

- Secret scanning (gitleaks, trufflehog, vendor equivalents), container image scanners, structured log redaction validators.

## References

- OWASP ASVS: V14 Configuration, V7 Error Handling, V8 Data Protection.
- CWE-497: Exposure of System Data to an Unauthorized Control Sphere
- CWE-200: Exposure of Sensitive Information to an Unauthorized Actor

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: `N/A` unless secrets surface in model context
- OWASP API Security Top 10: API03 Broken Object Property Exposure (analog)
- OWASP ASVS: V7, V8, V14
- MCP specification (versioned): N/A; server implementation
- CWE: CWE-200, CWE-497
- MITRE ATLAS: `N/A`
- Risk level: Critical
- Testing type: Hybrid
