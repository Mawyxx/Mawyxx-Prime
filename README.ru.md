# MAWYXX PRIME — стандарт AI-кодинга

*Build for Billions. Code for Vibe. Rule with Logic.*

[English version → README.md](README.md)

Две спеки одной философии: **v3.0** учит паттернам (MIT). **v5.2** именует каждое правило, добавляет workflow агента и требует `prime_check` для enforcement.

---

## Файлы

| Файл | Содержание |
|------|------------|
| `Mawyxx Prime V3.0.md` | 10 разделов · ~220 строк · MIT · публично |
| `Mawyxx Prime V5.2.md` | AGENT-0…5 · **A01–A32** · **B01–B14** · ~1300 строк · коммерция |
| `scripts/prime_check/` | Агент пишет по **AGENT-5** — в репо нет |

---

## v3.0 — паттерны, которые задаёт стандарт

Что v3 уже описывает (прозой, без ID правил, без machine gate):

### Архитектура и design-паттерны

| Паттерн | Что требует v3 |
|---------|----------------|
| **Clean / DDD · 4 слоя** | Domain · Application · Infrastructure · Presentation |
| **DI & IoC** | Зависимости снаружи; нет `new Repo()` внутри UC |
| **Coding to interfaces** | Порты для time, ID, DB, HTTP, random, notifications |
| **Plugin boundary** | Новый провайдер через interface — Core не трогаем |
| **CQRS** | Когда read/write разная сложность — не для trivial CRUD |
| **FSM** | Сущности со статусом — явный граф переходов |
| **Domain events** | Core публикует факты; infra доставляет |
| **Idempotency** | `idempotency_key` на опасных retry |
| **SOLID** | SRP, OCP, LSP, ISP, DIP — в §5 |
| **Fail-fast** | Валидация на границе системы |
| **Typed errors** | Доменные ошибки, не magic exceptions в глубине |

### Production-паттерны

| Паттерн | Что требует v3 |
|---------|----------------|
| **Observability** | trace_id, structured logs, метрики на критичных путях |
| **Resilience** | Circuit breaker, bulkheads, graceful degradation |
| **SRE** | SLI, SLO, error budget, self-healing |
| **ADR** | Контекст · варианты · решение · последствия в `docs/adr/` |
| **API contracts** | OpenAPI / schema; версионирование breaking changes |
| **Security hygiene** | Без секретов в коде; валидация ввода; least privilege; без PII в логах |

### Тестирование

| Паттерн | Что требует v3 |
|---------|----------------|
| **Пирамида** | Unit (fakes) → integration → contract |
| **DI в тестах** | InMemory / Fake — предсказуемость |
| **Баг → тест** | Каждый фикс = regression test |
| **Coverage** | 100% на CRITICAL; осмысленные тесты elsewhere — **агент решает** |

### Протокол агента (только v3)

- Контекст проекта до правки
- Risk Tier (LITE / STANDARD / PRIME / CRITICAL)
- Минимальный scope на фичу
- **Self-review чеклист** (§10) перед «готово» — на честности, без `exit 0`

---

## v5.2 — что НОВОЕ (в v3 этого нет)

| Добавление | Правило / модуль | Зачем |
|------------|------------------|-------|
| **Фазы агента** | AGENT-OMEGA 0→4 | LOCK → design → TDD → code → verify — строгий порядок |
| **Task router** | AGENT-1 | Тип задачи → какие правила применять |
| **Merge gate** | A22 · AGENT-5 | `prime_check` — единственное «готово» на PRIME+ |
| **Агент пишет checker** | AGENT-5 | Нет `scripts/prime_check/` → PHASE 0 · ~50 шагов |
| **Fix until green** | FIX-UNTIL-GREEN · A30 | Red → чини → re-run — агент не бросает |
| **TDD lock** | A24 | Failing test **до** prod-кода, тот же PR |
| **Evidence block** | A26 | `PRIME-VERIFY-EVIDENCE` — без него ответ невалиден |
| **Закон coverage** | A25 | 100.00% line **и** branch; 99.99% = fail; ratchet vs `main` |
| **ZTA matrix** | A02 · A29 | Каждый route × anon / expired / forbidden / valid |
| **Err matrix** | A10 · A12 | Каждый `Err` → обязательный `test_err_*` |
| **Route matrix** | A03 · A12 | method × path × HTTP status в contract-тестах |
| **FSM matrix** | B06 | Каждое ребро перехода + illegal jumps |
| **Качество тестов** | A27 | Нет пустых · нет `assert True` · flaky = ×3 прогона |
| **Mutation** | A28 | CRITICAL: ≥95% kill rate на `critical_scope` |
| **Legacy adoption** | A31 | Старый репо: 100% на **diff** + ratchet |
| **Monorepo tiers** | A32 | PRIME / LITE по пути в одном репо |
| **Anti-slack** | A30 | Нет «тесты в след. PR» · нет кода на red base |
| **RFC 2119** | все правила | MUST / MUST NOT — не «should» |
| **Structured report** | AGENT-5 reporter | EXEC SUMMARY · FIX PLAN · COVERAGE MAP |
| **Stack adapters** | AGENT-5 | python · node · rust · go · kotlin · swift |
| **Forbidden phrases** | AGENT-0 | «~99%» · «запустите сами» = нарушение |

---

## v5.2 — что УЛУЧШЕНО (было в v3 → стало жёстче + gates)

### Архитектура и паттерны

| v3.0 | Улучшение в v5.2 | Правила · gates |
|------|------------------|-----------------|
| «4 слоя» текстом | Таблица слоёв + import graph | **A05** · `import-boundaries` · `import-graph-gate` · `no-transport-in-domain` · `handler-purity-gate` |
| DI описан | Нет concrete в UC; wiring только в root | **A06** · `di-purity` · `di-graph-gate` |
| Design-first намёком | Design artifact: routes, Err, test_matrix | **A07** · AGENT-OMEGA PHASE 1 |
| Анти-дубли словами | Нет `*_v2` policy forks | **A08** · `anti-fork-gate` |
| Один владелец политики | Policy facades — SSOT | **A09** |
| Typed errors | Result в UC; Err в тестах | **A10** · `err-variant-gate` |
| «Режь если трудно тестить» | Лимиты: >300 строк fail, complexity >10 | **A11** · `file-size-guard` · `cyclomatic-gate` · `dead-code-gate` |
| CQRS «когда надо» | Формальное правило CQRS | **B01** |
| FSM «без прыжков» | Каждое ребро в тестах | **B06** · `fsm-transition-gate` |
| Детерминизм намёком | Ban `Date.now` / `uuid4` / random в domain | **A15** · `deterministic-runtime` |

### Безопасность

| v3.0 | Улучшение в v5.2 | Правила · gates |
|------|------------------|-----------------|
| 5 пунктов §7 | Secure-by-design + OWASP pack | **A16** · **A18** |
| «Без секретов» | Working tree + **вся git history** | **A19** · `gitleaks-history` · `no-secrets` |
| «Обновляй deps» | Zero high/critical CVE; SBOM | **A19** · `dependency-audit` · `sbom` |
| Валидация на границе | + injection fuzz · SSRF allowlist | **A18** · `injection-fuzz` · `ssrf-gate` |
| Debug в проде (намёк) | Ban `SKIP_AUTH`, `if True:` | **A16** · `no-debug-bypass` |
| PII в логах (пункт) | Regex scan строк логов | **A16** · `pii-log-scan` |
| Auth общими словами | Zero Trust: localhost = internet | **A02** · `zta-matrix-gate` |
| Docker вскользь | non-root · no public DB · TLS ≥1.2 | **A23** · `docker-security` · `compose-security` · `prod-config` |

### Тесты и качество

| v3.0 | Улучшение в v5.2 | Правила · gates |
|------|------------------|-----------------|
| Пирамида описана | unit → integration → contract → property | **A12** · `pytest-*` |
| «Ключевое поведение» | `test_matrix` в design = тесты в репо | **A12** · `test-matrix-gate` |
| E2E допустим | E2E без unit base = fail | **A12** · `e2e-only-anti-pattern` |
| Coverage на усмотрение | 100% line+branch на scope или diff | **A25** · `coverage-*` · `no-pragma-no-cover` |
| Баг → тест (норма) | Обязательный `test_regression_*` | **A12** · `regression-lock` |
| Property/fuzz опционально | hypothesis / proptest | **B12** · `pytest-property` |
| — | Mutation на critical код | **A28** · `mutation-critical` |

### Data · контракты · ops

| v3.0 | Улучшение в v5.2 | Правила · gates |
|------|------------------|-----------------|
| Миграции намёком | DDL только в `migrations/`; schema ≡ DB | **A20** · `migration-path-only` · `schema-drift` |
| OpenAPI «используй» | OpenAPI ≡ runtime; golden snapshots | **A21** · `api-contract-drift` · `snapshot-contract` |
| SemVer упомянут | Правила breaking + contract tests | **A21** |
| SRE / events текстом | Domain events в infra; error budget | **B03** · **B04** |
| Health «желательно» | `/health` + `/ready` с тестами | **B13** · `health-gate` |
| Client UI принципы | lint + types + unit для frontend | **B11** · `frontend-quality` |
| Self-review чеклист | B08 grep + machine AGENT-2 | **B08** · **AGENT-2** |
| DoD размытый | A13: handler · DI · Result · docs · threat model | **A13** |
| Handoff человеку нет | B14: evidence = артефакт передачи | **B14** |

---

## Карта правил v5.2 (полный индекс)

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
```

---

## Как v5.2 проверяет (prime_check)

Агент гоняет: `python -m scripts.prime_check` → **exit 0** + **PRIME-VERIFY-EVIDENCE**

```text
PHASE 0  bootstrap prime_check если нет
PHASE 1  design artifact (test_matrix, routes, Err)
PHASE 2  failing tests first (TDD-LOCK)
PHASE 3  реализация
PHASE 4  --only → --diff → full → evidence · fix-until-green
```

~50 шагов: static · architecture · security · pyramid · matrices · coverage · data/ops · evidence.

---

## Лицензия

| Использование | v3.0 | v5.2 |
|---------------|------|------|
| Лично / хобби | MIT · free | Бесплатно |
| Компания / прод | MIT (только v3) | $50 / сотрудник · разово → [@ExcitedSkam](https://t.me/ExcitedSkam) |

---

## Cursor

```markdown
# .cursor/rules/mawyxx-boot.mdc — короткий boot; @Mawyxx Prime V5.2.md по задаче
Реальный app = PRIME+. Нет prime_check? AGENT-5. Чини до exit 0. --diff → full → --evidence.
```

```bash
python -m scripts.prime_check --diff
python -m scripts.prime_check --evidence
python -m scripts.prime_check
```

---

*MAWYXX PRIME · [@ExcitedSkam](https://t.me/ExcitedSkam)*
