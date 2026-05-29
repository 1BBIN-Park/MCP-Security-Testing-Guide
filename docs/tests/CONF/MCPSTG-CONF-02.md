# Test Insecure Local Server Exposure

ID: MCPSTG-CONF-02

## Summary

“Local” MCP servers are often started on **localhost** with the assumption that only the trusted host process can connect. Exposure happens when servers bind to **all interfaces**, when **Unix domain sockets** have loose permissions, when **debug bridges** (for example HTTP-to-stdio proxies) are left enabled, or when **WSL / VM port forwarding** unintentionally publishes a port to the LAN. The impact equals remote access to powerful tools with **host user privileges**.

## Scenario

- Developer runs MCP server with `--host 0.0.0.0` “so the container can reach it.”
- Corporate Wi‑Fi allows device-to-device traffic; attacker on same subnet scans for open MCP ports.
- **Potential impact:** Same as `MCPSTG-AUTHN-01` but framed as configuration error rather than missing auth middleware.

## Test Objectives

- Verify effective **listen address** and **socket permissions** on all launch paths (CLI, IDE, CI).
- Verify **discovery** mechanisms (Bonjour, mDNS, IDE auto-expose) do not widen visibility unintentionally.
- Verify any HTTP bridge requires **loopback-only** binding or auth.

## Preconditions

- Lab machine with permission to inspect listening ports (`ss`, `lsof`).
- Container and bare-metal variants if your users run both.

## How to Test

### 1. Manual Review

Read scripts, README quickstarts, and IDE default configs for bind flags.

### 2. Configuration Review

- Check systemd unit files, Docker `compose` port mappings, Kubernetes `hostPort`.
- Inspect Unix socket path mode bits (`0777` vs `0600`).

### 3. Runtime Testing

1. Start the MCP server the same way developers do.
2. From **another lab host** on the same network segment, attempt TCP connect to the MCP port—expect **refuse/timeout** for localhost-only designs.
3. For stdio, confirm no secondary listener exists unless explicitly configured.

### 4. Abuse Case Testing

- IPv6 `::` dual-stack exposure when IPv4 is bound to loopback only—verify both families.

### 5. Log and Detection Review

**Detection:** host EDR or firewall logs unexpected inbound to MCP ports; container image lint rules flag `EXPOSE` with `0.0.0.0` patterns.

## Test Data / Example Payloads

Use `nc -vz <lab-ip> <port>` only against assets you own.

## Expected Results

- **Secure:** localhost or authenticated mesh only; tight socket permissions; bridges off by default.
- **Insecure:** LAN-reachable MCP with host-user power; world-writable socket path.
- **Evidence:** `ss -ltnp` output, compose file snippets, photo-redacted IDE settings.

## Remediation

- Default bind to `127.0.0.1`; require explicit env var to widen.
- Use `0600` sockets in user-private runtime dir; document WSL port-forward risks.
- Add CI checks that fail on dangerous defaults (`MCPSTG-GOV-03`).

## Tools

- `ss`, `lsof`, `docker inspect`, container image linters, IDE export of settings JSON.

## References

- OWASP ASVS: V13 Communications and V14 Configuration.
- CWE-419: Unprotected Primary Channel

## Mapping

- OWASP MCP Top 10: `N/A`
- OWASP LLM Top 10: `N/A`
- OWASP API Security Top 10: API02 / API07 (context-dependent)
- OWASP ASVS: V13, V14
- MCP specification (versioned): deployment; not protocol-only
- CWE: CWE-419
- MITRE ATLAS: `N/A`
- Risk level: Critical
- Testing type: Manual
