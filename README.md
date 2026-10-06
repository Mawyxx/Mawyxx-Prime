# MAWYXX PRIME — AI Architecture Constitution & System Prompt

### For Cursor · Windsurf · Copilot · AI Agents · Zero-Trust

[![Stars](https://img.shields.io/github/stars/Mawyxx/Mawyxx-Prime?style=social)](https://github.com/Mawyxx/Mawyxx-Prime/stargazers)
[![Forks](https://img.shields.io/github/forks/Mawyxx/Mawyxx-Prime?style=social)](https://github.com/Mawyxx/Mawyxx-Prime/network/members)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/Mawyxx/Mawyxx-Prime/pulls)

[Русская версия →](README.ru.md)

![MAWYXX PRIME — AI Agent Architecture Pipeline](assets/social-preview.svg)

⭐ **If you stand for pristine code and ultimate logic — leave a Star to support the Empire.**

**Keywords:** AI coding standard · system prompt · Cursor rules · Windsurf rules · Copilot instructions · AI agents · prompt engineering · zero-trust · software architecture · clean code · MCP · production-ready.

---

## Contents

- [What is MAWYXX PRIME](#-what-is-mawyxx-prime)
- [Why AI Agents Fail](#-why-ai-agents-fail)
- [Architecture Layers RUNTIME and LAW](#-architecture-layers-runtime-and-law)
- [LAW LAYER Strict AI Coding Restrictions A01 to A64](#-law-layer-strict-ai-coding-restrictions-a01-to-a64)
- [Honesty Pillars](#-honesty-pillars)
- [Prompt Engineering Rule Map](#-prompt-engineering-rule-map)
- [Automated Quality Gate Checker](#-automated-quality-gate-checker)
- [Standards Traceability](#-standards-traceability)
- [Quick Start](#-quick-start)
- [Files](#-files)

---

## 🚀 What is MAWYXX PRIME

**v3.0** = patterns (MIT). **v6.5** = Unified Constitution: **one file**, two layers (RUNTIME + LAW), one SSOT per topic, no duplicates, **tier-aware depth over width**. Router (§0) → Work (§1) → Law (§2) → Gates (§3) → Protocols (§4) → Reference (§5).

**Laws A01–A64 + B01–B14** · 5 roles (Orchestrator · Analyst · Builder · Guardian · Verifier) · **Why** under every law · **12 GOOD/BAD patterns (anti-anchoring)** · **Reasoning protocol** · **Adversarial self-review** · **Explain/ADR protocol** · **Feature Threat Model 10Q** · **Two-Agent Verify** · **Bug→Gate** · **P0–P3 priorities** · **Diagnostic tree** · **Testing recipes** · canonical checker map (**FOCUS 30 mandatory** → CORE 70 → **138** total, ratcheted) with depth gates (`reasoning` · `adversarial` · `decision-log` · `standards-map`) · **§5.7 Standards Traceability** (OWASP · CWE · ASVS · ISO 25010/5055 · CERT/MISRA), enforced **bidirectionally** (inline `standards.yaml`).

**Project Skin · Empire Engine:** write in the project's style — with Empire discipline. Green `prime_check` from AC-names, unused ports, ignored e2e, or excluded composition is **not** done.

**Tiers:** PRIME+ only for **multi-user/PII/payments/FSM/side-effect jobs/external mutations**; single-user auth (no foreign data) → **STANDARD**. **Security:** baseline is mandatory at **every** tier (incl. LITE); only *depth* scales — no hyper-protection on simple scripts.

**Senior protocols woven throughout:** Doctrine **Ask first** · per-role **self-questions** · sub-agent **questions block** · **Domain Elicitation** (§1.12) · **Senior Debugging** 12 steps (§4.12) · **Architecture Decision** 7 steps (§4.13) · **Senior Thinking Checklist** (§4.14) · **Cross-Service** (§4.15) · **Feedback Loop** post-mortem→gate (§4.16) · **Self-Sufficiency** (§4.17 — the AI decides everything itself, no human in the loop).

**v6.5 is open in this repo** — read, fork, use.

---

## 🧠 Why AI Agents Fail

AI agents ship "green" code that lies. MAWYXX PRIME removes the evasions:

- Acceptance tied to a **test name** instead of an **observable oracle** (A34).
- **Unused ports / dead contracts** that look architectural but never run (A35/A36).
- **Swallowed errors** — `let _ =` on I/O, dump-bucket `Err` (A10).
- **Theatre checker** — `return GREEN`, existence-only steps (A22).
- **Algorithm clones** instead of one owner (A39).
- **`write-all` CI / `.env` in chat** while the app looks "secure" (A40).
- **IDOR & mass assignment** — "logged in ⇒ any id", `update(**body)` (A41).
- **Backend holes** — webhook without signature, upload without streaming/scan, no retention (A60–A63).

---

## 🏗️ Architecture Layers RUNTIME and LAW

| Layer | Purpose |
|-------|---------|
| **RUNTIME** (§0–§1) | How the agent works: router, tiers, roles, phases, sub-agents, protocols. |
| **LAW** (§2) | What the agent must/must-not do: A01–A64 + B01–B14, each with **Why**. |

---

## ⚖️ LAW LAYER Strict AI Coding Restrictions A01 to A64

| Group | Laws |
|-------|------|
| **Core** | A01 Context/tier · A02 Zero Trust · A03 API contract · A04 Plugin boundary · A05 Layer law · A05a Cohesion · A06 DI & ports · A07 Design-first · A08 Anti-fork · A09 alias→A08 · A10 Errors · A11 Decomposition |
| **Tests** | A12 Tests · A12a Taxonomy (24 families) · A13 DoD · A24 TDD-LOCK · A25 Coverage by risk · A27 Test quality · A28 Mutation |
| **Security** | A16 Secure-by-design · A18 OWASP · A19 Secrets SSOT · A29 ZTA matrix · A40 Secure Continuum · A41 Trust Pipeline · A60 Webhooks · A61 Upload safety · A63 Privacy/retention |
| **Data** | A14 Idempotency+Atomicity · A20 Migrations+Data+Transactions · A21 Contracts+Spec parity |
| **Quality** | A15 Deterministic · A17 Clean code · A22 Checker+integrity · A23 Docker/IaC · A26 Evidence · A30 Anti-slack · A31 Legacy · A32 Monorepo · A33 Blast · A34 Intent lock · A35 Contract Surface · A36 Live Surface · A39 Behavior SSOT |
| **Hardening** | A42 Bounds · A44 Dep isolation · A46 Config guard |
| **Perf/API/Ops** | A48 Performance · A50 API Hygiene · A51 alias→B03 · A52 alias→B04 · A53 alias→A14 · B03 SRE+Observability · B04 Resilience+Retry |
| **Backend** | A54 Budgets · A62 Load/soak · A64 Notifications |
| **Platform** | A55 GraphQL · A56 WebSocket · A57 Search · A58 i18n · A59 PCI |
| **Aliases** | A37→A10 · A38→A22 · A43→A14 · A45→A14 · A47→A21 · A49→A20 |

> Reference by ID: full normative text is in **`Mawyxx Prime V6.5.md`**.

---

## 🛡️ Honesty Pillars

| Pillar | Rule · gates | Kills |
|--------|--------------|-------|
| **Intent lock** | **A34** · `intent-lock-gate` | AC↔test-name synonym; AC without oracle |
| **Contract Surface** | **A35** · port-surface · composition/Fake | Concrete in UC · unused ports |
| **Live Surface** | **A36** · `live-surface-gate` | Port in yaml never called · unread field |
| **No swallow** | **A10** · no-swallow · err-variant | `let _ =` on I/O · dump-bucket Err |
| **Checker integrity** | **A22** · `checker-integrity-gate` | Theatre `return GREEN` · existence-only |
| **Behavior SSOT** | **A39** · `behavior-ssot-gate` | Algorithm clones · fake-split |
| **Secure Continuum** | **A40** · ci-harden · channel-secret · headers · cors-csrf · iac | Green zta + `write-all` · `.env` in chat |
| **Trust Pipeline** | **A41** · trust-pipeline · idor · mass-assign · path · session | "logged-in ⇒ any id" · `update(**body)` |
| **Parameter Bounds** | **A42** · `param-bounds-gate` | `digest[i]` without bounds · difficulty without clamp |
| **Idempotency & Atomicity** | **A14** · idempotency-matrix · atomicity | replay → 2 side-effects · claim without release |
| **Dependency Isolation** | **A44** · `dep-isolation-gate` | hot-path depends on cold dep |
| **Config Guard** | **A46** · `prod-guard-gate` | `if TESTING` without env-guard · fail-open |
| **Contracts & Spec Parity** | **A21** · api-contract-drift · snapshot · spec-parity | field without version · spec ≠ code |

Also: **A05a** cohesion · **A12a** taxonomy (24 families) · Anti-N/A · **A25** coverage honesty · **A33** blast · rich domain (**A05**/**B06**).

---

## 🧭 Prompt Engineering Rule Map

```text
§0 IDENTITY & ROUTER   0.3 Task router · 0.4 Tier · 0.5 Default-secure 5Q · 0.6 Principles · 0.7 Depth
§1 HOW TO WORK         1.1 Roles · 1.2 Phases · 1.3 Design Artifact · 1.5 Conflict Matrix
                       1.6 Anti-N/A · 1.7 Failure modes · 1.9 3-strike · 1.10 Reasoning (PRIME+)
                       1.11 Sub-agent execution · 1.12 Domain Elicitation
§2 LAWS (A01–A64)  —  each with Why + checklist (+ GOOD/BAD patterns on 12 key rules)
   A01 Context/tier      A14 Idempotency+Atom  A27 Test quality        A41 Trust Pipeline
   A02 Zero Trust        A15 Deterministic     A28 Mutation            A42 Param bounds
   A03 API contract      A16 Secure-by-design  A29 ZTA matrix          A44 Dep isolation
   A04 Plugin boundary   A17 Clean code        A30 Anti-slack          A46 Config guard
   A05 Layer law         A18 OWASP             A31 Legacy              A48 Performance
   A05a Cohesion         A19 Secrets SSOT      A32 Monorepo            A50 API Hygiene
   A06 DI & ports        A20 Migrations+Data   A33 Blast               A54 Budgets
   A07 Design-first      A21 Contracts+Parity  A34 Intent lock         A55–A59 Platform
   A08 Anti-fork         A22 Checker+integrity A35 Contract Surface    A60 Webhooks
   A10 Errors            A23 Docker/IaC        A36 Live Surface        A61 Upload safety
   A11 Decomposition     A24 TDD-LOCK          A39 Behavior SSOT       A62 Load/soak
   A12 Tests             A12a Taxonomy         A40 Secure Continuum    A63 Privacy/retention
   A13 DoD               A25 Coverage          A26 Evidence            A64 Notifications
   B01 CQRS … B14 Handoff Artifact
§3 GATES               3.0 groups · 3.1 algorithms · 3.2 prime_check (FOCUS 30 → CORE 70 → 138) ·
                       3.4 P0–P3 priorities · 3.5 evidence
§4 PROTOCOLS           4.1 Threat Model 10Q · 4.2 Two-Agent · 4.3 Bug→Gate · 4.4 Pre-Flight
                       4.5 Fix-until-green · 4.6 3-strike · 4.7 Decision Log · 4.8 Diagnostic tree
                       4.9 Testing recipes · 4.10 Adversarial · 4.11 Explain
                       4.12 Senior Debugging · 4.13 Architecture Decision · 4.14 Senior Thinking
                       4.15 Cross-Service · 4.16 Feedback Loop · 4.17 Self-Sufficiency
§5 REFERENCE           5.1 Quality Constellation (7 AST gates) · 5.2 Pattern Catalog ·
                       5.3 Glossary · 5.4 Forbidden · 5.5 Rule families · 5.6 Changelog ·
                       5.7 Standards Traceability (concrete IDs)
```

International maps (ISO 25010 · CISQ · OWASP ASVS · CERT/MISRA): **Quality Constellation** in §5.1. OWASP Top 10 closure table: **A18 only**.

---

## 🤖 Automated Quality Gate Checker

**Roles run as sub-agents (§1.11):** the Orchestrator delegates **Analyst · Builder · Guardian · Verifier** via Task tool, each with a self-contained spawn prompt (role, tier, sections to read, handoff IN, gates, output contract). Writer ≠ Verifier — adversarial review runs in a fresh session. Sub-agents return structured `[OUTPUT]`; the Orchestrator merges, dedupes, chains, and returns fixes (fix-until-green).

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

## 📦 Standards Traceability

Every security/quality finding maps to a concrete control ID — **OWASP Top 10 / API Top 10 · CWE Top 25 · OWASP ASVS 4.0 · ISO/IEC 25010 · ISO/IEC 5055 (CISQ) · SEI CERT · MISRA** — enforced **bidirectionally** by `standards-map-gate` (inline `standards.yaml` in §5.7.8). Full mapping: **§5.7**.

---

## ⚡ Quick Start

1. Put **`Mawyxx Prime V6.5.md`** in your repository.
2. Copy **`.cursorrules`** or **`.cursor/rules/prime.mdc`** into your project (both ship in this repo).
3. Let the agent bootstrap the quality gate (`FOCUS` → `CORE` → `FULL`) and work fix-until-green.

---

## 📁 Files

| File | Content | Access |
|------|---------|--------|
| `Mawyxx Prime V3.0.md` | Patterns · ~220 lines | **MIT** |
| `Mawyxx Prime V6.5.md` | **Single file** · Unified Constitution · **§0–§5** · **A01–A64** · **B01–B14** · §5.7 standards mapping (inline) | **Open in repo** |
| `Mawyxx-Security.md` | Standalone security-audit mega-prompt (§1.1 Surface Matrix S01–S23 · 19 sub-agents) | **Open in repo** |
| `scripts/prime_check/` | Agent creates FOCUS→CORE→FULL per §3.2 | **Not shipped** — agent bootstraps |

Full normative text lives **only** in `Mawyxx Prime V6.5.md`. This README is an index — not a second SSOT.

---

*MAWYXX PRIME · [@ExcitedSkam](https://t.me/ExcitedSkam)*
