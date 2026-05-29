#!/usr/bin/env python3
"""Generate MCPSTG skeleton test markdown files and index.json (lab placeholders only).

By default, skips overwriting hand-authored tests (see HAND_AUTHORED). Use --force to
regenerate every markdown file from the skeleton template (will destroy curated content).
index.json is always rewritten from TESTS_SPEC.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TESTS = ROOT / "docs" / "tests"

DEEP = {"AUTHZ", "TOOL", "RSRC", "PRMT", "GW", "TRNS"}

# Curated markdown — do not overwrite unless --force
HAND_AUTHORED: set[tuple[str, int]] = {
    ("TOOL", 1),
    ("TOOL", 5),
    ("AUTHZ", 2),
    ("AUTHZ", 4),
    ("CTX", 2),
    ("GW", 1),
    ("GW", 2),
    ("GW", 3),
    ("TRNS", 1),
    ("TRNS", 2),
    ("TRNS", 3),
    ("RSRC", 4),
    ("PRMT", 2),
    ("SECR", 1),
    ("SECR", 2),
    ("SECR", 3),
    ("AUTHN", 1),
    ("CONF", 2),
    ("INFO", 4),
}

TESTS_SPEC: list[tuple[str, int, str, str, str]] = [
    # cat, num, title, risk, testingType
    ("INFO", 1, "Identify MCP Servers and Clients", "Medium", "Hybrid"),
    ("INFO", 2, "Enumerate Exposed Tools", "Medium", "Manual"),
    ("INFO", 3, "Identify MCP Resources and Data Sources", "Medium", "Manual"),
    ("INFO", 4, "Map MCP Trust Boundaries", "High", "Manual"),
    ("INFO", 5, "Identify Sensitive Context Flows", "High", "Manual"),
    ("CONF", 1, "Test MCP Server Configuration", "High", "Hybrid"),
    ("CONF", 2, "Test Insecure Local Server Exposure", "Critical", "Manual"),
    ("CONF", 3, "Test Debug Mode and Verbose Errors", "Medium", "Manual"),
    ("CONF", 4, "Test File and Workspace Permissions", "High", "Hybrid"),
    ("CONF", 5, "Test Unsafe Transport Configuration", "High", "Hybrid"),
    ("AUTHN", 1, "Test Missing Authentication on MCP Server", "Critical", "Hybrid"),
    ("AUTHN", 2, "Test Weak Token Handling", "High", "Hybrid"),
    ("AUTHN", 3, "Test Credential Reuse Across Tools", "High", "Manual"),
    ("AUTHN", 4, "Test Expired or Revoked Token Acceptance", "High", "Hybrid"),
    ("AUTHZ", 1, "Test Excessive Tool Permissions", "High", "Hybrid"),
    ("AUTHZ", 2, "Test Bypassing User Approval", "Critical", "Hybrid"),
    ("AUTHZ", 3, "Test Cross-User Resource Access", "Critical", "Hybrid"),
    ("AUTHZ", 4, "Test Privilege Escalation Through Tool Chaining", "Critical", "Hybrid"),
    ("AUTHZ", 5, "Test Workspace Boundary Escape", "Critical", "Hybrid"),
    ("TOOL", 1, "Test Tool Description Poisoning", "High", "Hybrid"),
    ("TOOL", 2, "Test Unsafe Tool Execution", "Critical", "Hybrid"),
    ("TOOL", 3, "Test Command Injection in Tool Parameters", "Critical", "Hybrid"),
    ("TOOL", 4, "Test Tool Schema Manipulation", "High", "Hybrid"),
    ("TOOL", 5, "Test Dangerous Tool Chaining", "Critical", "Hybrid"),
    ("TOOL", 6, "Test Human Approval for High-Risk Tools", "High", "Manual"),
    ("RSRC", 1, "Test Sensitive Resource Exposure", "High", "Hybrid"),
    ("RSRC", 2, "Test Resource Enumeration", "Medium", "Hybrid"),
    ("RSRC", 3, "Test Cross-Workspace Data Access", "Critical", "Hybrid"),
    ("RSRC", 4, "Test Secret Leakage Through Resources", "Critical", "Hybrid"),
    ("RSRC", 5, "Test Unauthorized File Access", "Critical", "Hybrid"),
    ("PRMT", 1, "Test Direct Prompt Injection", "High", "Hybrid"),
    ("PRMT", 2, "Test Indirect Prompt Injection Through Resources", "High", "Hybrid"),
    ("PRMT", 3, "Test Tool Instruction Override", "High", "Manual"),
    ("PRMT", 4, "Test Hidden Instruction Leakage", "Medium", "Manual"),
    ("PRMT", 5, "Test Prompt Template Manipulation", "High", "Hybrid"),
    ("CTX", 1, "Test Context Over-Sharing", "High", "Manual"),
    ("CTX", 2, "Test Memory Poisoning", "High", "Hybrid"),
    ("CTX", 3, "Test Sensitive Context Leakage", "High", "Hybrid"),
    ("CTX", 4, "Test Cross-Session Context Confusion", "Critical", "Hybrid"),
    ("CTX", 5, "Test Untrusted Context Prioritization", "High", "Manual"),
    ("AGNT", 1, "Test Excessive Agency", "High", "Manual"),
    ("AGNT", 2, "Test Unsafe Autonomous Actions", "Critical", "Hybrid"),
    ("AGNT", 3, "Test Approval Bypass in Multi-Step Workflows", "Critical", "Hybrid"),
    ("AGNT", 4, "Test Goal Manipulation", "High", "Hybrid"),
    ("AGNT", 5, "Test Unsafe Retry and Loop Behavior", "High", "Hybrid"),
    ("INPV", 1, "Test Input Validation for Tool Parameters", "High", "Hybrid"),
    ("INPV", 2, "Test Path Traversal in Tool Inputs", "Critical", "Hybrid"),
    ("INPV", 3, "Test JSON and Schema Confusion", "Medium", "Hybrid"),
    ("OUTV", 1, "Test Unsafe Output Rendering", "High", "Manual"),
    ("OUTV", 2, "Test Sensitive Data in Tool Output", "High", "Hybrid"),
    ("LOG", 1, "Test Tool Call Logging", "Medium", "Hybrid"),
    ("LOG", 2, "Test User Approval Audit Logs", "High", "Manual"),
    ("LOG", 3, "Test Detection of Prompt Injection Attempts", "Medium", "Hybrid"),
    ("LOG", 4, "Test Secret Exposure Logging", "High", "Hybrid"),
    ("LOG", 5, "Test Incident Reconstruction", "Medium", "Manual"),
    ("SUPP", 1, "Test MCP Server Provenance", "High", "Hybrid"),
    ("SUPP", 2, "Test Dependency Vulnerabilities", "High", "Automated"),
    ("SUPP", 3, "Test Malicious MCP Server Installation", "Critical", "Manual"),
    ("SUPP", 4, "Test Registry Trust and Verification", "High", "Manual"),
    ("SUPP", 5, "Test Unsafe Auto-Updates", "High", "Hybrid"),
    ("GOV", 1, "Test MCP Server Inventory", "Medium", "Manual"),
    ("GOV", 2, "Test Approved Server Registry", "High", "Manual"),
    ("GOV", 3, "Test Enterprise Policy Enforcement", "High", "Hybrid"),
    ("GOV", 4, "Test Exception Handling", "Medium", "Manual"),
    ("GOV", 5, "Test Compliance Evidence Collection", "Medium", "Manual"),
    ("TRNS", 1, "Test TLS Configuration and Certificate Validation", "High", "Hybrid"),
    ("TRNS", 2, "Test Transport Authentication Binding", "High", "Hybrid"),
    ("TRNS", 3, "Test Message Size Limits and Timeouts Under Load", "Medium", "Hybrid"),
    ("GW", 1, "Test Gateway Allowlist Enforcement for Upstream Tool Destinations", "Critical", "Hybrid"),
    ("GW", 2, "Test SSRF Protections for Tool-Mediated HTTP Requests", "Critical", "Hybrid"),
    ("GW", 3, "Test Rate Limiting and Abuse Throttling at the Gateway", "Medium", "Hybrid"),
    ("SECR", 1, "Test Secrets in Server Configuration and Environment Exposure", "Critical", "Hybrid"),
    ("SECR", 2, "Test Token Storage and Rotation Behavior on the Host", "High", "Manual"),
    ("SECR", 3, "Test Redaction of Secrets in Logs and Traces", "High", "Hybrid"),
    ("ABUS", 1, "Test Tool-Call Storms and Concurrency Limits", "Medium", "Hybrid"),
    ("ABUS", 2, "Test Retry Behavior for Idempotent versus Non-Idempotent Side Effects", "High", "Hybrid"),
    ("PRVC", 1, "Test PII in Resources and Tool Outputs", "High", "Manual"),
    ("PRVC", 2, "Test Log Retention and Downstream Copying of Sensitive Transcripts", "High", "Manual"),
    ("PRVC", 3, "Test Tenant and Customer Boundary Labeling in Context", "High", "Manual"),
]


def deep_extra(category: str) -> str:
    if category not in DEEP:
        return ""
    return """
### Additional focus (high-risk category)
- Exercise **multi-hop** paths: resource → model → tool → upstream API.
- Capture **before/after** capability lists if tools can register dynamically.
- Validate **detection**: at least one log/metric should fire on suspicious sequences (even if only in SIEM queries).
"""


def skeleton_md(
    category: str, num: int, title: str, risk: str, testing_type: str
) -> str:
    test_id = f"MCPSTG-{category}-{num:02d}"
    return f"""# {title}

ID: {test_id}

## Summary

Summarize the weakness in practical language for MCP systems (host, server, tools, model routing). Explain why it matters in composed deployments.

## Scenario

Describe a realistic lab scenario using placeholders:

- **MCP host/client:** `<TEST_USER>` on a managed workstation running `<AUTHORIZED_LAB_SERVER>` integrations only.
- **MCP server:** a lab server package under `<TEST_WORKSPACE>`.
- **Tools/resources/prompts involved:** `<TEST_TOOL_NAME>`, `<TEST_RESOURCE>`.
- **Trust boundary:** between host, server, OS, and upstream APIs.
- **Attacker position:** external network attacker, malicious insider, or compromised upstream content (pick what applies).
- **Potential impact:** confidentiality, integrity, availability, or financial abuse.

## Test Objectives

- Verify the specific insecure behavior is absent or mitigated.
- Identify missing controls (authorization, input validation, egress policy, logging).
- Describe what **secure** behavior looks like under the same inputs.

## Preconditions

- Authorized lab environment and written scope.
- Access to host configuration, server configuration, and (if applicable) gateway policy UI.
- Test principal `<TEST_USER>` and non-privileged secondary account if testing cross-user issues.
- Log access for host, gateway, and MCP server.

## How to Test

### 1. Manual Review

Review documentation, tool metadata, and permission manifests for risky defaults.

### 2. Configuration Review

Inspect environment variables, config files, and transport settings with secrets redacted.

### 3. Runtime Testing

Execute safe, bounded calls through the MCP client using synthetic arguments only.

### 4. Abuse Case Testing

Attempt benign mutations of parameters and sequencing (no destructive payloads, no third-party targets).

### 5. Log and Detection Review

Confirm events contain enough structured fields to reconstruct tool name, principal, decision, and outcome without leaking secrets.
{deep_extra(category)}
## Test Data / Example Payloads

Use only synthetic examples, for example:

- Tool argument: `{{"query": "benign-lab-string-123", "workspace": "<TEST_WORKSPACE>"}}`
- Resource URI: `<TEST_RESOURCE>`

## Expected Results

- **Secure:** policy blocks unsafe actions; logs show a deny/alert with stable reason codes.
- **Insecure:** sensitive data returned, dangerous side effect occurs, or approvals are bypassed.
- **Evidence:** redacted logs, policy screenshots, hashes of server build artifacts.

## Remediation

Apply least privilege, strong defaults, approvals for high-risk tools, input validation, output filtering, gateway egress controls, and secret hygiene.

## Tools

Generic categories: MCP inspection utilities, HTTP/TLS proxies, static analysis, dependency scanners, structured log queries, policy-as-code test harnesses.

## References

- OWASP Web Security Testing Guide (structure inspiration only).
- OWASP LLM Top 10 for LLM Applications.
- OWASP API Security Top 10.
- OWASP ASVS (verification requirements).
- Model Context Protocol documentation (cite versioned sections when possible).
- CWE and MITRE ATLAS where applicable.

## Mapping

- OWASP MCP Top 10: `N/A` (cite your organizational list if adopted)
- OWASP LLM Top 10: TBD (pick entry if credible, else `N/A`)
- OWASP API Security Top 10: TBD / `N/A`
- OWASP ASVS: TBD / `N/A`
- MCP specification (versioned): TBD
- CWE: TBD / `N/A`
- MITRE ATLAS: TBD / `N/A`
- Risk level: {risk}
- Testing type: {testing_type}
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite all test markdown files, including hand-authored tests",
    )
    args = parser.parse_args()

    TESTS.mkdir(parents=True, exist_ok=True)
    index: list[dict] = []
    preserved = 0

    for category, num, title, risk, testing_type in TESTS_SPEC:
        cat_dir = TESTS / category
        cat_dir.mkdir(parents=True, exist_ok=True)
        test_id = f"MCPSTG-{category}-{num:02d}"
        rel = f"docs/tests/{category}/{test_id}.md"
        path = ROOT / rel
        key = (category, num)
        if key in HAND_AUTHORED and path.exists() and not args.force:
            preserved += 1
        else:
            path.write_text(
                skeleton_md(category, num, title, risk, testing_type), encoding="utf-8"
            )
        index.append(
            {
                "id": test_id,
                "title": title,
                "category": category,
                "risk": risk,
                "testingType": testing_type,
                "file": rel,
                "mappings": {
                    "owaspMcpTop10": "N/A",
                    "owaspLlmTop10": "TBD",
                    "owaspApiTop10": "TBD",
                    "owaspAsvs": "TBD",
                    "cwe": "TBD",
                    "mitreAtlas": "TBD",
                },
            }
        )

    (ROOT / "index.json").write_text(
        json.dumps({"version": 1, "tests": index}, indent=2) + "\n", encoding="utf-8"
    )
    msg = f"Wrote {len(index)} tests and index.json"
    if preserved and not args.force:
        msg += f" (preserved {preserved} hand-authored markdown files; use --force to overwrite)"
    print(msg)


if __name__ == "__main__":
    main()
