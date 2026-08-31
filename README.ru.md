# MAWYXX PRIME — стандарт AI-кодинга

*Build for Billions. Code for Vibe. Rule with Logic.*

[English version → README.md](README.md)

**v3.0** = паттерны (MIT). **v5.7** = именованные законы + Law→Gate + правда исхода. Spec Skin + Spec Engine: один Law Template, один SSOT на OWASP/Anti-N/A, [Conflict Matrix](Mawyxx%20Prime%20V5.7.md#conflict-matrix-при-сомнении--читать-это-не-конкурирующие-абзацы) для «при сомнении», **Default-secure 5Q** до кода (CRUD с id/PATCH → Trust Pipeline в том же PR).

**Project Skin · Empire Engine:** пиши в стиле проекта — с дисциплиной Empire. Зелёный `prime_check` из имён AC, мёртвых портов, ignored e2e или exclude composition — **не** done.

**v5.7 открыт в репо** для чтения/форка/личного использования. **Корп / команда / клиентский прод** → разовая лицензия ($50/сотрудник) → [@ExcitedSkam](https://t.me/ExcitedSkam).

---

## Файлы

| Файл | Содержание | Доступ |
|------|------------|--------|
| `Mawyxx Prime V3.0.md` | Паттерны · ~220 строк | **MIT** |
| `Mawyxx Prime V5.7.md` | AGENT-0…5 · **A01–A41** · **B01–B14** | **Открыт в репо** · корп = платно |
| `Mawyxx-Security.md` | Отдельный mega-prompt для security-аудита (опционально; не часть Prime) | **Открыт в репо** |
| `scripts/prime_check/` | Агент создаёт FULL по **AGENT-5** | **Не в репо** — агент bootstrap |

Норматив — **только** в `Mawyxx Prime V5.7.md`. Этот README = карта, не второй SSOT.

---

## Столпы честности (A34–A41)

| Столп | Правило · gates | Убивает |
|-------|-----------------|---------|
| **Intent lock** | **A34** · `intent-lock-gate` | AC↔имя теста |
| **Contract Surface** | **A35** · port-surface · composition/Fake | Concrete в UC · мёртвые порты |
| **Live Surface** | **A36** · `live-surface-gate` | Порт в yaml без вызова |
| **No swallow** | **A37** · no-swallow · err-variant | `let _ =` на I/O · dump-bucket Err |
| **Checker integrity** | **A38** · `checker-integrity-gate` | Театр `return GREEN` |
| **Behavior SSOT** | **A39** · `behavior-ssot-gate` | Клоны алгоритма · fake-split |
| **Secure Continuum** | **A40** · ci-harden · channel-secret · headers · cors-csrf · iac | Зелёный zta + `write-all` · `.env` в чат |
| **Trust Pipeline** | **A41** · trust-pipeline · idor · mass-assign · path · session | «залогинен ⇒ любой id» · `update(**body)` |

Также: **A05a** cohesion · **A12a** taxonomy · Anti-N/A (SSOT в Doctrine) · **A25** coverage honesty · **A33** blast · rich domain (**A05**/**B06**).

---

## Карта правил

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
        A09 → alias A08        A19 Supply chain        A30 Anti-slack
        A10 Result/errors      A20 Migrations          A31 Legacy · A32 Monorepo
                                                      A33–A41 honesty + continuum + pipeline

PART B — B01 CQRS … B14 Human handoff
```

Международные карты (ISO 25010 · CISQ · OWASP ASVS · CERT/MISRA): **Quality Constellation** в V5.7. Таблица OWASP Top 10: **только A18**.

---

## Checker = работа агента

На ≥PRIME агент создаёт `scripts/prime_check/`, пишет steps, вешает CI, гоняет `--diff` → FULL, чинит до `exit 0`, печатает `PRIME-VERIFY-EVIDENCE`. Пользователь не ставит и не запускает checker.

```text
PHASE 0  bootstrap checker если нет
PHASE 1  design maps (taxonomy · contracts · behavior_owners · continuum · trust · AC · blast)
PHASE 2  TDD по applicable family + оракул AC
PHASE 3  implement внутри blast_radius — вызов owner, не клон
PHASE 4  --only → --diff → FULL → evidence
```

---

## Лицензия

| Использование | v3.0 | v5.7 |
|---------------|------|------|
| Читать / форк / учиться | MIT | Открыт в репо |
| Личное / hobby | Бесплатно | Бесплатно |
| Компания / команда / клиентский прод | MIT (v3) | **$50 / сотрудник · разово** → [@ExcitedSkam](https://t.me/ExcitedSkam) |

---

## Cursor — без загрязнения User Rules

Держи V5.7 **в workspace**; грузи по требованию. Короткий boot-rule:

```markdown
---
description: MAWYXX PRIME boot — short; full spec on demand
alwaysApply: true
---

Project Skin + Empire Engine. Читай `Mawyxx Prime V5.7.md` для архитектуры / merge.
Нет checker? Агент строит FULL по AGENT-5. Не проси пользователя гонять тесты.
На RED: fix-until-green. Anti-N/A · Conflict Matrix · Default-secure 5Q · A34–A41 — coverage ≠ done.
```

**Опционально — промпт для аудита:** [`Mawyxx-Security.md`](Mawyxx-Security.md) — отдельный standalone-файл для полного security-ревью (`@Mawyxx-Security.md` или project rule). Для Prime не обязателен; не заменяет A18/A41 в обычной разработке.

---

*MAWYXX PRIME · [@ExcitedSkam](https://t.me/ExcitedSkam)*
