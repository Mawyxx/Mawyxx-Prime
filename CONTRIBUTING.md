# Contributing to MAWYXX PRIME

Thanks for your interest. This repository is a **standards document**, so
contributions are mostly about correctness, clarity and coverage.

## Ways to contribute

- **Fix an error** — wrong rule, broken reference, wrong standards ID (OWASP/CWE/ASVS/ISO).
- **Report a gap** — a real exploit/failure class the standard does not cover.
- **Improve wording** — make a rule unambiguous (keep the dense style).
- **Translate** — keep `README.md` (English, main face) and `README.ru.md` (Russian) in sync.

## Rules for a good PR

1. **One topic per PR** (matches Blast Radius, A33).
2. **Keep the style** — dense, bold, tables, `code`, `Why` under each law.
3. **Law → Gate** — any new MUST must map to a real gate (A22).
4. **Use IDs** — reference laws as `Axx` / `Bxx`, sections as `§x.y`.
5. **No N/A without reason** — see the Anti-N/A doctrine.
6. **No secrets** — never commit keys, tokens or `.env`.

## Commit style

```
docs: short imperative summary
```
