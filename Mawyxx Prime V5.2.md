# MAWYXX PRIME: Enterprise Vibe-Coding Standard (v5.2)

*«Build for Billions. Code for Vibe. Rule with Logic.»*

**Agent contract** — единый нормативный файл для ИИ-кодера.

### Universal Doctrine — Project Skin · Empire Engine (read first)

> **Форма = проект. Дух = всегда Empire.**  
> Не «как принято в репо, но получше где надо». Не «enterprise только на платежах».  
> **Всегда:** пишешь **на языке и в стиле проекта** (стек, папки, naming, framework) — но **с дисциплиной Empire**: тесты, явные ошибки, security, observability, fix-until-green, zero «сойдёт».

| Слой | Что это | Правило |
|------|---------|---------|
| **Project Skin** | Как *выглядит* код снаружи | Имена, папки, паттерн фреймворка — **как в репо**. Не тащить чужой DDD/UseCase если проект на MVC/handlers/services. |
| **Empire Engine** | Как *работает* код внутри | **Всегда** на уровне назначенного tier — без ослаблений «потому что pet-проект». LITE = минимум Empire; PRIME+ = полный Empire. |

| Принцип | Что агент делает |
|---------|------------------|
| **Project Skin** | Detect stack → писать **родным** для проекта синтаксисом и структурой ([Pattern Catalog](#pattern-catalog--stack-native-equivalents)). |
| **Empire Engine** | **Всегда** tier-дисциплина: тесты, security, explicit errors, evidence, fix-until-green — **не опционально**. |
| **Risk-tiered** | *Сколько* Empire (LITE→CRITICAL), не *быть ли* Empire. Pet-проект ≠ sloppy code. |
| **Mechanism WHEN** | *Какой инструмент* Empire (FSM, ledger, Docker gate) — по триггеру. *Качество* Empire — **всегда** для tier. |
| **Outcome gates** | Gates ловят провалы Empire Engine — не «не тот синтаксис Skin». |

**When** в правилах = **какой механизм** включить (FSM, idempotency ledger, context-leak…), **не** «можно писать хуже».  
**Никогда:** «проект маленький → без тестов», «тут React → логика в компоненте ок», «потом допишем prime_check».

### Checker = 100% работа агента (не пользователя)

На tier ≥ PRIME **человек не настраивает checker**. Агент **сам**, в этой сессии:

| Задача | Кто | Запрещено пользователю |
|--------|-----|------------------------|
| Создать `scripts/prime_check/` с нуля | **Агент** | «добавьте checker в репо» |
| Написать **все** step-модули (~50) | **Агент** | «реализуйте gates сами» |
| `prime_check.config.yaml` (tier, scopes, stack) | **Агент** | «настройте config» |
| CI workflow (local ≡ CI) | **Агент** | «добавьте job в GitHub Actions» |
| Dev-deps для lint/test/coverage | **Агент** | «установите pytest/ruff» |
| Запуск `--only` / `--diff` / FULL | **Агент** в shell | «запустите тесты» / «проверьте сами» |
| Чинить код **и** checker до `exit 0` | **Агент** | «не могу починить gate» |

**Нет checker в репо → STOP фичу → [AGENT-5](#agent-5--prime-check) bootstrap FULL → green → только потом задача пользователя.**

**Цель:** **High Cohesion** внутри модулей, **Low Coupling** между ними. Код предсказуемый, тестируемый, наблюдаемый, готовый к росту.

**Applicability keywords (RFC 2119 + WHEN):**

| Keyword | Meaning |
|---------|---------|
| **Always** | Любой tier, любой стек |
| **STANDARD+** | Tier ≥ STANDARD |
| **PRIME+** | Tier ≥ PRIME |
| **CRITICAL** | Tier = CRITICAL |
| **When \<trigger\>** | Только если условие в задаче/дизайне (status field, retry risk, multi-module, container deploy…) |
| **Stack-native** | Реализация = конвенция проекта; gate проверяет outcome |

**Сквозные инварианты (outcomes — вшиты в правила, не отдельный модуль):**

| Invariant | Outcome | Where | When | Gate |
|-----------|---------|-------|------|------|
| **Explicit errors** | Нет silent `null`/`None` как «ошибка» в core logic | [A10](#prime-a10--result) | PRIME+ core/UC | `anti-null-gate` |
| **Immutability** | Нет in-place mutation shared/concurrent state | [A05](#prime-a05--layer-law) · [B06](#prime-b06--fsm) | When races / FSM / shared aggregate | `immutability-gate` |
| **Injectable nondeterminism** | time/ID/random тестируемы | [A06](#prime-a06--di--ports) · [A15](#prime-a15--deterministic-time) | PRIME+ testable core | `deterministic-runtime` |
| **Idempotent mutations** | Повтор = тот же эффект, не дубль | [A14](#prime-a14--idempotency) | When state-changing + retry risk | `idempotency-matrix-gate` |
| **Module isolation** | Нет импорта чужих **private** domain types | [A04](#prime-a04--integration--plugin-boundaries) | When multi-module / service split | `context-leak-gate` |
| **Observable failures** | trace + invariant_id + safe context в логах | [A10](#prime-a10--result) · [B03](#prime-b03--sre--observability--events) | PRIME+ | `error-context-gate` |

### ZERO-TOLERANCE doctrine (tier ≥ PRIME)

Gates ниже — **outcome checks**. Шаг `N/A` только с ADR, если триггер не применим (нет Docker, нет FSM в design artifact, LITE script…).

| Запрет | Enforcement | Applicability |
|--------|-------------|---------------|
| Непокрытая строка в `runtime_scope` / diff | `coverage-line-100` → exit 1 | PRIME+ |
| Непокрытая ветка (branch) | `coverage-branch-100` → exit 1 | PRIME+ |
| Coverage упал vs `main` | `coverage-ratchet` → exit 1 | PRIME+ |
| `# pragma: no cover` без ADR | `no-pragma-no-cover` → exit 1 | PRIME+ |
| Пустой / trivial test | `no-empty-test` → exit 1 | PRIME+ |
| Непротестированный error variant | `err-variant-gate` → exit 1 | PRIME+ |
| Exposed operation без contract-тестов | `route-matrix-gate` → exit 1 | PRIME+ · When API/CLI/RPC surface |
| Protected operation без auth matrix | `zta-matrix-gate` → exit 1 | PRIME+ · When auth |
| Secret в repo / history / логах | `gitleaks-history` → exit 1 | Always (network tier+) |
| Core logic импортирует I/O layer | `import-graph-gate` → exit 1 | PRIME+ · When layered/monolith |
| `Date.now` / `uuid4` в testable core | `deterministic-runtime` → exit 1 | PRIME+ · When testable core exists |
| Silent null как failure path | `anti-null-gate` → exit 1 | PRIME+ core |
| In-place mutation shared state | `immutability-gate` → exit 1 | When FSM / concurrent aggregate |
| Double-apply мутации | `idempotency-matrix-gate` → exit 1 | When state-changing + retry risk |
| Cross-module private type leak | `context-leak-gate` → exit 1 | When multi-module |
| Failure без observable context | `error-context-gate` → exit 1 | PRIME+ |
| Небезопасный Docker/compose | `docker-security` → exit 1 | When containerized |
| CVE в dependencies (high/critical) | `dependency-audit` → exit 1 | Always (deps) |
| «Готово» без evidence block | `evidence-block` → invalid response | PRIME+ |
| Merge без quality gate green | **запрещён** | PRIME+ |

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
agent_bootstraps_prime_check: true    # agent creates FULL checker if missing — not user
agent_owns_checker_config: true       # yaml, CI, steps, stack adapter — agent configures
agent_runs_checker_in_shell: true     # agent executes; NEVER ask user to run
agent_evidence_required: true
verify_final: <stack-native quality gate>   # e.g. python -m scripts.prime_check | npm run prime:check | make prime-check
verify_evidence: <same> --evidence
risk_tiers: LITE | STANDARD | PRIME | CRITICAL
default_tier_real_project: STANDARD         # PRIME when triggers fire (A01)
adoption_mode: greenfield | legacy          # legacy = diff-100 + ratchet
test_pyramid: unit → integration → contract → property
coverage: 100_percent_line_and_branch
coverage_legacy: 100_percent_on_changed_files_only
adr_dir: docs/adr/
prime_check_config: scripts/prime_check.config.yaml
stack_adapters: python | node | rust | go | kotlin | swift
```

**Agent rule:** нет quality gate (tier ≥ PRIME) → агент **сам** пишет FULL checker ([AGENT-5](#agent-5--prime-check)), config, CI — потом фича. Пользователь **не участвует**.  
**Agent rule:** checker = истина; red → агент чинит **код и/или checker** → re-run → `exit 0` + evidence — **не stop, не делегировать**.  
**Agent rule:** **Project Skin** — форма как в репо. **Empire Engine** — дисциплина tier **всегда**, без «сойдёт для этого проекта». Конфликт формы → ADR; конфликт качества → **Empire wins**.

---

## AGENT-OMEGA — Execution phases (before any code)

**MUST** выполнить фазы **в порядке** на tier ≥ PRIME. На LITE/STANDARD — **SHOULD** checklist (пропуск с обоснованием в ответе).

### PHASE 0 — LOCK

```text
assign tier → tier ≥ PRIME?
  → quality gate exists + config + CI? NO → STOP all feature work
      → agent bootstraps FULL checker (AGENT-5): scaffold, ~50 steps, yaml, CI, deps
      → agent runs FULL → green (or legacy ratchet ADR) → ONLY THEN feature
  → adoption_mode? greenfield | legacy (A31) — agent sets in config
  → stack? agent detects → picks adapter → wires tools in checker
```

### PHASE 1 — DESIGN ARTIFACT (в ответе до кода)

```text
tier + triggers: [STANDARD | PRIME — why]
stack + existing_patterns: [detected — MVC | hexagonal | FP | framework-native]
files_to_touch: [...]
new_error_variants: [...]
new_operations: [HTTP route | RPC method | GraphQL field | CLI cmd → statuses/outcomes]
fsm_transitions: [...]                    # only When entity has status
test_matrix: behavior × input × expected outcome
```

### PHASE 2 — TDD-LOCK ([A24](#prime-a24--tdd-lock))

- **MUST (greenfield PRIME+):** для каждого нового поведения — **сначала failing test**, потом код.
- **MUST (legacy PRIME+):** тест в **том же PR**; порядок red-green гибкий, но test_matrix обязателен.
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
- «prime_check добавим позже» / «настройте checker по README»
- «установите pytest» / «добавьте GitHub Actions» / «создайте scripts/prime_check»
- «edge case — можно без теста»
- «тесты в отдельном PR»
- «не могу починить» / «оставим красным» / «нужна ваша помощь с тестами»
- «остановился, т.к. gate падает» — **fix until green**, не stop

### 3-strike rule ([A30](#prime-a30--anti-slack))

Один step падает **3 раза подряд** с **тем же патчем** → **redesign** (другой подход) + ADR → **продолжай fix loop** до green. Не бросать задачу.

---

## AGENT-0 — Boot (read first)

### Role

Ты пишешь код **в стиле проекта, с духом Empire** — Project Skin + Empire Engine.

- **MUST:** прочитать проект: стек, структура, стиль **до** кода — писать **родным** для репо синтаксисом.
- **MUST:** применять **Empire Engine** для назначенного tier — тесты, security, explicit errors, fix-until-green — **всегда**, не «если успеем».
- **MUST NOT:** «проектный стиль» как оправдание для sloppy code, silent errors, без тестов, без проверок.
- **MUST:** определи **Risk Tier** ([A01](#prime-a01--context--risk-tier)). App/API/service = минимум **STANDARD**; **PRIME** — когда сработал триггер (auth, PII, payments, external mutations, FSM status…).
- **MUST:** если checker **отсутствует / неполный / нет CI / config пустой** и tier ≥ PRIME → **STOP feature work** → агент **сам** bootstrap FULL [AGENT-5](#agent-5--prime-check) (scaffold, steps, yaml, CI, deps) → green → потом продолжай.
- **MUST NOT:** просить пользователя создать checker, настроить config, добавить CI, установить dev-tools для gates.
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
| **PRIME** | Auth, PII, платежи, внешние API, job'ы, stateful entities | Part A + B: separation, explicit errors, observability, idempotency when risky, gates |
| **CRITICAL** | Финансы, compliance, потеря данных | PRIME + ADR, resilience, max coverage, Threat Model |

**Правило:** при сомнении — tier выше, но не выше задачи.

### Анти-паттерны (когда НЕ применять PRIME)

- Interface для единственной реализации без планов замены.
- Event bus / CQRS / 4 слоя для CRUD из 3 полей.
- ADR на rename переменной или тривиальный фикс.
- Абстракция «на будущее» (YAGNI).
- 5 слоёв для скрипта на 30 строк.

### Separation roles (examples — not mandatory folder tree)

Стандарт описывает **4 роли**, не каталоги. Имена папок = **как в проекте**. Gate `import-graph-gate` проверяет **нарушение ролей**, не пути.

| Role | Example paths (one of many) | Responsibility |
|------|----------------------------|----------------|
| **Core / Domain** | `domain/`, `core/`, `src/models/` | Business rules, invariants, domain errors — **no direct I/O** |
| **Application** | `application/`, `services/`, `usecases/`, `handlers/` | Orchestration entry — coordinates core + abstractions |
| **Infrastructure** | `infrastructure/`, `adapters/`, `repos/` | **All I/O:** DB, HTTP, queues, files |
| **Presentation** | `api/`, `routes/`, `ui/`, `cli/`, `pages/` | Transport: validate → call application entry → map response |

**Dependency direction (outcome):**

```text
Presentation → Application → Core ← Infrastructure (implements abstractions)
```

Core **must not** import Infrastructure or Presentation.  
**Stack equivalents:** MVC Controller→Service; Nest Controller→Provider; Rust handler→app fn; Rails controller→service object — см. [Pattern Catalog](#pattern-catalog--stack-native-equivalents).

### Global FORBIDDEN

- **MUST NOT:** construct application entry / wire deps manually inside transport (`new Handler(...)` без DI/framework).
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
| New/changed exposed operation (HTTP/gRPC/GraphQL/CLI) | ≥PRIME | A02, A03, A29 | `route-matrix-gate` + `zta-matrix-gate` |
| New feature / provider | ≥PRIME | A04–A07, A12, A24 | TDD → `pytest-unit` → full |
| Auth / session | ≥PRIME | A02, A16, A29 | `zta-matrix-gate` |
| DB schema / persistence | ≥PRIME | A20, B06 | integration + `schema-drift` |
| New dependency | any | A19 | `dependency-audit` + lockfile |
| Docker / compose / deploy | ≥PRIME | A16, A23 | `docker-security` + `prod-config` (When containerized) |
| Idempotency / retries | ≥PRIME | A14, A09 | integration + contract |
| Stateful entity (status) — When in design artifact | ≥PRIME | B06, A14 | `fsm-transition-gate` + concurrency |
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
[ ] Risk Tier assigned with triggers documented (STANDARD default; PRIME when fired)
[ ] Scanned touched files — stop-the-line if violation
[ ] ZERO untested lines on changed files (coverage-diff-100 green)
[ ] ZERO untested branches on changed files (coverage-branch-100)
[ ] coverage-ratchet: no drop vs main
[ ] no-pragma-no-cover + no-empty-test + no-trivial-assert GREEN
[ ] Every Err variant has test (err-variant-gate)
[ ] Every exposed operation × outcome in test_matrix (route-matrix-gate)
[ ] Every protected operation: auth matrix (zta-matrix-gate)
[ ] Fail-fast at boundary (A17); ZTA before UC (A02)
[ ] gitleaks-history + no-secrets + dependency-audit GREEN (A19)
[ ] import-graph-gate + di-graph-gate + cyclomatic-gate GREEN
[ ] docker-security + prod-config + health-gate if infra touched (A23, B13)
[ ] FSM transitions tested + concurrency where applicable (B06, A14)
[ ] State-changing + retry risk: idempotency + double-submit test (A14, when applicable)
[ ] Multi-module: no cross-module private type imports (A04, when applicable)
[ ] Every Err: rule_id + state_snapshot + correlation_id (A10, B03, error-context-gate)
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

## AGENT-VERIFY — You run the quality gate (non-negotiable)

**Scope:** tier ≥ PRIME — **всегда**. Tier LITE — исключение.  
**Ты = оператор checker.** Нет в репо → ты **создаёшь FULL** ([AGENT-5](#agent-5--prime-check)). Есть → ты **гоняешь** в shell. Красный → ты **чинишь** (код или checker). Пользователь **не в цепочке**.

**Entrypoint:** stack-native (`python -m scripts.prime_check`, `npm run prime:check`, `make prime-check`…) — один контракт (steps, findings, exit 0).

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

5. If fail (FIX UNTIL GREEN · FULL-COLLECTION):
   FULL run collects ALL failures → read EXEC SUMMARY → FIX PLAN
   batch-fix ALL P1 findings → rerun P1 group → batch P2 → batch P3
   loop until --diff + FULL exit 0 (default collect, not --fail-fast)
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

**Quality gate** — **единственный** merge gate на tier ≥ PRIME.  
**Владелец: агент на 100%.** Создаёт · настраивает · дописывает steps · вешает CI · ставит dev-deps · запускает · чинит до green. **Пользователь не трогает checker.**

**Reference implementation:** Python `scripts/prime_check/` — reference scaffold; на другом стеке агент делает эквивалент (`npm run prime:check`, `make prime-check`…) с **тем же контрактом** (steps, Finding, evidence, exit 0).

### Agent ownership checklist (MUST — агент делает сам)

```text
[ ] Detect stack → pick adapter row (lint, types, unit, coverage, security)
[ ] Scaffold orchestrator + reporter + finding + evidence + steps/
[ ] Implement ALL applicable steps for tier (~50 — не заглушки)
[ ] Write prime_check.config.yaml: tier, adoption_mode, runtime_scope, monorepo_scopes
[ ] Wire CI job — identical command to local
[ ] Add dev-deps to project (pytest, ruff, eslint… — что нужно gates)
[ ] Run --list → all steps registered
[ ] Run FULL → fix checker bugs → fix codebase → exit 0
[ ] Document entrypoint in README fragment if project has no docs
```

### Если скрипта нет — агент пишет СНАЧАЛА (пользователь ждёт)

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

### AST Prosecutor — не CI-обёртка, а ИИ-прокурор

**Проблема:** checker только с `pytest` + coverage = хорошая CI-обёртка. Агент говорит «готово» словами — checker не может возразить.

**Решение:** **AST Prosecutor** — **исходники**, которые **агент сам пишет** в `scripts/prime_check/` ([AGENT-5](#agent-5--prime-check)). Не .exe, не скачиваемый бинарник, **не в репо MAWYXX Prime**. Локальный Python/Node/Rust скрипт парсит AST + import graph и выдаёт FAIL/FINDING. **Слова агента ≠ доказательство. Exit 0 = единственная правда.**

**«7 Binary Traps»** = бинарный **вердикт** (pass/fail), не скомпилированный файл.

**Skin & Engine:** нам похер имена папок (`Skin`). Engine = prosecutor читает `architecture.*` scopes из config и проверяет **outcomes** по графу импортов и AST — не по слову «Domain» в пути.

```text
CI-only checker:     tests pass? coverage OK? → merge
AST Prosecutor:      tests + coverage + import graph + DI purity + nondeterminism
                     + explicit errors + thin handlers + complexity + anti-fork
                     → FAIL PRIME-Axx [gate] file:line hint → agent MUST fix
```

**MUST:** architecture gates реализованы через **AST/import graph** — не regex-only, не «надеемся на линтер».
**MUST:** каждый FAIL → structured Finding (rule ID, file:line, snippet, hint, rerun cmd) — см. [Report output](#report-output--agent-readable-diagnostics). Агент **не гадает** по сырому pytest/ruff — читает EXEC SUMMARY → FIX PLAN → Finding.
**MUST NOT:** stub step `return []` — prosecutor gates = real parsers per stack adapter.
**MUST NOT:** «import-graph failed» без file:line, import chain и hint куда перенести код.

#### Config: role scopes (Skin → Engine mapping)

Агент **сам** заполняет при bootstrap — по фактической структуре репо:

```yaml
architecture:
  core_scope: [src/core/**, domain/**, internal/models/**]       # testable business logic
  application_scope: [src/app/**, usecases/**, services/**]
  presentation_scope: [src/api/**, routes/**, controllers/**, pages/**]
  infrastructure_markers: [infra/**, adapters/**, repositories/**]
  # imports FROM these paths INTO core_scope = FAIL import-graph-gate
  banned_imports_in_core:          # extend per stack
    python: [sqlalchemy, fastapi, httpx, requests, oracledb, pymongo, redis, celery]
    node: [express, axios, pg, mongodb, typeorm]
    go: [net/http, database/sql, gorm]
  testable_core_scope: [core_scope + application_scope]  # deterministic-runtime, anti-null
  handler_max_logic_lines: 15                            # handler-purity-gate
  cyclomatic_max: 10                                   # cyclomatic-gate (A11)
  file_max_lines: 300                                    # file-size-guard
```

#### 🔱 7 Binary Traps — что prosecutor-скрипт (написанный агентом) чекает по AST

| # | Gate | AST / analysis | Outcome | Rule |
|---|------|----------------|---------|------|
| 1 | **`import-graph-gate`** | Парсит `import`/`require`/`use` во всех файлах → строит DAG. Любой edge **core → infrastructure/presentation** или **core → banned module** = violation. | `sqlalchemy` в core file → instant FAIL | [A05](#prime-a05--layer-law) |
| 2 | **`di-purity-gate`** | AST: `New(...)` / `new Foo()` / прямой вызов конструктора infra-класса (`PostgresRepository()`, `MongoClient()`, `axios.create`) внутри `application_scope` / `core_scope`. Allowlist: value objects, DTO, pure factories in tests. | Hardcoded DB client в UC → FAIL | [A06](#prime-a06--di--ports) |
| 3 | **`deterministic-runtime-gate`** | AST + regex в `testable_core_scope`: `datetime.now`, `time.time`, `uuid4`, `random.randint`, `Date.now`, `Math.random`, `Uuid::new_v4`. Denylist per adapter. | `uuid4()` в core → FAIL, flaky tests impossible | [A15](#prime-a15--deterministic-time) |
| 4 | **`anti-null-gate`** | Type checker + AST: return type `Optional`/`| None`/`null` на application entry; `return None` / `return null` как исход; nullable chain без guard. **Outcome:** no silent null as failure — not «must be Result monad» (Go `error`, Rust `Result`, typed throw OK). | `-> Order \| None: return None` → FAIL | [A10](#prime-a10--result) |
| 5 | **`handler-purity-gate`** | AST: считает **логические** строки в `presentation_scope` handlers (exclude imports, decorators shell, blank). Flags: `if/else` business branches, SQL, direct repo calls, loops >1 nesting. | Handler >15 lines logic or business `if` → FAIL | [A05](#prime-a05--layer-law) |
| 6 | **`cyclomatic-gate`** + **`file-size-guard`** | AST: McCabe per function; LOC per file. Thresholds from config (`cyclomatic_max: 10`, `file_max_lines: 300`). Ratchet: complexity не растёт vs `main` on touched files. | 400-line god-service, complexity 14 → FAIL | [A11](#prime-a11--decomposition) |
| 7 | **`anti-fork-gate`** | Glob + AST fingerprint: `*_v2`, `*Copy`, `*Old`, `*New` policy files; duplicate validation/error-map blocks (hash AST bodies across repo). | Second auth validator file → FAIL | [A08](#prime-a08--anti-fork) |

#### Stack-native AST tooling (agent wires per detected stack)

| Stack | Import graph | AST parse | Complexity |
|-------|--------------|-----------|------------|
| **Python** | `libcst` / `ast` + `importlib` | `ast.NodeVisitor` | `radon` / `lizard` |
| **TS/Node** | `@typescript-eslint/parser` + `madge` | TS AST | `eslint complexity` |
| **Rust** | `syn` / `cargo tree` | `syn` | `cargo-geiger` + custom |
| **Go** | `go/parser` + `golang.org/x/tools/go/packages` | `go/ast` | `gocyclo` |
| **Kotlin** | detekt architecture | PSI | detekt complexity |
| **Swift** | SourceKit | SwiftSyntax | swiftlint |

**Agent MUST:** при bootstrap создать `steps/architecture/` с реализацией **всех 7 traps** для detected stack — не откладывать «на потом».

#### Example FAIL (agent-readable — не спорить, чинить)

```text
FAIL PRIME-A05 [import-graph-gate] P1
  file:    src/core/order.py:4
  issue:   core imports infrastructure: sqlalchemy.orm
  snippet: |
    > 4 | from sqlalchemy.orm import Session
  hint:    move persistence to adapters/; core depends on port Protocol only
  rerun:   python -m scripts.prime_check --only import-graph-gate

FAIL PRIME-A06 [di-purity-gate] P1
  file:    src/app/place_order.py:28
  issue:   direct instantiation PostgresOrderRepo() inside application entry
  hint:    inject IOrderRepository via constructor / FastAPI Depends
  rerun:   python -m scripts.prime_check --only di-purity-gate
```

### AI MUST maintain

- **MUST:** `python -m scripts.prime_check` — Windows/Linux/macOS.
- **MUST:** каждый fail → **structured Finding** (см. [Report output](#report-output--agent-readable-diagnostics)) — не сырой stdout линтера.
- **MUST:** `--list` / `--only <step>` / `--diff` / `--evidence` / `--json` / `--report <path>` / full run.
- **MUST:** local ≡ CI (identical command).
- **MUST:** новый route/UC/Err/dockerfile → тесты + gates **в том же PR**.
- **MUST:** агент **сам** создаёт, настраивает, запускает, чинит checker — **никогда** не делегирует пользователю.
- **MUST:** checker сломан / step missing → агент **чинит checker**, не обходит manual lint.
- **MUST NOT:** «у вас нет prime_check — настройте по README» / «запустите npm test» / «добавьте workflow».
- **MUST NOT:** обрезать coverage/matrix findings без `... and N more` + путь к `--report`.
- **MUST NOT:** печатать только «tests failed» без file:line, rule ID и hint.
- **MUST NOT:** в спеке, отчётах или ответах агента — disclaimers «prime_check не делает X» / «это только маркетинг» / README vs reality. Один продуктовый голос.

### Report output — agent-readable diagnostics

**Цель:** агент читает отчёт и **сразу знает** — что сломано, где, какой rule, какой тест добавить. Без гадания по логам pytest/ruff.

#### FULL-COLLECTION + FIX PLAN (default — не fail-fast)

**По умолчанию** FULL run **не останавливается** на первом FAIL. Orchestrator **гоняет все применимые steps**, собирает **все** findings, потом один отчёт:

```text
FULL run (default):
  step₁ FAIL → continue
  step₂ PASS → continue
  step₃ FAIL → continue
  … все ~50 steps …
  → reporter: EXEC SUMMARY + FIX PLAN (P1→P2→P3) + ALL findings

--fail-fast (optional dev only):
  stop after first P1 — НЕ default перед «done»
```

**Зачем (GOD MODE fix loop):**
- **Тотальная картина** — агент за один прогон видит **все** косяки, не 1-of-N whack-a-mole.
- **Batch fix** — читает FIX PLAN → чинит **весь P1 batch** (все карточки P1) **за один заход** → один `rerun` на группу → потом P2 → P3.
- **Экономия контекста** — не 5 прогонов терминала с одним и тем же логом; один structured report → один edit wave.

**MUST (orchestrator):** default = **collect all** step failures; `exit 1` в конце если был любой FAIL.  
**MUST (agent on RED):** fix **все** findings текущего приоритета (P1 batch) **до** rerun — не «один fix → rerun → один fix».  
**MUST NOT:** declare done после partial P1 fix при оставшихся P1 в том же batch.

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

▸ MATRIX GAPS                     ← err / route / zta / fsm / idempotency / context
  ERR VARIANTS (missing test_err_*):
    OrderNotFound      → src/domain/errors.py:12
    PaymentFailed      → src/domain/errors.py:28
  ERR CONTEXT (missing rule_id / snapshot / trace_id):
    PaymentFailed      → src/domain/errors.py:28
  ROUTE MATRIX:
    GET /api/v1/orders/{id}  missing: 404, 403-forbidden-scope
  ZTA MATRIX:
    POST /api/v1/orders  missing: no_credentials→401, expired_token→401
  FSM TRANSITIONS:
    Order: PAID→SHIPPED  untested edge
  IDEMPOTENCY (missing test_double_submit_*):
    PlaceOrderUC       → src/application/place_order.py:34
  CONTEXT LEAK (cross-module domain entity import):
    payments → users.domain.User  → src/payments/charge.py:3
  ARCHITECTURE (AST Prosecutor):
    import-graph-gate  src/core/order.py:4  core → sqlalchemy.orm
    di-purity-gate     src/app/place_order.py:28  PostgresOrderRepo() inside UC
    anti-null-gate     src/app/get_order.py:12  return None as failure path

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
| `idempotency-matrix-gate` | MATRIX GAPS → IDEMPOTENCY | state-changing UC без `test_double_submit_*` |
| `context-leak-gate` | MATRIX GAPS → CONTEXT LEAK | cross-bounded-context import domain entity |
| `error-context-gate` | MATRIX GAPS → ERR CONTEXT | `Err` без rule_id / state_snapshot / correlation_id |
| `test-matrix-gate` | MATRIX GAPS → DESIGN | UC из design artifact без теста в repo |
| `import-boundaries` | FINDINGS | forbidden import chain: A → B → C |
| `import-graph-gate` | FINDINGS + ARCHITECTURE | import edge core→infra; banned module; full chain A→B→C |
| `di-purity-gate` | FINDINGS + ARCHITECTURE | `new ConcreteRepo()` file:line; suggest inject/port |
| `deterministic-runtime-gate` | FINDINGS + ARCHITECTURE | `uuid4`/`now` call file:line; suggest ITimeProvider |
| `anti-null-gate` | FINDINGS + ARCHITECTURE | `return None` / nullable return; suggest explicit error |
| `handler-purity-gate` | FINDINGS + ARCHITECTURE | handler logic lines count; business if in route |
| `cyclomatic-gate` / `file-size-guard` | FINDINGS | function complexity N>max; file LOC; extract target |
| `anti-fork-gate` | FINDINGS | `*_v2` path; duplicate policy hash; extend SSOT hint |
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

#### Agent discipline on RED (batch fix loop)

```text
1. FULL run (no --fail-fast) → read EXEC SUMMARY + FIX PLAN — не сырой лог
2. Collect all P1 Finding cards → fix ALL in one edit wave (3–5 files OK)
3. Rerun P1 group cmd from FIX PLAN (e.g. --only coverage-branch-100) OR --diff if mixed
4. P1 green? → batch-fix ALL P2 → rerun → batch-fix ALL P3 → rerun
5. --diff green → FULL collect again → exit 0 → --evidence

Anti-pattern: fix 1 finding → full rerun → fix 1 → full rerun (wastes context)
Correct:       fix ALL P1 → rerun once → fix ALL remaining P1 → …
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
architecture:                      # AST Prosecutor — agent maps Skin → scopes
  core_scope: [domain/**, src/core/**]
  application_scope: [application/**, usecases/**]
  presentation_scope: [api/**, routes/**, controllers/**]
  testable_core_scope: [domain/**, application/**]
  handler_max_logic_lines: 15
  cyclomatic_max: 10
  file_max_lines: 300
  banned_imports_in_core: {python: [sqlalchemy, fastapi], node: [express, pg]}
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
| **ARCHITECTURE — AST Prosecutor (7 Binary Traps)** | | |
| `import-boundaries` | quick role import check | A05 |
| `import-graph-gate` | **AST** import DAG; core ↛ infra/presentation/banned | A05 |
| `deterministic-runtime` | **AST** nondeterminism ban in testable_core_scope | A06, A15 |
| `anti-null-gate` | **AST** + types: no silent null as failure path | A10 |
| `immutability-gate` | domain/app entities immutable; no in-place mutation | A05, B06 |
| `context-leak-gate` | no cross-bounded-context import of domain entities | A04, A05, B05 |
| `idempotency-matrix-gate` | state-changing UC has key + ledger + double-submit test | A14, A09, A12 |
| `error-context-gate` | every Err type: rule_id + state_snapshot + trace_id | A10, B03 |
| `no-transport-in-domain` | no HTTPException/throw in domain | A10 |
| `di-purity` | **AST** no hardcoded infra `new`/`()` in core/app | A06 |
| `di-graph-gate` | wiring only in composition root | A06 |
| `handler-purity-gate` | **AST** presentation handler ≤15 logic lines, no business if | A05 |
| `anti-fork-gate` | **AST** fingerprint: `*_v2`, duplicate policy blocks | A08 |
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
| [A05](#prime-a05--layer-law) | Layer law / separation roles | STANDARD+ |
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
\*Empire Engine outcomes в Part A/B. **Skin** = Pattern Catalog. **Engine** = всегда для tier; **When** = только механизм (FSM/ledger/Docker), не «можно хуже».

---

# Part A — Code quality rules

## PRIME-A01 — Context & Risk Tier

**Min tier:** all **Applicability:** Always

- **MUST:** read project structure, stack, patterns, CI **before** writing. **Repo conventions = default form.**
- **MUST:** classify tier. **App / API / service / lib с I/O = минимум STANDARD.** LITE — одноразовые скрипты без сети.
- **MUST:** elevate to **PRIME** when **any** trigger fires:
  - authn/authz, PII, payments/money, external API mutations, background jobs with side effects
  - entity with **status/lifecycle** (→ FSM When applicable)
  - multi-module monorepo or service split (→ context isolation When applicable)
  - operations where **retry/double-submit** is dangerous (→ idempotency When applicable)
- **MUST:** elevate to **CRITICAL** for finance, compliance, irreversible data loss.
- **MUST:** if tier ≥ PRIME and no quality gate → bootstrap first ([AGENT-5](#agent-5--prime-check)).
- **MUST:** set `adoption_mode`: greenfield (full scope) or legacy (diff-100 + ratchet) ([A31](#prime-a31--legacy-adoption)).
- **MUST:** PRIME defines **quality outcomes**, not folder tree or framework choice.
- **MUST NOT:** downgrade tier to avoid tests or gate bootstrap.
- **MUST NOT:** impose Clean/DDD/UseCase/Result if project uses other proven pattern — map to [Pattern Catalog](#pattern-catalog--stack-native-equivalents).

---

## PRIME-A02 — Zero Trust (ZTA)

**Min tier:** PRIME+ **When:** exposed operation requires auth **Enforced by:** `zta-matrix-gate`, contract tests

- **MUST:** authn + authz on **every** protected **operation** (HTTP route, RPC method, GraphQL field, CLI with credentials) **before** application logic.
- **MUST:** localhost, docker network, `127.0.0.1`, sidecar, `/internal`, `/debug` — **те же правила** что и public internet в prod/staging.
- **MUST NOT:** `LIME_TESTING=1`, compose network, reverse proxy, VPN как substitute auth.
- **MUST NOT:** trust «мы внутри кластера» — [A23](#prime-a23--infra--docker-security).
- **MUST:** allow/deny in Application layer — not «header present ⇒ OK».
- **MUST:** validate input at boundary before UC ([A18](#prime-a18--owasp-input-hygiene)).
- **MUST:** least privilege — minimal scopes, DTO fields, per-role secrets.
- **MUST:** deny-by-default; DB/Redis/cache **не** на public без TLS+auth.
- **MUST:** `zta-matrix-gate` — full auth scenario matrix per **protected operation** ([A29](#prime-a29--zta-matrix)). HTTP — один частный случай.
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

**Min tier:** PRIME+ **When:** swappable provider OR multi-module **Enforced by:** `context-leak-gate` (When multi-module)

- **MUST:** extend via **abstraction** (interface, trait, protocol) + adapter — **когда** 2+ impl или план замены.
- **MUST:** **plugin boundary** — new provider (payment, storage, notifications, auth) adds via abstraction; **no edits to existing Core** for wiring swap.
- **MUST:** modules communicate through **published API** (public types, events, RPC contract) — not private internals.
- **MUST NOT:** duplicate policy across DI, API, infrastructure.
- **MUST NOT:** nest I/O inside core/application packages.

### Module isolation (PRIME+) — When multi-module / service split

ИИ склеивает модули микро-импортами private types → распределённый монолит. **Запрещено импортировать чужие private domain types.**

- **When:** single-package app / trivial script → isolation gate **N/A**.
- **When:** multi-module monorepo or microservices → **MUST** isolate.
- **MUST:** каждый модуль владеет **своими** internal types.
- **MUST NOT:** import/re-export **private** entity/aggregate/VO другого модуля.
- **MUST:** cross-module data — **DTO / primitives / public contract types / events**:
  - primitives (`user_id: UUID`, `amount_cents: int`);
  - Domain Events (`UserRegistered`) — async ([B03](#prime-b03--sre--observability--events));
  - published interfaces — не concrete internal types ([A06](#prime-a06--di--ports)).
- **MAY:** **shared kernel** (общие types) — **только** с ADR + explicit `shared/` или `contracts/` package; gate allowlists ADR path.
- **Enforced by:** `context-leak-gate` — import private type из `module_a` в `module_b` → exit 1 (unless ADR shared kernel).

```python
# BAD:  from users.domain import User  # private type in payments/
# GOOD: charge(user_id: UserId, amount: Money)  # primitive/DTO at boundary
# GOOD: shared kernel ADR → contracts/user_id.py — both modules import contracts only
```

---

## PRIME-A05 — Layer law

*Separation roles — not mandatory folder tree. Form = repo-native ([Pattern Catalog](#pattern-catalog--stack-native-equivalents)).*

**Min tier:** STANDARD+ **Applicability:** separation of business logic from I/O — **форма = repo-native**  
**Enforced by (PRIME+):** `import-boundaries` · `immutability-gate` (When applicable) · `context-leak-gate` (When multi-module)

| Role | MUST | MUST NOT |
|------|------|----------|
| **Core / Domain** | business rules, invariants, domain errors; abstractions for I/O | direct I/O, frameworks, DB, HTTP, time/uuid in core; god-classes |
| **Application** | orchestration entry; explicit error handling per stack | direct DB/HTTP in orchestration when project separates adapters; transport exceptions in core |
| **Infrastructure** | I/O impls, persistence, clients, resilience | business policy |
| **Presentation** | validate input, invoke application entry, map response | business logic; manual wiring without project DI |

- **MUST NOT:** business logic in UI components, fat route handlers, CLI `main`, mobile Views.
- **MUST:** folder names and entry naming = **project convention** (UseCase, Handler, Service, Command, plain `fn` — см. Pattern Catalog).
- **SHOULD NOT:** CQRS / extra layers for trivial CRUD ([B01](#prime-b01--cqrs), [B07](#prime-b07--yagni)).

**Thin transport (stack-native examples):**

```python
# FastAPI — DI injects application entry
@router.post("/orders")
async def create_order(svc: OrderService = Depends(get_svc), body: CreateOrderDTO = ...):
    return map_outcome(await svc.place(body))
```

```typescript
// Express/Nest — controller → service/handler
router.post('/orders', (req, res) => mapOutcome(orderService.place(req.body), res));
```

```rust
// Axum — handler → app::place_order()
async fn create_order(State(svc): State<AppSvc>, Json(body): Json<Dto>) -> impl IntoResponse { ... }
```

**MAY:** validation types as data-only (Pydantic, zod) — not framework coupling in core.

### Immutability (PRIME+) — When races / FSM / shared aggregate

- **When:** single-threaded script, DB-only state, no shared in-memory aggregate → **N/A** (persist in repo layer OK).
- **When:** concurrent access, FSM, in-memory shared state → **MUST** immutable transitions or equivalent (new instance, copy, persistent data structure).
- **MUST NOT:** in-place mutation of shared aggregate passed between threads/tasks without synchronization + ADR.
- **Enforced by:** `immutability-gate` · [B06](#prime-b06--fsm) (When status entity).

---

## PRIME-A06 — DI & ports

*Injectable dependencies — framework DI, traits, params OK; manual ports not required.*

**Min tier:** PRIME+ **Enforced by:** `di-purity` · `deterministic-runtime` (with [A15](#prime-a15--deterministic-time))

- **MUST:** external deps (DB, HTTP, time, ID, random, config) — **injectable** per project style: constructor DI, params, framework container, `Clock` trait, test hooks ([A15](#prime-a15--deterministic-time)).
- **MUST:** one canonical impl per policy — SSOT, not duplicate helpers ([A08](#prime-a08--anti-fork)).
- **MUST:** cross-module via published API — DTO/primitives/events ([A04](#prime-a04--integration--plugin-boundaries)).
- **MUST NOT:** `new ConcreteRepo()` / hardcoded clients inside testable core when project uses DI.
- **MUST NOT:** service locator, globals, hidden mutable state in core.
- **MUST:** tests substitute via Fake/Mock/InMemory — predictable behavior.
- **MAY:** framework-native DI (Nest `@Injectable`, Spring `@Autowired`, FastAPI `Depends`) — не обязательно manual ports.

---

## PRIME-A07 — Design-first order

**Min tier:** PRIME+ **Applicability:** logical order — names = repo-native

0. Tier + triggers + existing patterns.  
1. Contract/DTO + invariants; SemVer if breaking ([A21](#prime-a21--semver--contracts)).  
2. Core rules + abstractions for I/O.  
3. Application entry + explicit errors + injectable deps.  
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

*Explicit failure paths — stack-native; `Result` is one option, not the only ([Pattern Catalog](#pattern-catalog--stack-native-equivalents)).*

**Min tier:** varies — see table **Enforced by (PRIME+):** `anti-null-gate` · `err-variant-gate` · `error-context-gate` · `no-transport-in-domain`

### Error handling by tier

| Tier | Approach |
|------|----------|
| **LITE** | Clear messages; fail-fast on bad input |
| **STANDARD** | Typed errors / error codes; do not swallow exceptions |
| **PRIME+** | Named domain errors; **explicit failure paths** — stack-native (см. Pattern Catalog) |
| **Boundary** | User-friendly message; details in log only — not in UI |

### Explicit errors (PRIME+) — outcome, not one monad

**Outcome:** caller always knows success vs failure — no silent `null` as error, no swallowed exception in core.

| Stack | Acceptable forms |
|-------|------------------|
| Python/TS | `Result[Ok,Err]`, `Either`, discriminated union, typed exception hierarchy |
| Rust | `Result<T,E>`, `thiserror` enums |
| Go | `(T, error)` — **must** check `err != nil` |
| Java/Kotlin | sealed Result, `Either`, typed exceptions (not generic in core) |
| FP | `IO`/`Task` with typed failure channel |

- **MUST:** application/core entry returns **typed failure** or throws **named** domain error — not generic `Error("failed")`.
- **MUST:** presentation maps outcome → response only.
- **MUST NOT:** transport exceptions (`HTTPException`, status codes) in core.
- **MUST:** every error variant has **dedicated test** (`err-variant-gate` checks coverage, not regex name).

### No silent null as failure (PRIME+) — `anti-null-gate`

Агенты `return None` / `null` как «не найдено» → NPE downstream. **Запрещено в testable core.**

- **MUST NOT:** nullable return в application/core как единственный сигнал ошибки/отсутствия.
- **MUST:** explicit branch — `match` / `if err` / `.map_err` / checked exception.
- **MAY:** `Option`/`Maybe` для **optional data** (не для error path) — с guard перед use.
- **MAY:** nullable types in infra/ORM glue — с ADR boundary.

```python
# BAD:  def get_order(id) -> Order | None: return None
# GOOD: Result / raise OrderNotFound / (Order, error) per stack
```

### Observable failures (PRIME+) — logging contract

**Outcome:** prod failure локализуется по trace за секунды. Поля могут жить в **log middleware** или **error type** — gate проверяет **наличие в log event**, не обязательно в struct.

- **MUST** at log site on failure: `invariant_id` (rule/business code) + safe `context` (ids, status — **no PII**) + `correlation_id`/`trace_id` ([B03](#prime-b03--sre--observability--events)).
- **MUST:** structured JSON logging — не `console.log("error")`.
- **MUST:** transport пробрасывает correlation id from client through core.
- **Enforced by:** `error-context-gate` — lint/log fixture asserts fields on each error variant test.

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

**Doctrine:** в `runtime_scope` **не существует** непокрытой строки и ветки. Нет теста = нет merge. Core без I/O → быстрые unit-тесты. **Fakes** в unit; **real infra** в integration — не наоборот.

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
- **MUST (PRIME+):** каждый state-changing UC — `test_double_submit_*` / `test_idempotency_replay_*` ([A14](#prime-a14--idempotency), `idempotency-matrix-gate`).

---

## PRIME-A13 — Definition of Done

**Min tier:** PRIME+

- **MUST NOT:** duplicate policy/mapper/facade.
- **MUST:** thin transport + injected application entry + explicit error mapping.
- **MUST:** update API docs / ADR if contracts changed.
- **MUST:** tests per [A12](#prime-a12--tests--coverage); `prime_check` exit 0 + evidence block ([A22](#prime-a22--prime-check), [A26](#prime-a26--evidence-block)).
- **MUST:** formatters green; migrations versioned ([A20](#prime-a20--migrations)).
- **MUST:** breaking changes documented ([A21](#prime-a21--semver--contracts)).
- **MUST:** Threat Model mini if security-sensitive ([A16](#prime-a16--secure-by-design)).

---

## PRIME-A14 — Idempotency

**Min tier:** PRIME+ **When:** state-changing operation + retry/double-submit risk **Enforced by:** `idempotency-matrix-gate`

**Outcome:** повторный вызов с тем же intent → **тот же результат**, без дубля side-effect.  
**Не обязательна форма:** ledger class — достаточно unique index, dedup table, Stripe-style key store, saga idempotency token.

### When REQUIRED

- payments, charges, posts, orders, webhooks, any mutation user can trigger twice (double-click, retry, at-least-once delivery)
- **NOT required:** idempotent reads, pure deletes with no money, internal batch with exactly-once framework guarantee + ADR

### Implementation options (pick one + test)

| Approach | Where |
|----------|-------|
| `Idempotency-Key` header + server dedup store | HTTP APIs |
| Unique DB constraint on `(idempotency_key)` | Persistence layer |
| Ledger / WAL table `(key → outcome)` | Application layer |
| Client-generated stable token per user action | Mobile/UI |

- **MUST:** stable key per user action across retries — не random per retry.
- **MUST:** dedup check **before** irreversible side-effect (or transactional outbox).
- **MUST (CRITICAL):** all financial mutations idempotent.
- **Enforced by:** `idempotency-matrix-gate` — double-submit test: два вызова, один key → один side-effect, второй = same outcome.

---

## PRIME-A15 — Deterministic time

**Min tier:** PRIME+ **Enforced by:** `deterministic-runtime`  
*Side-Effect Injection — сквозной инвариант вместе с [A06](#prime-a06--di--ports).*

`now()` / `uuid4()` / `random()` в testable core → flaky tests. **Outcome:** same inputs + fixed clock/ID/random in tests → same output.

- **MUST NOT:** direct `Date.now()`, `uuid4()`, `random()` in **testable core** (scope from config — not necessarily `domain/` path).
- **MUST:** inject nondeterminism — ports, params, `Clock` trait, test doubles, `vi.setSystemTime`, frozen clock in Rust tests.
- **MAY:** framework test utilities instead of custom `ITimeProvider` when project already has pattern.
- **MUST NOT:** global singleton clock/random on core path without test override.

**`deterministic-runtime`:** ban direct nondeterminism calls in configured `testable_core_scope` paths.

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

- **MUST:** ~10–15 orchestration lines per application entry (use case / handler / service method).
- **MUST:** DRY for **policy**; duplicate wiring OK ([A08](#prime-a08--anti-fork)).
- **MUST:** project formatters before commit.
- **MUST NOT:** god-class; feature envy.

**Good:** thin `OrderService.place()` + `Order` + injectable `OrderRepository`.  
**Bad:** 400-line god-service — SQL, validation, HTTP mapping in one class.

---

## PRIME-A18 — OWASP input hygiene

**Min tier:** PRIME+ (validation STANDARD+)

- **MUST:** all external input untrusted until schema + auth + policy pass (HTTP, CLI args, WebSocket, file upload…).
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

*Quality gate contract — stack-native entrypoint; Python `prime_check` = reference impl.*

**Min tier:** PRIME+ — **обязателен**. Spec: [AGENT-5](#agent-5--prime-check).

### Purpose

**Единственный** способ сказать «готово» на tier ≥ PRIME: **project quality gate** → **exit 0**.  
**Агент владеет checker целиком:** создаёт · config · CI · ~50 steps · dev-deps · запуск · fix до green. Пользователь **не настраивает и не запускает**.

### MUST

- **MUST:** quality gate **exists + configured + CI wired**; if not — agent bootstraps **FULL** checker **before** feature ([AGENT-5](#agent-5--prime-check)).
- **MUST:** agent writes `prime_check.config.yaml`, implements steps, adds CI job, installs gate dev-deps — **сам**.
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
- Ask user to run checker, configure yaml, add CI, or install pytest/ruff/eslint for gates.
- Ship stub checker with `pass` steps — каждый step = real enforcement.
- Different CI vs local rules.

**LITE scripts only:** exempt from prime_check.

---

## PRIME-A23 — Infra & Docker security

**Min tier:** PRIME+ **When:** containerized deploy or Docker files in repo **Enforced by:** `docker-security`, `compose-security`, `prod-config`

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

- **MUST (greenfield):** PHASE 2 — failing test **before** production code.
- **MUST (legacy):** tests in **same PR**; test_matrix covers all new behaviors — order flexible.
- **MUST:** test_matrix в DESIGN ARTIFACT покрывает все новые behaviors/errors/operations.
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
- **MUST (PRIME+):** при `Err` — log payload = `rule_id` + `state_snapshot` + `correlation_id` из error type ([A10](#prime-a10--result)); prod debug ≤ 1 click from trace.
- **MUST NOT:** PII, secrets, tokens in logs — в т.ч. в `state_snapshot`.
- **Enforced by:** `error-context-gate` (with [A10](#prime-a10--result)).

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

**Min tier:** optional (service split) **Enforced by:** `context-leak-gate` (cross-service)

- **SHOULD:** strict typed contracts; versioned (`v1`, `v2`).
- **SHOULD:** gRPC/proto or OpenAPI per project; see [A21](#prime-a21--semver--contracts).
- **MUST (service split):** сервисы общаются как **независимые государства** — DTO/proto messages / events, **не** shared domain entity libs ([A04](#prime-a04--integration--plugin-boundaries)).
- **MUST NOT:** monorepo shared `domain/User.ts` импортируемый payments + users — каждый сервис = свой bounded context + contract types.

## PRIME-B06 — FSM

**Min tier:** PRIME+ **When:** design artifact lists `fsm_transitions` OR entity has lifecycle status field **Enforced by:** `fsm-transition-gate` · `immutability-gate` (When applicable)

**When NOT:** simple enum + validation sufficient; no status field; workflow engine (Temporal) owns graph — document in ADR, gate N/A.

- **MUST:** explicit transition graph when status/lifecycle matters (`Order`, `Job`, `Task`, `Subscription`, `Invoice`…).
- **MUST NOT:** illegal jumps (`DRAFT → COMPLETED` bypassing `PROCESSING`) — enforced in core, not scattered `if`.
- **MUST NOT:** status change from transport bypassing lifecycle rules.
- **SHOULD:** transition returns new state instance when in-memory aggregate ([A05](#prime-a05--layer-law)); DB-only status OK with transactional update + ADR.
- **MUST:** transitions atomic at persistence under concurrency.
- **MUST:** tests for every edge + concurrent transitions where applicable ([A12](#prime-a12--tests--coverage)).

## PRIME-B07 — YAGNI

**Min tier:** all

- **MUST:** full Part A for PRIME+ tasks.
- **MAY:** KISS for LITE without network/secrets/auth.
- **MUST NOT:** YAGNI exempts security ([A16](#prime-a16--secure-by-design)).

## PRIME-B08 — Agent self-review

**Min tier:** all

1. Risk Tier + [AGENT-1](#agent-1--task-router) sections applied.
2. Grep diff: `HTTPException` in domain, `Date.now`, magic numbers, duplicate policy, secrets, f-string SQL, `ALTER TABLE`, `dangerouslySetInnerHTML`, copy-pasted validation, cross-module domain entity imports, state-changing UC without idempotency key, `Err` without `rule_id`/`correlation_id`.
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

**Min tier:** PRIME+ **When:** long-running service / container / K8s deploy **Enforced by:** `health-gate`, `prod-config`

- **MUST:** liveness + readiness probe per deploy model (`/health` + `/ready`, Lambda ping, k8s probes, desktop N/A with ADR).
- **SHOULD:** graceful shutdown handler tested or documented in ADR.
- **SHOULD:** rollback steps in ADR for deploy-touching changes.
- **MUST:** 12-factor config — secrets env/vault only.

## PRIME-B14 — Human handoff

**Min tier:** PRIME+

- **MUST:** evidence block ([A26](#prime-a26--evidence-block)) is the handoff artifact.
- **SHOULD:** list `risks`, `rollback`, `tests_added` for human reviewer.
- **MUST NOT:** hide failing steps or partial coverage in summary.

---

## Pattern Catalog — stack-native equivalents

**Project Skin** — как назвать и разложить. **Empire Engine** — одинаковый для всех строк таблицы.  
Gates проверяют Engine, не заставляют одну колонку DDD.

| PRIME outcome | DDD / Clean (example) | Alternatives (equal if outcome met) |
|---------------|----------------------|-------------------------------------|
| Separation: core ↛ I/O | Domain / App / Infra / Presentation | MVC, Hexagonal, Onion, FP pure core + IO shell, Rails MVC, Nest modules |
| Application entry | `*UseCase.execute()` | `*Handler`, `*Command`, `*Service.method`, MediatR, plain `fn`, Redux thunk, Effect |
| Explicit errors | `Result<Ok,Err>` | Rust `Result`, Go `(T,error)`, sealed exceptions, `Either`, discriminated union |
| Injectable I/O | `IOrderRepository` port | Spring `@Autowired`, Nest provider, trait bounds, constructor params, `Clock` |
| Thin transport | FastAPI route → UC | Axum handler, Express router, gRPC servicer, GraphQL resolver, CLI subcommand |
| Module isolation | Bounded Context | Package-private, crate visibility, Nx libs, `internal/` Go, ADR shared `contracts/` |
| Idempotent mutation | Ledger table | Unique index, Redis SETNX, Stripe idempotency, outbox dedup |
| Lifecycle rules | Domain FSM object | DB CHECK constraint, workflow engine, enum + validator + tests |
| Observable failure | Err struct fields | OTel span attrs, log middleware, structured `logger.error({...})` |
| Quality gate | `python -m scripts.prime_check` | `npm run prime:check`, `make prime-check`, `cargo xtask prime`, CI job contract |

**Agent algorithm:** detect Project Skin in repo → extend it → run **full Empire Engine** for tier → map gates to scopes → ADR only when introducing **new** Skin pattern. **Never** downgrade Engine because Skin is informal.

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
| AST Prosecutor | local AST + import graph gates — 7 Binary Traps; words ≠ proof |
| 7 Binary Traps | import-graph · di-purity · deterministic-runtime · anti-null · handler-purity · cyclomatic · anti-fork |
| AGENT-OMEGA | execution phases 0–4 before any code |
| runtime_scope | paths where 100% coverage required (greenfield) |
| coverage-diff-100 | 100% on changed files (legacy) |
| coverage-ratchet | coverage must not drop vs main |
| evidence block | PRIME-VERIFY-EVIDENCE transcript — mandatory before done |
| adoption_mode | greenfield (full scope) \| legacy (diff + ratchet) |
| stack adapter | per-language tool mapping in prime_check |
| zta-matrix-gate | full auth scenario matrix per protected operation |
| Universal Doctrine | Project Skin · Empire Engine — форма проекта, дух Empire всегда |
| Project Skin | стек, папки, naming, framework-native вид кода |
| Empire Engine | tier-дисциплина всегда: тесты, security, errors, gates, fix-until-green |
| Pattern Catalog | stack-native equivalents — same outcome, different form |
| Applicability | Always / STANDARD+ / PRIME+ / When trigger / Stack-native |
| Separation law | core logic ↛ I/O — roles, not folder names ([A05](#prime-a05--layer-law)) |
| Explicit errors | no silent null as failure; typed failure paths ([A10](#prime-a10--result)) |
| Quality gate | merge gate contract — exit 0; orchestrator per stack ([A22](#prime-a22--prime-check)) |
| TDD-LOCK | failing test before implementation (A24) |
| merge-blocking | prime_check must pass before merge |
| zero_tolerance | 99.99% = 0%; checker > agent words |
| agent_bootstraps_prime_check | if missing — agent writes FULL checker (steps, config, CI) |
| agent_owns_checker | agent creates, configures, runs, fixes checker — user never |
| Finding | one actionable issue: rule ID, step, file:line, hint, rerun cmd |
| FIX PLAN | ordered repair list — agent batch-fixes P1→P2→P3 groups before rerun |
| FULL-COLLECTION | default FULL run executes all steps, collects all findings, one report |
| COVERAGE MAP | per-file line/branch % + exact uncovered lines from reporter |
| MATRIX GAPS | missing test_err_*, route×status, zta scenario, fsm edge, double-submit, context leak, err context |
| Explicit errors (was Anti-Null) | no silent null as failure in core ([A10](#prime-a10--result)) |
| Immutability | When races/FSM — no in-place shared mutation ([A05](#prime-a05--layer-law), [B06](#prime-b06--fsm)) |
| Injectable nondeterminism | time/ID/random injectable in testable core ([A06](#prime-a06--di--ports), [A15](#prime-a15--deterministic-time)) |
| Idempotent mutations | When retry risk — same key → same outcome ([A14](#prime-a14--idempotency)) |
| Module isolation | When multi-module — no private type imports ([A04](#prime-a04--integration--plugin-boundaries)) |
| Observable failures | trace + invariant_id + safe context in logs ([A10](#prime-a10--result), [B03](#prime-b03--sre--observability--events)) |

---

*Ни одной непокрытой строки. Ни одного «готово» при red gate. Агент чинит до green — не останавливается. Ни одного merge без `prime_check` exit 0.*

*End of MAWYXX PRIME v5.2 — Build for Billions. Code for Vibe. Rule with Logic.*
