#!/usr/bin/env python3
"""Add markdown hyperlinks to Mapping sections in Chapter 4 test docs."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "04-mcp-security-testing"

URLS = {
    "owasp_llm": "https://owasp.org/www-project-top-10-for-large-language-model-applications/",
    "owasp_api": "https://owasp.org/API-Security/",
    "owasp_asvs": "https://owasp.org/www-project-application-security-verification-standard/",
    "cwe": "https://cwe.mitre.org/",
    "atlas": "https://atlas.mitre.org/",
    "mcp": "https://modelcontextprotocol.io/",
}

LLM = {
    "01": "https://genai.owasp.org/llmrisk/llm01/",
    "02": "https://genai.owasp.org/llmrisk/llm02/",
    "04": "https://genai.owasp.org/llmrisk/llm04/",
    "06": "https://genai.owasp.org/llmrisk/llm06/",
    "08": "https://genai.owasp.org/llmrisk/llm08/",
    "10": "https://genai.owasp.org/llmrisk/llm10/",
}

API = {
    "1": "https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/",
    "2": "https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/",
    "3": "https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/",
    "4": "https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/",
    "5": "https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/",
    "6": "https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/",
    "7": "https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/",
    "8": "https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/",
    "9": "https://owasp.org/API-Security/editions/2023/en/0xa9-improper-inventory-management/",
}

ASVS = {
    "1": "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x11-V1-Architecture.md",
    "2": "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x12-V2-Authentication.md",
    "3": "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x13-V3-Session-management.md",
    "4": "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x14-V4-Access-control.md",
    "5": "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x15-V5-Validation-sanitization-encoding.md",
    "7": "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x17-V7-Error-logging.md",
    "8": "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x18-V8-Data-protection.md",
    "10": "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x20-V10-Malicious-code.md",
    "11": "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x21-V11-Business-logic.md",
    "12": "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x22-V12-Files-resources.md",
    "13": "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x23-V13-API-web-services.md",
    "14": "https://github.com/OWASP/ASVS/blob/master/5.0/en/0x24-V14-Configuration.md",
}

def md_link(text: str, url: str) -> str:
    return f"[{text}]({url})"


def link_llm_value(value: str) -> str:
    parts = split_top_level(value, ",")
    linked = []
    for part in parts:
        part = part.strip()
        m = re.match(r"(LLM\d{2})(.*)", part)
        if not m:
            linked.append(part)
            continue
        code, rest = m.group(1), m.group(2)
        num = code[3:5]
        url = LLM.get(num)
        if url:
            linked.append(md_link(code + rest, url))
        else:
            linked.append(code + rest)
    return ", ".join(linked)


def link_api_value(value: str) -> str:
    def repl(match: re.Match) -> str:
        num = match.group(1)
        rest = match.group(2)
        url = API.get(num)
        text = f"API{num}:2023{rest}"
        return md_link(text, url) if url else text

    return re.sub(r"API(\d):2023([^,]*(?:\([^)]*\))?)", repl, value)


def link_asvs_value(value: str) -> str:
    def repl(match: re.Match) -> str:
        chapter = match.group(1)
        sub = match.group(2) or ""
        suffix = match.group(3) or ""
        url = ASVS.get(chapter)
        text = f"V{chapter}{sub}{suffix}"
        return md_link(text, url) if url else text

    return re.sub(
        r"\bV(\d{1,2})(\.\d+)?(\s+[A-Za-z][^,)]*)?",
        repl,
        value,
    )


def link_cwe_value(value: str) -> str:
    def repl(match: re.Match) -> str:
        num = match.group(1)
        rest = match.group(2) or ""
        return md_link(f"CWE-{num}{rest}", f"https://cwe.mitre.org/data/definitions/{num}.html")

    return re.sub(r"CWE-(\d+)(\s*\([^)]+\))?", repl, value)


def normalize_atlas_fragment(text: str) -> str:
    text = text.strip()
    m = re.match(r"(AML\.T[A-Z0-9.]+)(.*)", text)
    if not m:
        return text
    atlas_id, rest = m.group(1), m.group(2)
    if rest.endswith(atlas_id):
        rest = rest[: -len(atlas_id)]
    return atlas_id + rest


def link_atlas_value(value: str) -> str:
    parts = split_top_level(value, ",")
    linked = []
    for part in parts:
        part = normalize_atlas_fragment(part)
        m = re.match(r"(AML\.T[A-Z0-9.]+)(\s.*)?", part)
        if not m:
            linked.append(part)
            continue
        atlas_id = m.group(1)
        rest = m.group(2) or ""
        if ".TA" in atlas_id:
            url = f"{URLS['atlas']}tactics/{atlas_id}"
        else:
            url = f"{URLS['atlas']}techniques/{atlas_id}"
        linked.append(md_link(atlas_id + rest, url))
    return ", ".join(linked)


def unwrap_markdown_links(text: str) -> str:
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)


def split_top_level(text: str, sep: str) -> list[str]:
    parts = []
    current = []
    depth = 0
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == sep and depth == 0:
            parts.append("".join(current))
            current = []
        else:
            current.append(ch)
    parts.append("".join(current))
    return parts


def linkify_line(line: str) -> str:
    if line.startswith("- Risk level") or line.startswith("- Testing type"):
        return line

    body = line[2:] if line.startswith("- ") else line

    handlers = [
        ("OWASP LLM Top 10: ", "owasp_llm", link_llm_value),
        ("OWASP API Security Top 10: ", "owasp_api", link_api_value),
        ("OWASP ASVS: ", "owasp_asvs", link_asvs_value),
        ("CWE: ", "cwe", link_cwe_value),
        ("MITRE ATLAS: ", "atlas", link_atlas_value),
        ("MCP specification (versioned): ", "mcp", lambda v: v),
    ]

    for prefix, key, fn in handlers:
        plain_prefix = prefix
        linked_prefix = f"{md_link(prefix.rstrip(': '), URLS[key])}: "
        if body.startswith(plain_prefix):
            value = fn(body[len(plain_prefix) :])
            label = prefix.rstrip(": ")
            return f"- {md_link(label, URLS[key])}: {value}"
        if body.startswith(linked_prefix):
            raw_value = unwrap_markdown_links(body[len(linked_prefix) :])
            value = fn(raw_value)
            label = prefix.rstrip(": ")
            return f"- {md_link(label, URLS[key])}: {value}"

    return line


def repair_atlas_markdown(text: str) -> str:
    """Fix malformed ATLAS links produced when descriptions contain parentheses."""
    return re.sub(
        r"\[(AML\.T[A-Z0-9.]+) (.+?)\1\)\]\((https://atlas\.mitre\.org/(?:techniques|tactics)/\1)\)",
        r"[\1 \2](\3)",
        text,
    )


def linkify_file(path: Path) -> int:
    text = path.read_text()
    text = repair_atlas_markdown(text)
    lines = text.splitlines()
    changed = 0
    in_mapping = False

    for i, line in enumerate(lines):
        if line.strip() == "#### Mapping":
            in_mapping = True
            continue
        if in_mapping:
            if line.startswith("### ") or line.startswith("## "):
                in_mapping = False
                continue
            if line.startswith("- "):
                new_line = linkify_line(line)
                if new_line != line:
                    lines[i] = new_line
                    changed += 1

    if changed:
        path.write_text("\n".join(lines) + "\n")
    return changed


def main() -> None:
    total = 0
    for path in sorted(DOCS.glob("4.*.md")):
        n = linkify_file(path)
        if n:
            print(f"{path.name}: {n} mapping lines linked")
            total += n
    print(f"Done. Updated {total} mapping lines.")


if __name__ == "__main__":
    main()
