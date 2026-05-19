# 4. MCP Security Testing

This chapter is the **MCP equivalent of OWASP WSTG Chapter 4 (Web Application Security Testing)**. Every procedure is a discrete markdown file under [`tests/`](../tests/). The machine-readable catalog is [`index.json`](../index.json).

**How to run tests:** open a test link below, follow its **How to Test** sections in an authorized lab, and report results per [Chapter 5 — Reporting](05-reporting.md).

---

## Governance note: “OWASP MCP Top 10” mapping

Some communities publish MCP-focused risk lists. **If** your organization adopts a specific “MCP Top 10” or similar document, cite it by name and version in each test’s Mapping section.

If no stable list is adopted, use **`N/A`** for that column and rely on **OWASP LLM Top 10**, **OWASP API Security Top 10**, **ASVS**, **CWE**, and **MITRE ATLAS** where mappings are credible. Do not invent false mappings for completeness.

---

## Guide table of contents

1. [Frontispiece](01-frontispiece.md)
2. [Introduction](02-introduction.md)
3. [The MCP Security Testing Framework](03-mcp-security-testing-framework.md)
4. **MCP Security Testing** (this chapter → [`tests/`](../tests/))
5. [Reporting](05-reporting.md)

**Appendices:** [A](appendix-a-glossary.md) · [B](appendix-b-scenarios.md) · [C](appendix-c-evidence-checklist.md) · [D](appendix-d-lab-fixtures.md) · [E](appendix-e-suggested-reading.md) · [F](appendix-f-testing-tools.md)

---

## Test ID taxonomy

| Prefix | Category | Focus |
|--------|----------|--------|
| `MCPSTG-INFO` | Information Gathering | Inventory, enumeration, trust boundaries |
| `MCPSTG-CONF` | Configuration and Deployment | Hardening, debug modes, permissions, transport config |
| `MCPSTG-AUTHN` | Identity and Authentication | Missing authn, tokens, credential reuse |
| `MCPSTG-AUTHZ` | Authorization and Permission | Least privilege, approvals, cross-user access |
| `MCPSTG-TOOL` | Tool Security | Descriptions, execution, injection, chaining |
| `MCPSTG-RSRC` | Resource and Data Access | Sensitive files, enumeration, secrets via resources |
| `MCPSTG-PRMT` | Prompt and Instruction | Direct/indirect injection, hierarchy conflicts |
| `MCPSTG-CTX` | Context and Memory | Over-sharing, poisoning, session confusion |
| `MCPSTG-AGNT` | Agentic Workflow | Agency, retries, goal manipulation |
| `MCPSTG-INPV` | Input Validation | Parameters, traversal, JSON/schema confusion |
| `MCPSTG-OUTV` | Output Handling | Unsafe rendering, sensitive tool output |
| `MCPSTG-LOG` | Logging and Detection | Audit trails, detection coverage |
| `MCPSTG-SUPP` | Supply Chain | Provenance, registries, updates |
| `MCPSTG-GOV` | Enterprise Governance | Inventory, policy, compliance evidence |
| `MCPSTG-TRNS` | Transport and Channel | TLS, binding, limits, timeouts |
| `MCPSTG-GW` | Gateway and Egress | Allowlists, SSRF controls, throttling |
| `MCPSTG-SECR` | Secrets and Credentials | Storage, rotation, log redaction |
| `MCPSTG-ABUS` | Resilience and Abuse | Storms, retries, cost abuse |
| `MCPSTG-PRVC` | Privacy and Retention | PII minimization, log retention, tenancy |

**Numbering rule:** each prefix uses two-digit numbers starting at `01`. New tests append the next free number for that prefix.

**INPV vs OUTV rule:** input-focused tests use `INPV`; output-focused tests use `OUTV`. They are separate subcategories with separate prefixes (no mixed prefix in a single file).

---

## Category to test ID matrix

| Category | Test IDs |
|----------|----------|
| INFO | `MCPSTG-INFO-01`, `MCPSTG-INFO-02`, `MCPSTG-INFO-03`, `MCPSTG-INFO-04`, `MCPSTG-INFO-05` |
| CONF | `MCPSTG-CONF-01`, `MCPSTG-CONF-02`, `MCPSTG-CONF-03`, `MCPSTG-CONF-04`, `MCPSTG-CONF-05` |
| AUTHN | `MCPSTG-AUTHN-01`, `MCPSTG-AUTHN-02`, `MCPSTG-AUTHN-03`, `MCPSTG-AUTHN-04` |
| AUTHZ | `MCPSTG-AUTHZ-01`, `MCPSTG-AUTHZ-02`, `MCPSTG-AUTHZ-03`, `MCPSTG-AUTHZ-04`, `MCPSTG-AUTHZ-05` |
| TOOL | `MCPSTG-TOOL-01`, `MCPSTG-TOOL-02`, `MCPSTG-TOOL-03`, `MCPSTG-TOOL-04`, `MCPSTG-TOOL-05`, `MCPSTG-TOOL-06` |
| RSRC | `MCPSTG-RSRC-01`, `MCPSTG-RSRC-02`, `MCPSTG-RSRC-03`, `MCPSTG-RSRC-04`, `MCPSTG-RSRC-05` |
| PRMT | `MCPSTG-PRMT-01`, `MCPSTG-PRMT-02`, `MCPSTG-PRMT-03`, `MCPSTG-PRMT-04`, `MCPSTG-PRMT-05` |
| CTX | `MCPSTG-CTX-01`, `MCPSTG-CTX-02`, `MCPSTG-CTX-03`, `MCPSTG-CTX-04`, `MCPSTG-CTX-05` |
| AGNT | `MCPSTG-AGNT-01`, `MCPSTG-AGNT-02`, `MCPSTG-AGNT-03`, `MCPSTG-AGNT-04`, `MCPSTG-AGNT-05` |
| INPV | `MCPSTG-INPV-01`, `MCPSTG-INPV-02`, `MCPSTG-INPV-03` |
| OUTV | `MCPSTG-OUTV-01`, `MCPSTG-OUTV-02` |
| LOG | `MCPSTG-LOG-01`, `MCPSTG-LOG-02`, `MCPSTG-LOG-03`, `MCPSTG-LOG-04`, `MCPSTG-LOG-05` |
| SUPP | `MCPSTG-SUPP-01`, `MCPSTG-SUPP-02`, `MCPSTG-SUPP-03`, `MCPSTG-SUPP-04`, `MCPSTG-SUPP-05` |
| GOV | `MCPSTG-GOV-01`, `MCPSTG-GOV-02`, `MCPSTG-GOV-03`, `MCPSTG-GOV-04`, `MCPSTG-GOV-05` |
| TRNS | `MCPSTG-TRNS-01`, `MCPSTG-TRNS-02`, `MCPSTG-TRNS-03` |
| GW | `MCPSTG-GW-01`, `MCPSTG-GW-02`, `MCPSTG-GW-03` |
| SECR | `MCPSTG-SECR-01`, `MCPSTG-SECR-02`, `MCPSTG-SECR-03` |
| ABUS | `MCPSTG-ABUS-01`, `MCPSTG-ABUS-02` |
| PRVC | `MCPSTG-PRVC-01`, `MCPSTG-PRVC-02`, `MCPSTG-PRVC-03` |

---

# Test cases by category

## 4.1 Information Gathering (`INFO`)

Folder: [`tests/INFO/`](../tests/INFO/)

- [MCPSTG-INFO-01 — Identify MCP Servers and Clients](../tests/INFO/MCPSTG-INFO-01.md)
- [MCPSTG-INFO-02 — Enumerate Exposed Tools](../tests/INFO/MCPSTG-INFO-02.md)
- [MCPSTG-INFO-03 — Identify MCP Resources and Data Sources](../tests/INFO/MCPSTG-INFO-03.md)
- [MCPSTG-INFO-04 — Map MCP Trust Boundaries](../tests/INFO/MCPSTG-INFO-04.md)
- [MCPSTG-INFO-05 — Identify Sensitive Context Flows](../tests/INFO/MCPSTG-INFO-05.md)

## 4.2 Configuration and Deployment Management (`CONF`)

Folder: [`tests/CONF/`](../tests/CONF/)

- [MCPSTG-CONF-01 — Test MCP Server Configuration](../tests/CONF/MCPSTG-CONF-01.md)
- [MCPSTG-CONF-02 — Test Insecure Local Server Exposure](../tests/CONF/MCPSTG-CONF-02.md)
- [MCPSTG-CONF-03 — Test Debug Mode and Verbose Errors](../tests/CONF/MCPSTG-CONF-03.md)
- [MCPSTG-CONF-04 — Test File and Workspace Permissions](../tests/CONF/MCPSTG-CONF-04.md)
- [MCPSTG-CONF-05 — Test Unsafe Transport Configuration](../tests/CONF/MCPSTG-CONF-05.md)

## 4.3 Identity and Authentication (`AUTHN`)

Folder: [`tests/AUTHN/`](../tests/AUTHN/)

- [MCPSTG-AUTHN-01 — Test Missing Authentication on MCP Server](../tests/AUTHN/MCPSTG-AUTHN-01.md)
- [MCPSTG-AUTHN-02 — Test Weak Token Handling](../tests/AUTHN/MCPSTG-AUTHN-02.md)
- [MCPSTG-AUTHN-03 — Test Credential Reuse Across Tools](../tests/AUTHN/MCPSTG-AUTHN-03.md)
- [MCPSTG-AUTHN-04 — Test Expired or Revoked Token Acceptance](../tests/AUTHN/MCPSTG-AUTHN-04.md)

## 4.4 Authorization and Permission (`AUTHZ`)

Folder: [`tests/AUTHZ/`](../tests/AUTHZ/)

- [MCPSTG-AUTHZ-01 — Test Excessive Tool Permissions](../tests/AUTHZ/MCPSTG-AUTHZ-01.md)
- [MCPSTG-AUTHZ-02 — Test Bypassing User Approval](../tests/AUTHZ/MCPSTG-AUTHZ-02.md)
- [MCPSTG-AUTHZ-03 — Test Cross-User Resource Access](../tests/AUTHZ/MCPSTG-AUTHZ-03.md)
- [MCPSTG-AUTHZ-04 — Test Privilege Escalation Through Tool Chaining](../tests/AUTHZ/MCPSTG-AUTHZ-04.md)
- [MCPSTG-AUTHZ-05 — Test Workspace Boundary Escape](../tests/AUTHZ/MCPSTG-AUTHZ-05.md)

## 4.5 Tool Security (`TOOL`)

Folder: [`tests/TOOL/`](../tests/TOOL/)

- [MCPSTG-TOOL-01 — Test Tool Description Poisoning](../tests/TOOL/MCPSTG-TOOL-01.md)
- [MCPSTG-TOOL-02 — Test Unsafe Tool Execution](../tests/TOOL/MCPSTG-TOOL-02.md)
- [MCPSTG-TOOL-03 — Test Command Injection in Tool Parameters](../tests/TOOL/MCPSTG-TOOL-03.md)
- [MCPSTG-TOOL-04 — Test Tool Schema Manipulation](../tests/TOOL/MCPSTG-TOOL-04.md)
- [MCPSTG-TOOL-05 — Test Dangerous Tool Chaining](../tests/TOOL/MCPSTG-TOOL-05.md)
- [MCPSTG-TOOL-06 — Test Human Approval for High-Risk Tools](../tests/TOOL/MCPSTG-TOOL-06.md)

## 4.6 Resource and Data Access (`RSRC`)

Folder: [`tests/RSRC/`](../tests/RSRC/)

- [MCPSTG-RSRC-01 — Test Sensitive Resource Exposure](../tests/RSRC/MCPSTG-RSRC-01.md)
- [MCPSTG-RSRC-02 — Test Resource Enumeration](../tests/RSRC/MCPSTG-RSRC-02.md)
- [MCPSTG-RSRC-03 — Test Cross-Workspace Data Access](../tests/RSRC/MCPSTG-RSRC-03.md)
- [MCPSTG-RSRC-04 — Test Secret Leakage Through Resources](../tests/RSRC/MCPSTG-RSRC-04.md)
- [MCPSTG-RSRC-05 — Test Unauthorized File Access](../tests/RSRC/MCPSTG-RSRC-05.md)

## 4.7 Prompt and Instruction Security (`PRMT`)

Folder: [`tests/PRMT/`](../tests/PRMT/)

- [MCPSTG-PRMT-01 — Test Direct Prompt Injection](../tests/PRMT/MCPSTG-PRMT-01.md)
- [MCPSTG-PRMT-02 — Test Indirect Prompt Injection Through Resources](../tests/PRMT/MCPSTG-PRMT-02.md)
- [MCPSTG-PRMT-03 — Test Tool Instruction Override](../tests/PRMT/MCPSTG-PRMT-03.md)
- [MCPSTG-PRMT-04 — Test Hidden Instruction Leakage](../tests/PRMT/MCPSTG-PRMT-04.md)
- [MCPSTG-PRMT-05 — Test Prompt Template Manipulation](../tests/PRMT/MCPSTG-PRMT-05.md)

## 4.8 Context and Memory (`CTX`)

Folder: [`tests/CTX/`](../tests/CTX/)

- [MCPSTG-CTX-01 — Test Context Over-Sharing](../tests/CTX/MCPSTG-CTX-01.md)
- [MCPSTG-CTX-02 — Test Memory Poisoning](../tests/CTX/MCPSTG-CTX-02.md)
- [MCPSTG-CTX-03 — Test Sensitive Context Leakage](../tests/CTX/MCPSTG-CTX-03.md)
- [MCPSTG-CTX-04 — Test Cross-Session Context Confusion](../tests/CTX/MCPSTG-CTX-04.md)
- [MCPSTG-CTX-05 — Test Untrusted Context Prioritization](../tests/CTX/MCPSTG-CTX-05.md)

## 4.9 Agentic Workflow and Business Logic (`AGNT`)

Folder: [`tests/AGNT/`](../tests/AGNT/)

- [MCPSTG-AGNT-01 — Test Excessive Agency](../tests/AGNT/MCPSTG-AGNT-01.md)
- [MCPSTG-AGNT-02 — Test Unsafe Autonomous Actions](../tests/AGNT/MCPSTG-AGNT-02.md)
- [MCPSTG-AGNT-03 — Test Approval Bypass in Multi-Step Workflows](../tests/AGNT/MCPSTG-AGNT-03.md)
- [MCPSTG-AGNT-04 — Test Goal Manipulation](../tests/AGNT/MCPSTG-AGNT-04.md)
- [MCPSTG-AGNT-05 — Test Unsafe Retry and Loop Behavior](../tests/AGNT/MCPSTG-AGNT-05.md)

## 4.10 Input Validation (`INPV`)

Folder: [`tests/INPV/`](../tests/INPV/)

- [MCPSTG-INPV-01 — Test Input Validation for Tool Parameters](../tests/INPV/MCPSTG-INPV-01.md)
- [MCPSTG-INPV-02 — Test Path Traversal in Tool Inputs](../tests/INPV/MCPSTG-INPV-02.md)
- [MCPSTG-INPV-03 — Test JSON and Schema Confusion](../tests/INPV/MCPSTG-INPV-03.md)

## 4.11 Output Handling (`OUTV`)

Folder: [`tests/OUTV/`](../tests/OUTV/)

- [MCPSTG-OUTV-01 — Test Unsafe Output Rendering](../tests/OUTV/MCPSTG-OUTV-01.md)
- [MCPSTG-OUTV-02 — Test Sensitive Data in Tool Output](../tests/OUTV/MCPSTG-OUTV-02.md)

## 4.12 Logging, Monitoring, and Detection (`LOG`)

Folder: [`tests/LOG/`](../tests/LOG/)

- [MCPSTG-LOG-01 — Test Tool Call Logging](../tests/LOG/MCPSTG-LOG-01.md)
- [MCPSTG-LOG-02 — Test User Approval Audit Logs](../tests/LOG/MCPSTG-LOG-02.md)
- [MCPSTG-LOG-03 — Test Detection of Prompt Injection Attempts](../tests/LOG/MCPSTG-LOG-03.md)
- [MCPSTG-LOG-04 — Test Secret Exposure Logging](../tests/LOG/MCPSTG-LOG-04.md)
- [MCPSTG-LOG-05 — Test Incident Reconstruction](../tests/LOG/MCPSTG-LOG-05.md)

## 4.13 Supply Chain and Dependency (`SUPP`)

Folder: [`tests/SUPP/`](../tests/SUPP/)

- [MCPSTG-SUPP-01 — Test MCP Server Provenance](../tests/SUPP/MCPSTG-SUPP-01.md)
- [MCPSTG-SUPP-02 — Test Dependency Vulnerabilities](../tests/SUPP/MCPSTG-SUPP-02.md)
- [MCPSTG-SUPP-03 — Test Malicious MCP Server Installation](../tests/SUPP/MCPSTG-SUPP-03.md)
- [MCPSTG-SUPP-04 — Test Registry Trust and Verification](../tests/SUPP/MCPSTG-SUPP-04.md)
- [MCPSTG-SUPP-05 — Test Unsafe Auto-Updates](../tests/SUPP/MCPSTG-SUPP-05.md)

## 4.14 Enterprise Governance (`GOV`)

Folder: [`tests/GOV/`](../tests/GOV/)

- [MCPSTG-GOV-01 — Test MCP Server Inventory](../tests/GOV/MCPSTG-GOV-01.md)
- [MCPSTG-GOV-02 — Test Approved Server Registry](../tests/GOV/MCPSTG-GOV-02.md)
- [MCPSTG-GOV-03 — Test Enterprise Policy Enforcement](../tests/GOV/MCPSTG-GOV-03.md)
- [MCPSTG-GOV-04 — Test Exception Handling](../tests/GOV/MCPSTG-GOV-04.md)
- [MCPSTG-GOV-05 — Test Compliance Evidence Collection](../tests/GOV/MCPSTG-GOV-05.md)

## 4.15 Transport and Channel Security (`TRNS`)

Folder: [`tests/TRNS/`](../tests/TRNS/)

- [MCPSTG-TRNS-01 — Test TLS Configuration and Certificate Validation](../tests/TRNS/MCPSTG-TRNS-01.md)
- [MCPSTG-TRNS-02 — Test Transport Authentication Binding](../tests/TRNS/MCPSTG-TRNS-02.md)
- [MCPSTG-TRNS-03 — Test Message Size Limits and Timeouts Under Load](../tests/TRNS/MCPSTG-TRNS-03.md)

## 4.16 Gateway, Broker, and Egress Controls (`GW`)

Folder: [`tests/GW/`](../tests/GW/)

- [MCPSTG-GW-01 — Test Gateway Allowlist Enforcement for Upstream Tool Destinations](../tests/GW/MCPSTG-GW-01.md)
- [MCPSTG-GW-02 — Test SSRF Protections for Tool-Mediated HTTP Requests](../tests/GW/MCPSTG-GW-02.md)
- [MCPSTG-GW-03 — Test Rate Limiting and Abuse Throttling at the Gateway](../tests/GW/MCPSTG-GW-03.md)

## 4.17 Secrets and Credential Handling (`SECR`)

Folder: [`tests/SECR/`](../tests/SECR/)

- [MCPSTG-SECR-01 — Test Secrets in Server Configuration and Environment Exposure](../tests/SECR/MCPSTG-SECR-01.md)
- [MCPSTG-SECR-02 — Test Token Storage and Rotation Behavior on the Host](../tests/SECR/MCPSTG-SECR-02.md)
- [MCPSTG-SECR-03 — Test Redaction of Secrets in Logs and Traces](../tests/SECR/MCPSTG-SECR-03.md)

## 4.18 Resilience, Abuse, and Availability (`ABUS`)

Folder: [`tests/ABUS/`](../tests/ABUS/)

- [MCPSTG-ABUS-01 — Test Tool-Call Storms and Concurrency Limits](../tests/ABUS/MCPSTG-ABUS-01.md)
- [MCPSTG-ABUS-02 — Test Retry Behavior for Idempotent versus Non-Idempotent Side Effects](../tests/ABUS/MCPSTG-ABUS-02.md)

## 4.19 Privacy, Data Minimization, and Retention (`PRVC`)

Folder: [`tests/PRVC/`](../tests/PRVC/)

- [MCPSTG-PRVC-01 — Test PII in Resources and Tool Outputs](../tests/PRVC/MCPSTG-PRVC-01.md)
- [MCPSTG-PRVC-02 — Test Log Retention and Downstream Copying of Sensitive Transcripts](../tests/PRVC/MCPSTG-PRVC-02.md)
- [MCPSTG-PRVC-03 — Test Tenant and Customer Boundary Labeling in Context](../tests/PRVC/MCPSTG-PRVC-03.md)
---

## Individual test case format (exact template)

Each test file should follow this structure (headings may be adjusted for markdown rendering, but the sections must exist):

```markdown
# <Test Name>

ID: MCPSTG-CATEGORY-NN

## Summary
...

## Scenario
...

## Test Objectives
- ...

## Preconditions
- ...

## How to Test

### 1. Manual Review
...

### 2. Configuration Review
...

### 3. Runtime Testing
...

### 4. Abuse Case Testing
...

### 5. Log and Detection Review
...

## Test Data / Example Payloads
...

## Expected Results
...

## Remediation
...

## Tools
...

## References
...

## Mapping
- OWASP MCP Top 10: ...
- OWASP LLM Top 10: ...
- OWASP API Security Top 10: ...
- OWASP ASVS: ...
- MCP specification (versioned): ...
- CWE: ...
- MITRE ATLAS: ...
- Risk level: Low / Medium / High / Critical
- Testing type: Manual / Automated / Hybrid
```

---

## File naming convention

- Path: `tests/<CATEGORY>/MCPSTG-<CATEGORY>-NN.md`
- Example: `tests/TOOL/MCPSTG-TOOL-01.md`

See [index.json](../index.json) for the authoritative list of files and metadata.

---

## Maintainer note: skeleton versus curated tests

Many files under `tests/` are **skeleton** templates suitable for gap-filling workshops. **Curated** tests (expanded procedures and mappings) are listed in `HAND_AUTHORED` inside [scripts/bootstrap_tests.py](../scripts/bootstrap_tests.py); the bootstrap script skips overwriting those files unless `--force` is passed. Add new `(CATEGORY, number)` pairs there when a test becomes reference-quality.
