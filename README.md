# MAWYXX PRIME — AI Coding Standard

*Build for Billions. Code for Vibe. Rule with Logic.*

[Russian version → README.ru.md](README.ru.md)

**v3.0** = patterns (MIT). **v5.7** = named laws + Law→Gate + outcome honesty. Spec Skin + Spec Engine: one Law Template, one SSOT for OWASP/Anti-N/A, [Conflict Matrix](Mawyxx%20Prime%20V5.7.md#conflict-matrix-при-сомнении--читать-это-не-конкурирующие-абзацы) for «при сомнении», **Default-secure 5Q** before code (CRUD with id/PATCH → Trust Pipeline in the same PR).

**Project Skin · Empire Engine:** write in the project's style — with Empire discipline. Green `prime_check` from AC-names, unused ports, ignored e2e, or excluded composition is **not** done.

**v5.7 is open in this repo** for read/fork/personal use. **Corporate / team / client production** → one-time license ($50/employee) → [@ExcitedSkam](https://t.me/ExcitedSkam).

---

## Files

| File | Content | Access |
|------|---------|--------|
| `Mawyxx Prime V3.0.md` | Patterns · ~220 lines | **MIT** |
| `Mawyxx Prime V5.7.md` | AGENT-0…5 · **A01–A41** · **B01–B14** | **Open in repo** · corp = paid |
| `scripts/prime_check/` | Agent creates FULL per **AGENT-5** | **Not shipped** — agent bootstraps |

Full normative text lives **only** in `Mawyxx Prime V5.7.md`. This README is an index — not a second SSOT.

---

## Honesty pillars (A34–A41)

| Pillar | Rule · gates | Kills |
|--------|--------------|-------|
| **Intent lock** | **A34** · `intent-lock-gate` | AC↔test-name synonym |
| **Contract Surface** | **A35** · `port-surface-gate` · composition/Fake | Concrete in UC · unused ports |
| **Live Surface** | **A36** · `live-surface-gate` | Port in yaml never called |
| **No swallow** | **A37** · `no-swallow-gate` · `err-variant-gate` | `let _ =` on I/O · dump-bucket Err |
| **Checker integrity** | **A38** · `checker-integrity-gate` | Theatre `return GREEN` |
| **Behavior SSOT** | **A39** · `behavior-ssot-gate` | Algorithm clones · fake-split |
| **Secure Continuum** | **A40** · ci-harden · channel-secret · headers · cors-csrf · iac | Green zta + `write-all` · `.env` in chat |
| **Trust Pipeline** | **A41** · trust-pipeline · idor · mass-assign · path · session | «logged-in ⇒ any id» · `update(**body)` |

Also: **A05a** cohesion · **A12a** taxonomy · Anti-N/A (Doctrine SSOT) · **A25** coverage honesty · **A33** blast · rich domain (**A05**/**B06**).

---

## Rule map

```text
PART A — A01 Context/tier      A11 Decomposition       A21 SemVer/contracts
        A02 Zero Trust         A12 Tests/pyramid       A22 prime_check
        A03 API contract       A12a Test taxonomy      A23 Docker/infra
        A04 Plugin boundaries  A13 Definition of done  A24 TDD-LOCK
        A05 Layer law          A14 Idempotency         A25 Coverage 100%
        A05a Package cohesion  A15 Deterministic time  A26 Evidence block
        A06 DI & ports         A16 Secure-by-design    A27 Test quality
        A07 Design-first       A17 Clean code          A28 Mutation
        A08 Anti-fork          A18 OWASP/hygiene       A29 ZTA matrix
        A09 → A08 alias        A19 Supply chain        A30 Anti-slack
        A10 Result/errors      A20 Migrations          A31 Legacy · A32 Monorepo
                                                      A33–A41 honesty + continuum + pipeline

PART B — B01 CQRS … B14 Human handoff
```

International maps (ISO 25010 · CISQ · OWASP ASVS · CERT/MISRA): **Quality Constellation** in V5.7. OWASP Top 10 closure table: **A18 only**.

---

## Checker = agent job

On ≥PRIME the agent scaffolds `scripts/prime_check/`, implements steps, wires CI, runs `--diff` → FULL, fixes until `exit 0`, prints `PRIME-VERIFY-EVIDENCE`. You do not install or run the checker.

```text
PHASE 0  bootstrap checker if missing
PHASE 1  design maps (taxonomy · contracts · behavior_owners · continuum · trust · AC · blast)
PHASE 2  TDD per applicable family + AC oracle
PHASE 3  implement inside blast_radius — call owners, don't clone
PHASE 4  --only → --diff → FULL → evidence
```

---

## License

| Use | v3.0 | v5.7 |
|-----|------|------|
| Read / fork / study | MIT | Open in repo |
| Personal / hobby | Free | Free |
| Company / team / client prod | MIT (v3) | **$50 / employee · one-time** → [@ExcitedSkam](https://t.me/ExcitedSkam) |

---

## Cursor — adopt without polluting User Rules

Keep V5.7 **in the workspace**; load on demand. Short boot rule only (path adjust as needed):

```markdown
---
description: MAWYXX PRIME boot — short; full spec on demand
alwaysApply: true
---

Project Skin + Empire Engine. Read `Mawyxx Prime V5.7.md` for architecture / merge.
No checker? Agent builds FULL per AGENT-5. Never ask user to run tests.
On RED: fix-until-green. Anti-N/A · Conflict Matrix · Default-secure 5Q · A34–A41 — coverage alone ≠ done.
```

---

*MAWYXX PRIME · [@ExcitedSkam](https://t.me/ExcitedSkam)*
