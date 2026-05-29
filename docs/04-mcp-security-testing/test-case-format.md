# Test Case Format and Maintenance

[← Chapter 4 overview](../04-mcp-security-testing.md) · [About `docs/tests/`](about-docs-tests.md)

Authors and contributors should follow this template for every file under [`docs/tests/`](../tests/).

## Required sections

Each procedure file must include these sections (heading levels may vary for rendering, but content must exist):

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

## Placeholders (lab only)

Use synthetic placeholders—never real customer data or non-lab endpoints:

| Placeholder | Typical use |
|-------------|-------------|
| `<TEST_USER>` | Lab principal for cross-user tests |
| `<TEST_WORKSPACE>` | Sandboxed directory |
| `<TEST_TOOL_NAME>` | Synthetic tool identifier |
| `<TEST_RESOURCE>` | Synthetic resource URI |
| `<AUTHORIZED_LAB_SERVER>` | In-scope MCP server package |

## File path convention

```
docs/tests/<CATEGORY>/MCPSTG-<CATEGORY>-NN.md
```

Example: [`docs/tests/TOOL/MCPSTG-TOOL-01.md`](../tests/TOOL/MCPSTG-TOOL-01.md)

## Skeleton vs. curated procedures

Many files under `docs/tests/` are **skeleton** templates for workshops. **Curated** tests (expanded procedures and mappings) are listed in `HAND_AUTHORED` inside [`scripts/bootstrap_tests.py`](../../scripts/bootstrap_tests.py).

| Command | Behavior |
|---------|----------|
| `python3 scripts/bootstrap_tests.py` | Refreshes `index.json`; writes skeletons only for missing or non-curated files |
| `python3 scripts/bootstrap_tests.py --force` | Overwrites **all** procedure markdown—use only when intentionally resetting content |

When a test reaches reference quality, add `(CATEGORY, number)` to `HAND_AUTHORED` so normal bootstrap runs preserve it.

## Optional metadata

YAML front matter aligned with [`schemas/test-case.schema.json`](../../schemas/test-case.schema.json) is optional for tooling integration.

## Index maintenance

When adding or renaming a test:

1. Add or update the markdown under `docs/tests/<CATEGORY>/`.
2. Update [`index.json`](../../index.json) with `id`, `title`, `category`, `risk`, `testingType`, `file`, and mappings.
3. Update the relevant [category guide](4.01-information-gathering.md) table (or regenerate via project scripts).

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for contribution rules.
