# MAWYXX PRIME — AI Coding Standard

*Build for Billions. Code for Vibe. Rule with Logic.*

[Russian version → README.ru.md](README.ru.md)

Two specs for the same philosophy: **v3.0** teaches patterns (MIT). **v5.7** names every rule and requires a **quality gate** that enforces **truth of outcome**, not presence of artifacts — honest N/A, test **oracles**, **live** ports, no swallowed errors, FFI on PRIME, coverage on I/O/composition, checker integrity. Compact SSOT.

**Project Skin · Empire Engine:** write in **your project's style** — but **always with Empire discipline**. A green `prime_check` built from AC-names, unused ports, `#[ignore]` e2e, and excluded composition is **not** done. Coverage % of fakes is **not** done.

**v5.7 is open in this repo** — read, fork, study, use personally for free. **Corporate / team / client production** still requires a one-time license ($50/employee) → [@ExcitedSkam](https://t.me/ExcitedSkam).

---

## Files

| File | Content | Access |
|------|---------|--------|
| `Mawyxx Prime V3.0.md` | 10 sections · ~220 lines | **MIT · open** |
| `Mawyxx Prime V5.7.md` | AGENT-0…5 · **A01–A38** (+ A05a, A12a) · **B01–B14** | **Open in repo** · corp use = paid |
| `scripts/prime_check/` | **Agent creates FULL** per **AGENT-5** (~50+ steps, config, CI) | **Not in repo** — agent bootstraps, configures, runs, fixes — **user does nothing** |

---

## v3.0 — patterns the standard defines

What v3 already teaches (prose, no rule IDs, no machine gate):

### Architecture & design patterns

| Pattern | What v3 requires |
|---------|------------------|
| **Separation of concerns** | Core ↛ I/O — often 4 roles; **folder names = project convention** |
| **DI & IoC** | Dependencies injected; no hardcoded clients in testable core |
| **Coding to interfaces** | Ports for time, ID, DB, HTTP, random, notifications |
| **Plugin boundary** | New provider via interface — no Core edits for swap |
| **CQRS** | When read/write complexity differs — not for trivial CRUD |
| **FSM** | Status entities use explicit transition graph |
| **Domain events** | Core publishes facts; infra handles delivery |
| **Idempotency** | `idempotency_key` on dangerous retries — v5.7 adds **Idempotent-Ledger** (ledger + double-submit gate) |
| **SOLID** | SRP, OCP, LSP, ISP, DIP — named in §5 |
| **Fail-fast** | Validate at system boundary |
| **Typed errors** | Domain errors, not magic exceptions in depth |
| **DI for time/ID** | `uuid()`, `Date.now()` behind interfaces — mentioned, not enforced |

### Production patterns

| Pattern | What v3 requires |
|---------|------------------|
| **Observability** | trace_id, structured logs, metrics on critical paths |
| **Resilience** | Circuit breaker, bulkheads, graceful degradation |
| **SRE** | SLI, SLO, error budget, self-healing jobs |
| **ADR** | Context · options · decision · consequences in `docs/adr/` |
| **API contracts** | OpenAPI / schema; versioned breaking changes |
| **Security hygiene** | No secrets in code; input validation; least privilege; no PII in logs |

### Testing patterns

| Pattern | What v3 requires |
|---------|------------------|
| **Pyramid** | Unit (fakes) → integration → contract |
| **DI in tests** | InMemory / Fake — predictable behavior |
| **Bug → test** | Every fix gets a regression test |
| **Coverage** | 100% on CRITICAL paths; meaningful tests elsewhere — **agent decides** |

### Agent protocol (v3 only)

- Read project context before edit
- Pick Risk Tier (LITE / STANDARD / PRIME / CRITICAL)
- Minimal scope on feature
- **Self-review checklist** (§10) before «done» — honor system, no `exit 0`

---

## v5.7 — Enforcement honesty + Contract Surface (core of current standard)

What makes the current contract hard to fake:

| Pillar | Rule / gate | What it kills |
|--------|-------------|---------------|
| **Package cohesion** | **A05a** · `package-cohesion-gate` | Flat layer-dump while import-graph is green |
| **Test taxonomy** | **A12a** · `test-taxonomy-gate` | Happy-path-only · coverage vanity without families |
| **Anti-N/A** | **A12a** · **A35** | `N/A(потом)` / `N/A(одна реализация)` when trigger fired |
| **Behavior lock** | **A34** · `intent-lock-gate` (oracle in test **body**) | AC↔test-name synonym · `assert!(!name.contains("Window"))` |
| **Live Surface** | **A36** · `live-surface-gate` | Port in yaml never called · identity/todo impl · unread Settings field |
| **No swallow** | **A37** · `no-swallow-gate` · `err-variant-gate` (provoke path) | `let _ = register` · dump-bucket Err · err test without producer |
| **Checker integrity** | **A38** · `checker-integrity-gate` | `return GREEN` · path.exists-only · `"AC{i}" in text` |
| **Coverage honesty** | **A25** · `exclude-honesty-gate` · `ignored-test-gate` | exclude composition · `#[ignore]` e2e without skipped_steps |
| **FFI on PRIME** | **A16** · `ffi-safety-gate` | unsafe without SAFETY · `safety_profile: false` while Win32 in src |
| **Blast radius** | **A33** · soft `blast-radius-gate` | Touching half the monorepo for one button |
| **Contract Surface** | **A35** · `port-surface-gate` · `composition-root-gate` · `port-test-double-gate` | Concrete infra in UC · framework DI as excuse · mock concrete instead of Fake port |
| **Rich domain / Anti-anemic** | **A05** · **B06** · `anemic-mutation-gate` | `user.status = 'active'` outside the entity · public setter without invariant |
| **Expected vs unexpected errors** | **A10** | try/catch forest in the use-case · swallowing DB-down as Ok |
| **Law→Gate** | **AGENT-5** | MUST without a real checker step |
| **Agent failure modes** | Doctrine header | Typical AI self-deception → which rule FAILs it |
| **Evidence honesty** | **A26** | Evidence lists taxonomy · **contract_surface** · **rich_domain** · **error_split** · AC · blast |

**Deprecated reading (do not apply):** «green prime_check = 10/10» · «AC name = lock» · «port in yaml = architecture» · «ignore e2e if the name exists» · «exclude composition, 100% fakes» · «unsafe OK until CRITICAL».

---

## v5.7 — what is NEW (not in v3 at all)

| Addition | Rule / module | What it does |
|----------|---------------|--------------|
| **Agent phases** | AGENT-OMEGA 0→4 | LOCK → design → TDD → implement → verify — mandatory order |
| **Design artifact** | OMEGA PHASE 1 | `capability_slices` · `acceptance_criteria` · `blast_radius` · `test_taxonomy_map` · `contract_surface_map` before code |
| **Task router** | AGENT-1 | Maps task type → which rules apply |
| **Merge gate spec** | A22 · AGENT-5 | `prime_check` — only way to declare «done» at PRIME+ |
| **Agent owns checker 100%** | AGENT-5 · A22 | No checker? Agent creates FULL: scaffold, steps, yaml, CI, deps, run, fix until green — **never asks user** |
| **Law→Gate** | AGENT-5 | Every `Enforced by:` MUST → real step in the same session |
| **AST Prosecutor** | AGENT-5 | Agent writes checker scripts; 7 AST gates + cohesion — **not shipped, not CI-only** |
| **Package cohesion** | **A05a** | Capability slices / feature packages; mirrored or vertical Skin forms |
| **Test taxonomy** | **A12a** | Normative families: unit · integration · contract/E2E · regression · mutation · property · injection · access control · scenario · acceptance · boundary · FSM · negative · observability |
| **Blast radius** | **A33** | Declare + respect minimal files/capabilities per feature |
| **Intent lock** | **A34** | Each AC carries an **oracle**; test **body** must break if behavior lied |
| **Contract Surface** | **A35** | Outbound/inbound ports · DTO/ACL · SPI · API/event · Fake vs port · composition root |
| **Live Surface** | **A36** | Declared port/field must be constructed and called; identity impl FAIL |
| **Honest errors / no swallow** | **A37** | Process-boundary Result mapped; dump-bucket FAIL; err-variant provokes producer |
| **Checker integrity** | **A38** | AST of `prime_check`: no unconditional GREEN, no existence-only, no substring-lock |
| **Rich domain / Anti-anemic** | **A05** · **B06** | Lifecycle/status via entity methods; `anemic-mutation-gate`; textbook Clean tree is a **catalog sample**, not a mandatory Skin |
| **Expected vs unexpected errors** | **A10** | Named business Err in core; infra crash → adapter + global presentation handler |
| **Fix until green** | FIX-UNTIL-GREEN · A30 | Red gate → fix → re-run — agent never abandons |
| **TDD lock** | A24 | Failing test **before** production code per applicable family + AC |
| **Evidence block** | A26 | `PRIME-VERIFY-EVIDENCE` with taxonomy/AC/blast — chat «done» without it = invalid |
| **100% coverage law** | A25 | 100.00% line **and** branch; 99.99% = fail; **does not replace** taxonomy |
| **ZTA matrix** | A02 · A29 | Every protected route × anon / expired / forbidden / valid |
| **Err matrix** | A10 · A12 | Every `Err` variant → mandatory `test_err_*` |
| **Route matrix** | A03 · A12 | method × path × HTTP status in contract tests |
| **FSM matrix** | B06 | Every transition edge + illegal jumps tested |
| **Test quality gates** | A27 | No empty tests · no `assert True` · flaky = run ×3 |
| **Mutation testing** | A28 | CRITICAL: ≥95% kill rate on `critical_scope` |
| **Legacy adoption** | A31 | Old repo: 100% on **changed files** + ratchet — not exempt |
| **Monorepo tiers** | A32 | PRIME / LITE per path in one repo |
| **Anti-slack** | A30 | No «tests next PR» · no code on red base |
| **RFC 2119** | all rules | MUST / MUST NOT — not «should» |
| **Structured report** | AGENT-5 reporter | EXEC SUMMARY · FIX PLAN · COVERAGE MAP on red |
| **Stack adapters** | AGENT-5 | python · node · rust · go · kotlin · swift |
| **Forbidden phrases** | AGENT-0 | «~99% coverage» · «run tests yourself» = violations |
| **Idempotent-Ledger gate** | A14 · A12 | `idempotency-matrix-gate` — double-submit test per state-changing UC |
| **Bounded-Context gate** | A04 · B05 | `context-leak-gate` — AST blocks cross-module domain entity imports |
| **Error Context gate** | A10 · B03 | `error-context-gate` — every `Err` = rule_id + snapshot + trace_id |
| **Quality Constellation** | Quality Constellation · A16 · A18 | ISO 25010 · ISO 5055 CISQ · OWASP Top 10/ASVS · CERT/MISRA When safety-critical |

---

## Quality Constellation — international standards (not decoration)

PRIME is not an isolated checklist. v5.7 **operationalizes** global quality and secure-coding standards into rules + machine gates:

| Standard | Role | PRIME implementation |
|----------|------|----------------------|
| **ISO/IEC 25010** | 9 measurable quality characteristics (reliability, security, maintainability…) | Each characteristic → Part A/B rules + gates (full table in spec) |
| **ISO/IEC 5055** (CISQ) | Automated structural defect detection in source | **AST Prosecutor** + static steps — 4 CISQ pillars tagged per step |
| **OWASP Top 10 · ASVS** | Web app security risks + verification depth | **A02** · **A16** · **A18** · `zta-matrix-gate` · `injection-fuzz` · ASVS scales with tier |
| **SEI CERT** | Safe systems coding (C/C++/Java) | Forbidden constructs · concurrency · memory safety **When** native/unsafe stack |
| **MISRA C/C++** | Safety-critical predictability | **CRITICAL** / embedded profile — `safety_profile` in config · `clang-tidy`/`cppcheck`/`clippy` |

**100% line+branch coverage** = ISO 25010 **Reliability** + **Maintainability** — but v5.7 also requires **taxonomy families** for Functional suitability / Security paths.  
**AST Prosecutor** = local **ISO 5055-class** analysis — agent-written, not external SaaS.  
**ZTA matrix** = closes OWASP **A01** + **A07** on every protected operation.

---

## Empire Engine outcomes (always — tier-scaled)

Not optional «where needed». **Skin** = project-native; **Engine** = always on for assigned tier. Pattern Catalog in v5.7.

| Outcome | When | Where in v5.7 | Gate |
|---------|------|---------------|------|
| **Explicit errors** | PRIME+ core | **A10** — `Result` / Go error / typed exception; no silent null as failure | `anti-null-gate` · `err-variant-gate` |
| **Immutability** | races / FSM / shared aggregate | **A05** · **B06** | `immutability-gate` |
| **Injectable nondeterminism** | PRIME+ testable core | **A06** · **A15** — ports, traits, test doubles | `deterministic-runtime` |
| **Idempotent mutations** | state-changing + retry risk | **A14** · **A09** · **A12** — key + dedup (ledger optional) | `idempotency-matrix-gate` |
| **Module isolation** | multi-module / services | **A04** · **B05** — DTO/events; shared kernel = ADR | `context-leak-gate` |
| **Package cohesion** | ≥2 capabilities / growing domain | **A05a** — mirrored slices or feature packages | `package-cohesion-gate` |
| **Test taxonomy** | STANDARD+; full matrix PRIME+ | **A12a** — applicable families or valid N/A | `test-taxonomy-gate` · matrix gates |
| **Intent lock** | PRIME+ features | **A34** — AC + oracle ↔ test body | `intent-lock-gate` |
| **Live surface** | PRIME+ · When ports/DTO | **A36** — declared must be called | `live-surface-gate` |
| **No swallow** | PRIME+ | **A37** — mapped Result; provoke err path | `no-swallow-gate` · `err-variant-gate` |
| **Checker integrity** | PRIME+ | **A38** — checker cannot be theatre | `checker-integrity-gate` |
| **Blast radius** | STANDARD+ | **A33** — minimal capabilities/files | soft `blast-radius-gate` + DoD |
| **Contract surface** | PRIME+ · When I/O / boundary | **A35** — ports · DTO · API/event · composition root | `port-surface-gate` · `composition-root-gate` · `port-test-double-gate` |
| **Rich domain** | When entity has status/lifecycle | **A05** · **B06** — mutate via entity methods, not public assign | `anemic-mutation-gate` · `fsm-transition-gate` |
| **Expected vs unexpected errors** | PRIME+ | **A10** — named Err in core; infra → global handler | `err-variant-gate` · `no-transport-in-domain` |
| **Observable failures** | PRIME+ | **A10** · **B03** · **A12a** observability family | `error-context-gate` |

---

## v5.7 — what is IMPROVED (v3 had it → v5.7 stricter + gated)

### Architecture & patterns

| v3.0 | v5.7 improvement | Rules · gates |
|------|------------------|---------------|
| «4 layers» in prose | **Separation roles** + import graph + **capability packaging** + **rich domain** | **A05** · **A05a** · `import-graph-gate` · `package-cohesion-gate` · `anemic-mutation-gate` |
| DI described | **Explicit Ports** even for one impl; framework DI wires Port→Adapter; Fake vs port | **A06** · **A35** · `port-surface-gate` · `di-purity` · `composition-root-gate` |
| Coding to interfaces (v3 prose) | Full **Contract Surface** taxonomy (outbound/inbound/DTO/SPI/API/event/DbC) | **A35** · Pattern Catalog |
| Default tier implied | **STANDARD** for app; **PRIME** when triggers (auth, PII, payments, FSM…) | **A01** |
| Python-only verify | **Quality gate contract** — stack-native entrypoint + Law→Gate | **A22** · **AGENT-5** |
| Design-first implied | Design artifact: slices, AC, blast, taxonomy map, **contract_surface_map**, routes, Err | **A07** · AGENT-OMEGA PHASE 1 |
| Anti-duplication verbal | No `*_v2` policy forks | **A08** · `anti-fork-gate` |
| Single policy owner | Policy facades — one SSOT | **A09** |
| Result / typed errors | Explicit failure paths; **expected vs unexpected**; every Err tested + error context | **A10** · `anti-null-gate` · `err-variant-gate` · `error-context-gate` |
| File size «split if hard to test» | Hard limits: >300 fail, complexity >10 fail; packages not only smaller files | **A11** · **A05a** · `file-size-guard` · `cyclomatic-gate` |
| CQRS «when needed» | Formal CQRS rule when read/write diverge | **B01** |
| FSM «no illegal jumps» | Every edge tested; transition = **entity method** + **new** immutable state When in-memory | **B06** · **A05** · `fsm-transition-gate` · `anemic-mutation-gate` · `immutability-gate` |
| Idempotency «key on retry» | **Idempotent-Ledger:** key + WAL/ledger; `test_double_submit_*` | **A14** · **A09** · `idempotency-matrix-gate` |
| Module boundaries verbal | **Bounded-Context Lock:** no shared domain entities — DTO/primitives/events only | **A04** · **A05** · **B05** · `context-leak-gate` |
| Minimal scope verbal | **Blast radius** declared and soft-gated | **A33** · `blast-radius-gate` |
| «Interface only if 2+ impl» | **I/O → port always** on PRIME+; YAGNI only for pure functions | **A35** · **A04** · **A06** |

### Security & international standards

| v3.0 | v5.7 improvement | Rules · gates |
|------|------------------|---------------|
| 5 security bullets | Full secure-by-design + **OWASP Top 10 table** + ASVS by tier | **A16** · **A18** · Quality Constellation |
| No ISO mapping | **ISO 25010** 9 characteristics → rules/gates | Quality Constellation |
| No structural defect standard | **ISO 5055 CISQ** → AST Prosecutor pillars | AGENT-5 · 7 AST gates · `package-cohesion-gate` |
| No safety-critical profile | **CERT/MISRA** When C/C++/embedded/CRITICAL | `safety_profile` · `cert-forbidden-gate` |
| «No secrets in repo» | Working tree + **full git history** scan | **A19** · `gitleaks-history` · `no-secrets` |
| «Update dependencies» | Zero high/critical CVE; SBOM | **A19** · `dependency-audit` · `sbom` |
| Input validation at boundary | + injection fuzz · SSRF allowlist | **A18** · `injection-fuzz` · `ssrf-gate` |
| No debug in prod (implied) | Explicit ban `SKIP_AUTH`, `if True:` bypass | **A16** · `no-debug-bypass` |
| No PII in logs (bullet) | Regex scan log strings | **A16** · `pii-log-scan` |
| Auth on endpoints (general) | Zero Trust: localhost = internet; deny-by-default | **A02** · `zta-matrix-gate` |
| Docker mentioned lightly | non-root · no public DB · TLS ≥1.2 · prod env | **A23** · `docker-security` · `compose-security` · `prod-config` · `tls-min-version` |

### Tests & quality

| v3.0 | v5.7 improvement | Rules · gates |
|------|------------------|---------------|
| Pyramid described | Enforced pyramid **plus** normative **taxonomy families** | **A12** · **A12a** · `test-taxonomy-gate` |
| «Key behavior» tests | `test_matrix` + `test_taxonomy_map` + Anti-N/A | **A12** · **A12a** · `test-matrix-gate` |
| Acceptance verbal | Each AC ↔ **oracle in test body** | **A34** · `intent-lock-gate` |
| E2E allowed | E2E without unit base = fail; API-only uses contract@boundary | **A12** · **A12a** · `e2e-only-anti-pattern` |
| Coverage agent picks | 100.00% line+branch **and** taxonomy green | **A25** · **A12a** · `coverage-*` |
| Bug → test (norm) | Named `test_regression_*` required | **A12** · `regression-lock` |
| Property/fuzz optional | hypothesis / proptest on boundaries | **B12** · `pytest-property` |
| Mutation on financial/critical code | **PRIME greenfield MUST** on `critical_scope`; CRITICAL ≥95% | **A28** · `mutation-critical` |

### Data · contracts · ops

| v3.0 | v5.7 improvement | Rules · gates |
|------|------------------|---------------|
| Migrations implied | DDL only in `migrations/`; schema ≡ DB | **A20** · `migration-path-only` · `schema-drift` |
| OpenAPI «use schema» | OpenAPI/proto ≡ runtime; golden snapshots | **A21** · `api-contract-drift` · `snapshot-contract` |
| SemVer mentioned | Breaking change rules + contract tests | **A21** |
| SRE / events prose | Domain events in infra; error budget | **B03** · **B04** |
| Health «should» | `/health` + `/ready` tested | **B13** · `health-gate` |
| Client UI principles | lint + types + unit gate for frontend | **B11** · `frontend-quality` |
| Self-review checklist | B08 grep + **machine** pre-commit AGENT-2 | **B08** · **AGENT-2** |
| Definition of done vague | A13: thin handler · DI · Result · taxonomy · AC · blast · threat model | **A13** |
| Human handoff none | B14: evidence = handoff artifact | **B14** |

---

## v5.7 rule map (full index)

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
        A09 Policy facades     A19 Supply chain        A30 Anti-slack
        A10 Result/errors      A20 Migrations          A31 Legacy adoption
                                                      A32 Monorepo scope
                                                      A33 Blast radius
                                                      A34 Behavior lock
                                                      A35 Contract Surface
                                                      A36 Live Surface
                                                      A37 Honest errors
                                                      A38 Checker integrity

PART B — B01 CQRS              B06 FSM                 B11 Client apps
        B02 SOLID/GRASP        B07 YAGNI               B12 Fuzz/property
        B03 SRE/observability  B08 Agent self-review   B13 Ops/runbook
        B04 Resilience         B09 ADR                 B14 Human handoff
        B05 Inter-service      B10 Performance

Outcomes: Behavior lock · Live surface · No swallow · Checker integrity · Explicit errors · Rich domain When · Test taxonomy (oracle APPLIED) · Contract surface · Coverage honesty · FFI When
```

---

## Checker = agent job (not yours)

On tier ≥ PRIME the **agent** owns the quality gate end-to-end:

```text
MISSING?  → agent scaffolds scripts/prime_check/ + all applicable step modules
CONFIG?   → agent writes prime_check.config.yaml (tier, scopes, capabilities, ports, composition_root)
CI?       → agent adds workflow — same command as local
DEPS?     → agent adds pytest/ruff/eslint/… for gates
LAW→GATE? → every Enforced-by MUST has a real step — no stubs
RUN?      → agent executes in shell — never «run tests yourself»
RED?      → agent fixes code AND/OR checker → re-run → exit 0
DONE?     → agent prints PRIME-VERIFY-EVIDENCE (taxonomy + contract_surface + AC + blast)
```

**You** don't install, configure, or run the checker. **Agent does.**

## How v5.7 verifies

```text
PHASE 0  agent bootstraps FULL checker if missing (STOP feature until green)
PHASE 1  design artifact: slices · AC · blast · test_taxonomy_map · contract_surface_map
PHASE 2  failing tests first (TDD-LOCK) per family + AC — against Fake ports
PHASE 3  implement inside blast_radius — ports before adapters
PHASE 4  --only → --diff → full → evidence · fix-until-green
```

~50+ steps: static · **AST Prosecutor (7 gates + cohesion + port-surface)** · security · pyramid · **taxonomy / intent-lock / contract surface** · matrices · coverage · data/ops · evidence.

**AST Prosecutor ≠ CI wrapper.** Checker parses import graphs and AST locally — agent words don't count, `exit 0` does.

**FULL-COLLECTION:** default run hits **all** steps, collects **all** failures — one report, not whack-a-mole.

**On RED:** EXEC SUMMARY → FIX PLAN (P1→P3) → Finding cards (`file:line`, snippet, hint, rerun). Agent **batch-fixes entire P1 group** → one rerun — not fix-one-rerun-loop.

---

## License

| Use | v3.0 | v5.7 |
|-----|------|------|
| **Read / fork / study** | MIT · open | **Open** — full spec in repo |
| **Personal / hobby / pet** | MIT · free | **Free** |
| **Company / team / client prod** | MIT (v3 only) | **$50 / employee · one-time** → [@ExcitedSkam](https://t.me/ExcitedSkam) |

Open ≠ free for corporations. The spec is public; commercial deployment on company metal requires clearance.

---

## Cursor — how to adopt (don't pollute global rules)

**Do not** paste the full v5.7 spec into `.cursor/rules` or User Rules. The spec in always-on context burns tokens, fights project rules, and the agent still won't internalize everything — it needs the file when the task needs it.

**Do** keep the spec **locally in the workspace** and load it **on demand**.

### 1. Put the file in your project

Pick one:

| Method | When |
|--------|------|
| **Copy** `Mawyxx Prime V5.7.md` into the repo (e.g. `docs/standards/`) | Simplest — one file, version pinned by you |
| **Submodule** this repo into `standards/mawyxx-prime/` | Pin a commit; `git submodule update` when you upgrade |
| **Clone** beside the project and add both folders to one Cursor workspace | Spec lives outside app repo — fine for personal use |

The agent must be able to **read the path** — `@` mention or `Read` tool. No cloud-only link required.

### 2. Short boot rule only

One small rule in `.cursor/rules/mawyxx-boot.mdc` (or project `AGENTS.md` one-liner). **Boot, not textbook:**

```markdown
---
description: MAWYXX PRIME boot — short; full spec on demand
alwaysApply: true
---

Project Skin + Empire Engine. Tier by risk (see spec §Tier).
Full rules: read `docs/standards/Mawyxx Prime V5.7.md` when starting work, changing architecture, or before merge — do not guess.
No checker? Agent builds FULL per AGENT-5 (steps, config, CI) — runs & fixes alone. Never ask user to run tests.
On RED: FULL-COLLECTION report → batch-fix P1 → rerun.
Anti-N/A · taxonomy · intent lock · blast radius · **contract surface (ports)** — coverage alone ≠ done.
```

Adjust the path to where you copied the file.

### 3. Load on demand — you or the agent

| Who | How |
|-----|-----|
| **You** | `@Mawyxx Prime V5.7.md` (or your path) at task start: «implement X per PRIME», «bootstrap checker», «fix RED» |
| **Agent** | Boot rule says read spec → agent opens file itself; for narrow tasks, read only **AGENT-*** / **A*** / **B*** sections cited in the task |
| **Neither** | v3.0-only vibe coding with no tier — boot rule optional |

**Good:** boot rule + local file + `@` when stakes are high.  
**Bad:** entire v5.7 in User Rules; duplicating A01–A38 into ten `.mdc` files; expecting the agent to remember last week's chat instead of re-reading AGENT-5.

### 4. Checker commands (after agent bootstraps `scripts/prime_check/`)

```bash
python -m scripts.prime_check --diff
python -m scripts.prime_check --evidence
python -m scripts.prime_check
```

User does not run these — agent does. Listed here so you know what «green» means.

---

*MAWYXX PRIME · [@ExcitedSkam](https://t.me/ExcitedSkam)*
