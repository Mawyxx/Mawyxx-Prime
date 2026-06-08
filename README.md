# 👑 MAWYXX PRIME

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║  THE ENTERPRISE AI VIBE-CODING STANDARD                                      ║
║  Build for Billions. Code for Vibe. Rule with Logic.                         ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

You don't buy lint rules. You buy **liability insulation** for AI-generated code at scale.
Cursor · DeepSeek · Copilot · Claude. Any stack. **No prose. No mercy. Only evidence.**

[Russian version → README.ru.md](README.ru.md)

---

## 🔱 THE ARCHITECTURE COMPLIANCE MATRIX

```text
================================================================================
   MAWYXX PRIME v3.0 [COMMUNITY CORE]      │      MAWYXX PRIME v6.0 [GOD MODE]
================================================================================
 ✦ RISK TIERS    : Rigor by threat level   │  ✦ AGENT-OMEGA   : Phase-0 to Phase-4
 ✦ AI PROTOCOL   : Context-first engine    │  ✦ TDD-LOCK      : Failing test first
 ✦ ARCHITECTURE  : Domain-driven 4 layers  │  ✦ PILATE PROTOCOL: Liability handoff trap
 ✦ DEPENDENCY    : Injected ports via DI   │  ✦ EVIDENCE LOCK : Court-grade verify dump
 ✦ STATE ENGINE  : Strict FSM transitions  │  ✦ FORBIDDEN BUF : No word-bypasses
 ✦ INTEGRITY     : Idempotency & Events    │  ✦ LEDGER GRADE  : Financial-state proofs
 ✦ RESILIENCE    : SRE budgets & Recovery  │  ✦ SECTION 230   : Spec-shield vs impl-liability
-------------------------------------------┼------------------------------------
    TEST PYRAMID & SECURITY BASELINE       │     MUTATION & REINFORCED GATES
-------------------------------------------┼------------------------------------
 ▪ UNIT SHARD    : Domain logic, zero I/O  │  ▪ COVERAGE GOD  : 100.00% or instant 0
 ▪ CONTRACT SHARD: HTTP envelope validation │  ▪ DIFF-LOCK     : 100% only on change
 ▪ PROPERTY SHARD: Invariant fuzz testing  │  ▪ AST DETECTORS : No #pragma cheats
 ▪ INTEGRATION   : Real Docker state nodes │  ▪ FLAKY SHIELD  : Auto ×3 test runs
 ▪ SEC HYGIENE   : Baseline hygiene only    │  ▪ MATRIX GATES  : UC × Err × Status × Auth
 ▪ DEPS HARMONY  : Lockfile, zero high-CVE │  ▪ APP STORE BYPASS: Rules ≠ shippable binary
 ▪ TELEMETRY     : Domain log sanitization │  ▪ KERNEL DNAT   : Deep infra shield
================================================================================
```

*v6.0 [GOD MODE] = `Mawyxx Prime V5.2.md` · ~50 `prime_check` gates · not a linter pack*

---

## 📋 WHAT v5.2 ADDS OVER v3.0 (plain list)

**v3.0** tells the agent *what good code looks like*.  
**v5.2** makes the agent *prove it* — **by fixing and re-running until `exit 0`**. No «done» on red. No giving up.

### For the agent (how it works)

- **AGENT-OMEGA** — clear phases: plan → failing test → code → verify (no chaos)
- **Task router** — table «what you're doing → which rules to read»
- **Agent runs checks itself** — never «please run tests»
- **Forbidden phrases** — can't say «99% coverage is fine» or «tests later»
- **Evidence block** — before «done», must paste verify transcript (`exit 0`, coverage %)
- **Fix-until-green** — red gate → fix → re-run → repeat until `exit 0`; never abandon task to user
- **3-strike rule** — same patch fails 3× → redesign approach, then **keep fixing** until green

### prime_check (~50 automated gates)

- **Agent writes `prime_check`** if missing — then writes features
- **One command** for everything: `python -m scripts.prime_check`
- **Works on any stack** — Python, Node, Rust, Go, Kotlin (auto-detect)
- **CI = local** — same command in GitHub Actions and on your machine
- **~50 steps**: lint, types, tests, security, architecture, Docker, contracts

### Tests & coverage (main upgrade)

- **100% line + 100% branch** — `99.99%` = fail, not «almost»
- **TDD-LOCK** — failing test first, then code
- **Legacy mode** — old repo: 100% on *changed files only*, not whole codebase at once
- **Ratchet** — coverage can't drop vs `main`
- **No cheat tests** — empty `assert True`, `# pragma: no cover` without ADR = blocked
- **Matrices** — every error code, every HTTP status, every auth scenario = tested
- **Flaky shield** — unstable test (×3 runs) = fix before merge
- **Mutation testing** — on critical code (CRITICAL tier)

### Security & infrastructure

- **Zero Trust** — localhost and Docker are *not* trusted; auth tests mandatory
- **Full auth matrix** per route: no token → 401, bad token → 403, valid → OK
- **Secrets scan** — repo + git history, not just current files
- **CVE gate** — no high/critical vulnerabilities in lockfile
- **Docker rules** — non-root, no privileged, DB not exposed to internet
- **Health checks** — `/health`, `/ready` with tests

### Architecture & quality

- **Stable rule IDs** — `PRIME-A01`…`A32` — cite exact rule in errors
- **RFC 2119** — MUST / MUST NOT (not vague «should try»)
- **Import graph** — domain can't import infrastructure
- **File/function limits** — no 500-line monsters
- **Monorepo** — different strictness per folder (`api/` = PRIME, `scripts/` = LITE)
- **Design-first order** — contract → domain → tests → API (documented sequence)

### Production

- **SRE block** — SLI, SLO, error budget, self-healing
- **Migration gates** — DB changes only in versioned migrations
- **API drift check** — OpenAPI matches real code
- **ADR template** — why architectural decisions were made

### One-line summary

| v3.0 | v5.2 |
|------|------|
| ~220 lines, philosophy | ~1300 lines, enforcement |
| «Write clean code» | «Fix until tests pass — then prove with evidence» |
| MIT, everyone | Personal free · company → TG |

---

## ☠️ THE LIABILITY TRAP — WHY v3 IS FREE AND v6 COSTS MONEY

```text
  v3.0 [COMMUNITY CORE]
  ─────────────────────
  A philosophy PDF. MIT. Fork it. Tattoo it on your intern.
  Nobody sues you for reading Clean Architecture on GitHub.
  Your lawyer sleeps.

  v6.0 [GOD MODE]
  ───────────────
  An OPERATIONAL WEAPON you inject into CI, Cursor Rules, and remote squads.
  The moment your company runs God Mode without clearance — you didn't "try a tool".
  You DISTRIBUTED A NORMATIVE STANDARD inside a commercial organism.
  That triggers copyright. That triggers audit trails. That triggers investor due diligence.
```

**v3 teaches your agent how to think.**  
**v6 forces your agent to testify.** Every merge ships a `PRIME-VERIFY-EVIDENCE` block — a machine-generated affidavit that coverage, auth matrices, and architecture gates were satisfied **or the build never happened**.

Your General Counsel doesn't fear `gitleaks`. They fear **discoverable, reproducible proof** that engineering knew the standard and shipped anyway.

---

## 💀 OPERATIONAL EXPLOITS — NOT YOUR $5 CI LINTER PACK

Senior architects don't pay $50 for `bandit`. They pay to avoid being the person who explained to the board why AI slop shipped without **ledger-grade invariants**.

```text
  ┌─ PILATE PROTOCOL ─────────────────────────────────────────────────────────┐
  │  Wash your hands? No. Force liability to surface BEFORE merge.            │
  │  Agent cannot "looks good" — red gate → fix loop → exit 0 only.          │
  │  Uncleared corp use = YOU inherit the spec's enforcement DNA in discovery │
  └───────────────────────────────────────────────────────────────────────────┘

  ┌─ SECTION 230 SHIELD (SPEC vs SHIPMENT) ───────────────────────────────────┐
  │  The STANDARD is speech. Your PRODUCTION REPO is action.                  │
  │  Personal use: protected noncommercial expression.                        │
  │  Corporate deployment without license: commercial reproduction.           │
  │  We don't sue your vibes. We sue unauthorized DISTRIBUTION of the cage.   │
  └───────────────────────────────────────────────────────────────────────────┘

  ┌─ APP STORE BYPASS ────────────────────────────────────────────────────────┐
  │  Apple reviews binaries. GitHub does not review your Cursor Rules.        │
  │  God Mode rides the IDE — normative spec straight into the codegen loop.  │
  │  You bypass store friction. You do NOT bypass copyright on the spec.      │
  └───────────────────────────────────────────────────────────────────────────┘

  ┌─ LEDGER-GRADE ENFORCEMENT ──────────────────────────────────────────────┐
  │  Not "we log errors". Immutable test matrices: UC × Err × Route × Auth. │
  │  Financial & stateful domains get FSM + idempotency + mutation gates.   │
  │  Your auditor gets a chain of evidence — not a Jira ticket and prayers. │
  └─────────────────────────────────────────────────────────────────────────┘
```

**DIY gitleaks in 5 minutes? Congratulations.** You still don't have AGENT-OMEGA, evidence locks, diff-100 ratchet, zta-matrix, or an agent that **cannot legally say "done"** without a verify dump. That's the product.

---

## ⚖️ UNAUTHORIZED CORPORATE USE — READ THIS TO YOUR LAWYER

```text
████████████████████████████████████████████████████████████████████████████████
█  IF YOUR COMPANY RUNS v6 GOD MODE WITHOUT TELEGRAM CLEARANCE — YOU ARE LIVE █
████████████████████████████████████████████████████████████████████████████████

  You are not "evaluating a dev tool".
  You are REPRODUCING A COPYRIGHTED NORMATIVE STANDARD across employees,
  contractors, CI runners, and client deliverables.

  Our monitoring does not need your permission to notice prime_check fingerprints,
  AGENT-OMEGA phase markers, or MAWYXX rule IDs in private org repos.

  WHAT HAPPENS NEXT IS NOT A SUPPORT TICKET:

    ► DMCA STRIKE — GitHub/GitLab org-wide freeze. Your pipeline stops cold.
    ► C&D TO COUNSEL — formal notice to your legal team. Not a Discord DM.
    ► C&D TO INVESTORS — yes, your VCs get the letter. Due diligence loves surprises.
    ► STATUTORY DAMAGES — retroactive $50/seat × headcount × months of unlicensed use.
    ► COMPLIANCE EXPOSURE — "we didn't know" is not a merge strategy.

  You want God Mode in production? Fine. Act like adults. Pay $50/seat ONCE.
  Telegram. One human. No sales team. No handshake bullshit.

  Clearance: @ExcitedSkam
████████████████████████████████████████████████████████████████████████████████
```

**Personal / hobby / pet-project** → v6 God Mode: **100% FREE.** We want killers, not invoices.

---

## 🛒 COMMERCIAL CLEARANCE

```text
  $50 / employee · ONE-TIME · no subscription · no Stripe · no "enterprise demo"
  Whitelist your org · invoice if your accountant cries · case-by-case verification
```

💬 [**@ExcitedSkam**](https://t.me/ExcitedSkam) — Sovereign Architect. Direct line. No middlemen.

*Do NOT run `prime_check` on corporate metal before your org hash is cleared. We meant what we said.*

---

## 📦 DISTRIBUTION MANIFEST

```text
  [PUBLIC]    Mawyxx Prime V3.0.md      MIT · community core · bait
  [PRIVATE]   Mawyxx Prime V5.2.md       v6 God Mode · the cage
  [GENERATED] scripts/prime_check/        agent builds if missing · ~50 gates
```

---

## 🎯 DEPLOYMENT SELECTOR

```text
  Hobby / learning              →  v3.0 MIT (free, harmless)
  Personal God Mode             →  v6 FREE (enjoy the weapon)
  Company + CI + remote team    →  v6 + @ExcitedSkam OR lawsuit bingo
  Broke corp                    →  stay on v3.0 MIT — legally boring, safe
```

---

## 🧠 CONTEXT HYGIENE — DON'T DUMP 1300 LINES INTO RULES

**Full v6 spec in always-on Cursor Rules = destroyed context window.** The standard lives **locally**. You **feed** it when needed.

```text
  ✗ BAD   Paste entire Mawyxx Prime V5.2.md into .cursor/rules/ (always applied)
  ✗ BAD   Duplicate AGENT-5 + all PRIME-A rules in every chat
  ✗ BAD   Keep 3 copies: Rules + User Rules + repo (they drift and fight)

  ✓ GOOD  Standard in repo: docs/standards/ or project root
  ✓ GOOD  Tiny always-on rule (~15–40 lines) — boot contract only
  ✓ GOOD  @-mention or explicit read when task needs depth
  ✓ GOOD  prime_check in repo — enforcement is code, not prompt weight
```

### Minimal always-on rule (example)

Put this in `.cursor/rules/mawyxx-boot.mdc` — **not** the full spec:

```markdown
---
description: MAWYXX PRIME boot — load full spec on demand only
alwaysApply: true
---

Before non-trivial code: read Risk Tier from user or infer (real app = PRIME+).
Full standard: @Mawyxx Prime V5.2.md — read ONLY relevant sections (AGENT-1 router).
If no scripts/prime_check: bootstrap first (AGENT-5), then feature work.
You run prime_check yourself. Never ask user to run tests.
Before «done»: --diff → full → --evidence → exit 0.
Do NOT load entire spec every message — use task router (AGENT-1).
```

### When to feed what

| Situation | What to give the agent |
|-----------|-------------------------|
| Daily coding, small tasks | **v3.0** snippet or nothing — tier LITE/STANDARD |
| New feature / API / auth | `@V5.2` → AGENT-OMEGA + AGENT-1 row + linked PRIME-A* |
| prime_check missing | `@V5.2` → AGENT-5 only |
| Coverage / test fight | `@V5.2` → A12, A25, AGENT-VERIFY |
| Security / Docker | `@V5.2` → A02, A16, A23 + relevant steps |
| «Just fix this bug» | Paste **one** rule ID + file context — not full doc |

### Workflow

```text
  1. KEEP     Mawyxx Prime V5.2.md in repo (gitignored ok for private copy)
  2. BOOT     minimal .mdc rule (alwaysApply) — points to file, not copies it
  3. TASK     user says tier + task type → agent reads AGENT-1 → pulls 2–5 sections
  4. ENFORCE  prime_check in shell — truth lives outside the LLM context
  5. DONE     evidence block in chat — spec can be dropped from context after
```

**Rule of thumb:** Rules = **triggers**. Spec = **reference manual**. CI/`prime_check` = **judge**.

---

## ⚡ ACTIVATION SEQUENCE

```text
  [01] ACQUIRE   v5.2 spec locally (personal: free · corp: cleared via TG)
  [02] BOOT      tiny .cursor/rules/*.mdc — NOT the full 1300-line dump
  [03] LOCK      tier ≥ PRIME · greenfield | legacy
  [04] BOOTSTRAP prime_check — ZERO feature work until base is green
  [05] EXECUTE   TDD → --diff → FULL → --evidence → exit 0 or shut up
```

```bash
python -m scripts.prime_check --diff
python -m scripts.prime_check --evidence
python -m scripts.prime_check
```

`99.99%` = `0%`. Checker > agent. «Run tests yourself» = automatic bad faith.

---

## 🔒 ENFORCEMENT LOOP

```text
  TASK → prime_check? → NO → BOOTSTRAP ONLY
       → YES → DESIGN MATRIX → FAILING TEST → CODE
       → --diff → RED → FIX UNTIL GREEN → EVIDENCE → DONE ✓
```

---

*MAWYXX PRIME — the spec your agent fears · the evidence your auditor wants · the letter your investors dread*

*[@ExcitedSkam](https://t.me/ExcitedSkam)*
