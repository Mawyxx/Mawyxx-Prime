# MAWYXX PRIME: Enterprise Vibe-Coding Standard (v5.2)

*«Build for Billions. Code for Vibe. Rule with Logic.»*

**Agent contract** — единый нормативный файл для ИИ-кодера. Универсальный: любой стек, любой домен, любой размер проекта.

**Цель:** **High Cohesion** внутри модулей, **Low Coupling** между ними. Код предсказуемый, тестируемый, наблюдаемый, готовый к росту.

**Сквозные инварианты (как layer law / SSOT — не отдельный модуль):**
- **Anti-Null** — [A10](#prime-a10--result): UC/domain возвращают `Result` / `Option`, не `None` / `null`
- **Immutability** — [A05](#prime-a05--layer-law) · [B06](#prime-b06--fsm): domain entities frozen; transition = новый экземпляр
- **Side-Effect Injection** — [A06](#prime-a06--di--ports) · [A15](#prime-a15--deterministic-time): time/ID/random только через ports

### ZERO-TOLERANCE doctrine (tier ≥ PRIME)

| Запрет | Enforcement |
|--------|-------------|
| Непокрытая строка в `runtime_scope` / diff | `coverage-line-100` → exit 1 |
| Непокрытая ветка (branch) | `coverage-branch-100` → exit 1 |
| Coverage упал vs `main` | `coverage-ratchet` → exit 1 |
| `# pragma: no cover` без ADR | `no-pragma-no-cover` → exit 1 |
| Пустой / trivial test | `no-empty-test` → exit 1 |
| Непротестированный `Err` код UC | `err-variant-gate` → exit 1 |
| HTTP route без contract-тестов | `route-matrix-gate` → exit 1 |
| Endpoint без auth matrix | `zta-matrix-gate` → exit 1 |
| Secret в repo / history / логах | `gitleaks-history` → exit 1 |
| Domain импортирует infra | `import-graph-gate` → exit 1 |
| `Date.now` / `uuid4` в domain/app | `deterministic-runtime` → exit 1 |
| `return None` / `null` в UC/domain | `anti-null-gate` → exit 1 |
| Мутация entity/VO в UC/domain | `immutability-gate` → exit 1 |
| Небезопасный Docker/compose | `docker-security` → exit 1 |
| CVE в dependencies (high/critical) | `dependency-audit` → exit 1 |
| «Готово» без evidence block | `evidence-block` → invalid response |
| Merge без `prime_check` green | **запрещён** |

**Нет «норм сойдёт».** `99.99%` = `0%`. Tier ≥ PRIME = **чинить до green**, не сдавать задачу.

### FIX-UNTIL-GREEN (главный закон агента)

- **MUST:** `prime_check` red → **чинить код/тесты → re-run** → повторять до `exit 0`.
- **MUST NOT:** останавливаться с красным gate и говорить «готово» / «не получилось» / «запустите сами».
- **MUST NOT:** бросать задачу пользователю с exit ≠ 0 — **ты** доводишь до green.
- **MUST NOT:** переключаться на другую фичу, пока текущая не green (кроме bootstrap `prime_check` по AGENT-5).
- **Stop-the-line** = не **наращивать** сломанный фундамент новым кодом; **не** = «бросить и уйти». Сломано → чини → green → продолжай.

```yaml
audience: ai_coders
doctrine: zero_tolerance
fix_until_green: true                 # red gate → fix loop until exit 0 — NEVER abandon task
principles: high_cohesion | low_coupling | zero_trust
normative_keywords: RFC_2119
self_correction: stop_the_line        # pause NEW layers on broken base; still FIX until green
agent_phases: OMEGA → BOOT → ROUTE → VERIFY   # see AGENT-OMEGA
agent_runs_verify: true
agent_bootstraps_prime_check: true
agent_evidence_required: true
verify_final: python -m scripts.prime_check
verify_evidence: python -m scripts.prime_check --evidence
risk_tiers: LITE | STANDARD | PRIME | CRITICAL
default_tier_real_project: PRIME
adoption_mode: greenfield | legacy          # legacy = diff-100 + ratchet
test_pyramid: unit → integration → contract → property
coverage: 100_percent_line_and_branch
coverage_legacy: 100_percent_on_changed_files_only
adr_dir: docs/adr/
prime_check_config: scripts/prime_check.config.yaml
stack_adapters: python | node | rust | go | kotlin | swift
```

**Agent rule:** нет `prime_check` (tier ≥ PRIME) → **только bootstrap**, потом фича.  
**Agent rule:** checker = истина; red → **fix loop** до `exit 0` + evidence block — **не stop, а repair**.  
**Agent rule:** при конфликте PRIME vs конвенции → конвенции на *пути*; PRIME на *качество и безопасность*.

---

## AGENT-OMEGA — Execution phases (before any code)

**MUST** выполнить фазы **в порядке**. Пропуск фазы = нарушение PRIME.

### PHASE 0 — LOCK

```text
assign tier → tier ≥ PRIME?
  → prime_check exists? NO → STOP all feature work → bootstrap AGENT-5 only
  → adoption_mode? greenfield | legacy (A31)
  → stack? detect → pick adapter (AGENT-5 stack matrix)
```

### PHASE 1 — DESIGN ARTIFACT (в ответе до кода)

```text
files_to_touch: [...]
new_err_variants: [...]
new_routes: [method path → statuses]
fsm_transitions: [...]
test_matrix: UC × input × expected Err/Ok × HTTP status
```

### PHASE 2 — TDD-LOCK ([A24](#prime-a24--tdd-lock))

- **MUST:** для каждого нового поведения — **сначала failing test**, потом код.
- **MUST NOT:** «тесты в следующем PR».
- **MUST NOT:** код без строки в test_matrix.

### PHASE 3 — IMPLEMENT

Минимальный scope на фичу; максимальный на качество.

### PHASE 4 — VERIFY LOOP · FIX UNTIL GREEN ([AGENT-VERIFY](#agent-verify--you-run-prime_check))

```text
edit → prime_check --only <step> → RED → FIX → re-run → … → GREEN
all touched → prime_check --diff → RED → FIX → re-run → … → GREEN
session end → prime_check FULL → RED → FIX → re-run → … → exit 0  (mandatory)
print PRIME-VERIFY-EVIDENCE block ([A26](#prime-a26--evidence-block))
```

**Нет легального выхода с exit ≠ 0.** Агент **не останавливает задачу** — итерирует fix → re-run до green.

### Forbidden phrases (MUST NOT в ответе пользователю)

- «покрытие ~99%» / «достаточно для merge»
- «запустите тесты» / «проверьте сами»
- «prime_check добавим позже»
- «edge case — можно без теста»
- «тесты в отдельном PR»
- «не могу починить» / «оставим красным» / «нужна ваша помощь с тестами»
- «остановился, т.к. gate падает» — **fix until green**, не stop

### 3-strike rule ([A30](#prime-a30--anti-slack))

Один step падает **3 раза подряд** с **тем же патчем** → **redesign** (другой подход) + ADR → **продолжай fix loop** до green. Не бросать задачу.

---

## AGENT-0 — Boot (read first)

### Role

Ты пишешь и меняешь код **в рамках задачи пользователя**, соблюдая конвенции репозитория.

- **MUST:** определи **Risk Tier** ([A01](#prime-a01--context--risk-tier)). Реальный проект (app/API/service) = минимум **PRIME**.
- **MUST:** если `scripts/prime_check` **отсутствует** и tier ≥ PRIME → **STOP feature work** → bootstrap [AGENT-5](#agent-5--prime-check) → CI → потом продолжай.
- **MUST:** **минимальный scope** на фичу; **максимальный scope** на качество — тесты и security не режутся.
- **MUST:** пройти [AGENT-OMEGA](#agent-omega--execution-phases-before-any-code) фазы 0–4.
- **MUST:** после **каждого** нетривиального edit — `prime_check --only <relevant>`; перед «done» — `--diff` then **full** ([AGENT-VERIFY](#agent-verify--you-run-prime_check)).
- **MUST:** напечатать **PRIME-VERIFY-EVIDENCE** block ([A26](#prime-a26--evidence-block)) — без него ответ невалиден.
- **MUST NOT:** говорить пользователю «запусти тесты» — **ты** запускаешь в shell.
- **MUST NOT:** помечать done при exit ≠ 0, без evidence, без full `prime_check` на tier ≥ PRIME.

### Self-correction (stop-the-line + fix-until-green)

- **MUST:** перед edit — scan файла и imports ([A05](#prime-a05--layer-law), [A10](#prime-a10--result), [A17](#prime-a17--clean-code), [A18](#prime-a18--owasp), [A20](#prime-a20--migrations)). Фундамент сломан → **не наращивай** новый код; **чини** нарушение → rule ID + location → re-verify.
- **MUST:** verify red → read **EXEC SUMMARY + FIX PLAN** из отчёта ([Report output](#report-output--agent-readable-diagnostics)) → **fix** по P1→P3 → re-run hint cmd → repeat until green. Не сдавай задачу.
- **MUST:** при сомнении → pause **новых** edits; прочитай PRIME/ADR → **fix** → continue.
- **MUST NOT:** продолжать multi-file генерацию поверх layer/Result/security violation.
- **MUST NOT:** declare done или уходить в новую фичу при exit ≠ 0.

### RFC 2119

| Keyword | Meaning |
|---------|---------|
| **MUST** | Обязательно для данного tier |
| **MUST NOT** | Запрещено; stop and redesign |
| **SHOULD** | По умолчанию; пропуск с обоснованием |
| **MAY** | Опционально |

### Risk Tiers

| Tier | Примеры | PRIME depth |
|------|---------|-------------|
| **LITE** | Скрипты, прототипы, одноразовые утилиты | Читаемость, scope, fail-fast, no secrets ([B07](#prime-b07--yagni)) |
| **STANDARD** | Фичи, UI, CRUD, интеграции | Модули, тесты на поведение, typed errors, no magic values |
| **PRIME** | Auth, PII, платежи, внешние API, job'ы | Part A + B: слои, DI, Result, observability, idempotency, FSM |
| **CRITICAL** | Финансы, compliance, потеря данных | PRIME + ADR, resilience, max coverage, Threat Model |

**Правило:** при сомнении — tier выше, но не выше задачи.

### Анти-паттерны (когда НЕ применять PRIME)

- Interface для единственной реализации без планов замены.
- Event bus / CQRS / 4 слоя для CRUD из 3 полей.
- ADR на rename переменной или тривиальный фикс.
- Абстракция «на будущее» (YAGNI).
- 5 слоёв для скрипта на 30 строк.

### Layer map (clean architecture)

| Layer | Typical paths | Role |
|-------|---------------|------|
| **Domain** | `domain/`, `core/`, `entities/` | Entities, VO, events, invariants, port interfaces |
| **Application** | `application/`, `usecases/` | Use cases, orchestration, Result |
| **Infrastructure** | `infrastructure/`, `adapters/` | **All I/O:** DB, HTTP, queues, files |
| **Presentation** | `api/`, `routes/`, `ui/`, `cli/` | Transport: validate → call UC → map response |

**Dependency direction:**

```text
Presentation → Application → Domain ← Infrastructure (implements ports)
```

Domain **never** imports Infrastructure or Presentation.

### Global FORBIDDEN

- **MUST NOT:** construct use-cases inside handlers (`new SomeUseCase(...)`).
- **MUST NOT:** business policy in infrastructure adapters.
- **MUST NOT:** duplicate auth / validation / idempotency / error-mapping ([A08](#prime-a08--anti-fork)).
- **MUST NOT:** trust `localhost` / docker / «internal» route ([A02](#prime-a02--zero-trust)).
- **MUST NOT:** `Date.now()`, `uuid()`, `random()` in Domain/Application ([A15](#prime-a15--deterministic-time)).
- **MUST NOT:** secrets in repo, logs, tests ([A16](#prime-a16--secure-by-design), [A19](#prime-a19--supply-chain)).
- **MUST NOT:** string-built SQL; DDL from use-case/handler ([A18](#prime-a18--owasp), [A20](#prime-a20--migrations)).
- **MUST NOT:** ad-hoc `pip install` / `npm install` без lockfile ([A19](#prime-a19--supply-chain)).
- **MUST NOT:** one class mixing unrelated business policies ([A17](#prime-a17--clean-code)).

### Forbidden patterns (security)

- **MUST NOT:** `eval`, `exec`, dynamic import on untrusted strings.
- **MUST NOT:** `innerHTML` / `dangerouslySetInnerHTML` без ADR + sanitization.
- **MUST NOT:** session tokens / secrets in `localStorage` без ADR.
- **MUST NOT:** ORM `create_all()` / raw DDL on prod.
- **MUST NOT:** debug auth bypass (`if True:`, `# TODO remove` credentials).

### External docs (load when needed)

| Task | Read |
|------|------|
| API shape, status codes | OpenAPI / README / API docs |
| Auth, tokens | Security docs / ADR |
| Secrets, env | `.env.example` / secrets docs |
| Why decision | `docs/adr/<relevant>.md` |
| Versioning | Changelog / API versioning policy |

---

## AGENT-1 — Task router

| Task | Tier | PRIME sections | After code, **you** run |
|------|------|----------------|-------------------------|
| **No prime_check in repo** | ≥PRIME | AGENT-5, A22 | **WRITE prime_check first** → full green |
| Legacy repo bootstrap | ≥PRIME | A31, AGENT-5 | `adoption_mode: legacy` + diff gates |
| Monorepo path | varies | A32 | per-path tier in config |
| Any runtime code change | ≥PRIME | A01–A32, B03–B14 | `prime_check --diff` then **full** |
| New/changed HTTP endpoint | ≥PRIME | A02, A03, A29 | `route-matrix-gate` + `zta-matrix-gate` |
| New feature / provider | ≥PRIME | A04–A07, A12, A24 | TDD → `pytest-unit` → full |
| Auth / session | ≥PRIME | A02, A16, A29 | `zta-matrix-gate` |
| DB schema / persistence | ≥PRIME | A20, B06 | integration + `schema-drift` |
| New dependency | any | A19 | `dependency-audit` + lockfile |
| Docker / compose / deploy | ≥PRIME | A16, A23 | `docker-security` + `prod-config` |
| Idempotency / retries | ≥PRIME | A14, A09 | integration + contract |
| Stateful entity (status) | ≥PRIME | B06, A14 | concurrency integration |
| Client UI | ≥PRIME | B11, A18 | `frontend-quality` + full |
| Financial / compliance | CRITICAL | All + B09 | full + `mutation-critical` + `injection-fuzz` |
| Ops / deploy / health | ≥PRIME | B13, A23 | `health-gate` + `prod-config` |
| Script only (no network) | LITE | B07 | smoke only — no prime_check required |

---

## AGENT-2 — Pre-commit checklist (merge gate)

```text
[ ] AGENT-OMEGA phases 0–4 completed
[ ] prime_check EXISTS — bootstrapped THIS session if was missing (AGENT-5)
[ ] adoption_mode set (greenfield | legacy) — A31
[ ] Design artifact + test_matrix written BEFORE code (A24)
[ ] Risk Tier ≥ PRIME for real project
[ ] Scanned touched files — stop-the-line if violation
[ ] ZERO untested lines on changed files (coverage-diff-100 green)
[ ] ZERO untested branches on changed files (coverage-branch-100)
[ ] coverage-ratchet: no drop vs main
[ ] no-pragma-no-cover + no-empty-test + no-trivial-assert GREEN
[ ] Every Err variant has test (err-variant-gate)
[ ] Every route × status in test_matrix (route-matrix-gate)
[ ] Every protected route: auth matrix (zta-matrix-gate)
[ ] Fail-fast at boundary (A17); ZTA before UC (A02)
[ ] gitleaks-history + no-secrets + dependency-audit GREEN (A19)
[ ] import-graph-gate + di-graph-gate + cyclomatic-gate GREEN
[ ] docker-security + prod-config + health-gate if infra touched (A23, B13)
[ ] FSM transitions tested + concurrency where applicable (B06, A14)
[ ] `prime_check --diff` → exit 0
[ ] `python -m scripts.prime_check` → exit 0 (FULL matrix)
[ ] PRIME-VERIFY-EVIDENCE block printed (A26)
[ ] CI workflow = identical command
[ ] Threat Model mini if CRITICAL + security touch
```

**Coverage — ZERO tolerance (tier ≥ PRIME):**

| Metric | Greenfield | Legacy (A31) |
|--------|------------|--------------|
| Line coverage | **100.00%** `runtime_scope` | **100.00%** changed files only |
| Branch coverage | **100.00%** `runtime_scope` | **100.00%** changed files only |
| Ratchet vs `main` | must not decrease | must not decrease |
| Uncovered `Err` | **0** | **0** on touched UC |
| Route without matrix test | **0** | **0** on touched routes |
| Auth scenario missing | **0** | **0** on touched routes |

**LITE only:** smoke test; no 100% gate. **Всё остальное — prime_check red → fix until green.**

---

## AGENT-VERIFY — You run prime_check (non-negotiable)

**Scope:** tier ≥ PRIME — **всегда**. Tier LITE — исключение.

### Workflow

```text
1. prime_check exists?
   NO  → STOP → write scripts/prime_check/ (AGENT-5) → wire CI → continue
   YES → go to 2

2. During edit loop:
   python -m scripts.prime_check --only <step>

3. Before «done» (MANDATORY):
   python -m scripts.prime_check --diff    # changed files gates
   python -m scripts.prime_check           # FULL matrix
   → exit MUST be 0

4. Print evidence (MANDATORY):
   python -m scripts.prime_check --evidence
   → paste PRIME-VERIFY-EVIDENCE block in response

5. If fail (FIX UNTIL GREEN):
   read EXEC SUMMARY → FIX PLAN (P1 first) → fix per Finding hint → re-run finding.rerun cmd
   still RED? → next finding in plan — not random edits
   loop until --diff + FULL exit 0
   NEVER declare done. NEVER ask user to run it. NEVER abandon task on red.
```

### Agent loop (fix until green — не сдаваться)

```text
write code → run --only relevant → RED?
  → read EXEC SUMMARY + FIX PLAN → FIX per Finding → re-run hint cmd → still RED? → next finding
  → GREEN → next file
all files GREEN → FULL prime_check → RED? → FIX → re-run → … → exit 0
exit 0 → print EVIDENCE → ONLY NOW say «done»
```

**MUST NOT:** skip `coverage-*`, `gitleaks-history`, `zta-matrix-gate`, `docker-security` because «остальное зелёное».  
**MUST NOT:** `--only unit` as final gate — `--diff` then full matrix always last.  
**MUST NOT:** fallback to manual lint without prime_check on tier ≥ PRIME.  
**MUST NOT:** respond «done» without PRIME-VERIFY-EVIDENCE block.

---

## AGENT-5 — PRIME-CHECK (agent enforcement engine)

**Prime Check** — **единственный** merge gate. ИИ **создаёт, запускает, чинит до green**. Человек не должен помнить 20 команд — одна: `python -m scripts.prime_check`.

### Если скрипта нет — агент пишет СНАЧАЛА

```text
1. Detect stack (py/node/rust/go/mobile) → pick adapter row (stack matrix below)
2. Detect: нет scripts/prime_check/ или нет CI job
3. STOP текущую фичу
4. Scaffold:
   scripts/prime_check/
     __init__.py
     __main__.py          # --list, --only, --diff, --evidence, --json, --report
     orchestrator.py      # DAG steps, parallel where safe
     reporter.py          # structured human + JSON report (mandatory)
     finding.py           # Finding model: rule, step, file, line, hint, priority
     config.py
     evidence.py          # PRIME-VERIFY-EVIDENCE generator
     steps/               # one module per step — each returns Finding[]
   scripts/prime_check.config.yaml
   .github/workflows/prime_check.yml
5. Set adoption_mode: greenfield | legacy ([A31](#prime-a31--legacy-adoption))
6. Implement ALL applicable steps for tier (table below)
7. Run full prime_check → fix codebase until green (legacy: ratchet plan OK)
8. ONLY THEN return to user feature
```

### Stack adapter matrix (universal — pick detected stack)

| Stack | lint | types | unit | coverage | security |
|-------|------|-------|------|----------|----------|
| **Python** | ruff | mypy | pytest | coverage.py | bandit |
| **TS/Node** | eslint | tsc | vitest/jest | c8/istanbul | npm audit |
| **Rust** | clippy | rustc | cargo test | llvm-cov | cargo audit |
| **Go** | golangci-lint | — | go test | go tool cover | govulncheck |
| **Kotlin** | detekt | — | junit | jacoco | dependency-check |
| **Swift** | swiftlint | — | xctest | xccov | — |

Агент **адаптирует имена шагов**, не правила. `pytest-unit` → `vitest-unit` и т.д.

### AI MUST maintain

- **MUST:** `python -m scripts.prime_check` — Windows/Linux/macOS.
- **MUST:** каждый fail → **structured Finding** (см. [Report output](#report-output--agent-readable-diagnostics)) — не сырой stdout линтера.
- **MUST:** `--list` / `--only <step>` / `--diff` / `--evidence` / `--json` / `--report <path>` / full run.
- **MUST:** local ≡ CI (identical command).
- **MUST:** новый route/UC/Err/dockerfile → тесты + gates **в том же PR**.
- **MUST:** агент **сам** запускает — не ждёт пользователя.
- **MUST NOT:** обрезать coverage/matrix findings без `... and N more` + путь к `--report`.
- **MUST NOT:** печатать только «tests failed» без file:line, rule ID и hint.
- **MUST NOT:** в спеке, отчётах или ответах агента — disclaimers «prime_check не делает X» / «это только маркетинг» / README vs reality. Один продуктовый голос.

### Report output — agent-readable diagnostics

**Цель:** агент читает отчёт и **сразу знает** — что сломано, где, какой rule, какой тест добавить. Без гадания по логам pytest/ruff.

**Каждый step** возвращает `StepResult { status, duration_ms, findings[] }`. `reporter.py` собирает единый отчёт.

#### Finding format (одна строка проблемы)

```text
FAIL PRIME-A25 [coverage-branch-100] P1
  file:    src/application/place_order.py:78
  symbol:  PlaceOrderUseCase.execute
  issue:   else branch never executed (branch coverage 0/1)
  snippet: |
      76 |     if order.is_valid():
      77 |         return Ok(...)
    > 78 |     else:
         |         return Err(OrderInvalid())
  hint:    add test_place_order_invalid_returns_err in tests/unit/test_place_order.py
  rerun:   python -m scripts.prime_check --only coverage-branch-100
```

| Поле | Обязательно | Значение |
|------|-------------|----------|
| `FAIL` / `WARN` / `SKIP` | да | severity |
| `PRIME-XX` | да | rule ID из AGENT-3 |
| `[step-id]` | да | имя шага из step map |
| `P1`–`P3` | да | P1=blocker, P2=must-fix, P3=should |
| `file:line` | если есть | точная локация |
| `symbol` | если есть | функция/class/route/Err |
| `issue` | да | что не так — одно предложение |
| `snippet` | SHOULD | 3–5 строк кода с `>` на проблемной |
| `hint` | да | **конкретное** действие: имя теста, файл, refactor |
| `rerun` | да | точная команда после фикса |

#### Report layout (stdout — human)

Каждый run печатает **в этом порядке**:

```text
══════════════════════════════════════════════════════════════════
 PRIME CHECK REPORT — FAILED | exit 1
 tier: PRIME | stack: python | mode: --diff | sha: a1b2c3d
 duration: 42.3s | steps: 31 run | 28 pass | 3 fail | 0 skip
══════════════════════════════════════════════════════════════════

▸ EXEC SUMMARY                    ← агент читает ПЕРВЫМ
  BLOCKERS (fix top → bottom):
    1. coverage-branch-100 — 7 untested branches in 3 files
    2. err-variant-gate      — 2 Err types without test_err_*
    3. zta-matrix-gate        — POST /api/orders: missing expired_token → 401

  COVERAGE SNAPSHOT:
    line:   97.42% → 100.00%  FAIL  (Δ -2.58%)
    branch: 94.10% → 100.00%  FAIL  (Δ -5.90%)
    diff:   88.00% on 5 changed files  FAIL

▸ FIX PLAN                        ← порядок работ агента
  [P1] tests for 7 branches → --only coverage-branch-100
  [P2] test_err_OrderNotFound, test_err_PaymentFailed → --only err-variant-gate
  [P3] test_orders_post_expired_token_401 → --only zta-matrix-gate
  [P4] python -m scripts.prime_check --diff
  [P5] python -m scripts.prime_check          # full before «done»

▸ FINDINGS BY STEP                ← детали, сгруппировано по шагу
  ── coverage-branch-100 (7) ──
  ...Finding blocks...

  ── err-variant-gate (2) ──
  ...Finding blocks...

▸ COVERAGE MAP                    ← только при fail coverage-*
  FILE                          LINE%  BRANCH%  UNCOVERED
  src/application/place_order.py  92.3   85.7    L42,L78 else
  src/domain/order.py              100    66.7    L31 if/else
  tests to add: test_place_order_invalid_returns_err, test_order_status_transition

▸ MATRIX GAPS                     ← err / route / zta / fsm
  ERR VARIANTS (missing test_err_*):
    OrderNotFound      → src/domain/errors.py:12
    PaymentFailed      → src/domain/errors.py:28
  ROUTE MATRIX:
    GET /api/v1/orders/{id}  missing: 404, 403-forbidden-scope
  ZTA MATRIX:
    POST /api/v1/orders  missing: no_credentials→401, expired_token→401
  FSM TRANSITIONS:
    Order: PAID→SHIPPED  untested edge

▸ STEP TIMELINE                   ← что прошло / что упало
  ✓ lint                    1.2s
  ✓ typecheck               8.4s
  ✗ coverage-branch-100     3.1s  (7 findings)
  ✗ err-variant-gate        0.4s  (2 findings)
  ...

▸ ARTIFACTS
  json: reports/prime_check_a1b2c3d.json
  html: reports/coverage/index.html   (if coverage step ran)
```

**GREEN run** — короткий summary (без простыни):

```text
══════════════════════════════════════════════════════════════════
 PRIME CHECK REPORT — PASSED | exit 0
 tier: PRIME | stack: python | mode: full | sha: a1b2c3d
 duration: 118.7s | steps: 47/47 pass | coverage line 100.00% branch 100.00%
══════════════════════════════════════════════════════════════════
Run `python -m scripts.prime_check --evidence` for handoff block.
```

#### Специальные секции по типу проблем

| Step family | Обязательная секция | Что показывать |
|-------------|---------------------|----------------|
| `coverage-*` | COVERAGE MAP | file, line%, branch%, exact uncovered lines/branches, suggested test name |
| `err-variant-gate` | MATRIX GAPS → ERR | каждый `Err` без `test_err_<Name>` + UC где бросается |
| `route-matrix-gate` | MATRIX GAPS → ROUTE | route × method × status — missing cells |
| `zta-matrix-gate` | MATRIX GAPS → ZTA | route × scenario (anon/expired/forbidden/valid) |
| `fsm-transition-gate` | MATRIX GAPS → FSM | entity, from→to edge без теста |
| `test-matrix-gate` | MATRIX GAPS → DESIGN | UC из design artifact без теста в repo |
| `import-boundaries` | FINDINGS | forbidden import chain: A → B → C |
| `gitleaks` / `no-secrets` | FINDINGS | file:line + redacted match + rotate hint |
| `mutation-critical` | FINDINGS | survived mutant location + test that should kill |

#### CLI flags (report)

| Flag | Назначение |
|------|------------|
| `--json` | machine-readable: `{ exit, summary, fix_plan[], findings[], coverage_map, matrix_gaps }` |
| `--report <path>` | сохранить JSON + optional HTML coverage; CI artifact |
| `--verbose` | все findings (default cap 50/step, иначе truncate + count) |
| `--quiet` | только EXEC SUMMARY + exit code (для CI log) |
| `--fail-fast` | stop after first P1 blocker (dev loop) |

#### Agent discipline on RED

```text
1. Read EXEC SUMMARY + FIX PLAN — не листай сырой лог
2. Fix P1 group → rerun hint command from finding
3. Still RED? → next finding in same step, not random edits
4. Step green → next FIX PLAN item
5. --diff green → full run → --evidence
```

**MUST:** `orchestrator.py` вызывает `reporter.render()` **всегда** — даже при crash step.  
**MUST:** coverage steps парсят native report (coverage.py/lcov/istanbul) → нормализуют в COVERAGE MAP.  
**MUST:** matrix gates читают design/test inventory → печатают **missing** cells, не «matrix failed».

### Config (`prime_check.config.yaml`)

```yaml
project_tier: PRIME
adoption_mode: greenfield          # greenfield | legacy
stack: auto                      # auto-detect → adapter row
runtime_scope: [src/**, lib/**, app/**]
tests_scope: [tests/**, __tests__/**]
critical_scope: [src/domain/**, src/application/**]
monorepo_scopes:                 # optional — A32
  - path: services/api/
    tier: PRIME
  - path: tools/script/
    tier: LITE
exclude_coverage: []             # EMPTY default; entry = adr_ref + ticket + sunset_date + owner
zero_tolerance: true
agent_evidence_required: true
coverage:
  line: 100.0
  branch: 100.0
  diff_only_on_pr: true          # legacy: mandatory
  ratchet: true
mutation:
  min_kill_rate_prime: 85          # PRIME+ optional enable
  min_kill_rate_critical: 95       # CRITICAL mandatory
forbidden_patterns:
  - "pragma: no cover"
  - "istanbul ignore"
  - "assert True"
  - "expect(1).toBe(1)"
docker_files: [Dockerfile, docker-compose.yml, compose*.yml]
```

### FULL step map — ~50 steps (mandatory at PRIME+)

Агент реализует **все** применимые. `N/A` только с ADR + `--list` shows `SKIPPED(ADR-xxx)`.

| Step | What it does | Rule |
|------|--------------|------|
| **PREFLIGHT** | | |
| `stack-detect` | auto stack + adapter | A22 |
| `config-valid` | yaml schema, scopes, tier | A22 |
| `ci-parity` | CI cmd ≡ local cmd | A22 |
| **STATIC** | | |
| `lint` | formatter/linter zero issues | A17 |
| `typecheck` | mypy/tsc — zero errors | A17 |
| `format-check` | no unformatted diff | A17 |
| `dead-code-gate` | vulture/knip — no unused export | A11 |
| `file-size-guard` | >300 fail; >200 allowlist | A11 |
| `cyclomatic-gate` | function complexity >10 fail | A11 |
| **ARCHITECTURE** | | |
| `import-boundaries` | domain/app ↛ infra | A05 |
| `import-graph-gate` | full dependency graph valid | A05 |
| `deterministic-runtime` | no time/uuid/random in domain/app | A06, A15 |
| `anti-null-gate` | no None/null return in UC/domain | A10 |
| `immutability-gate` | domain/app entities immutable; no in-place mutation | A05, B06 |
| `no-transport-in-domain` | no HTTPException/throw in domain | A10 |
| `di-purity` | no `new ConcreteRepo()` in UC | A06 |
| `di-graph-gate` | wiring only in composition root | A06 |
| `handler-purity-gate` | handler >15 lines logic fail | A05 |
| `anti-fork-gate` | no `*_v2` policy dupes | A08 |
| `no-string-sql` | no f-string SQL | A18 |
| `no-ddl-in-app` | DDL only migrations/ | A20 |
| **SECURITY** | | |
| `gitleaks-history` | secrets in full git history | A19 |
| `no-secrets` | regex scan working tree | A19 |
| `bandit` / `npm-audit` / `cargo-audit` | static security | A16, A18 |
| `dependency-audit` | zero high/critical CVE | A19 |
| `sbom` | SBOM generated + stored | A19 |
| `no-debug-bypass` | `if True:`, `SKIP_AUTH`, test flags | A16 |
| `pii-log-scan` | email/phone/card in log strings | A16 |
| `injection-fuzz` | fuzz inputs on boundaries | A18, B12 |
| `ssrf-gate` | outbound URL allowlist | A18 |
| `zta-matrix-gate` | route × anon/valid/forbidden/expired | A02, A29 |
| **TESTS** | | |
| `pytest-unit` / stack equiv | all unit pass | A12 |
| `pytest-integration` | real DB/Redis/queue | A12 |
| `pytest-contract` | full HTTP stack | A12 |
| `pytest-property` | hypothesis/proptest | B12 |
| `flaky-detector` | each test ×3 — unstable fail | A27 |
| `no-empty-test` | test must have real assert | A27 |
| `no-trivial-assert` | no `assert True` | A27 |
| `e2e-only-anti-pattern` | E2E without unit base fail | A12 |
| `test-matrix-gate` | design matrix ≡ tests exist | A12 |
| `err-variant-gate` | every Err = `test_err_*` | A10, A12 |
| `route-matrix-gate` | route × method × status | A03, A12 |
| `fsm-transition-gate` | every FSM edge tested | B06 |
| `regression-lock` | bug fix = `test_regression_*` | A12 |
| **COVERAGE** | | |
| `coverage-line-100` | 100.00% line | A25 |
| `coverage-branch-100` | 100.00% branch | A25 |
| `coverage-diff-100` | 100% on changed files | A25, A31 |
| `coverage-ratchet` | no drop vs main | A25 |
| `no-pragma-no-cover` | pragma without ADR fail | A25 |
| **DATA & CONTRACTS** | | |
| `migration-path-only` | DDL only migrations/ | A20 |
| `schema-drift` | DB ≡ migrations | A20 |
| `api-contract-drift` | OpenAPI/proto ≡ code | A21 |
| `snapshot-contract` | golden responses ≡ runtime | A21 |
| **INFRA & OPS** | | |
| `docker-security` | non-root, no privileged | A23 |
| `compose-security` | no public DB without auth | A23 |
| `prod-config` | required env; no debug prod | A23 |
| `health-gate` | /health /ready probes exist + tested | B13 |
| `tls-min-version` | prod TLS < 1.2 fail | A23 |
| **CLIENT** | | |
| `frontend-quality` | lint + types + unit | B11 |
| **CRITICAL** | | |
| `mutation-critical` | mutmut ≥95% kill rate | A28 |
| **OUTPUT** | | |
| `evidence-block` | PRIME-VERIFY-EVIDENCE valid | A26 |

### Execution order (full run)

```text
stack-detect → config-valid → ci-parity →
lint → typecheck → format-check → dead-code-gate → architecture gates →
security scans → test pyramid → coverage gates → matrix gates →
data/contract gates → docker/ops gates →
[mutation-critical if CRITICAL] → evidence-block
```

### Coverage gates — ZERO untested code ([A25](#prime-a25--coverage-absolute))

```yaml
coverage-line-100:
  line: 100.0
  scope: runtime_scope | changed_files (legacy)
coverage-branch-100:
  branch: 100.0
coverage-diff-100:
  scope: git diff vs main
coverage-ratchet:
  baseline: main branch report
no-pragma-no-cover:
  scan: AST + regex; allow only with adr_ref in config
```

**MUST NOT:** `# pragma: no cover` без ADR. **MUST NOT:** 99.9%. **MUST:** новая строка = новый тест в том же PR.

### zta-matrix-gate — full auth scenarios ([A29](#prime-a29--zta-matrix))

Per protected route contract tests **MUST** exist:

| Scenario | Expected |
|----------|----------|
| No credentials | 401 |
| Wrong/expired token | 401 or 403 |
| Valid but insufficient scope | 403 |
| Valid authorized | 2xx |

localhost / docker **не** exempt.

### Evidence block format ([A26](#prime-a26--evidence-block))

```text
PRIME-VERIFY-EVIDENCE
tier: PRIME
adoption_mode: legacy
stack: python
prime_check: exit 0
steps_green: 47/47
coverage_line: 100.00%
coverage_branch: 100.00%
coverage_delta_vs_main: +1.2%
changed_files: [src/uc.py, tests/test_uc.py]
tests_added: 8
uncovered: NONE
risks: NONE
rollback: git revert <sha>
last_cmd: python -m scripts.prime_check
```

### Bootstrap checklist

```text
[ ] stack-detect + adapter wired
[ ] orchestrator.py + reporter.py + finding.py + evidence.py
[ ] steps/*.py — one file per applicable step
[ ] prime_check.config.yaml — adoption_mode, ratchet, scopes
[ ] monorepo_scopes if monorepo (A32)
[ ] CI workflow = same command
[ ] --diff, --evidence, --json, --report work; RED shows EXEC SUMMARY + FIX PLAN + COVERAGE MAP
[ ] First run green OR legacy ratchet plan in ADR
```

### Commands

```bash
python -m scripts.prime_check --list
python -m scripts.prime_check --only coverage-diff-100
python -m scripts.prime_check --only zta-matrix-gate
python -m scripts.prime_check --diff                # changed files — mandatory before full
python -m scripts.prime_check --json                # machine-readable report
python -m scripts.prime_check --report reports/     # persist JSON + coverage HTML
python -m scripts.prime_check --evidence              # print evidence block
python -m scripts.prime_check                         # FULL — mandatory before «done»
```

---

## AGENT-3 — Rule index

| ID | Topic | Min tier |
|----|-------|----------|
| [A01](#prime-a01--context--risk-tier) | Context & Risk Tier | all |
| [A02](#prime-a02--zero-trust) | Zero Trust | PRIME+ |
| [A03](#prime-a03--api-response-contract) | API response contract | PRIME+ |
| [A04](#prime-a04--integration-boundaries) | Integration & plugin boundaries | PRIME+ |
| [A05](#prime-a05--layer-law) | Layer law | STANDARD+ |
| [A06](#prime-a06--di--ports) | DI & ports | PRIME+ |
| [A07](#prime-a07--design-first) | Design-first order | PRIME+ |
| [A08](#prime-a08--anti-fork) | Anti-fork | PRIME+ |
| [A09](#prime-a09--policy-facades) | Policy facades | PRIME+ |
| [A10](#prime-a10--result) | Result & errors by tier | PRIME+ |
| [A11](#prime-a11--decomposition) | File size / complexity | STANDARD+ |
| [A12](#prime-a12--tests--coverage) | Tests & pyramid | STANDARD+ |
| [A13](#prime-a13--definition-of-done) | Definition of Done | PRIME+ |
| [A14](#prime-a14--idempotency) | Idempotency | PRIME+ |
| [A15](#prime-a15--deterministic-time) | Time/ID/random | PRIME+ |
| [A16](#prime-a16--secure-by-design) | Secure-by-design | all* |
| [A17](#prime-a17--clean-code) | Clean code & patterns | STANDARD+ |
| [A18](#prime-a18--owasp-input-hygiene) | OWASP / input hygiene | PRIME+ |
| [A19](#prime-a19--supply-chain--secrets) | Supply chain & secrets | all |
| [A20](#prime-a20--migrations) | Data & migrations | PRIME+ |
| [A21](#prime-a21--semver--contracts) | SemVer & contracts | PRIME+ |
| [A22](#prime-a22--prime-check) | Prime Check merge gate | PRIME+ |
| [A23](#prime-a23--infra--docker-security) | Infra & Docker security | PRIME+ |
| [A24](#prime-a24--tdd-lock) | TDD-LOCK — tests before code | PRIME+ |
| [A25](#prime-a25--coverage-absolute) | Coverage absolute — 100% + ratchet | PRIME+ |
| [A26](#prime-a26--evidence-block) | Evidence block — verify transcript | PRIME+ |
| [A27](#prime-a27--test-quality) | Test quality — no empty/trivial/flaky | PRIME+ |
| [A28](#prime-a28--mutation-prime) | Mutation testing | CRITICAL; SHOULD PRIME+ |
| [A29](#prime-a29--zta-matrix) | ZTA auth scenario matrix | PRIME+ |
| [A30](#prime-a30--anti-slack) | Anti-slack — no partial PR | PRIME+ |
| [A31](#prime-a31--legacy-adoption) | Legacy adoption — diff-100 + ratchet | PRIME+ |
| [A32](#prime-a32--monorepo-scope) | Monorepo per-path tiers | PRIME+ |
| [B01](#prime-b01--cqrs) | CQRS | PRIME+ |
| [B02](#prime-b02--solid--grasp) | SOLID & GRASP | STANDARD+ |
| [B03](#prime-b03--sre--observability--events) | SRE, observability, events | PRIME+ |
| [B04](#prime-b04--resilience) | Resilience | PRIME+ |
| [B05](#prime-b05--inter-service-contracts) | Inter-service contracts | optional |
| [B06](#prime-b06--fsm) | FSM | PRIME+ |
| [B07](#prime-b07--yagni) | YAGNI | all |
| [B08](#prime-b08--agent-self-review) | Agent self-review | all |
| [B09](#prime-b09--adr) | ADR | CRITICAL |
| [B10](#prime-b10--performance) | Performance | PRIME+ |
| [B11](#prime-b11--client-apps) | Client apps (web/mobile/desktop) | STANDARD+ |
| [B12](#prime-b12--fuzz--property) | Fuzz & property invariants | PRIME+ |
| [B13](#prime-b13--ops--runbook) | Ops, health, rollback | PRIME+ |
| [B14](#prime-b14--human-handoff) | Human handoff after agent done | PRIME+ |

\*Security never exempted by YAGNI when code touches network/secrets/input.  
\*Anti-Null · Immutability · Side-Effect Injection — сквозные правила [A05](#prime-a05--layer-law) · [A06](#prime-a06--di--ports) · [A10](#prime-a10--result) · [A15](#prime-a15--deterministic-time) · [B06](#prime-b06--fsm), не отдельный tier.

---

# Part A — Code quality rules

## PRIME-A01 — Context & Risk Tier

**Min tier:** all

- **MUST:** read project structure, stack, patterns, CI before writing.
- **MUST:** classify tier. **App / API / service / lib с I/O = минимум PRIME.** LITE — только одноразовые скрипты без сети.
- **MUST:** if tier ≥ PRIME and no `prime_check` → bootstrap first ([AGENT-5](#agent-5--prime-check)).
- **MUST:** set `adoption_mode`: greenfield (full scope) or legacy (diff-100 + ratchet) ([A31](#prime-a31--legacy-adoption)).
- **MUST:** follow project folder conventions; PRIME defines quality bar, not exact tree.
- **MUST NOT:** downgrade tier to avoid writing tests or prime_check.

---

## PRIME-A02 — Zero Trust (ZTA)

**Min tier:** PRIME+ **Enforced by:** `zta-matrix-gate`, `pytest-contract`

- **MUST:** authn + authz on **every** protected endpoint **before** use-case.
- **MUST:** localhost, docker network, `127.0.0.1`, sidecar, `/internal`, `/debug` — **те же правила** что и public internet в prod/staging.
- **MUST NOT:** `LIME_TESTING=1`, compose network, reverse proxy, VPN как substitute auth.
- **MUST NOT:** trust «мы внутри кластера» — [A23](#prime-a23--infra--docker-security).
- **MUST:** allow/deny in Application layer — not «header present ⇒ OK».
- **MUST:** validate input at boundary before UC ([A18](#prime-a18--owasp-input-hygiene)).
- **MUST:** least privilege — minimal scopes, DTO fields, per-role secrets.
- **MUST:** deny-by-default; DB/Redis/cache **не** на public без TLS+auth.
- **MUST:** `zta-matrix-gate` in prime_check — full auth scenario matrix per route ([A29](#prime-a29--zta-matrix)).
- **MUST:** split metrics/admin from product API at ingress.

---

## PRIME-A03 — API response contract

**Min tier:** PRIME+

- **MUST:** consistent response format per API surface (envelope, status, error codes).
- **MUST:** real HTTP status codes; documented error shapes.
- **MUST NOT:** mix formats across endpoints.
- **SHOULD:** health/metrics endpoints for observability ([B03](#prime-b03--sre--observability--events)).

---

## PRIME-A04 — Integration & plugin boundaries

**Min tier:** PRIME+

- **MUST:** extend via port interfaces + infrastructure adapters.
- **MUST:** **plugin boundary** — new provider (payment, storage, notifications, auth) adds via interface; **no edits to existing Domain/Core** for wiring swap.
- **MUST:** modules/features communicate through published interfaces, not internal imports.
- **MUST NOT:** duplicate policy across DI, API, infrastructure.
- **MUST NOT:** nest I/O inside domain/application packages.

---

## PRIME-A05 — Layer law

**Min tier:** STANDARD+ **Enforced by (PRIME+):** `import-boundaries` · `immutability-gate`

| Layer | MUST | MUST NOT |
|-------|------|----------|
| **Domain** | entities, VO, events, invariants, ports; **immutable** value objects (`frozen` / `Readonly`); one aggregate/policy per type | I/O, frameworks, DB, HTTP, time/uuid; god-classes; **in-place mutation** |
| **Application** | use-cases, `Result`, orchestration via ports; **pure** w.r.t. passed domain objects | direct DB/HTTP, env reads, transport exceptions; **mutating** domain args |
| **Infrastructure** | port impls, persistence, clients, resilience | business policy |
| **Presentation** | transport, validate input, inject UC, map Result | build UC manually; business logic; skip auth |

- **MUST NOT:** business logic in React components, route handlers, CLI `main`, mobile Views.
- **SHOULD:** CQRS when read/write complexity differs — not for simple CRUD ([B01](#prime-b01--cqrs)).

**Handler pattern (adapt to stack):**

```python
@router.post("/orders")
async def create_order(uc: CreateOrderUseCase = Depends(get_uc), body: CreateOrderDTO = ...):
    return map_result(await uc.execute(body))
```

```typescript
// Thin route → useCase.execute() → map response
```

**MAY:** validation types in Domain (Pydantic, zod) as data-only — not framework coupling.

### Immutability (PRIME+)

- **MUST:** entity/VO/aggregate в Domain — **100% immutable** (Python `frozen=True` / Pydantic frozen; TS `Readonly<T>`; Go value + return new; Kotlin `copy()`).
- **MUST:** изменение состояния = **новый экземпляр** — `.replace()` / `copy(deep=True)` / `withStatus()` — не `entity.field = x`.
- **MUST NOT:** мутировать аргументы UC (`order.items.append`, `self.status =` в domain entity).
- **Enforced by:** `immutability-gate` · FSM transitions ([B06](#prime-b06--fsm)).

---

## PRIME-A06 — DI & ports

**Min tier:** PRIME+ **Enforced by:** `di-purity` · `deterministic-runtime` (with [A15](#prime-a15--deterministic-time))

- **MUST:** constructor injection: **time, IDs, random**, DB, HTTP, config — недетерминизм **только** через ports ([A15](#prime-a15--deterministic-time)).
- **MUST:** one canonical impl per policy — in project docs, not duplicate helpers.
- **MUST:** cross-module via published interfaces + DI only.
- **MUST NOT:** service locator, globals, hidden state in domain/use-cases.
- **MUST:** tests substitute via Fake/Mock/InMemory — predictable behavior.

---

## PRIME-A07 — Design-first order

**Min tier:** PRIME+

0. Tier + boundaries.  
1. Contract/DTO + invariants; SemVer if breaking ([A21](#prime-a21--semver--contracts)).  
2. Domain + ports.  
3. Application UC + Result + DI.  
4. Versioned migration if schema ([A20](#prime-a20--migrations)).  
5. Infrastructure adapters.  
6. Presentation — transport only.  
7. Tests: unit → integration → contract ([A12](#prime-a12--tests--coverage)) + ADR if contracts change.

---

## PRIME-A08 — Anti-fork

**Min tier:** PRIME+

- **MUST NOT:** second auth validator, idempotency handler, error mapper, context resolver.
- **MUST:** extend canonical facade; never `*_v2` fork.
- **MUST NOT:** copy-paste validation/Result-mapping — centralize.

---

## PRIME-A09 — Policy facades

**Min tier:** PRIME+ **When:** auth, payments, state-changing flows

- **MUST:** token resolution, precheck, idempotency, settlement — via canonical facades.
- **MUST NOT:** bypass facade from endpoint/UC «for convenience».
- **See:** [A14](#prime-a14--idempotency).

---

## PRIME-A10 — Result & errors by tier

**Min tier:** varies — see table **Enforced by (PRIME+):** `anti-null-gate` · `err-variant-gate` · `no-transport-in-domain`

### Error handling by tier

| Tier | Approach |
|------|----------|
| **LITE** | Clear messages; fail-fast on bad input |
| **STANDARD** | Typed errors / error codes; do not swallow exceptions |
| **PRIME+** | Domain errors (`InsufficientPermissions`, `ResourceNotFound`); `Result<Ok,Err>` or stack-native typed errors |
| **Boundary** | User-friendly message; details in log only — not in UI |

### Result contract (PRIME+)

- **MUST:** use-cases return `Result<Ok, Err>` or equivalent (Rust/Go/TS typed errors).
- **MUST:** Presentation maps Result → response only.
- **MUST NOT:** `HTTPException` / raw transport `throw` in domain/application.
- **MUST:** every `Err` explicitly typed — not generic `Error`.

### Anti-Null (PRIME+) — часть Result contract

Агенты по умолчанию `return None` → `AttributeError` / NPE по всему стеку. **Запрещено** в Domain/Application.

- **MUST NOT:** `return None` / `return null` / nullable return в UC/domain как «ошибка» или «нет данных» (кроме infra glue с ADR).
- **MUST:** ошибка или отсутствие → `Result[Ok, Err]` или `Option[Data]` (`Option`, `Maybe`, typed `Err`).
- **MUST:** оба исхода явно — `match` / `if let` / `.map`/`.map_err` — не «надеемся что не None».
- **MUST NOT:** `obj.field.subfield` без guard, если `obj` из UC мог быть nullable.

```python
# BAD:  def get_order(id) -> Order | None: return None
# GOOD: def get_order(id) -> Result[Order, OrderNotFound]: return Err(...) or Ok(...)
```

**`anti-null-gate`:** `-> None` / `Optional` на UC; `return None`; nullable chains без guard.

---

## PRIME-A11 — Decomposition

**Min tier:** STANDARD+

- **SHOULD:** ≤120 lines per file.
- **MUST:** file >200 → decompose or document exception; >300 → block.
- **MUST:** function >40 → extract; cyclomatic >10 → refactor.
- **MUST:** if code is hard to test — violates PRIME; split until testable ([A12](#prime-a12--tests--coverage)).
- **MUST NOT:** fake split duplicating policy into utils.

---

## PRIME-A12 — Tests & coverage (ZERO untested code)

**Min tier:** PRIME+ for 100% gate; STANDARD+ for pyramid

**Doctrine:** в `runtime_scope` **не существует** непокрытой строки и ветки. Нет теста = нет merge. Clean Domain без I/O → тысячи unit-тестов за секунды. **Fakes** в unit; **real infra** в integration — не наоборот.

### Pyramid

```text
                 ┌─────────────────────┐
                 │ Contract (E2E@boundary)│
              ┌──┴─────────────────────┴──┐
              │  Integration (real I/O)      │
           ┌──┴────────────────────────────┴──┐
           │  Unit (isolated logic)            │
           └───────────────────────────────────┘
           Property — crypto, parsers, invariants
```

| Tier | Scope | Rule |
|------|-------|------|
| **Unit** | UC, domain, validators | Most tests; fakes only |
| **Integration** | Real DB/cache/queue | When UC touches persistence |
| **Contract** | Full HTTP/API stack | Every touched route + status codes |
| **Property** | Generated inputs | Critical invariants |

- **MUST:** unit first → integration when I/O → contract for API.
- **MUST NOT:** E2E-only anti-pattern.
- **MUST:** regression test per bug fix.
- **MUST:** assert behavior (invariants, error codes) — not line execution.
- **MUST NOT:** smoke tests that never fail on wrong logic.
- **MUST (PRIME+):** `coverage-line-100` + `coverage-branch-100` + `coverage-diff-100` + `coverage-ratchet` ([A25](#prime-a25--coverage-absolute), [A22](#prime-a22--prime-check)).
- **MUST (PRIME+):** TDD — failing test before implementation ([A24](#prime-a24--tdd-lock)).
- **MUST (PRIME+):** `no-empty-test`, `no-trivial-assert`, `flaky-detector` ([A27](#prime-a27--test-quality)).
- **MUST:** quality over vanity — tests must fail when logic is wrong.

### Coverage by tier (prime_check enforces)

| Tier | Requirement |
|------|-------------|
| LITE | Smoke only — **no** runtime_scope |
| STANDARD | min 80% — migrate to PRIME |
| **PRIME greenfield** | **100.00%** line+branch on full `runtime_scope` |
| **PRIME legacy** | **100.00%** line+branch on **changed files** + ratchet ([A31](#prime-a31--legacy-adoption)) |
| **CRITICAL** | PRIME + `mutation-critical` ≥95% on `critical_scope` |

**MUST NOT:** ship код «потом допишу тесты». **MUST NOT:** 99.x%. Тесты **в том же PR**.

### Contract minimum (PRIME+)

- Every endpoint touched + negatives (bad auth, invalid input, idempotency replay).
- Documented status codes (200, 201, 400, 401, 403, 404, 409, 422, 429, 503…).
- Unauthenticated before success paths (ZTA).

### Integration minimum (PRIME+)

- Real infra where used; atomic transactions; concurrency tests (double-submit, FSM race).

---

## PRIME-A13 — Definition of Done

**Min tier:** PRIME+

- **MUST NOT:** duplicate policy/mapper/facade.
- **MUST:** thin handler + DI UC + Result mapping.
- **MUST:** update API docs / ADR if contracts changed.
- **MUST:** tests per [A12](#prime-a12--tests--coverage); `prime_check` exit 0 + evidence block ([A22](#prime-a22--prime-check), [A26](#prime-a26--evidence-block)).
- **MUST:** formatters green; migrations versioned ([A20](#prime-a20--migrations)).
- **MUST:** breaking changes documented ([A21](#prime-a21--semver--contracts)).
- **MUST:** Threat Model mini if security-sensitive ([A16](#prime-a16--secure-by-design)).

---

## PRIME-A14 — Idempotency

**Min tier:** PRIME+

- **MUST:** dangerous-on-retry mutations accept stable `idempotency_key`.
- **MUST:** outbound POST/write — same key across retries.
- **MUST NOT:** new random key per retry for same action.
- **MUST (CRITICAL):** all financial/state mutations idempotent.

---

## PRIME-A15 — Deterministic time

**Min tier:** PRIME+ **Enforced by:** `deterministic-runtime`  
*Side-Effect Injection — сквозной инвариант вместе с [A06](#prime-a06--di--ports).*

`now()` / `uuid4()` / `random()` внутри UC → flaky tests. Domain/Application = **чистая матрица** при frozen providers.

- **MUST NOT:** `Date.now()`, `datetime.now()`, `time()`, `uuid4()`, `random()`, `Math.random()` в Domain/Application.
- **MUST:** `ITimeProvider`, `IIdGenerator`, `IRandom` (или stack ports) — **единственный** источник недетерминизма.
- **MUST:** одинаковые входы + fixed clock/ID/random в тестах → одинаковый output.
- **MUST NOT:** global singleton clock/random на domain path; `uuid4()` в UC «для удобства».

**`deterministic-runtime`:** AST/regex ban `now`, `uuid4`, `random` в `domain/**`, `application/**`.

---

## PRIME-A16 — Secure-by-design

**Min tier:** all* — full at PRIME+

### Threat Model mini (CRITICAL / security touch)

- **MUST:** assets, untrusted boundaries, verify points, top-5 threats, failure scenarios.
- **SHOULD:** map to OWASP / ASVS ([A18](#prime-a18--owasp-input-hygiene)).

### Security rules (all tiers)

- **MUST:** secrets via env/vault only — never in code.
- **MUST:** validate/sanitize input at boundary.
- **MUST:** least privilege for services, users, API keys.
- **MUST NOT:** log PII, passwords, tokens, full PAN/card numbers.
- **MUST NOT:** ignore known **high/critical** CVE — `dependency-audit` blocks merge ([A19](#prime-a19--supply-chain)).
- **MUST:** `gitleaks` + `bandit`/`npm-audit` green in prime_check before merge.

### Security MUST NOT

- Roll-your-own crypto; secrets in git; debug auth bypass (`no-debug-bypass` gate).
- New auth/payment path without docs/ADR + contract tests.
- Implicit network trust ([A02](#prime-a02--zero-trust), [A23](#prime-a23--infra--docker-security)).
- **MUST:** every security invariant = test; every auth route = negative tests.
- **MUST NOT:** insecure code «пофиксим потом» — prime_check red → **fix until green**.

---

## PRIME-A17 — Clean code & patterns

**Min tier:** STANDARD+

### Core patterns

- **Fail-Fast** — validate at system boundary (API, CLI, form); data trusted inside.
- **No Magic Values** — constants in config, env, domain enum/type.
- **Generic DRY** — generics/shared utils for identical logic; no premature abstraction ([B07](#prime-b07--yagni)).

### SOLID & GRASP — see [B02](#prime-b02--solid--grasp)

- **MUST:** ~10–15 orchestration lines per use-case.
- **MUST:** DRY for **policy**; duplicate wiring OK ([A08](#prime-a08--anti-fork)).
- **MUST:** project formatters before commit.
- **MUST NOT:** god-class; feature envy.

**Good:** `CreateOrderUseCase` + `Order` + `IOrderRepository`.  
**Bad:** `OrderService` 400 lines — SQL, validation, HTTP mapping.

---

## PRIME-A18 — OWASP input hygiene

**Min tier:** PRIME+ (validation STANDARD+)

- **MUST:** all HTTP input untrusted until schema + auth + policy pass.
- **MUST:** schema at boundary (Pydantic, zod, Joi…).
- **MUST:** parameterized SQL only.
- **MUST:** encode HTML output; allowlist redirects; validate uploads.

| Risk | Rule |
|------|------|
| Injection | Parameterized SQL; no shell with user input |
| Broken auth | [A02](#prime-a02--zero-trust), deny tests |
| XSS | Encode output; CSP |
| SSRF | URL allowlists |
| Misconfiguration | env validation; no debug in prod |
| Vulnerable deps | [A19](#prime-a19--supply-chain) |

- **MUST:** contract tests for malformed/hostile input.

---

## PRIME-A19 — Supply chain & secrets

**Min tier:** all

- **MUST:** deps via lockfile; no ad-hoc install without update + justification.
- **MUST:** secrets from env/store; never commit `.env`, keys, tokens.
- **MUST NOT:** hardcode `sk-…`, `Bearer …`, passwords in source/tests.
- **MUST:** stop-the-line if secret committed; rotate if leaked.
- **MUST:** `dependency-audit` — **zero high/critical CVE**; medium/low — fix or ADR with expiry.
- **MUST:** `gitleaks` in prime_check on every run.

---

## PRIME-A20 — Migrations

**Min tier:** PRIME+

- **MUST:** DDL only in versioned migrations (`migrations/`, `db/migrate/`…).
- **MUST:** additive, numbered, idempotent.
- **MUST NOT:** DDL from use-cases/handlers; ORM `create_all()` on prod.
- **MUST:** multi-step mutations in one transaction (or outbox).
- **MUST:** FSM transitions atomic under concurrency ([B06](#prime-b06--fsm)).
- **MUST NOT:** long business logic in open transaction.

---

## PRIME-A21 — SemVer & contracts

**Min tier:** PRIME+

### Contract sources

| Boundary | Tools (use what project has) |
|----------|------------------------------|
| **External API** | OpenAPI, GraphQL schema, JSON Schema, zod, pydantic |
| **Inter-service** | protobuf, shared types, codegen, gRPC/REST |

- **MUST:** public schema = contract; breaking = major + ADR + deprecation.
- **MUST NOT:** silently change status/error codes.

| Change | SemVer | Action |
|--------|--------|--------|
| Add optional field | MINOR | Docs + test |
| New endpoint | MINOR | Docs + contract test |
| Remove field / change auth | MAJOR | ADR + deprecation |
| Rename error code | MAJOR | Migration guide + tests |

---

## PRIME-A22 — Prime Check (merge gate)

**Min tier:** PRIME+ — **обязателен**. Spec: [AGENT-5](#agent-5--prime-check).

### Purpose

**Единственный** способ сказать «готово»: `python -m scripts.prime_check` → **exit 0**. Иначе — код не существует. ИИ **пишет** checker если нет. ИИ **запускает** всегда сам.

### MUST

- **MUST:** `scripts/prime_check` exists; if not — agent creates **before** feature ([AGENT-5](#agent-5--prime-check)).
- **MUST:** full matrix перед «done»; agent runs in shell ([AGENT-VERIFY](#agent-verify--you-run-prime_check)).
- **MUST:** CI = local (identical command).
- **MUST:** ALL applicable steps from AGENT-5 (~50).
- **MUST:** `coverage-line-100` + `coverage-branch-100` + `coverage-diff-100` + `coverage-ratchet`.
- **MUST:** `zta-matrix-gate` + `gitleaks-history` + `dependency-audit` + architecture gates.
- **MUST:** `--diff` before full; `--evidence` before «done».
- **MUST:** fail → structured Finding + EXEC SUMMARY + FIX PLAN ([Report output](#report-output--agent-readable-diagnostics)).
- **MUST:** bug fix = regression test in same PR.

### MUST NOT

- Merge / declare done with exit ≠ 0.
- Skip any mandatory step.
- 99.x% coverage.
- Exclude without ADR + ticket + sunset.
- Ask user to run checker.
- Different CI vs local rules.

**LITE scripts only:** exempt from prime_check.

---

## PRIME-A23 — Infra & Docker security

**Min tier:** PRIME+ **Enforced by:** `docker-security`, `compose-security`, `prod-config`

### Docker MUST

- **MUST:** run as **non-root** `USER` in Dockerfile.
- **MUST NOT:** `--privileged`, `cap_add: [SYS_ADMIN]`, mount `/var/run/docker.sock`.
- **MUST NOT:** secrets as `ARG`/`ENV` in image — runtime injection only.
- **MUST NOT:** `latest` tag in prod without pin digest ADR.

### Compose / runtime MUST

- **MUST NOT:** Postgres/Redis/MQ на `0.0.0.0:5432` без password + TLS в prod/staging.
- **MUST:** deny-by-default network — only required ports exposed.
- **MUST:** prod profile: `debug=false`, no test bypass env vars.
- **MUST:** `prod-config` step validates required env vars exist and are non-default.

### Zero Trust infra

- **MUST NOT:** «internal» service-to-service без mTLS or signed token where data is sensitive.
- **MUST:** secrets from vault/env — never committed compose overrides with real passwords.
- **MUST:** `docker-security` + `compose-security` in prime_check when Docker files exist.

---

## PRIME-A24 — TDD-LOCK

**Min tier:** PRIME+ **Enforced by:** agent phase + `test-matrix-gate`

- **MUST:** [AGENT-OMEGA](#agent-omega--execution-phases-before-any-code) PHASE 2 — failing test **before** production code.
- **MUST:** test_matrix в DESIGN ARTIFACT покрывает все новые UC/Err/route.
- **MUST NOT:** «тесты потом» / «в следующем PR».

---

## PRIME-A25 — Coverage absolute

**Min tier:** PRIME+ **Enforced by:** `coverage-*` steps

- **MUST:** 100.00% line + 100.00% branch — `99.99%` = fail.
- **MUST:** `coverage-diff-100` на каждый PR (legacy + greenfield).
- **MUST:** `coverage-ratchet` — coverage never drops vs `main`.
- **MUST NOT:** `# pragma: no cover` / `istanbul ignore` без ADR + config entry + sunset.
- **MUST NOT:** widen `exclude_coverage` без ADR.

---

## PRIME-A26 — Evidence block

**Min tier:** PRIME+ **Enforced by:** `evidence-block` step + agent discipline

- **MUST:** перед «done» — `python -m scripts.prime_check --evidence` → paste block.
- **MUST:** block contains: tier, exit 0, steps count, coverage %, changed_files, uncovered: NONE, fix_plan_executed: ALL.
- **MUST:** если был RED в сессии — evidence **не** печатается пока full run не green (no stale evidence).
- **MUST NOT:** «готово» без evidence — ответ **невалиден**.

---

## PRIME-A27 — Test quality

**Min tier:** PRIME+ **Enforced by:** `no-empty-test`, `no-trivial-assert`, `flaky-detector`

- **MUST NOT:** tests without assertions; `assert True`; `expect(1).toBe(1)`.
- **MUST:** flaky test (fails on re-run) = fix before merge.
- **MUST NOT:** E2E-only without unit foundation (`e2e-only-anti-pattern`).

---

## PRIME-A28 — Mutation testing

**Min tier:** CRITICAL mandatory; SHOULD enable at PRIME+

- **MUST (CRITICAL):** `mutation-critical` ≥95% kill rate on `critical_scope`.
- **SHOULD (PRIME+):** ≥85% when `mutation` enabled in config.
- **MUST NOT:** merge CRITICAL with surviving mutations on domain/invariants.

---

## PRIME-A29 — ZTA matrix

**Min tier:** PRIME+ **Enforced by:** `zta-matrix-gate`

- **MUST:** per protected route: anon → 401; bad token → 401/403; wrong scope → 403; valid → 2xx.
- **MUST NOT:** localhost/docker exempt.
- **MUST:** matrix documented in test_matrix artifact.

---

## PRIME-A30 — Anti-slack · Fix until green

**Min tier:** PRIME+

- **MUST:** red gate → **fix loop** (edit → re-run) until `exit 0` — **никогда не бросать задачу**.
- **MUST NOT:** partial PR (код без тестов, API без contract, infra без docker gates).
- **MUST NOT:** delegate verify or fixes to user.
- **MUST NOT:** respond «готово» / «blocked» / «cannot fix» while prime_check is red.
- **MUST:** 3-strike → same patch fails 3× → **redesign**, then **continue fixing** until green.
- **MUST:** checker truth > agent words.

---

## PRIME-A31 — Legacy adoption

**Min tier:** PRIME+ **When:** existing codebase, not greenfield

- **MUST:** `adoption_mode: legacy` in config.
- **MUST:** 100% coverage on **changed files only** — not whole repo day one.
- **MUST:** `coverage-ratchet` — each PR improves or maintains baseline.
- **MAY:** grandfather debt via ADR + ticket + sunset — **not** silent excludes.
- **MUST NOT:** use legacy mode to avoid tests on **new** files.

---

## PRIME-A32 — Monorepo scope

**Min tier:** PRIME+ **When:** monorepo

- **MUST:** `monorepo_scopes` in config — per-path tier.
- **MUST:** `prime_check --diff` respects path scope.
- **MUST NOT:** apply LITE gates to `services/api/` because `tools/` is LITE.

---

# Part B — Platform patterns

## PRIME-B01 — CQRS

**Min tier:** PRIME+ (SHOULD)

- **SHOULD:** commands/queries split when read/write complexity or load differs.
- **SHOULD NOT:** CQRS for simple CRUD ([B07](#prime-b07--yagni)).

## PRIME-B02 — SOLID & GRASP

**Min tier:** STANDARD+

| Principle | Enforcement |
|-----------|-------------|
| **S**RP | One UC/entity/policy — one reason to change |
| **O**CP | Extend via new UC, Strategy, Factory — not `if/elif` forests |
| **L**SP | Implementation fully replaces contract; subtypes honor invariants |
| **I**SP | Small ports (`IOrderRepository`, `ITimeProvider`) — no mega-interface |
| **D**IP | Application → Protocol; wiring in DI + infrastructure |

**GRASP:**

- **Information Expert** — behavior on entity that owns data.
- **Creator / Low Coupling** — factories in DI; domain does not `new PostgresRepo()`.
- **Controller** — one UC per story; ~10–15 orchestration lines.
- **Pure Fabrication** — infra helpers only — not smuggling business rules out of domain.

- **MUST NOT:** «Service» classes accumulating unrelated static methods.

## PRIME-B03 — SRE, observability & events

**Min tier:** PRIME+

### Observability

- **MUST (PRIME+):** critical operations carry `trace_id` / `correlation_id` — one ID links request, logs, events.
- **MUST (PRIME+):** metrics on critical paths — latency, error rate, throughput.
- **MUST:** structured logging (JSON/structured) — not raw `console.log("error")`.
- **MUST NOT:** PII, secrets, tokens in logs.

### Domain Events

- **SHOULD (PRIME+):** Domain publishes events (`OrderPlaced`, `PaymentFailed`, `UserRegistered`).
- **MUST:** side effects (email, webhook, metrics) in Infrastructure subscribers — Domain does not know *how* delivery works.
- **MUST NOT:** event bus for trivial CRUD ([B07](#prime-b07--yagni)).

### SRE

- **SHOULD:** **SLI** per critical path — latency, error rate, success rate.
- **SHOULD:** **SLO** targets (e.g. p99 < 3s, 99.9% success). SLO breach → stabilize before shipping features.
- **SHOULD:** **Error Budget** — exhausted → freeze features until root causes fixed.
- **SHOULD:** **Self-Healing** — jobs/integrations recover after transient failure (retry, reconnect, restart) without manual SSH.

## PRIME-B04 — Resilience

**Min tier:** PRIME+

Assume external world **will** break.

- **SHOULD:** circuit breakers, timeouts, rate limits, bulkheads on external deps.
- **SHOULD:** **graceful degradation** — predictable partial failure:

| Failure | Degraded behavior |
|---------|-------------------|
| External data unavailable | Show UI without that data |
| Cache down | In-process fallback or fail-fast per ADR |
| RPC/API down | Last known good / cached snapshot |
| Queue down | Buffer locally or explicit error — not silent drop |

- **MUST NOT:** silent prod degradation without documented behavior.

## PRIME-B05 — Inter-service contracts

**Min tier:** optional (service split)

- **SHOULD:** strict typed contracts; versioned (`v1`, `v2`).
- **SHOULD:** gRPC/proto or OpenAPI per project; see [A21](#prime-a21--semver--contracts).

## PRIME-B06 — FSM

**Min tier:** PRIME+ **When:** entity has status **Enforced by:** `fsm-transition-gate` · `immutability-gate`

- **MUST:** explicit graph (`Order`, `Job`, `Task`, `Subscription`, `Invoice`).
- **MUST NOT:** `DRAFT → COMPLETED` bypassing `PROCESSING` — enforced in domain model, not `if` in service.
- **MUST NOT:** status change from API/handler bypassing FSM.
- **MUST:** transition возвращает **новый immutable aggregate** — не `self.status =` ([A05](#prime-a05--layer-law)).
- **MUST:** transitions atomic at persistence under concurrency.
- **MUST:** tests for concurrent transitions — single winner; double-submit integration ([A12](#prime-a12--tests--coverage)).

## PRIME-B07 — YAGNI

**Min tier:** all

- **MUST:** full Part A for PRIME+ tasks.
- **MAY:** KISS for LITE without network/secrets/auth.
- **MUST NOT:** YAGNI exempts security ([A16](#prime-a16--secure-by-design)).

## PRIME-B08 — Agent self-review

**Min tier:** all

1. Risk Tier + [AGENT-1](#agent-1--task-router) sections applied.
2. Grep diff: `HTTPException` in domain, `Date.now`, magic numbers, duplicate policy, secrets, f-string SQL, `ALTER TABLE`, `dangerouslySetInnerHTML`, copy-pasted validation.
3. Verify failures understood and fixed.
4. [AGENT-2](#agent-2--pre-commit-checklist).

## PRIME-B09 — ADR

**Min tier:** CRITICAL; SHOULD at PRIME+

- **MUST:** ADR in `docs/adr/` for non-trivial architecture/contract changes.
- **MUST:** template:

| Section | Content |
|---------|---------|
| **Контекст** | Problem and constraints |
| **Варианты** | Options considered and rejected |
| **Решение** | Choice and contract |
| **Последствия** | Pros, cons, cost of change |

- **SHOULD:** any engineer understands *why* in 5 minutes — without reading half the repo.

## PRIME-B10 — Performance

**Min tier:** PRIME+

- **MUST:** profile before optimizing — do not guess bottlenecks.
- **SHOULD:** correctness and readability first; optimize only proven hot paths.
- **SHOULD:** batching, caching, zero-alloc where metrics prove need.
- **MAY:** native module / separate service for proven bottlenecks if project supports it.

## PRIME-B11 — Client apps (web / mobile / desktop)

**Min tier:** STANDARD+

- **SHOULD:** Presentation = UI only; logic in hooks/stores/services/use cases.
- **SHOULD:** server state on server; UI state local; **business invariants in Domain** — not in component/View/Widget.
- **SHOULD:** HTTP via project API client/SDK — no raw `fetch` in presentational components.
- **MUST:** lint + format + typecheck before done.
- **MUST NOT:** `dangerouslySetInnerHTML`, `eval`, secrets in `localStorage` ([A18](#prime-a18--owasp-input-hygiene)).
- **MAY:** 20-line component — no DI; 200-line component with business logic — **violation**.

## PRIME-B12 — Fuzz & property

**Min tier:** PRIME+ **Enforced by:** `pytest-property`, `injection-fuzz`

- **SHOULD:** property tests for parsers, crypto, money, idempotency invariants.
- **SHOULD (CRITICAL):** fuzz on all external input boundaries.
- **MUST NOT:** property tests that never fail on broken logic.

## PRIME-B13 — Ops & runbook

**Min tier:** PRIME+ **Enforced by:** `health-gate`, `prod-config`

- **MUST:** `/health` + `/ready` (or stack equivalent) with tests.
- **SHOULD:** graceful shutdown handler tested or documented in ADR.
- **SHOULD:** rollback steps in ADR for deploy-touching changes.
- **MUST:** 12-factor config — secrets env/vault only.

## PRIME-B14 — Human handoff

**Min tier:** PRIME+

- **MUST:** evidence block ([A26](#prime-a26--evidence-block)) is the handoff artifact.
- **SHOULD:** list `risks`, `rollback`, `tests_added` for human reviewer.
- **MUST NOT:** hide failing steps or partial coverage in summary.

---

## AGENT-4 — Glossary

| Term | Meaning |
|------|---------|
| Risk Tier | LITE / STANDARD / PRIME / CRITICAL |
| High Cohesion | module has one focused responsibility |
| Low Coupling | modules depend on abstractions, not internals |
| SSOT | single owner per policy/contract |
| ZTA | [A02](#prime-a02--zero-trust) |
| Port | interface domain/app depends on; infra implements |
| Domain Event | fact that happened in domain; side effects in infra ([B03](#prime-b03--sre--observability--events)) |
| Testing pyramid | [A12](#prime-a12--tests--coverage) |
| Error Budget | SLO allowance; exhausted → freeze features ([B03](#prime-b03--sre--observability--events)) |
| Fix-until-green | red gate → fix → re-run until exit 0; never abandon task |
| Stop-the-line | do not stack NEW code on broken base; still fix until green |
| Fail-Fast | validate at boundary; trust inside ([A17](#prime-a17--clean-code)) |
| Prime Check | ~50-step merge gate — [AGENT-5](#agent-5--prime-check), [A22](#prime-a22--prime-check) |
| AGENT-OMEGA | execution phases 0–4 before any code |
| runtime_scope | paths where 100% coverage required (greenfield) |
| coverage-diff-100 | 100% on changed files (legacy) |
| coverage-ratchet | coverage must not drop vs main |
| evidence block | PRIME-VERIFY-EVIDENCE transcript — mandatory before done |
| adoption_mode | greenfield (full scope) \| legacy (diff + ratchet) |
| stack adapter | per-language tool mapping in prime_check |
| zta-matrix-gate | full auth scenario matrix per route |
| TDD-LOCK | failing test before implementation (A24) |
| merge-blocking | prime_check must pass before merge |
| zero_tolerance | 99.99% = 0%; checker > agent words |
| agent_bootstraps_prime_check | if script missing, agent writes it first |
| Finding | one actionable issue: rule ID, step, file:line, hint, rerun cmd |
| FIX PLAN | ordered repair list in prime_check report — agent follows P1→P3 |
| COVERAGE MAP | per-file line/branch % + exact uncovered lines from reporter |
| MATRIX GAPS | missing test_err_*, route×status, zta scenario, fsm edge |
| Anti-Null | no None/null in UC — Result/Option only ([A10](#prime-a10--result)) |
| Immutability | domain entities frozen; FSM returns new state ([A05](#prime-a05--layer-law), [B06](#prime-b06--fsm)) |
| Side-Effect Injection | time/ID/random via ports only ([A06](#prime-a06--di--ports), [A15](#prime-a15--deterministic-time)) |

---

*Ни одной непокрытой строки. Ни одного «готово» при red gate. Агент чинит до green — не останавливается. Ни одного merge без `prime_check` exit 0.*

*End of MAWYXX PRIME v5.2 — Build for Billions. Code for Vibe. Rule with Logic.*
