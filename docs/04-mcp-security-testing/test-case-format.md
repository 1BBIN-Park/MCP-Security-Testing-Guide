# Test Case Format and Maintenance

[← Chapter 4 overview](README.md) · [About test procedures](about-docs-tests.md)

Authors and contributors should follow this template when adding or editing tests in the matching [Chapter 4 section](README.md) (4.1–4.19).

## Required sections

Each test block within a section page must include these sections (as `####` headings under `### MCPSTG-CATEGORY-NN`):

```markdown
### MCPSTG-CATEGORY-NN — <Test Name>

<a id="mcpstg-category-nn"></a>

#### Summary
...

#### Scenario
...

#### Test Objectives
- ...

#### Preconditions
- ...

#### How to Test

##### 1. Manual Review
...

##### 2. Configuration Review
...

##### 3. Runtime Testing
...

##### 4. Abuse Case Testing
...

##### 5. Log and Detection Review
...

#### Test Data / Example Payloads
...

#### Expected Results
...

#### Remediation
...

#### Tools
...

#### References
...

#### Mapping
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

## Placeholders (lab only)

Use synthetic placeholders—never real customer data or non-lab endpoints:

| Placeholder | Typical use |
|-------------|-------------|
| `<TEST_USER>` | Lab principal for cross-user tests |
| `<TEST_WORKSPACE>` | Sandboxed directory |
| `<TEST_TOOL_NAME>` | Synthetic tool identifier |
| `<TEST_RESOURCE>` | Synthetic resource URI |
| `<AUTHORIZED_LAB_SERVER>` | In-scope MCP server package |

## Where tests live

Tests are embedded in section pages, not separate files:

| Category | Section file |
|----------|--------------|
| `INFO` | [4.01-information-gathering.md](4.01-information-gathering.md) |
| `CONF` | [4.02-configuration-deployment.md](4.02-configuration-deployment.md) |
| `AUTHN` | [4.03-identity-authentication.md](4.03-identity-authentication.md) |
| … | … |
| `PRVC` | [4.19-privacy-retention.md](4.19-privacy-retention.md) |

Example: `MCPSTG-TOOL-01` lives in [4.5 Tool Security](4.05-tool-security.md#mcpstg-tool-01).

## Maintainer workflow

1. Edit the test block in the matching section file (for example `4.05-tool-security.md`).
2. Update the **Test cases** summary table in that section if title, risk, or type changed.
3. Update [`index.json`](../../index.json) when adding or renaming tests (`id`, `title`, `category`, `risk`, `testingType`, `file`, `anchor`).

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for contribution rules.
