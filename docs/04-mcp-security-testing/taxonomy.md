# Test ID Taxonomy

[← Chapter 4 overview](README.md) · [About `docs/tests/`](about-docs-tests.md)

Every test in [`docs/tests/`](../tests/) uses the ID format **`MCPSTG-<CATEGORY>-<NN>`**. This page defines prefixes, numbering rules, and the category-to-ID matrix.

## ID format

```
MCPSTG-<CATEGORY>-<NN>
         │            └── two-digit sequence per category (01, 02, …)
         └── four-letter category code (matches folder under docs/tests/)
```

Example: `MCPSTG-TOOL-03` → procedure at [`docs/tests/TOOL/MCPSTG-TOOL-03.md`](../tests/TOOL/MCPSTG-TOOL-03.md).

## Prefix reference

| Prefix | Category | Focus | Category guide |
|--------|----------|--------|----------------|
| `MCPSTG-INFO` | Information Gathering | Inventory, enumeration, trust boundaries | [4.1](4.01-information-gathering.md) |
| `MCPSTG-CONF` | Configuration and Deployment | Hardening, debug modes, permissions, transport config | [4.2](4.02-configuration-deployment.md) |
| `MCPSTG-AUTHN` | Identity and Authentication | Missing authn, tokens, credential reuse | [4.3](4.03-identity-authentication.md) |
| `MCPSTG-AUTHZ` | Authorization and Permission | Least privilege, approvals, cross-user access | [4.4](4.04-authorization-permission.md) |
| `MCPSTG-TOOL` | Tool Security | Descriptions, execution, injection, chaining | [4.5](4.05-tool-security.md) |
| `MCPSTG-RSRC` | Resource and Data Access | Sensitive files, enumeration, secrets via resources | [4.6](4.06-resource-data-access.md) |
| `MCPSTG-PRMT` | Prompt and Instruction | Direct/indirect injection, hierarchy conflicts | [4.7](4.07-prompt-instruction.md) |
| `MCPSTG-CTX` | Context and Memory | Over-sharing, poisoning, session confusion | [4.8](4.08-context-memory.md) |
| `MCPSTG-AGNT` | Agentic Workflow | Agency, retries, goal manipulation | [4.9](4.09-agentic-workflow.md) |
| `MCPSTG-INPV` | Input Validation | Parameters, traversal, JSON/schema confusion | [4.10](4.10-input-validation.md) |
| `MCPSTG-OUTV` | Output Handling | Unsafe rendering, sensitive tool output | [4.11](4.11-output-handling.md) |
| `MCPSTG-LOG` | Logging and Detection | Audit trails, detection coverage | [4.12](4.12-logging-detection.md) |
| `MCPSTG-SUPP` | Supply Chain | Provenance, registries, updates | [4.13](4.13-supply-chain.md) |
| `MCPSTG-GOV` | Enterprise Governance | Inventory, policy, compliance evidence | [4.14](4.14-enterprise-governance.md) |
| `MCPSTG-TRNS` | Transport and Channel | TLS, binding, limits, timeouts | [4.15](4.15-transport-channel.md) |
| `MCPSTG-GW` | Gateway and Egress | Allowlists, SSRF controls, throttling | [4.16](4.16-gateway-egress.md) |
| `MCPSTG-SECR` | Secrets and Credentials | Storage, rotation, log redaction | [4.17](4.17-secrets-credentials.md) |
| `MCPSTG-ABUS` | Resilience and Abuse | Storms, retries, cost abuse | [4.18](4.18-resilience-abuse.md) |
| `MCPSTG-PRVC` | Privacy and Retention | PII minimization, log retention, tenancy | [4.19](4.19-privacy-retention.md) |

## Numbering rules

- Each prefix uses **two-digit numbers starting at `01`**.
- New tests append the **next free number** for that prefix (do not renumber published IDs).
- **One primary prefix per file** — the folder name must match the ID prefix.

## INPV vs. OUTV

| Prefix | Use when the test focuses on… |
|--------|----------------------------------|
| `INPV` | **Inputs** to tools: parameter validation, path traversal, schema confusion |
| `OUTV` | **Outputs** from tools: unsafe rendering in host UI, sensitive data in responses |

Do not mix input- and output-focused objectives in a single test file.

## Category to test ID matrix

| Category | Test IDs |
|----------|----------|
| INFO | `MCPSTG-INFO-01` … `MCPSTG-INFO-05` |
| CONF | `MCPSTG-CONF-01` … `MCPSTG-CONF-05` |
| AUTHN | `MCPSTG-AUTHN-01` … `MCPSTG-AUTHN-04` |
| AUTHZ | `MCPSTG-AUTHZ-01` … `MCPSTG-AUTHZ-05` |
| TOOL | `MCPSTG-TOOL-01` … `MCPSTG-TOOL-06` |
| RSRC | `MCPSTG-RSRC-01` … `MCPSTG-RSRC-05` |
| PRMT | `MCPSTG-PRMT-01` … `MCPSTG-PRMT-05` |
| CTX | `MCPSTG-CTX-01` … `MCPSTG-CTX-05` |
| AGNT | `MCPSTG-AGNT-01` … `MCPSTG-AGNT-05` |
| INPV | `MCPSTG-INPV-01` … `MCPSTG-INPV-03` |
| OUTV | `MCPSTG-OUTV-01` … `MCPSTG-OUTV-02` |
| LOG | `MCPSTG-LOG-01` … `MCPSTG-LOG-05` |
| SUPP | `MCPSTG-SUPP-01` … `MCPSTG-SUPP-05` |
| GOV | `MCPSTG-GOV-01` … `MCPSTG-GOV-05` |
| TRNS | `MCPSTG-TRNS-01` … `MCPSTG-TRNS-03` |
| GW | `MCPSTG-GW-01` … `MCPSTG-GW-03` |
| SECR | `MCPSTG-SECR-01` … `MCPSTG-SECR-03` |
| ABUS | `MCPSTG-ABUS-01` … `MCPSTG-ABUS-02` |
| PRVC | `MCPSTG-PRVC-01` … `MCPSTG-PRVC-03` |

Authoritative metadata (risk, testing type, file path) is in [`index.json`](../../index.json).

## Governance: “OWASP MCP Top 10” mapping

Some communities publish MCP-focused risk lists. **If** your organization adopts a specific “MCP Top 10” or similar document, cite it by name and version in each test’s **Mapping** section.

If no stable list is adopted, use **`N/A`** for that column and rely on **OWASP LLM Top 10**, **OWASP API Security Top 10**, **ASVS**, **CWE**, and **MITRE ATLAS** where mappings are credible. Do not invent false mappings for completeness.
