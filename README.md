# MAWYXX PRIME — AI Coding Standard

*Build for Billions. Code for Vibe. Rule with Logic.*

[Russian version → README.ru.md](README.ru.md)

**v3.0** = patterns (MIT). **v6.5** = Unified Constitution: **one file**, two layers (RUNTIME + LAW), one SSOT per topic, no duplicates, **tier-aware depth over width**. §0 Router → §1 Work → §2 Law → §3 Gates → §4 Protocols → §5 Reference. Laws **A01–A64** + **B01–B14**, 5 roles (Orchestrator · Analyst · Builder · Guardian · Verifier), **Why** under every law, **12 GOOD/BAD patterns (anti-anchoring)**, **Reasoning protocol**, **Adversarial self-review**, **Explain/ADR protocol**, **Feature Threat Model 10Q**, **Two-Agent Verify**, **Bug→Gate**, **P0–P3 priorities**, **Diagnostic tree**, **Testing recipes**, canonical checker map (**FOCUS 30 mandatory** → CORE 70 → **138** total, ratcheted) with **depth gates** (`reasoning` · `adversarial` · `decision-log` · `standards-map`) and **§5.7 Standards Traceability** (OWASP · CWE · ASVS · ISO 25010/5055 · CERT/MISRA), enforced **bidirectionally** (inline `standards.yaml` in §5.7.8).

**Project Skin · Empire Engine:** write in the project's style — with Empire discipline. Green `prime_check` from AC-names, unused ports, ignored e2e, or excluded composition is **not** done.

**Tiers:** PRIME+ only for **multi-user/PII/payments/FSM/side-effect jobs/external mutations**; single-user auth (no foreign data) → **STANDARD**. **Security:** baseline (§0.5) is mandatory at **every** tier (incl. LITE); only *depth* scales — no hyper-protection on simple scripts.

**v6.5+ (senior pass):** senior protocols **woven throughout (single file)** — Doctrine **Ask first**, per-role **self-questions**, sub-agent **questions block**, **Domain Elicitation** (§1.12), **Senior Debugging** 12 steps (§4.12), **Architecture Decision** 7 steps (§4.13), **Senior Thinking Checklist** (§4.14), **Cross-Service** (§4.15), **Feedback Loop** post-mortem→gate (§4.16), **Self-Sufficiency** (§4.17 — AI решает всё сам, без человека). **v6.5 (backend + holes fixed):** **A60 Webhooks · A61 Upload safety · A62 Load/soak · A63 Privacy/retention · A64 Notifications · A54 Budgets · A55–A59** (GraphQL/WS/Search/i18n/PCI) +11 gates (138) · per-language concurrency · failure modes 20→30. **Hole fixes:** depth enforcement via **files** (`docs/reasoning/`, `docs/reviews/`, `docs/adr/`) · honest **`steps_registered/green/skipped` + `skip_reasons`** · sub-agent **merge conflict rules** · **§5.7 inline (single file)** · §3.3 merged into §0.7 · flaky N=10/20 · `critical_scope` defined · aliases A49→A20, A51→B03, A52→B04, A53→A14. **v6.4:** A48–A53 + FOCUS 30. **v6.3:** Enough-vs-too-much · sub-agent hardening · standards mapping.

**v6.5 is open in this repo** for read/fork/personal use. **Corporate / team / client production** → one-time license ($50/employee) → [@ExcitedSkam](https://t.me/ExcitedSkam).

---

## Files

| File | Content | Access |
|------|---------|--------|
| `Mawyxx Prime V3.0.md` | Patterns · ~220 lines | **MIT** |
| `Mawyxx Prime V6.5.md` | **Single file** · Unified Constitution · **§0–§5** · **A01–A64** · **B01–B14** · §5.7 standards mapping (inline) | **Open in repo** · corp = paid |
| `Mawyxx-Security.md` | Standalone security-audit mega-prompt (§1.1 Surface Matrix S01–S23 · 19 sub-agents) | **Open in repo** |
| `scripts/prime_check/` | Agent creates FOCUS→CORE→FULL per §3.2 | **Not shipped** — agent bootstraps |

Full normative text lives **only** in `Mawyxx Prime V6.5.md`. This README is an index — not a second SSOT.

---

## Honesty pillars (A34–A47)

| Pillar | Rule · gates | Kills |
|--------|--------------|-------|
| **Intent lock** | **A34** · `intent-lock-gate` | AC↔test-name synonym; AC without oracle |
| **Contract Surface** | **A35** · port-surface · composition/Fake | Concrete in UC · unused ports |
| **Live Surface** | **A36** · `live-surface-gate` | Port in yaml never called · unread field |
| **No swallow** | **A10** · no-swallow · err-variant | `let _ =` on I/O · dump-bucket Err |
| **Checker integrity** | **A22** · `checker-integrity-gate` | Theatre `return GREEN` · existence-only |
| **Behavior SSOT** | **A39** · `behavior-ssot-gate` | Algorithm clones · fake-split |
| **Secure Continuum** | **A40** · ci-harden · channel-secret · headers · cors-csrf · iac | Green zta + `write-all` · `.env` in chat |
| **Trust Pipeline** | **A41** · trust-pipeline · idor · mass-assign · path · session | «logged-in ⇒ any id» · `update(**body)` |
| **Parameter Bounds** | **A42** · `param-bounds-gate` | `digest[i]` без bounds · difficulty без clamp |
| **Idempotency & Atomicity** | **A14** · idempotency-matrix · atomicity | replay → 2 side-effects · claim без release |
| **Dependency Isolation** | **A44** · `dep-isolation-gate` | hot-path зависит от cold dep |
| **Config Guard** | **A46** · `prod-guard-gate` | `if TESTING` без env-guard · fail-open |
| **Contracts & Spec Parity** | **A21** · api-contract-drift · snapshot · spec-parity | поле без version · спека ≠ код |

Also: **A05a** cohesion · **A12a** taxonomy (24 families) · Anti-N/A (Doctrine) · **A25** coverage honesty · **A33** blast · rich domain (**A05**/**B06**).

---

## Rule map

```text
§0 IDENTITY & ROUTER   0.3 Task router · 0.4 Tier · 0.5 Default-secure 5Q · 0.6 Principles
§1 HOW TO WORK         1.1 Roles · 1.2 Phases · 1.3 Design Artifact · 1.5 Conflict Matrix
                       1.6 Anti-N/A · 1.7 Failure modes · 1.9 3-strike · 1.10 Reasoning (PRIME+)
                       1.11 Sub-agent execution (spawn packs · contracts · merge)
§2 LAWS (A01–A47)  —  each with Why + checklist (+ GOOD/BAD patterns on 12 key rules)
   A01 Context/tier      A13 DoD               A25 Coverage absolute   A37 alias→A10
   A02 Zero Trust        A14 Idempotency+Atom  A26 Evidence            A38 alias→A22
   A03 API contract      A15 Deterministic     A27 Test quality        A39 Behavior SSOT
   A04 Plugin boundary   A16 Secure-by-design  A28 Mutation            A40 Secure Continuum
   A05 Layer law         A17 Clean code        A29 ZTA matrix          A41 Trust Pipeline
   A05a Cohesion         A18 OWASP             A30 Anti-slack          A42 Param bounds
   A06 DI & ports        A19 Secrets SSOT      A31 Legacy              A43 alias→A14
   A07 Design-first      A20 Migrations        A32 Monorepo            A44 Dep isolation
   A08 Anti-fork         A21 Contracts+Parity  A33 Blast               A45 alias→A14
   A09 alias→A08         A22 Checker+integrity A34 Intent lock         A46 Config guard
   A10 Errors            A23 Docker/IaC        A35 Contract Surface    A47 alias→A21
   A11 Decomposition     A12 Tests             A12a Taxonomy           A24 TDD-LOCK
   B01 CQRS … B14 Human handoff
§3 GATES               3.0 groups · 3.1 algorithms · 3.2 prime_check (FOCUS 30 → CORE 70 → 138) ·
                       3.3 Depth gates · 3.4 P0–P3 priorities · 3.5 evidence
§4 PROTOCOLS           4.1 Threat Model 10Q · 4.2 Two-Agent · 4.3 Bug→Gate · 4.4 Pre-Flight
                       4.5 Fix-until-green · 4.6 3-strike · 4.7 Decision Log ·
                       4.8 Diagnostic tree · 4.9 Testing recipes · 4.10 Adversarial · 4.11 Explain
§5 REFERENCE           5.1 Quality Constellation (7 AST gates) · 5.2 Pattern Catalog ·
                       5.3 Glossary · 5.4 Forbidden · 5.5 Rule families · 5.6 Changelog ·
                       5.7 Standards Traceability (concrete IDs)
```

International maps (ISO 25010 · CISQ · OWASP ASVS · CERT/MISRA): **Quality Constellation** in §5.1. OWASP Top 10 closure table: **A18 only**.

---

## Checker = agent job

**Roles run as sub-agents (§1.11):** the Orchestrator delegates **Analyst · Builder · Guardian · Verifier** via Task tool, each with a self-contained spawn prompt (role, tier, sections to read from this file, handoff IN, gates, output contract). Writer ≠ Verifier — adversarial review runs in a fresh session. Sub-agents return structured `[OUTPUT]`; the Orchestrator merges, dedupes, chains, and returns fixes (fix-until-green).

On ≥PRIME the agent scaffolds `scripts/prime_check/`, implements the **FOCUS 30 (mandatory honest MVP)** first → green → **then** feature work, and **ratchets** to CORE 70 / EXTENDED (138 total) by trigger/tier. `standards-map-gate` is **FOCUS+CORE** and checks **ID↔gate both ways** (ID claimed ⇒ its gate green; security gate ⇒ has an ID). A semantic gate that cannot be implemented correctly is `SKIPPED(ADR)`, **never fake-green**. Runs `--diff` → FULL until `exit 0`, prints `PRIME-VERIFY-EVIDENCE`. You do not install or run the checker.

```text
PHASE 0    Analyst   Tier + adoption_mode
PHASE 0.5  Analyst   Design Artifact + Default-secure 5Q + Threat Model 10Q + maps + AC oracles + blast
PHASE 1–3  Builder   Research → TDD-lock → ports/adapters/composition root
PHASE 4    B↔G       Fix-until-green loop   (P0 before P1 before P2)
PHASE 4.5–4.6 Guardian Security audit + review
PHASE 4.7  Builder   Docs + ADR
PHASE 4.8  Verifier  Two-Agent adversarial (another session/model)
PHASE 5    Verifier  prime_check FULL + evidence block
```

**Skip rules:** LITE = PHASE 0–3, no checker. Threat Model MUST when any Default-secure YES. Two-Agent MUST for PRIME+.

---

## License

| Use | v3.0 | v6.5 |
|-----|------|------|
| Read / fork / study | MIT | Open in repo |
| Personal / hobby | Free | Free |
| Company / team / client prod | MIT (v3) | **$50 / employee · one-time** → [@ExcitedSkam](https://t.me/ExcitedSkam) |

---

## Cursor — adopt without polluting User Rules

Keep V6.5 **in the workspace**; load on demand. Short boot rule only (path adjust as needed):

```markdown
---
description: MAWYXX PRIME boot — short; full spec on demand
alwaysApply: true
---

Project Skin + Empire Engine. Read `Mawyxx Prime V6.5.md` for architecture / merge.
No checker? Agent builds FULL per §3.2. Never ask user to run tests.
On RED: fix-until-green (P0→P1→P2). Anti-N/A · Conflict Matrix · Default-secure 5Q · A34–A47 — coverage alone ≠ done.
Unsure? §4.8 Diagnostic tree + §1.5 uncertainty table.
```

**Optional — security audit prompt:** [`Mawyxx-Security.md`](Mawyxx-Security.md) is a separate, standalone file for full-stack security reviews (`@Mawyxx-Security.md` or project rule). Not required for Prime; does not replace A18/A41 during normal development.

---

*MAWYXX PRIME · [@ExcitedSkam](https://t.me/ExcitedSkam)*
