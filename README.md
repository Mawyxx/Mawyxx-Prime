# MAWYXX PRIME

> **Build for Billions. Code for Vibe. Rule with Logic.**

Универсальный **enterprise-стандарт качества кода для ИИ-агентов** (Cursor, Copilot, Claude и др.). Любой стек, любой домен, любой размер проекта.

**English summary below** ↓

---

## Лицензия

| Версия | Лицензия |
|--------|----------|
| **v3.0** | [MIT](https://opensource.org/license/MIT) — бесплатно **всем**, хоть в компании хоть где |
| **v5.2** | [PolyForm Noncommercial 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0) — бесплатно **для себя** (pet-проекты, хобби, личное обучение) |

**v5.2 в компании — строго запрещено.** Корпоративный стандарт, CI, рабочие репозитории, проекты для клиентов, внедрение в команду — всё это **коммерческое использование** без лицензии.

Используете v5.2 в бизнесе без разрешения — это **нарушение авторских прав** и условий [PolyForm Noncommercial](https://polyformproject.org/licenses/noncommercial/1.0.0). Последствия: **претензия, требование прекратить использование, взыскание убытков и штрафов**, блокировка распространения, уведомление работодателя/заказчика. Лицензия автоматически прекращается при нарушении.

**Легально для компании** — только после письменного согласования. Пишите в Telegram: **[@ExcitedSkam](https://t.me/ExcitedSkam)**.

---

## Файлы в репозитории

| Файл | Назначение |
|------|------------|
| [`Mawyxx Prime V3.0.md`](Mawyxx%20Prime%20V3.0.md) | Краткий универсальный стандарт (~220 строк). Quick reference, onboarding. |
| [`Mawyxx Prime V5.2.md`](Mawyxx%20Prime%20V5.2.md) | Полный боевой стандарт (~1050 строк). PolyForm NC — бесплатно себе; компаниям → [@ExcitedSkam](https://t.me/ExcitedSkam). |

**Рекомендация:** v3 — всем бесплатно; **v5.2** — дома бесплатно, в компании — напиши в TG.

---

## MAWYXX PRIME v3.0 — что внутри

Краткий универсальный стандарт. Основа для любого проекта.

- **Risk Tiers** — LITE → STANDARD → PRIME → CRITICAL; жёсткость по риску, не по размеру файла
- **AI Protocol** — context-first, минимальный scope, self-review
- **Анти-паттерны** — когда стандарт *не* применять (no over-engineering)
- **Clean Architecture** — Domain / Application / Infrastructure / Presentation
- **DI & IoC** — зависимости снаружи, coding to interfaces
- **SOLID** — S.O.L.I.D. + small units (10–15 строк на UC)
- **Result / typed errors** — пропорционально tier
- **FSM** — явные графы переходов для сущностей со статусом
- **Domain Events** — core публикует, adapters подписываются
- **Idempotency** — для опасных мутаций
- **Production** — observability, resilience, SRE (SLI/SLO, Error Budget, Self-Healing)
- **Security baseline** — secrets, PII, least privilege, CVE
- **Тестируемость** — DI, чистый core, fakes, пирамида тестов
- **Frontend / mobile / desktop** — логика не в UI-компонентах
- **ADR** — архитектурные решения в `docs/adr/`
- **YAGNI** — не строить Звезду Смерти для скрипта на 30 строк

---

## Уникальное в v5.2 (поверх v3.0)

v5.2 = всё из v3 + **операционный enforcement** для ИИ. Краткий список улучшений:

### Операционка для ИИ-агента
- **RFC 2119** — MUST / MUST NOT / SHOULD / MAY на каждом правиле
- **Stable Rule IDs** — `PRIME-A01`…`A23`, `B01`…`B11` — цитируемые в ошибках и ревью
- **AGENT-0 Boot** — stop-the-line: не писать поверх сломанного фундамента
- **Task Router** — таблица «задача → какие правила → что запустить»
- **Pre-commit checklist** — merge gate перед «готово»
- **Агент сам запускает verify** — не просит пользователя «запусти тесты»

### Prime Check — главное отличие v5.2
- **`prime_check`** — единый merge-blocking скрипт; ИИ **пишет его сам**, если нет в репо
- **~25 автоматических шагов** — тесты, coverage, security, architecture, Docker, ZTA
- **ZERO-TOLERANCE** — нет «норм сойдёт» на tier ≥ PRIME
- **100% line + 100% branch** на `runtime_scope` — ни одной непокрытой строки
- **CI = local** — одна команда: `python -m scripts.prime_check`

### Безопасность (усилено)
- **Zero Trust (ZTA)** — localhost / docker / internal ≠ доверенная сеть
- **`zta-auth-gate`** — каждый endpoint: обязательные 401/403 contract-тесты
- **`gitleaks` + `no-secrets`** — zero secrets в repo, логах, тестах
- **`dependency-audit`** — zero high/critical CVE в lockfile
- **`bandit` / npm-audit** — static security lint
- **`no-debug-bypass`** — scan на `if True:`, `# TODO remove` credentials
- **OWASP mapping** — injection, XSS, SSRF, misconfiguration
- **Threat Model mini** — для CRITICAL / security touch
- **PRIME-A23** — Docker/compose security (non-root, no privileged, no public DB)

### Тестирование (усилено)
- **Пирамида** — unit → integration → contract → property
- **`result-coverage-gate`** — каждый `Err` код UC = unit-тест
- **`contract-scenario-gate`** — каждый HTTP status на route = тест
- **E2E-only anti-pattern** — запрещён
- **Concurrency tests** — FSM race, double-submit
- **`mutation-check`** — для CRITICAL tier
- **Регрессия** — каждый баг = тест в том же PR

### Архитектура и качество кода (усилено)
- **Design-first order** — контракт → domain → UC → migration → infra → API → tests
- **Anti-fork** — не плодить `*_v2`, один SSOT на политику
- **Policy facades** — auth/idempotency только через canonical facade
- **Plugin boundaries** — новый провайдер через interface, без правок Core
- **GRASP** — Information Expert, Controller, Pure Fabrication
- **Лимиты сложности** — файл 200/300, функция 40, cyclomatic >10
- **Good/Bad examples** — эталонные паттерны кода
- **Handler pattern** — inject UC → execute → map Result (Python + TS)
- **Architecture gates** — import-boundaries, deterministic-runtime, di-purity, no-string-sql

### Production & data (усилено)
- **SemVer table** — MINOR/MAJOR по типу изменения контракта
- **Migration gates** — DDL только в versioned migrations
- **`schema-drift`** — БД ≡ migrations
- **`api-contract-drift`** — OpenAPI/proto ≡ код
- **SRE block** — SLI, SLO, Error Budget, Self-Healing, domain events
- **Graceful degradation** — таблица поведения при partial failure

### Client apps
- **B11 Client apps** — web + mobile + desktop; server/UI/business state разделены

---

## Какую версию использовать

| Сценарий | Версия |
|----------|--------|
| Быстро понять философию | **v3.0** |
| Cursor Rule (личный pet-проект) | **v5.2** (бесплатно) |
| Enterprise-проект с CI | **v5.2** + TG [@ExcitedSkam](https://t.me/ExcitedSkam) |
| Компания без лицензии на v5.2 | **v3.0** (MIT, бесплатно) |
| Одноразовый скрипт | v3.0 tier **LITE** |

---

## Быстрый старт (v5.2)

1. Положи [`Mawyxx Prime V5.2.md`](Mawyxx%20Prime%20V5.2.md) в Cursor Rules или `.cursor/rules/`
2. ИИ определяет Risk Tier (реальный проект = минимум **PRIME**)
3. Если нет `scripts/prime_check` — ИИ **сначала пишет checker**, потом фичу
4. Перед merge: `python -m scripts.prime_check` → **exit 0**

---

---

# English

## License

| Version | License |
|---------|---------|
| **v3.0** | [MIT](https://opensource.org/license/MIT) — free for everyone |
| **v5.2** | [PolyForm Noncommercial 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0) — free for personal / hobby use |

**v5.2 at work — strictly prohibited.** Corporate standard, CI, work repos, client projects, team rollout = **unlicensed commercial use**.

Using v5.2 in business without authorization is **copyright infringement** under [PolyForm Noncommercial](https://polyformproject.org/licenses/noncommercial/1.0.0). Consequences: **cease-and-desist, damages, penalties**, distribution takedown, license termination.

**Legal business use** — contact **[@ExcitedSkam](https://t.me/ExcitedSkam)** on Telegram first.

---

## Repository files

| File | Purpose |
|------|---------|
| [`Mawyxx Prime V3.0.md`](Mawyxx%20Prime%20V3.0.md) | Concise universal standard (~220 lines). Quick reference. |
| [`Mawyxx Prime V5.2.md`](Mawyxx%20Prime%20V5.2.md) | Full operational standard. Personal use free; companies → [@ExcitedSkam](https://t.me/ExcitedSkam). |

**Recommendation:** v3 free for all; v5.2 free at home, companies → TG.

---

## MAWYXX PRIME v3.0 — core

- **Risk Tiers** — proportional rigor (LITE → CRITICAL)
- **AI Protocol** — context-first, minimal scope, anti-overengineering
- **Clean Architecture** — 4 layers, no business logic in handlers/UI
- **DI, SOLID, Result pattern, FSM, Domain Events, Idempotency**
- **Production** — observability, resilience, SRE, ADR
- **Security baseline** — secrets, PII, least privilege
- **Testability** — clean core, fakes, test pyramid
- **Universal** — any stack, any domain

---

## Unique in v5.2 (on top of v3)

### AI operations
- RFC 2119 normative language + stable rule IDs (`PRIME-A01`…`A23`)
- Stop-the-line, task router, pre-commit checklist
- Agent runs all verification — never delegates to user

### Prime Check (main v5.2 feature)
- AI **writes `prime_check`** if missing — then writes features
- Single merge gate: tests + security + architecture + Docker + ZTA
- **100% line + branch coverage** — zero untested lines in `runtime_scope`
- **ZERO-TOLERANCE** — no «good enough» on tier ≥ PRIME

### Security (enhanced)
- Zero Trust — localhost/docker not trusted
- Mandatory 401/403 contract tests per route
- gitleaks, CVE audit, bandit, no-debug-bypass scan
- OWASP mapping + Threat Model mini
- Docker/compose security (A23)

### Testing (enhanced)
- Full pyramid + property tests + mutation testing (CRITICAL)
- Every `Err` variant tested; every HTTP status tested
- Concurrency / FSM race tests; regression per bug

### Architecture (enhanced)
- Design-first order, anti-fork, policy facades, plugin boundaries
- GRASP, file/function limits, architecture static gates
- Handler patterns with code examples

### Production (enhanced)
- SemVer table, migration/schema/API drift gates
- SRE: SLI, SLO, Error Budget, Self-Healing
- Graceful degradation matrix

---

## Quick start (v5.2)

1. Add [`Mawyxx Prime V5.2.md`](Mawyxx%20Prime%20V5.2.md) to Cursor Rules
2. AI sets Risk Tier (real project = **PRIME** minimum)
3. AI bootstraps `scripts/prime_check` if absent
4. Merge only when `python -m scripts.prime_check` exits **0**

---

*MAWYXX PRIME — predictable, measurable, testable, resilient.*
