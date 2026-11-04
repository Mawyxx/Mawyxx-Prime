#!/usr/bin/env python3
"""REPO-ONLY validator for the MAWYXX PRIME standard text.

This tool is NOT part of the agent standard and must not be referenced from
`Mawyxx Prime V6.7.md`. It exists so maintainers can verify the constitution
itself: IDs, anchors, counters, required law fields, gate ownership, language
policy and duplicate-free structure.

Usage:
    python tools/doc_integrity.py [--json] [path]

Exit code 0 = pass, 1 = findings.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT = Path(__file__).resolve().parents[1] / "Mawyxx Prime V6.7.md"
LAW_RE = re.compile(r"^### (A\d{2}[a-z]?|B\d{2})\b", re.M)
CYR = re.compile(r"[А-Яа-яЁё]")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
GATE_RE = re.compile(r"`([a-z][a-z0-9]*(?:[-_][a-z0-9]+)+)`")
ALIAS_LINE_RE = re.compile(r"^(A\d{2}[a-z]?)\s*[→\-]>?\s*(A\d{2}[a-z]?|B\d{2})", re.M)


def load(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def law_blocks(text: str):
    lines = text.split("\n")
    heads = [(i, l) for i, l in enumerate(lines) if LAW_RE.match(l)]
    out = []
    for n, (i, l) in enumerate(heads):
        end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        lid = LAW_RE.match(l).group(1)
        out.append((lid, i + 1, "\n".join(lines[i:end])))
    return out


def section(text: str, start: str, end: str | None = None) -> str:
    i = text.find(start)
    if i < 0:
        return ""
    j = text.find(end, i) if end else -1
    return text[i:] if j < 0 else text[i:j]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=str(DEFAULT))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    text = load(Path(args.path))
    errors: list[str] = []
    warnings: list[str] = []

    blocks = law_blocks(text)
    ids = [x[0] for x in blocks]
    dup_ids = [k for k, v in Counter(ids).items() if v > 1]
    if dup_ids:
        errors.append(f"duplicate law IDs: {dup_ids}")

    alias_zone = text.split("### 2.0.1")[0]
    alias_map = dict(re.findall(r"(A\d{2}[a-z]?)\s*→\s*(A\d{2}[a-z]?|B\d{2})", alias_zone))
    alias_ids = set(alias_map)
    for a, target in alias_map.items():
        if target not in set(ids):
            errors.append(f"alias {a} targets missing law {target}")

    required = ("Derives", "FIT", "NOT-FIT", "Min tier", "Enforced by", "Why")
    for lid, line, block in blocks:
        if lid in alias_ids:
            if "**Derives:**" not in block or "**Inherits:**" not in block:
                errors.append(f"{lid}: alias must have Derives + Inherits")
            continue
        for field in required:
            if f"**{field}:**" not in block:
                errors.append(f"{lid}: missing **{field}:**")
        m = re.search(r"\*\*Derives:\*\*\s*([^\n]+)", block)
        if m and not re.search(r"\b(K[1-6]|AX[1-7])\b", m.group(1)):
            errors.append(f"{lid}: Derives does not reference Kx/AXy")

    # language policy: normative atoms are EN
    for i, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        if s.startswith("- [ ]") and CYR.search(s):
            errors.append(f"line {i}: checklist item contains Cyrillic")
        if s.startswith("**Why:**") and CYR.search(s):
            errors.append(f"line {i}: Why contains Cyrillic")
    for tok in re.findall(r"`([^`\n]+)`", text):
        if CYR.search(tok):
            errors.append(f"backticked token contains Cyrillic: {tok!r}")

    # test completeness markers
    for marker in ("Test Selection Matrix", "Edge-case sweep", "### 4.9a Test data & environment"):
        if marker not in text:
            errors.append(f"test completeness marker missing: {marker}")

    # performance contract markers
    for marker in ("### A62 Performance and Load Contract", "PERF-LOCK", "latency_p95"):
        if marker not in text:
            errors.append(f"performance marker missing: {marker}")

    # text-only boundary: runtime terms must not leak into the standard

    for term in ("R01", "R08", "tool_manifest", "agent_audit", "agent_budget", "CONTEXT-<task>"):
        if term in text:
            errors.append(f"text-only standard contains runtime term: {term}")

    # structure / counters
    for marker in ("### 0.0 Constitution kernel", "### 0.0.1 Constitution map",
                   "### 2.0.2 Law map", "### 2.1 Policy Index",
                   "### 3.0.1 Gate registry", "### A65 Cross-Cutting Aspect Law",
                   "### 0.0.2 Scope boundary", "#### 5.7.10 AI-agent standards"):
        if text.count(marker) != 1:
            errors.append(f"structural marker not found exactly once: {marker}")
    if not re.search(r"A01.*A65", text):
        errors.append("counter/range A01…A65 missing")
    if not re.search(r"B01.*B14", text):
        errors.append("counter/range B01…B14 missing")
    if "139" not in text:
        errors.append("gate count 139 missing")

    # law map coverage
    lawmap = section(text, "### 2.0.2 Law map", "### 2.1 Policy Index")
    mapped = set(re.findall(r"\b(A\d{2}[a-z]?|B\d{2})\b", lawmap))
    for prefix, lo, hi in re.findall(r"\b([AB])(\d{2})\s*[–-]\s*(?:\1)?(\d{2})\b", lawmap):
        for n in range(int(lo), int(hi) + 1):
            mapped.add(f"{prefix}{n:02d}")
    missing_map = sorted((set(ids) - alias_ids) - mapped)
    if missing_map:
        errors.append(f"§2.0.2 law map missing laws: {missing_map}")

    # duplicate headings + duplicate long sentences
    hc = Counter(l for l in text.split("\n") if l.startswith("### "))
    for h, c in hc.items():
        if c > 1:
            errors.append(f"duplicate heading: {h}")
    norm = Counter()
    for s in SENT_SPLIT.split(re.sub(r"\s+", " ", text)):
        s2 = re.sub(r"[`*_\[\]()]", "", s).strip().lower()
        if len(s2) >= 90:
            norm[s2] += 1
    for s, c in norm.items():
        if c > 1:
            errors.append(f"duplicate sentence x{c}: {s[:100]}")

    # Enough tables: no exact duplicate rows outside §2.0.1
    en = section(text, "### 2.0.1", "### 2.0.2")
    body = text.replace(en, "")
    rows = Counter()
    for line in body.split("\n"):
        if line.startswith("|") and line.count("|") >= 4:
            cells = tuple(c.strip() for c in line.strip().strip("|").split("|"))
            if len(cells) == 3 and not all(set(c) <= set("-: ") for c in cells) \
                    and cells[0] not in ("Задача", "Law"):
                rows[cells] += 1
    for row, c in rows.items():
        if c > 1:
            errors.append(f"duplicate Enough row x{c}: {' | '.join(row)}")

    # Gate registry vs §3.2 (SSOT) and law Enforced-by coverage
    s32 = section(text, "### 3.2 prime_check contract", "### 3.3")
    reg = section(text, "### 3.0.1 Gate registry", "### 3.1 Gate algorithms")
    reg_gates = set(GATE_RE.findall(reg))
    for g in sorted(reg_gates):
        if g not in s32:
            errors.append(f"registry gate not in §3.2 SSOT: {g}")
    NON_GATES = {"latency_budget", "prime_check"}
    law_gates = set()
    for lid, line, block in blocks:
        for m in re.finditer(r"\*\*Enforced by:\*\*([^\n]+)", block):
            law_gates.update(g for g in GATE_RE.findall(m.group(1)) if g not in NON_GATES)
    for g in sorted(law_gates):
        if g not in s32:
            warnings.append(f"law gate not found in §3.2 text (check): {g}")

    # STEP 0 dedup
    if text.count("First (MUST):** STEP 0") != 0:
        errors.append("role-pack STEP 0 duplicates still present")
    if "STEP 0 (load & obey) — §1.11.0" not in text:
        errors.append("canonical STEP 0 pointer missing")

    report = {
        "path": str(args.path),
        "laws": len(ids),
        "aliases": len(alias_ids),
        "registry_gates": len(reg_gates),
        "errors": errors,
        "warnings": warnings,
        "ok": not errors,
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"doc-integrity: {report['path']}")
        print(f"laws={report['laws']} aliases={report['aliases']} registry_gates={report['registry_gates']}")
        if warnings:
            print(f"\nWARN ({len(warnings)}):")
            for w in warnings:
                print("  -", w)
        if errors:
            print(f"\nFAIL ({len(errors)}):")
            for e in errors:
                print("  -", e)
        else:
            print("\nPASS")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
