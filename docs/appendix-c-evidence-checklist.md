# Appendix C: Evidence Checklist

Collect the minimum evidence needed for peer review and remediation tracking.

## For every finding

- [ ] Test ID and title
- [ ] Affected component and version (if known)
- [ ] Environment type (lab/staging) and date
- [ ] Redacted reproduction steps (placeholders only)
- [ ] Observed insecure behavior (quotes from logs or UI copy, redacted)
- [ ] Expected secure behavior
- [ ] Risk rating with rationale (impact × likelihood)

## Logs and telemetry

- [ ] Correlation ID across host, gateway, and server logs (if applicable)
- [ ] Tool name, arguments (redacted), approval decision, user principal
- [ ] Transport metadata (for example TLS version, client IP if relevant and permitted)

## Configuration artifacts

- [ ] Sanitized config snippets (secrets removed)
- [ ] File permissions output for sensitive paths (hashed paths acceptable)

## Integrity artifacts

- [ ] Package version, lockfile hash, container digest (for supply chain issues)
- [ ] Git commit hash for custom servers

## Legal and process

- [ ] Written authorization reference (ticket ID or statement of work clause—not private data)
