# 3. MCP Security Testing Framework

## 3.1 Testing principles

1. **Assume composition**: failures often arise from **chains** (resource → prompt → tool → upstream API), not single calls.
2. **Least privilege everywhere**: host, server, tool OS user, cloud IAM, and OAuth scopes must each be minimal.
3. **Human-in-the-loop is a control, not a guarantee**: test bypasses via indirect injection, misleading summaries, and race conditions in approval UIs.
4. **Defense in depth**: gateway allowlists do not remove the need for safe tools and server-side authorization.
5. **Evidence-driven**: every finding should be reproducible with safe lab artifacts and captured logs.

## 3.2 Testing methodology

A practical assessment combines:

1. **Architecture and data flow review** (trust boundaries from [02-introduction.md](02-introduction.md)).
2. **Configuration review** (host allowlists, server flags, transport mode, debug settings, file permissions).
3. **Source review** of tool implementations and resource providers (injection, path handling, secret access).
4. **Runtime testing** with benign abuse cases (parameter fuzzing within bounds, tool chaining paths).
5. **Agentic workflow testing** (multi-step plans, retries, replanning after partial failures).
6. **Detection validation** (whether the right events are logged and alertable).

Iterate by **risk**: start with remote exposure, powerful tools, secrets, and cross-tenant boundaries.

## 3.3 Threat modeling approach

Recommended steps:

1. **Inventory** MCP servers, tools, resources, transports, gateways, and identities (see `MCPSTG-INFO-*`).
2. **Identify assets**: data classes reachable via resources; actions reachable via tools.
3. **Identify actors**: end user, malicious coworker, compromised upstream, malicious package maintainer, external network attacker (if remote).
4. **List misuse cases** per STRIDE-style prompts adapted to MCP (for example tool spoofing, tool description poisoning, resource-driven injection).
5. **Map controls** to each misuse case; mark gaps as test objectives.

## 3.4 Manual review

Focus areas:

- Tool descriptions and JSON schemas shown to models (poisoning and over-broad semantics).
- Prompt templates bundled with servers (hidden instructions, unsafe defaults).
- Approval strings shown to users versus actual tool arguments (confusable summaries).
- Dynamic registration of tools at runtime.

## 3.5 Source and configuration review

- Server entrypoints, argument parsers, subprocess invocation, file path joins.
- Environment variable usage and `.env` loading patterns.
- CI/CD: pinned versions, provenance, signing expectations for images and packages.

## 3.6 Runtime testing

- Controlled lab host with logging enabled.
- Use **synthetic** tools/resources that echo arguments, simulate side effects, or return fixed documents—never customer data.

## 3.7 Agentic workflow testing

Exercise:

- Planner loops that can **retry** dangerous operations.
- Partial success states where later steps assume earlier steps were validated.
- “Goal text” mutability from untrusted resources.

## 3.8 Secure SDLC integration

Suggested integration points:

- **Design**: threat model gate for new tools with `writes`/`exec`/`network` side effects.
- **Implementation**: secure code review checklist derived from `MCPSTG-TOOL-*`, `MCPSTG-INPV-*`, `MCPSTG-SECR-*`.
- **Release**: dependency and image scanning (`MCPSTG-SUPP-*`), registry verification.
- **Operate**: gateway policy tests (`MCPSTG-GW-*`), log detection tests (`MCPSTG-LOG-*`).

## 3.9 Test harness guidance (lab)

Build a minimal MCP server that exposes:

- A **read tool** and a **write tool** (write restricted to a temp directory).
- A **resource** that returns static markdown and one that returns user-configurable lab text.
- Optional: a tool that performs **controlled** outbound HTTP to `<AUTHORIZED_LAB_SERVER>` only.

This enables consistent reproduction without touching production integrations.

## 3.10 Reporting (see Chapter 5)

Finding structure, evidence expectations, and stakeholder communication are covered in [Chapter 5 — Reporting](05-reporting.md). Use [Appendix C — Evidence Checklist](appendix-c-evidence-checklist.md) when packaging artifacts.

## 3.11 Authorization to test (operational)

Beyond technical scope:

- Confirm **vendor terms** for any SaaS used in the chain (host, model API, registry).
- Provide **emergency contacts** and an agreed **stop condition** if tests destabilize shared environments.

## 3.12 OAuth and delegated authorization (where used)

When MCP hosts use OAuth (or similar) to reach upstream APIs:

- Validate **redirect URI** exactness and environment separation (lab vs prod clients).
- Test **token audience** and **resource indicators** so access tokens minted for one API cannot be presented to another.
- Exercise **refresh** and **revocation**: local caches must invalidate (`MCPSTG-SECR-02`).
- Review **consent screens** for scope creep when new tools appear—tie to `MCPSTG-AUTHZ-*` tests.

## 3.13 Capability drift and dynamic registration

If servers can add tools or resources at runtime:

- Snapshot **before/after** capability lists during a session and assert change control (who can deploy, what CI signed).
- Test host behavior when a tool disappears mid-session (error handling, partial plans).
- Link findings to `MCPSTG-INFO-*`, `MCPSTG-SUPP-*`, and `MCPSTG-TOOL-*` cases.

## 3.14 Multi-tenant and shared-host isolation

For pooled agents or shared developer hosts:

- Verify context stores, memory caches, and temp directories are partitioned by **tenant** and **user principal**.
- Attempt benign cross-tenant reads using two lab accounts (`MCPSTG-AUTHZ-03`, `MCPSTG-CTX-04`).
- Confirm backups and crash dumps inherit the same partition rules (`MCPSTG-PRVC-*`).
