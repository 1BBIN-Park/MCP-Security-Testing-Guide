# About `docs/tests/`

[← Chapter 4 overview](../04-mcp-security-testing.md)

The [`docs/tests/`](../tests/) directory is the **executable body** of MCP Security Testing Guide (MCPSTG) Chapter 4. This page explains what lives there, how it connects to the narrative in this chapter, and how to use it during an assessment.

## What `docs/tests/` is

`docs/tests/` contains **79 discrete security test procedures**—one markdown file per test ID. Each file is a self-contained lab procedure you can run in an authorized environment. The directory is organized by **four-letter category prefix**, matching the test ID taxonomy (`INFO`, `TOOL`, `AUTHZ`, and so on).

```
docs/
├── 04-mcp-security-testing.md          ← Chapter hub (index + navigation)
├── 04-mcp-security-testing/            ← Category guides (this folder)
│   ├── about-docs-tests.md             ← You are here
│   ├── 4.01-information-gathering.md   ← Category narrative + test table
│   └── …
└── tests/                              ← Executable procedures
    ├── INFO/
    │   ├── MCPSTG-INFO-01.md
    │   └── …
    ├── TOOL/
    └── … (19 category folders)
```

**Chapter 4 has two layers:**

| Layer | Location | Purpose |
|-------|----------|---------|
| **Guide** | `docs/04-mcp-security-testing/` | Explains *why* each category matters, when to prioritize it, and how tests relate to each other |
| **Procedures** | `docs/tests/<CATEGORY>/` | Step-by-step *how to test* with scenarios, payloads, expected results, and mappings |

Think of the guide pages as the **textbook chapter**; think of `docs/tests/` as the **lab manual**.

## Relationship to `index.json`

The machine-readable catalog at [`index.json`](../../index.json) (repository root) lists every test with:

- `id` — for example `MCPSTG-TOOL-03`
- `title`, `category`, `risk`, `testingType`
- `file` — path to the procedure markdown (for example `docs/tests/TOOL/MCPSTG-TOOL-03.md`)

Use `index.json` when building tooling (dashboards, checklists, CI gates). Use the markdown in `docs/tests/` when executing tests manually or in a workshop.

## File naming convention

Every procedure follows the same path pattern:

```
docs/tests/<CATEGORY>/MCPSTG-<CATEGORY>-NN.md
```

Examples:

- `docs/tests/INFO/MCPSTG-INFO-01.md` — Identify MCP Servers and Clients
- `docs/tests/TOOL/MCPSTG-TOOL-01.md` — Test Tool Description Poisoning
- `docs/tests/GW/MCPSTG-GW-02.md` — Test SSRF Protections for Tool-Mediated HTTP Requests

The folder name **must** match the ID prefix. Input-validation tests use `INPV`; output-handling tests use `OUTV`—never mixed in one file.

## What each procedure file contains

Each file under `docs/tests/` follows the [test case format](test-case-format.md). At minimum you will find:

| Section | What it gives you |
|---------|-------------------|
| **Summary** | The weakness in MCP terms and why it matters in composed deployments |
| **Scenario** | A realistic lab setup using placeholders (`<TEST_USER>`, `<TEST_WORKSPACE>`, etc.) |
| **Test Objectives** | What secure vs. insecure behavior looks like |
| **Preconditions** | Scope, access, and logging requirements |
| **How to Test** | Manual review, configuration review, runtime testing, abuse cases, log review |
| **Test Data / Example Payloads** | Synthetic, lab-safe examples only |
| **Expected Results** | Pass/fail criteria and evidence to capture |
| **Remediation** | Control patterns (not vendor-specific product names) |
| **Mapping** | Links to OWASP LLM Top 10, API Top 10, ASVS, CWE, MITRE ATLAS where credible |

Some files are **skeleton** templates (workshop starting points). Others are **curated** with expanded prose; see the maintainer note in [test case format](test-case-format.md).

## Skeleton vs. curated procedures

| Type | Description | How to recognize |
|------|-------------|------------------|
| **Skeleton** | Generic sections with `TBD` mappings and placeholder scenario text | Suitable for gap-filling workshops |
| **Curated** | Expanded scenarios, concrete abuse cases, credible mappings | Listed in `HAND_AUTHORED` in [`scripts/bootstrap_tests.py`](../../scripts/bootstrap_tests.py) |

Running `python3 scripts/bootstrap_tests.py` refreshes skeletons and `index.json` but **preserves** curated files unless you pass `--force`.

## How to navigate from Chapter 4

1. Start at [Chapter 4 overview](../04-mcp-security-testing.md) for the full category list.
2. Open the **category guide** (for example [4.5 Tool Security](4.05-tool-security.md)) to understand scope and priority.
3. Follow the **Procedure** link to the file in `docs/tests/<CATEGORY>/`.
4. Execute steps in an **authorized lab** only; report per [Chapter 5 — Reporting](../05-reporting.md).

## Safe testing rules

- Use **written authorization** and synthetic lab data—never production customer data or third-party targets without engagement.
- Replace placeholders (`<AUTHORIZED_LAB_SERVER>`, `<TEST_TOOL_NAME>`) with your lab fixtures; see [Appendix D — Safe Lab Fixtures](../appendix-d-lab-fixtures.md).
- Do not copy steps from the OWASP Web Security Testing Guide; MCPSTG follows WSTG **structure**, not its prose or payloads.

## Related reading

- [How to run tests](how-to-run.md) — workflow from scope to evidence
- [Test ID taxonomy](taxonomy.md) — prefix meanings and numbering rules
- [Test case format](test-case-format.md) — template for authors and contributors
- [Chapter 3 — Framework](../03-mcp-security-testing-framework.md) — methodology and threat modeling before you pick test IDs
