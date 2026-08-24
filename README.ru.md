# MAWYXX PRIME — стандарт AI-кодинга

*Build for Billions. Code for Vibe. Rule with Logic.*

[English version → README.md](README.md)

Две спеки одной философии: **v3.0** учит паттернам (MIT). **v5.7** именует каждое правило и требует **quality gate** на **правду исхода**, не на наличие артефактов — честные N/A, оракулы в тестах, **живые** порты, no-swallow, **Behavior SSOT**, FFI на PRIME, coverage на I/O/composition, целостность checker. Компактный SSOT.

**Project Skin · Empire Engine:** пиши **в стиле проекта** — но **всегда с дисциплиной Empire**. Зелёный `prime_check` из имён AC, неиспользуемых портов, `#[ignore]` e2e и exclude composition — **не** done. 100% fakes — **не** done.

**v5.7 открыт в репо** — читай, форкай, учись, лично используй бесплатно. **Корпоративное / командное / клиентский прод** — разовая лицензия ($50/сотрудник) → [@ExcitedSkam](https://t.me/ExcitedSkam).

---

## Файлы

| Файл | Содержание | Доступ |
|------|------------|--------|
| `Mawyxx Prime V3.0.md` | 10 разделов · ~220 строк | **MIT · открыт** |
| `Mawyxx Prime V5.7.md` | AGENT-0…5 · **A01–A39** (+ A05a, A12a) · **B01–B14** | **Открыт в репо** · корп = платно |
| `scripts/prime_check/` | **Агент создаёт FULL** по **AGENT-5** (~50+ steps, config, CI) | **Не в репо** — агент bootstrap, config, run, fix — **пользователь не трогает** |

---

## v3.0 — паттерны, которые задаёт стандарт

Что v3 уже описывает (прозой, без ID правил, без machine gate):

### Архитектура и design-паттерны

| Паттерн | Что требует v3 |
|---------|----------------|
| **Separation of concerns** | Core ↛ I/O — часто 4 роли; **папки = конвенция проекта** |
| **DI & IoC** | Зависимости снаружи; нет hardcoded clients в testable core |
| **Coding to interfaces** | Порты для time, ID, DB, HTTP, random, notifications |
| **Plugin boundary** | Новый провайдер через interface — Core не трогаем |
| **CQRS** | Когда read/write разная сложность — не для trivial CRUD |
| **FSM** | Сущности со статусом — явный граф переходов |
| **Domain events** | Core публикует факты; infra доставляет |
| **Idempotency** | `idempotency_key` на опасных retry — v5.7 добавляет **Idempotent-Ledger** (ledger + double-submit gate) |
| **SOLID** | SRP, OCP, LSP, ISP, DIP — в §5 |
| **Fail-fast** | Валидация на границе системы |
| **Typed errors** | Доменные ошибки, не magic exceptions в глубине |
| **DI для time/ID** | `uuid()`, `Date.now()` за интерфейсами — упомянуто, не enforced |

### Production-паттерны

| Паттерн | Что требует v3 |
|---------|----------------|
| **Observability** | trace_id, structured logs, метрики на критичных путях |
| **Resilience** | Circuit breaker, bulkheads, graceful degradation |
| **SRE** | SLI, SLO, error budget, self-healing jobs |
| **ADR** | Context · options · decision · consequences в `docs/adr/` |
| **API contracts** | OpenAPI / schema; versioned breaking changes |
| **Security hygiene** | Нет секретов в коде; валидация ввода; least privilege; нет PII в логах |

### Тестирование

| Паттерн | Что требует v3 |
|---------|----------------|
| **Pyramid** | Unit (fakes) → integration → contract |
| **DI in tests** | InMemory / Fake — предсказуемое поведение |
| **Bug → test** | Каждый фикс — regression test |
| **Coverage** | 100% на CRITICAL paths; meaningful tests elsewhere — **решает агент** |

### Agent protocol (только v3)

- Читать контекст проекта до edit
- Выбрать Risk Tier (LITE / STANDARD / PRIME / CRITICAL)
- Минимальный scope на фичу
- **Self-review checklist** (§10) перед «готово» — honor system, без `exit 0`

---

## v5.7 — Enforcement honesty + Contract Surface (ядро актуального стандарта)

Чем текущий контракт тяжело фейкается:

| Столп | Правило / gate | Что убивает |
|-------|----------------|-------------|
| **Package cohesion** | **A05a** · `package-cohesion-gate` | Flat layer-dump при зелёном import-graph |
| **Test taxonomy** | **A12a** · `test-taxonomy-gate` | Только happy-path · vanity coverage без families |
| **Anti-N/A** | **A12a** · **A35** | `N/A(потом)` / `N/A(одна реализация)` при сработавшем триггере |
| **Behavior lock** | **A34** · `intent-lock-gate` (оракул в **теле** теста) | AC↔имя теста · `assert!(!name.contains("Window"))` |
| **Live Surface** | **A36** · `live-surface-gate` | Порт в yaml без вызова · identity/todo impl · непрочитанное поле Settings |
| **No swallow** | **A37** · `no-swallow-gate` · `err-variant-gate` (provoke path) | `let _ = register` · dump-bucket Err · err-тест без producer |
| **Checker integrity** | **A38** · `checker-integrity-gate` | `return GREEN` · только path.exists · `"AC{i}" in text` |
| **Behavior SSOT / Anti-Clone** | **A39** · `behavior-ssot-gate` · `anti-fork-gate` | Второй экземпляр того же алгоритма · clone-split под A11 · copy-paste чтобы blast A33 «маленький» |
| **Coverage honesty** | **A25** · `exclude-honesty-gate` · `ignored-test-gate` | exclude composition · `#[ignore]` e2e без skipped_steps |
| **FFI на PRIME** | **A16** · `ffi-safety-gate` | unsafe без SAFETY · `safety_profile: false` при Win32 в src |
| **Blast radius** | **A33** · soft `blast-radius-gate` | Потрогал half монорепо ради одной кнопки |
| **Contract Surface** | **A35** · `port-surface-gate` · `composition-root-gate` · `port-test-double-gate` | Concrete в UC · «framework DI = без порта» · mock concrete вместо Fake |
| **Rich domain / Anti-anemic** | **A05** · **B06** · `anemic-mutation-gate` | `user.status = 'active'` снаружи сущности · публичный сеттер без инварианта |
| **Expected vs unexpected errors** | **A10** | try/catch-лес в UC · глотать DB-down как Ok |
| **Law→Gate** | **AGENT-5** | MUST без реального step checker'а |
| **Agent failure modes** | шапка Doctrine | Типичный самообман ИИ → какой rule FAIL |
| **Evidence honesty** | **A26** | Evidence: taxonomy · **contract_surface** · **rich_domain** · **error_split** · **behavior_ssot** · AC · blast |

**Deprecated reading (не применять):** «зелёный prime_check = 10/10» · «имя AC = lock» · «порт в yaml = архитектура» · «ignore e2e если имя есть» · «exclude composition, 100% fakes» · «unsafe ок до CRITICAL» · «скопировал, чтобы не трогать shared» · «разрезал файл = DRY» · «InputRouter обязателен в каждом приложении».

---

## v5.7 — что НОВОЕ (в v3 этого нет)

| Добавление | Правило / модуль | Что делает |
|------------|------------------|------------|
| **Agent phases** | AGENT-OMEGA 0→4 | LOCK → design → TDD → implement → verify — обязательный порядок |
| **Design artifact** | OMEGA PHASE 1 | `capability_slices` · `acceptance_criteria` · `blast_radius` · `test_taxonomy_map` · `contract_surface_map` · `behavior_owners` до кода |
| **Task router** | AGENT-1 | Тип задачи → какие правила |
| **Merge gate spec** | A22 · AGENT-5 | `prime_check` — единственный способ сказать «готово» на PRIME+ |
| **Agent owns checker 100%** | AGENT-5 · A22 | Нет checker? Агент FULL: scaffold, steps, yaml, CI, deps, run, fix until green — **не просит пользователя** |
| **Law→Gate** | AGENT-5 | Каждый `Enforced by:` MUST → реальный step в той же сессии |
| **AST Prosecutor** | AGENT-5 | Агент пишет скрипты checker; 7 AST gates + cohesion — **не shipped, не CI-only** |
| **Package cohesion** | **A05a** | Capability slices / feature packages; mirrored или vertical Skin |
| **Test taxonomy** | **A12a** | Нормативные families: unit · integration · contract/E2E · regression · mutation · property · injection · access control · scenario · acceptance · boundary · FSM · negative · observability |
| **Blast radius** | **A33** | Объявить + держать минимум файлов/capabilities на фичу |
| **Intent lock** | **A34** | Каждый AC несёт **оракул**; тело теста обязано сломаться, если поведение соврало |
| **Contract Surface** | **A35** | Outbound/inbound ports · DTO/ACL · SPI · API/event · Fake vs port · composition root |
| **Live Surface** | **A36** | Объявленный порт/поле constructed и called; identity impl FAIL |
| **Honest errors / no swallow** | **A37** | Result на границе mapped; dump-bucket FAIL; err-variant провоцирует producer |
| **Checker integrity** | **A38** | AST `prime_check`: нет безусловного GREEN, нет existence-only, нет substring-lock |
| **Behavior SSOT / Anti-Clone** | **A39** | Один owner на политику/алгоритм; N≥2 копии → FAIL; форма = Skin (`fn`/facade/method/dispatcher) |
| **Rich domain / Anti-anemic** | **A05** · **B06** | Lifecycle/status через методы сущности; `anemic-mutation-gate`; учебник Clean-дерева — **sample в каталоге**, не обязательный Skin |
| **Expected vs unexpected errors** | **A10** | Named business Err в core; infra-сбой → adapter + global handler в presentation |
| **Fix until green** | FIX-UNTIL-GREEN · A30 | Red gate → fix → re-run — агент не бросает |
| **TDD lock** | A24 | Failing test **до** production code по family + AC |
| **Evidence block** | A26 | `PRIME-VERIFY-EVIDENCE` с taxonomy/AC/blast — «готово» без него = invalid |
| **100% coverage law** | A25 | 100.00% line **и** branch; 99.99% = fail; **не заменяет** taxonomy |
| **ZTA matrix** | A02 · A29 | Каждый protected route × anon / expired / forbidden / valid |
| **Err matrix** | A10 · A12 | Каждый `Err` → обязательный `test_err_*` |
| **Route matrix** | A03 · A12 | method × path × HTTP status в contract tests |
| **FSM matrix** | B06 | Каждое ребро + illegal jumps |
| **Test quality gates** | A27 | Нет empty tests · нет `assert True` · flaky = ×3 |
| **Mutation testing** | A28 | CRITICAL: ≥95% kill rate на `critical_scope` |
| **Legacy adoption** | A31 | Старый репо: 100% на **changed files** + ratchet |
| **Monorepo tiers** | A32 | PRIME / LITE per path |
| **Anti-slack** | A30 | Нет «тесты в следующем PR» · нет кода на red base |
| **RFC 2119** | все правила | MUST / MUST NOT — не «should» |
| **Structured report** | AGENT-5 reporter | EXEC SUMMARY · FIX PLAN · COVERAGE MAP на red |
| **Stack adapters** | AGENT-5 | python · node · rust · go · kotlin · swift |
| **Forbidden phrases** | AGENT-0 | «~99%» · «запустите сами» = нарушение |
| **Idempotent-Ledger gate** | A14 · A12 | `idempotency-matrix-gate` — double-submit на state-changing UC |
| **Bounded-Context gate** | A04 · B05 | `context-leak-gate` — AST блокирует кросс-импорт domain entity |
| **Error Context gate** | A10 · B03 | `error-context-gate` — каждый `Err` = rule_id + snapshot + trace_id |
| **Quality Constellation** | Quality Constellation · A16 · A18 | ISO 25010 · ISO 5055 CISQ · OWASP Top 10/ASVS · CERT/MISRA When safety-critical |

---

## Quality Constellation — международные стандарты (не для галочки)

PRIME — не изолированный чеклист. v5.7 **операционализирует** глобальные стандарты качества и безопасного кодинга в правила + machine gates:

| Стандарт | Роль | Реализация в PRIME |
|----------|------|-------------------|
| **ISO/IEC 25010** | 9 измеряемых характеристик качества (надёжность, security, сопровождаемость…) | Каждая → правила Part A/B + gates (полная таблица в спеке) |
| **ISO/IEC 5055** (CISQ) | Автопоиск **структурных** дефектов в исходниках | **AST Prosecutor** + static steps — 4 столпа CISQ с тегами на steps |
| **OWASP Top 10 · ASVS** | Риски веб-приложений + глубина верификации | **A02** · **A16** · **A18** · `zta-matrix-gate` · `injection-fuzz` · ASVS по tier |
| **SEI CERT** | Безопасный системный код (C/C++/Java) | Запрещённые конструкции · concurrency · memory safety **When** native/unsafe |
| **MISRA C/C++** | Safety-critical предсказуемость | **CRITICAL** / embedded — `safety_profile` в config · `clang-tidy`/`cppcheck`/`clippy` |

**100% line+branch** = ISO 25010 **Reliability** + **Maintainability** — но v5.7 ещё требует **taxonomy families** для Functional suitability / Security.  
**AST Prosecutor** = локальный анализ класса **ISO 5055** — пишет агент, не внешний SaaS.  
**ZTA matrix** = закрывает OWASP **A01** + **A07** на каждую protected operation.

---

## Empire Engine outcomes (всегда — по tier)

Не «где надо». **Skin** = как в репо; **Engine** = всегда для назначенного tier. Pattern Catalog в v5.7.

| Outcome | When | Где в v5.7 | Gate |
|---------|------|------------|------|
| **Explicit errors** | PRIME+ core | **A10** — Result / Go error / typed exception; нет silent null | `anti-null-gate` · `err-variant-gate` |
| **Immutability** | гонки / FSM / shared aggregate | **A05** · **B06** | `immutability-gate` |
| **Injectable nondeterminism** | PRIME+ testable core | **A06** · **A15** — ports, traits, test doubles | `deterministic-runtime` |
| **Idempotent mutations** | мутация + retry risk | **A14** · **A09** · **A12** — key + dedup (ledger опционален) | `idempotency-matrix-gate` |
| **Module isolation** | multi-module / services | **A04** · **B05** — DTO/events; shared kernel = ADR | `context-leak-gate` |
| **Package cohesion** | ≥2 capabilities / растущий domain | **A05a** — mirrored slices или feature packages | `package-cohesion-gate` |
| **Test taxonomy** | STANDARD+; full matrix PRIME+ | **A12a** — applicable families или валидный N/A | `test-taxonomy-gate` · matrix gates |
| **Intent lock** | PRIME+ features | **A34** — AC + oracle ↔ тело теста | `intent-lock-gate` |
| **Live surface** | PRIME+ · When ports/DTO | **A36** — объявленное должно вызываться | `live-surface-gate` |
| **No swallow** | PRIME+ | **A37** — mapped Result; provoke err path | `no-swallow-gate` · `err-variant-gate` |
| **Checker integrity** | PRIME+ | **A38** — checker не театр | `checker-integrity-gate` |
| **Behavior SSOT** | PRIME+ · When N≥2 один алгоритм | **A39** — один owner; callers делегируют | `behavior-ssot-gate` · `anti-fork-gate` |
| **Blast radius** | STANDARD+ | **A33** — минимум capabilities/files | soft `blast-radius-gate` + DoD |
| **Contract surface** | PRIME+ · When I/O / boundary | **A35** — порты · DTO · API/event · composition root | `port-surface-gate` · `composition-root-gate` · `port-test-double-gate` |
| **Rich domain** | When entity has status/lifecycle | **A05** · **B06** — мутация через методы сущности, не public assign | `anemic-mutation-gate` · `fsm-transition-gate` |
| **Expected vs unexpected errors** | PRIME+ | **A10** — named Err в core; infra → global handler | `err-variant-gate` · `no-transport-in-domain` |
| **Observable failures** | PRIME+ | **A10** · **B03** · family observability в **A12a** | `error-context-gate` |

---

## v5.7 — что УЛУЧШЕНО (было в v3 → стало жёстче + gates)

### Архитектура и паттерны

| v3.0 | Улучшение в v5.7 | Правила · gates |
|------|------------------|-----------------|
| «4 слоя» текстом | **Separation roles** + import graph + **capability packaging** + **rich domain** | **A05** · **A05a** · `import-graph-gate` · `package-cohesion-gate` · `anemic-mutation-gate` |
| DI описан | **Явные Ports** даже при 1 impl; framework DI вяжет Port→Adapter; Fake vs port | **A06** · **A35** · `port-surface-gate` · `di-purity` · `composition-root-gate` |
| Coding to interfaces (v3) | Полная taxonomy **Contract Surface** | **A35** · Pattern Catalog |
| Default tier | **STANDARD** для app; **PRIME** по триггерам | **A01** |
| Только Python verify | **Quality gate contract** + Law→Gate | **A22** · **AGENT-5** |
| Design-first намёком | Design artifact + **contract_surface_map** | **A07** · AGENT-OMEGA PHASE 1 |
| Анти-дубли словами | Нет `*_v2` policy forks **и** structural clones алгоритма | **A08** · **A39** · `anti-fork-gate` · `behavior-ssot-gate` |
| Один владелец политики | Policy facades — SSOT; Behavior SSOT на любой shared algorithm | **A09** · **A39** |
| Typed errors | Explicit failure paths; **expected vs unexpected**; каждый Err в тестах + error context | **A10** · `anti-null-gate` · `err-variant-gate` · `error-context-gate` |
| «Режь если трудно тестить» | Лимиты >300 / complexity >10; **extract owner, затем shrink** — clone-split = FAIL | **A11** · **A05a** · **A39** · `file-size-guard` · `cyclomatic-gate` · `behavior-ssot-gate` |
| CQRS «когда надо» | Формальное правило CQRS | **B01** |
| FSM «без прыжков» | Каждое ребро в тестах; transition = **метод сущности** + **новый** immutable state When in-memory | **B06** · **A05** · `fsm-transition-gate` · `anemic-mutation-gate` · `immutability-gate` |
| Idempotency «ключ на retry» | **Idempotent-Ledger:** key + WAL/ledger; `test_double_submit_*` | **A14** · **A09** · `idempotency-matrix-gate` |
| Границы модулей словами | **Bounded-Context Lock:** нет shared domain entities — только DTO/primitives/events | **A04** · **A05** · **B05** · `context-leak-gate` |
| Minimal scope словами | **Blast radius** объявлен; **MUST NOT** copy-paste, чтобы не трогать owner | **A33** · **A39** · `blast-radius-gate` · `behavior-ssot-gate` |
| «Interface только если 2+ impl» | **I/O → порт всегда** на PRIME+; YAGNI только для pure functions | **A35** · **A04** · **A06** |

### Безопасность и международные стандарты

| v3.0 | Улучшение в v5.7 | Правила · gates |
|------|------------------|-----------------|
| 5 пунктов §7 | Secure-by-design + **таблица OWASP Top 10** + ASVS по tier | **A16** · **A18** · Quality Constellation |
| Нет ISO mapping | **ISO 25010** — 9 характеристик → rules/gates | Quality Constellation |
| Нет стандарта структурных дефектов | **ISO 5055 CISQ** → столпы AST Prosecutor | AGENT-5 · 7 AST gates · `package-cohesion-gate` |
| Нет safety-critical профиля | **CERT/MISRA** When C/C++/embedded/CRITICAL | `safety_profile` · `cert-forbidden-gate` |
| «Без секретов» | Working tree + **вся git history** | **A19** · `gitleaks-history` · `no-secrets` |
| «Обновляй deps» | Zero high/critical CVE; SBOM | **A19** · `dependency-audit` · `sbom` |
| Валидация на границе | + injection fuzz · SSRF allowlist | **A18** · `injection-fuzz` · `ssrf-gate` |
| Debug в prod (намёк) | Явный бан `SKIP_AUTH`, `if True:` bypass | **A16** · `no-debug-bypass` |
| Нет PII в логах | Regex scan log strings | **A16** · `pii-log-scan` |
| Auth на эндпоинтах | Zero Trust: localhost = internet; deny-by-default | **A02** · `zta-matrix-gate` |
| Docker легко | non-root · no public DB · TLS ≥1.2 · prod env | **A23** · `docker-security` · `compose-security` · `prod-config` · `tls-min-version` |

### Тесты и качество

| v3.0 | Улучшение в v5.7 | Правила · gates |
|------|------------------|-----------------|
| Pyramid описана | Pyramid **плюс** нормативные **taxonomy families** | **A12** · **A12a** · `test-taxonomy-gate` |
| «Ключевые поведения» | `test_matrix` + `test_taxonomy_map` + Anti-N/A | **A12** · **A12a** · `test-matrix-gate` |
| Acceptance словами | Каждый AC ↔ **оракул в теле теста** | **A34** · `intent-lock-gate` |
| E2E можно | E2E без unit base = fail; API-only = contract@boundary | **A12** · **A12a** · `e2e-only-anti-pattern` |
| Coverage выбирает агент | 100.00% line+branch **и** taxonomy green | **A25** · **A12a** · `coverage-*` |
| Bug → test (норма) | Обязательный `test_regression_*` | **A12** · `regression-lock` |
| Property/fuzz опционально | hypothesis / proptest на границах | **B12** · `pytest-property` |
| Mutation на financial/critical | **PRIME greenfield MUST** на `critical_scope`; CRITICAL ≥95% | **A28** · `mutation-critical` |

### Data · contracts · ops

| v3.0 | Улучшение в v5.7 | Правила · gates |
|------|------------------|-----------------|
| Migrations намёком | DDL только в `migrations/`; schema ≡ DB | **A20** · `migration-path-only` · `schema-drift` |
| OpenAPI «используй schema» | OpenAPI/proto ≡ runtime; golden snapshots | **A21** · `api-contract-drift` · `snapshot-contract` |
| SemVer упомянут | Правила breaking + contract tests | **A21** |
| SRE / events прозой | Domain events в infra; error budget | **B03** · **B04** |
| Health «should» | `/health` + `/ready` tested | **B13** · `health-gate` |
| Client UI принципы | lint + types + unit gate для frontend | **B11** · `frontend-quality` |
| Self-review checklist | B08 grep + **machine** pre-commit AGENT-2 | **B08** · **AGENT-2** |
| DoD размыт | A13: thin handler · DI · Result · taxonomy · AC · blast · threat model | **A13** |
| Human handoff нет | B14: evidence = handoff artifact | **B14** |

---

## Карта правил v5.7 (полный индекс)

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
                                                      A39 Behavior SSOT

PART B — B01 CQRS              B06 FSM                 B11 Client apps
        B02 SOLID/GRASP        B07 YAGNI               B12 Fuzz/property
        B03 SRE/observability  B08 Agent self-review   B13 Ops/runbook
        B04 Resilience         B09 ADR                 B14 Human handoff
        B05 Inter-service      B10 Performance

Outcomes: Behavior lock · Live surface · No swallow · Checker integrity · Behavior SSOT · Explicit errors · Rich domain When · Test taxonomy (oracle APPLIED) · Contract surface · Coverage honesty · FFI When
```

---

## Checker = работа агента (не твоя)

На tier ≥ PRIME **агент** владеет quality gate end-to-end:

```text
MISSING?  → агент scaffold scripts/prime_check/ + все applicable step-модули
CONFIG?   → агент пишет prime_check.config.yaml (tier, scopes, capabilities, ports, composition_root)
CI?       → агент добавляет workflow — та же команда, что локально
DEPS?     → агент ставит pytest/ruff/eslint/… для gates
LAW→GATE? → каждый Enforced-by MUST = реальный step — без stubs
RUN?      → агент в shell — никогда «запустите сами»
RED?      → агент чинит код И/ИЛИ checker → re-run → exit 0
DONE?     → агент печатает PRIME-VERIFY-EVIDENCE (taxonomy + contract_surface + AC + blast)
```

**Ты** не ставишь, не настраиваешь и не запускаешь checker. **Агент делает.**

## Как v5.7 проверяет

```text
PHASE 0  агент bootstrap FULL checker если нет (STOP фичу до green)
PHASE 1  design artifact: slices · AC · blast · test_taxonomy_map · contract_surface_map
PHASE 2  сначала failing tests (TDD-LOCK) по family + AC — против Fake ports
PHASE 3  implement внутри blast_radius — ports before adapters
PHASE 4  --only → --diff → full → evidence · fix-until-green
```

~50+ шагов: static · **AST Prosecutor (7 gates + cohesion + port-surface)** · security · pyramid · **taxonomy / intent-lock / contract surface** · matrices · coverage · data/ops · evidence.

**AST Prosecutor ≠ CI-обёртка.** Checker сам парсит AST и import graph — слова агента не считаются, только `exit 0`.

**FULL-COLLECTION:** default прогон гоняет **все** steps, собирает **все** FAIL — один отчёт, не игра в молоток.

**При RED:** EXEC SUMMARY → FIX PLAN (P1→P3) → карточки Finding. Агент **чинит весь P1 batch за раз** → один rerun — не цикл «один фикс → полный прогон».

---

## Лицензия

| Использование | v3.0 | v5.7 |
|---------------|------|------|
| **Читать / форкать / учить** | MIT · открыт | **Открыт** — полная спека в репо |
| **Лично / хобби / pet** | MIT · free | **Бесплатно** |
| **Компания / команда / клиентский прод** | MIT (только v3) | **$50 / сотрудник · разово** → [@ExcitedSkam](https://t.me/ExcitedSkam) |

Открыт ≠ бесплатно для корпораций. Спека публична; коммерческий деплой на корп. железе — только с clearance.

---

## Cursor — как подключать (не засорять глобальные rules)

**Не надо** пихать всю v5.7 в `.cursor/rules` или User Rules. Спека в always-on контексте жрёт токены, конфликтует с правилами проекта, и агент всё равно не «запомнит» спеку — ему нужен файл **когда задача этого требует**.

**Надо** положить спеку **локально в workspace** и **подгружать по запросу**.

### 1. Положи файл в проект

На выбор:

| Способ | Когда |
|--------|-------|
| **Скопировать** `Mawyxx Prime V5.7.md` в репо (напр. `docs/standards/`) | Проще всего — один файл, версию фиксируешь ты |
| **Submodule** этого репо в `standards/mawyxx-prime/` | Пин на коммит; обновление через `git submodule update` |
| **Клон** рядом с проектом + оба каталога в одном workspace Cursor | Спека вне app-репо — ок для личного use |

Агент должен **читать путь** — `@`-упоминание или `Read`. Облачная ссылка без файла в workspace не считается.

### 2. Короткий boot rule — и только он

Один маленький rule в `.cursor/rules/mawyxx-boot.mdc` (или одна строка в `AGENTS.md`). **Boot, не учебник:**

```markdown
---
description: MAWYXX PRIME boot — короткий; полная спека по задаче
alwaysApply: true
---

Project Skin + Empire Engine. Tier по риску (см. спеку §Tier).
Полные правила: читай `docs/standards/Mawyxx Prime V5.7.md` при старте работы, смене архитектуры или перед merge — не угадывай.
Нет checker? Агент FULL по AGENT-5 (steps, config, CI) — сам гоняет и чинит. Не проси пользователя запускать тесты.
При RED: отчёт FULL-COLLECTION → batch-fix P1 → rerun.
Anti-N/A · taxonomy · intent lock · blast radius · **contract surface (ports)** — coverage alone ≠ done.
```

Путь поправь под то, куда положил файл.

### 3. Подгрузка по задаче — ты или агент

| Кто | Как |
|-----|-----|
| **Ты** | `@Mawyxx Prime V5.7.md` (или твой путь) в начале задачи: «сделай X по PRIME», «bootstrap checker», «почини RED» |
| **Агент** | Boot rule велит читать спеку → открывает сам; для узкой задачи — только нужные **AGENT-*** / **A*** / **B*** секции |
| **Никто** | Кодинг по v3.0 без tier — boot rule не обязателен |

**Норм:** boot rule + локальный файл + `@` когда ставки высокие.  
**Плохо:** вся v5.7 в User Rules; дублировать A01–A39 в десять `.mdc`; надеяться, что агент помнит прошлый чат вместо перечитывания AGENT-5.

### 4. Команды checker (после того как агент поднимет `scripts/prime_check/`)

```bash
python -m scripts.prime_check --diff
python -m scripts.prime_check --evidence
python -m scripts.prime_check
```

Пользователь их не запускает — агент. Здесь для понимания, что значит «green».

---

*MAWYXX PRIME · [@ExcitedSkam](https://t.me/ExcitedSkam)*
