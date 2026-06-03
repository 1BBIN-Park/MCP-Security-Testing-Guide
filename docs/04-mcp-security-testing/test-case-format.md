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
- [OWASP MCP Top 10](https://example.org/mcp-top-10): … (cite organizational list if adopted)
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/): [LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01/), …
- [OWASP API Security Top 10](https://owasp.org/API-Security/): [API1:2023 Broken Object Level Authorization](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/), …
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/): [V4.1](https://github.com/OWASP/ASVS/blob/master/5.0/en/0x14-V4-Access-control.md), …
- [MCP specification (versioned)](https://modelcontextprotocol.io/): … (cite version tested)
- [CWE](https://cwe.mitre.org/): [CWE-200](https://cwe.mitre.org/data/definitions/200.html), …
- [MITRE ATLAS](https://atlas.mitre.org/): [AML.T0051 LLM Prompt Injection](https://atlas.mitre.org/techniques/AML.T0051), …
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
