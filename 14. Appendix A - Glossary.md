# Appendix A: Glossary

| Term | Definition |
|------|------------|
| Host | Application that embeds an MCP client and orchestrates user sessions (IDE, agent runtime, assistant shell). |
| MCP client | Component that speaks MCP to a server on behalf of the host. |
| MCP server | Process exposing MCP capabilities (tools, resources, prompts) over a transport. |
| Tool | Callable capability advertised with a name, description, and commonly a JSON Schema for arguments. |
| Resource | Addressable data source MCP can read (often URI-shaped identifiers). |
| Prompt | Templated or named prompt material the server can offer for model use. |
| Transport | Mechanism linking client and server (for example stdio, streamable HTTP). |
| Gateway / broker | Intermediary enforcing policy (allowlists, auth, egress controls) in front of MCP servers. |
| Registry | Distribution or discovery mechanism for MCP servers or packages (exact meaning varies by ecosystem). |
| Session | A coherent interaction period between a client and server; session isolation is a common control. |
| Approval UI | Host UI prompting a human before high-risk tool execution. |
| Tool chaining | Sequences where outputs of one tool become inputs to another, possibly crossing privilege lines. |
| Indirect prompt injection | Instructions embedded in retrieved content (resources, web pages) that steer model behavior. |
| OAuth / OIDC | Delegated authorization used by hosts to obtain tokens for upstream APIs; must be audience- and scope-bound. |
| Elicitation / sampling | Host or protocol flows that collect structured user input mid-session; treat as a trust boundary for prompt and UI abuse tests. |
| stdio transport | MCP over standard input/output between a parent process and child server; OS process identity is the primary authenticator. |
| Streamable HTTP / SSE / WebSocket | Remote transports where TLS, origin, and message framing dominate the threat model. |
| Provenance | Build attestation, signatures, and SBOMs used to justify trust in a server package or container image. |
