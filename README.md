# MAWYXX PRIME — AI Coding Standard

*Build for Billions. Code for Vibe. Rule with Logic.*

[Russian version → README.ru.md](README.ru.md)

Normative specs for AI agents writing production code. Two tiers: **v3.0** (principles, MIT) and **v5.2** (enforcement layer, marketed as v6 God Mode).

---

## What is in this repo

| File | What it is |
|------|------------|
| `Mawyxx Prime V3.0.md` | ~220 lines · 10 sections · philosophy & architecture · **MIT · public** |
| `Mawyxx Prime V5.2.md` | ~1300 lines · AGENT-0…5 · rules A01–A32 · B01–B14 · **private / commercial** |
| `scripts/prime_check/` | Not shipped — **agent builds it** per AGENT-5 when tier ≥ PRIME |

**v3.0** — tells the agent *what good code looks like*.  
**v5.2** — adds *how the agent must verify it*: phases, `prime_check`, coverage law, evidence block.

---

## v3.0 vs v5.2 at a glance

```text
================================================================================
   v3.0 [PRINCIPLES]                      │   v5.2 [ENFORCEMENT]
================================================================================
 Risk tiers LITE → CRITICAL               │   Same tiers · default PRIME for real apps
 Read context · minimal scope             │   AGENT-OMEGA phases 0 → 4 (mandatory order)
 Self-review checklist (§10)             │   AGENT-2 checklist + machine gates
 4 layers · DI · FSM · idempotency        │   Same + import-graph · di-purity gates
 Security · tests · SRE in prose         │   ~50 prime_check steps per stack adapter
 «Tests on key behavior»                 │   100.00% line + branch (tier ≥ PRIME)
 «100% on CRITICAL paths»                │   diff-100 · ratchet vs main · legacy mode
 No merge gate                            │   exit 0 = only valid «done»
================================================================================
```

*v6 / God Mode in marketing = `Mawyxx Prime V5.2.md` + agent-built `prime_check`*

---

## v3.0 — the standard (summary)

Universal quality standard for AI coders. Proportional rigor by **Risk Tier**:

| Tier | Scope |
|------|--------|
| **LITE** | Scripts, one-off tools — readability, no secrets |
| **STANDARD** | Regular features — modules, key tests, clear errors |
| **PRIME** | Auth, payments, PII, APIs — layers, DI, FSM, observability |
| **CRITICAL** | Finance, compliance — PRIME + ADR, resilience, max test depth |

**Covers:** 4-layer boundaries · DI & interfaces · SOLID · typed errors · FSM · domain events · SRE/ADR · security hygiene · test pyramid · self-review checklist.

**Does not cover:** automated merge gate · mandatory coverage % · agent-run verify loop · `prime_check` spec.

---

## v5.2 — what the standard adds

Same architecture philosophy as v3. **Plus** agent contract and machine verification.

### Agent workflow (AGENT-OMEGA)

```text
PHASE 0  tier ≥ PRIME? → prime_check missing? → bootstrap AGENT-5 only (no feature code)
PHASE 1  design artifact: files · routes · Err variants · test_matrix
PHASE 2  TDD-LOCK: failing test before implementation
PHASE 3  implement (minimal feature scope · max quality scope)
PHASE 4  prime_check --only → --diff → full → exit 0 → PRIME-VERIFY-EVIDENCE
         RED → fix-until-green (agent does not stop · does not ask user to run tests)
```

### prime_check (AGENT-5)

Single CLI the agent creates and maintains: `python -m scripts.prime_check`

| Group | Examples of steps |
|-------|-------------------|
| Static | lint · typecheck · format · dead-code · file-size · complexity |
| Architecture | import boundaries · DI purity · no SQL strings · no transport in domain |
| Security | gitleaks history · CVE audit · bandit · PII in logs · SSRF · ZTA matrix |
| Tests | unit · integration · contract · property · flaky ×3 · empty/trivial test ban |
| Matrices | err-variant · route × status · FSM transitions · design test_matrix |
| Coverage | line 100% · branch 100% · diff-100 · ratchet · no pragma without ADR |
| Data/Ops | schema drift · API contract drift · docker security · health probes |
| Output | structured report · evidence block |

Stack adapters: **python · node · rust · go · kotlin · swift** — same rules, local linters.

### Done definition (tier ≥ PRIME)

- `python -m scripts.prime_check` → **exit 0**
- **PRIME-VERIFY-EVIDENCE** block printed in agent response
- Without both — response is **invalid** per A26

---

## PRIME UPGRADE SCAN — standard delta

```text
══════════════════════════════════════════════════════════════════════════════
 STANDARD DELTA                          v3.0 [MIT]  →  v5.2
══════════════════════════════════════════════════════════════════════════════
  Volume        10 sections · ~220 lines          A01–A32 · B01–B14 · AGENT-0…5
  Voice         recommendations                 RFC 2119 MUST / MUST NOT
  Agent model   read → code → self-review         AGENT-OMEGA 0 → 4
  «Done»        agent declares                    exit 0 + evidence block
  Merge gate    none                              prime_check (~50 steps)
──────────────────────────────────────────────────────────────────────────────

▸ ONLY IN v5.2
  prime_check · FIX-UNTIL-GREEN · TDD-LOCK (A24) · evidence block (A26)
  ~50 gates · 100% line+branch · ZTA/Err/Route/FSM matrices
  legacy diff-100 + ratchet (A31) · monorepo tiers (A32) · mutation (A28)
  stack adapters · structured report · forbidden phrases · anti-slack (A30)

▸ IN v3.0 — MADE ENFORCEABLE IN v5.2
  tiers · layers · DI · FSM · security §7 · tests §8 · SRE · ADR · docker
  → import-graph · err-variant · fsm-transition · gitleaks · schema-drift gates

▸ COVERAGE LINE
  v3.0   agent chooses «key paths» · 100% mentioned for CRITICAL only
  v5.2   99.99% = fail · pragma needs ADR · coverage cannot drop vs main

▸ VERIFY COMMAND (defined only in v5.2)
  python -m scripts.prime_check --diff → full → --evidence → exit 0
══════════════════════════════════════════════════════════════════════════════
```

---

## License

| Use | v3.0 | v5.2 |
|-----|------|------|
| Personal / hobby / pet project | MIT · free | **Free** |
| Company / team / client prod | MIT for v3 only | **$50 / employee · one-time** → Telegram |

Corporate use of v5.2 without clearance: contact before deploying on company runners or client code.

💬 [**@ExcitedSkam**](https://t.me/ExcitedSkam)

---

## Quick reference

```text
  Hobby / learning     →  Mawyxx Prime V3.0.md (MIT)
  Real app + AI agent  →  Mawyxx Prime V5.2.md + bootstrap prime_check

  python -m scripts.prime_check --diff
  python -m scripts.prime_check --evidence
  python -m scripts.prime_check
```

---

## Using v5.2 in Cursor

Do not paste all ~1300 lines into always-on Rules — context window drops enforcement weight.

```text
  ✗ Full V5.2 in alwaysApply every message
  ✓ Small boot rule (~20 lines) + @Mawyxx Prime V5.2.md when the task needs it
  ✓ prime_check in repo = verification lives outside the chat window
```

`.cursor/rules/mawyxx-boot.mdc`:

```markdown
---
description: MAWYXX boot — load spec on demand
alwaysApply: true
---
Real app = PRIME+. Spec: @Mawyxx Prime V5.2.md (AGENT-1 sections as needed).
No prime_check? Bootstrap AGENT-5 first. You run prime_check. Fix until exit 0.
Before done: --diff → full → --evidence.
```

---

*MAWYXX PRIME — v3 principles · v5.2 enforcement · [@ExcitedSkam](https://t.me/ExcitedSkam)*
