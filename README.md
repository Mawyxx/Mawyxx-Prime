# MAWYXX PRIME — AI Coding Standard

*Build for Billions. Code for Vibe. Rule with Logic.*

[Russian version → README.ru.md](README.ru.md)

Two specs for the same philosophy: **v3.0** teaches patterns (MIT). **v5.2** names every rule, adds agent workflow, and requires `prime_check` to enforce them.

**v5.2 is open in this repo** — read, fork, study, use personally for free. **Corporate / team / client production** still requires a one-time license ($50/employee) → [@ExcitedSkam](https://t.me/ExcitedSkam).

---

## Files

| File | Content | Access |
|------|---------|--------|
| `Mawyxx Prime V3.0.md` | 10 sections · ~220 lines | **MIT · open** |
| `Mawyxx Prime V5.2.md` | AGENT-0…5 · **A01–A32** · **B01–B14** · ~1300 lines | **Open in repo** · corp use = paid |
| `scripts/prime_check/` | Agent builds per **AGENT-5** | Not shipped — agent creates in your project |

---

## v3.0 — patterns the standard defines

What v3 already teaches (prose, no rule IDs, no machine gate):

### Architecture & design patterns

| Pattern | What v3 requires |
|---------|------------------|
| **Clean / DDD layers** | Domain · Application · Infrastructure · Presentation |
| **DI & IoC** | Dependencies injected; no `new Repo()` inside UC |
| **Coding to interfaces** | Ports for time, ID, DB, HTTP, random, notifications |
| **Plugin boundary** | New provider via interface — no Core edits for swap |
| **CQRS** | When read/write complexity differs — not for trivial CRUD |
| **FSM** | Status entities use explicit transition graph |
| **Domain events** | Core publishes facts; infra handles delivery |
| **Idempotency** | `idempotency_key` on dangerous retries |
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

## v5.2 — what is NEW (not in v3 at all)

| Addition | Rule / module | What it does |
|----------|---------------|--------------|
| **Agent phases** | AGENT-OMEGA 0→4 | LOCK → design → TDD → implement → verify — mandatory order |
| **Task router** | AGENT-1 | Maps task type → which rules apply |
| **Merge gate spec** | A22 · AGENT-5 | `prime_check` — only way to declare «done» at PRIME+ |
| **Agent builds checker** | AGENT-5 | If no `scripts/prime_check/` → PHASE 0 bootstrap ~50 steps |
| **Fix until green** | FIX-UNTIL-GREEN · A30 | Red gate → fix → re-run — agent never abandons |
| **TDD lock** | A24 | Failing test **before** production code, same PR |
| **Evidence block** | A26 | `PRIME-VERIFY-EVIDENCE` — chat «done» without it = invalid |
| **100% coverage law** | A25 | 100.00% line **and** branch; 99.99% = fail; ratchet vs `main` |
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

---

## Cross-cutting invariants (woven into rules — like layers / SSOT)

Not a separate module. Same status as **layer law** or **SSOT** — live inside **A05 · A06 · A10 · A15 · B06**.

| Invariant | Problem v3 leaves open | Where in v5.2 | Gate |
|-----------|------------------------|---------------|------|
| **Anti-Null** | Agent `return None` → NPE / `AttributeError` downstream | **A10** Result contract — only `Result` / `Option`, explicit branches | `anti-null-gate` · `err-variant-gate` |
| **Immutability** | UC mutates `order.status` in-place → races | **A05** layer law (frozen entities) · **B06** FSM (new aggregate per transition) | `immutability-gate` |
| **Side-Effect Injection** | `datetime.now()` / `uuid4()` in UC → flaky tests | **A06** DI ports · **A15** deterministic time/ID/random | `deterministic-runtime` |

---

## v5.2 — what is IMPROVED (v3 had it → v5.2 stricter + gated)

### Architecture & patterns

| v3.0 | v5.2 improvement | Rules · gates |
|------|------------------|---------------|
| «4 layers» in prose | Layer table + import graph + **immutable domain** | **A05** · `import-boundaries` · `immutability-gate` · `handler-purity-gate` |
| DI described | Ports for time/ID/random; no concrete in UC | **A06** · `di-purity` · **A15** · `deterministic-runtime` |
| Design-first implied | Design artifact before code: routes, Err, test_matrix | **A07** · AGENT-OMEGA PHASE 1 |
| Anti-duplication verbal | No `*_v2` policy forks | **A08** · `anti-fork-gate` |
| Single policy owner | Policy facades — one SSOT | **A09** |
| Result / typed errors | **Anti-Null:** `Result`/`Option` only — no `None` in UC/domain; every Err tested | **A10** · `anti-null-gate` · `err-variant-gate` |
| File size «split if hard to test» | Hard limits: >300 fail, complexity >10 fail | **A11** · `file-size-guard` · `cyclomatic-gate` · `dead-code-gate` |
| CQRS «when needed» | Formal CQRS rule when read/write diverge | **B01** |
| FSM «no illegal jumps» | Every edge tested; transition returns **new** immutable state | **B06** · `fsm-transition-gate` · `immutability-gate` |

### Security

| v3.0 | v5.2 improvement | Rules · gates |
|------|------------------|---------------|
| 5 security bullets | Full secure-by-design + OWASP pack | **A16** · **A18** |
| «No secrets in repo» | Working tree + **full git history** scan | **A19** · `gitleaks-history` · `no-secrets` |
| «Update dependencies» | Zero high/critical CVE; SBOM | **A19** · `dependency-audit` · `sbom` |
| Input validation at boundary | + injection fuzz · SSRF allowlist | **A18** · `injection-fuzz` · `ssrf-gate` |
| No debug in prod (implied) | Explicit ban `SKIP_AUTH`, `if True:` bypass | **A16** · `no-debug-bypass` |
| No PII in logs (bullet) | Regex scan log strings | **A16** · `pii-log-scan` |
| Auth on endpoints (general) | Zero Trust: localhost = internet; deny-by-default | **A02** · `zta-matrix-gate` |
| Docker mentioned lightly | non-root · no public DB · TLS ≥1.2 · prod env | **A23** · `docker-security` · `compose-security` · `prod-config` · `tls-min-version` |

### Tests & quality

| v3.0 | v5.2 improvement | Rules · gates |
|------|------------------|---------------|
| Pyramid described | Enforced: unit → integration → contract → property | **A12** · `pytest-*` / stack equiv |
| «Key behavior» tests | Design `test_matrix` must match tests in repo | **A12** · `test-matrix-gate` |
| E2E allowed | E2E without unit base = fail | **A12** · `e2e-only-anti-pattern` |
| Coverage agent picks | 100.00% line+branch on `runtime_scope` or diff | **A25** · `coverage-*` · `no-pragma-no-cover` |
| Bug → test (norm) | Named `test_regression_*` required | **A12** · `regression-lock` |
| Property/fuzz optional | hypothesis / proptest on boundaries | **B12** · `pytest-property` |
| — | Mutation on financial/critical code | **A28** · `mutation-critical` |

### Data · contracts · ops

| v3.0 | v5.2 improvement | Rules · gates |
|------|------------------|---------------|
| Migrations implied | DDL only in `migrations/`; schema ≡ DB | **A20** · `migration-path-only` · `schema-drift` |
| OpenAPI «use schema» | OpenAPI/proto ≡ runtime; golden snapshots | **A21** · `api-contract-drift` · `snapshot-contract` |
| SemVer mentioned | Breaking change rules + contract tests | **A21** |
| SRE / events prose | Domain events in infra; error budget | **B03** · **B04** |
| Health «should» | `/health` + `/ready` tested | **B13** · `health-gate` |
| Client UI principles | lint + types + unit gate for frontend | **B11** · `frontend-quality` |
| Self-review checklist | B08 grep + **machine** pre-commit AGENT-2 | **B08** · **AGENT-2** |
| Definition of done vague | A13: thin handler · DI · Result · docs · threat model | **A13** |
| Human handoff none | B14: evidence = handoff artifact | **B14** |

---

## v5.2 rule map (full index)

```text
PART A — A01 Context/tier      A11 Decomposition       A21 SemVer/contracts
        A02 Zero Trust         A12 Tests/pyramid       A22 prime_check
        A03 API contract       A13 Definition of done  A23 Docker/infra
        A04 Plugin boundaries  A14 Idempotency         A24 TDD-LOCK
        A05 Layer law          A15 Deterministic time  A25 Coverage 100%
        A06 DI & ports         A16 Secure-by-design    A26 Evidence block
        A07 Design-first       A17 Clean code          A27 Test quality
        A08 Anti-fork          A18 OWASP/hygiene       A28 Mutation
        A09 Policy facades     A19 Supply chain        A29 ZTA matrix
        A10 Result/errors      A20 Migrations          A30 Anti-slack
                                                      A31 Legacy adoption
                                                      A32 Monorepo scope

PART B — B01 CQRS              B06 FSM                 B11 Client apps
        B02 SOLID/GRASP        B07 YAGNI               B12 Fuzz/property
        B03 SRE/observability  B08 Agent self-review   B13 Ops/runbook
        B04 Resilience         B09 ADR                 B14 Human handoff
        B05 Inter-service      B10 Performance

Cross-cutting (in A05·A06·A10·A15·B06): Anti-Null · Immutability · Side-Effect Injection
```

---

## How v5.2 verifies (prime_check)

Agent runs: `python -m scripts.prime_check` → **exit 0** + **PRIME-VERIFY-EVIDENCE**

```text
PHASE 0  bootstrap prime_check if missing
PHASE 1  design artifact (test_matrix, routes, Err list)
PHASE 2  failing tests first (TDD-LOCK)
PHASE 3  implement
PHASE 4  --only → --diff → full → evidence · fix-until-green
```

~50 steps: static · architecture · security · pyramid · matrices · coverage · data/ops · evidence.

---

## License

| Use | v3.0 | v5.2 |
|-----|------|------|
| **Read / fork / study** | MIT · open | **Open** — full spec in repo |
| **Personal / hobby / pet** | MIT · free | **Free** |
| **Company / team / client prod** | MIT (v3 only) | **$50 / employee · one-time** → [@ExcitedSkam](https://t.me/ExcitedSkam) |

Open ≠ free for corporations. The spec is public; commercial deployment on company metal requires clearance.

---

## Cursor

```markdown
# .cursor/rules/mawyxx-boot.mdc — keep short; load @Mawyxx Prime V5.2.md on demand
Real app = PRIME+. No prime_check? AGENT-5 first. Fix until exit 0. --diff → full → --evidence.
```

```bash
python -m scripts.prime_check --diff
python -m scripts.prime_check --evidence
python -m scripts.prime_check
```

---

*MAWYXX PRIME · [@ExcitedSkam](https://t.me/ExcitedSkam)*
