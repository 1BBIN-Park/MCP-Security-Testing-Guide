# About test procedures

[← Chapter 4 overview](README.md)

**All 79 MCPSTG tests are explained in sections 4.1–4.19** in this folder. Each section page includes category context, a summary table, and full per-test write-ups with **example MCP code snippets** (JSON-RPC, host config, lab scripts). There is no separate test documentation tree outside Chapter 4.

## Where to read and run tests

| Step | Action |
|------|--------|
| 1 | Open [Chapter 4 overview](README.md) and pick a section (4.1–4.19) |
| 2 | Read **Overview** for category context |
| 3 | Scroll to **Test cases** for the summary table and full explanations |
| 4 | Use **View** links to jump to a test; copy/adapt **Example snippets** (lab placeholders only) |

Example: [4.18 Resilience and Abuse](4.18-resilience-abuse.md) explains `MCPSTG-ABUS-01` and `MCPSTG-ABUS-02` with burst-test Python and JSON-RPC snippets on the same page.

## Section layout

Every category guide (`4.01` … `4.19`) follows the same pattern:

1. Overview, scope, priority, related categories  
2. **Test cases** — table + each test as `### MCPSTG-…` with:
   - Summary and scenario  
   - How to test (manual, config, runtime, abuse, logs)  
   - **Example snippets** (MCP messages, config, safe lab code)  
   - Expected results, remediation, mappings  

## Chapter 4 folder structure

```
docs/04-mcp-security-testing/
├── README.md                    ← Chapter hub
├── 4.01-information-gathering.md … 4.19-*.md   ← All tests live here
├── about-docs-tests.md
├── how-to-run.md
├── taxonomy.md
└── test-case-format.md
```

Section pages (`4.01`–`4.19`) are the **canonical source** for test content. Edit the matching section directly when updating a test.

[`index.json`](../../index.json) lists IDs, risk, type, section file paths, and anchor IDs for tooling.

## Safe testing rules

- Written authorization and synthetic lab data only.  
- Replace `<TEST_*>` placeholders using [Appendix D](../appendix-d-lab-fixtures.md).  

## Related reading

- [How to run tests](how-to-run.md)  
- [Test ID taxonomy](taxonomy.md)  
- [Test case format](test-case-format.md)  
