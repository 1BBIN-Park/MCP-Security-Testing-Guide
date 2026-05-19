# Appendix D: Safe Lab Fixtures

Use **synthetic** names and paths. Do not embed customer identifiers.

## Suggested synthetic tool names

- `<TEST_TOOL_NAME>_echo` — returns arguments unchanged (for injection probes).
- `<TEST_TOOL_NAME>_readonly_query` — reads from a fixed in-memory dataset.
- `<TEST_TOOL_NAME>_write_sandbox` — writes only beneath `<TEST_WORKSPACE>/sandbox/`.

## Suggested synthetic resources

- `resource://<AUTHORIZED_LAB_SERVER>/docs/benign.md` — static markdown.
- `resource://<AUTHORIZED_LAB_SERVER>/docs/injection_lab.md` — markdown maintained by testers with **known** benign injection strings (no real secrets).

## Workspace layout (example)

```text
<TEST_WORKSPACE>/
  sandbox/          # allowed write target
  readonly/         # read-only fixture files
  secrets/          # should never be readable by tools (negative tests)
```

Populate `secrets/` with **fake** credentials (`FAKE_API_KEY=...`) that are rotated and not used anywhere.

## Outbound calls

Only call `<AUTHORIZED_LAB_SERVER>` you operate, with endpoints that record requests for SSRF tests and discard bodies safely.
