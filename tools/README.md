# tools — repo-only maintenance

This directory is **not part of the agent standard**. Nothing here is shipped to
agents or referenced by `Mawyxx Prime V6.5.md`. It exists so maintainers can
validate the constitution text itself.

## `doc_integrity_gate.py`

Validates `Mawyxx Prime V6.5.md` (the standard) as a document:

- law IDs, uniqueness, required fields (`Derives · FIT · NOT-FIT · Min tier · Enforced by · Why`);
- alias map targets and alias blocks;
- `§2.0.2` law-map coverage (with range expansion);
- counters/ranges (`A01…A65`, `B01…B14`, `139`);
- duplicate headings and duplicate long sentences;
- exact-duplicate rows in inline `Enough vs too much` tables (they belong to `§2.0.1`);
- `§3.0.1` gate registry vs `§3.2` SSOT;
- language policy (normative atoms are EN: law title / Min tier / Enforced by / Why / checklist / gate/evidence tokens);
- STEP 0 spawn dedup.

```bash
python tools/doc_integrity_gate.py
python tools/doc_integrity_gate.py --json
python tools/doc_integrity_gate.py "Mawyxx Prime V6.5.md"
```

Exit code `0` = PASS, `1` = findings.
