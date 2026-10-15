# About the tests

How the test documentation in this folder is organised, and how the pieces fit together.

## One file per category

Chapter 3 is split into 19 category files, `3.01-…` through `3.19-…`, listed in the [chapter overview](<3. MCP Threats and Attack Patterns.md>). Each file follows the same shape:

1. **Category context** — overview, why the category matters, scope, when to prioritise it, related categories, and the common test chains it participates in.
2. **Threats and attack patterns** — published cases with sources, written up as what they change for a test. These are the sourced record: quoted extracts, version ranges and dates as the source states them.
3. **Canonical attack patterns** — where present, the abuse patterns that belong to this category, each naming the abuse, a lab-safe example, the impact, red flags and defensive checks.
4. **`## Test cases`** — the summary table for the category, followed by one test block per test.

## Test blocks

Every test is one `### MCPSTG-…` block with the same subsections, so tests can be skimmed, diffed and reviewed mechanically:

`Summary` · `Scenario` · `Preconditions` · `Test Objectives` · `Tools` · `Test Data / Example Payloads` · `How to Test` · `Expected Results` · `Example snippets` · `Mapping` · `Remediation` · `References`

The authoring rules are in [Test case format](test-case-format.md).

## Summary tables and anchors

Each test block carries an `<a id="mcpstg-…"></a>` anchor immediately after its heading, and the summary table links to it with `[View](#mcpstg-…)`. The anchor is what makes the table navigable — a missing anchor produces a dead link even though the heading exists.

Identifiers are `MCPSTG-<PREFIX>-<NN>`; the prefix matrix is in [Test ID taxonomy](taxonomy.md).

## Category context vs test cases

The prose before `## Test cases` explains *why* the category exists and what published attacks changed the testing approach. The tests are what you actually run. Where a category is large, the two are deliberately separate so that a test can be updated on its own — a published case that gets patched does not invalidate a test, but it may change its priority.

## Cross-references

- Tests are referenced by identifier (`MCPSTG-LOG-05`), not by position, so reordering does not break references.
- Categories cross-reference each other in their `Related categories` and `Common test chains` sections; use those to build a test plan that follows an attack chain rather than a checklist.
- Controls, review rows and reporting live outside the test files: [Chapter 3 hub](<3. MCP Threats and Attack Patterns.md>), [Appendix C — Security Review](<../09. Appendix C - Security Review.md>), and the [finding template](<test-case-format.md#mcp-red-team-finding-template>).

## What this chapter is not

It is not a scanner specification and not a product comparison. The tests describe observations to make and evidence to collect; [Appendix F — Testing Tools](../11. Appendix F - Testing Tools.md) lists the tool *categories* that make those observations, and every fixture convention is in [Appendix D — Safe Lab Fixtures](../10. Appendix D - Safe Lab Fixtures.md).
