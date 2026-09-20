# MAWYXX PRIME — стандарт AI-кодинга

*Build for Billions. Code for Vibe. Rule with Logic.*

[English version → README.md](README.md)

**v3.0** = паттерны (MIT). **v6.5** = Unified Constitution: **один файл**, два слоя (RUNTIME + LAW), один SSOT на тему, без дублей, **tier-aware глубина важнее ширины**. §0 Router → §1 Work → §2 Law → §3 Gates → §4 Protocols → §5 Reference. Законы **A01–A64** + **B01–B14**, 5 ролей (Orchestrator · Analyst · Builder · Guardian · Verifier), **Why** под каждым законом, **12 GOOD/BAD паттернов (anti-anchoring)**, **Reasoning protocol**, **Adversarial self-review**, **Explain/ADR protocol**, **Feature Threat Model 10Q**, **Two-Agent Verify**, **Bug→Gate**, **P0–P3**, **Diagnostic tree**, **Testing recipes**, канонический checker map (**FOCUS 30 обязательны** → CORE 70 → **138** всего, ratchet) с **depth gates** (`reasoning` · `adversarial` · `decision-log` · `standards-map`) и **§5.7 Standards Traceability** (OWASP · CWE · ASVS · ISO 25010/5055 · CERT/MISRA), проверяется **двусторонне** (inline `standards.yaml` в §5.7.8).

**Project Skin · Empire Engine:** пиши в стиле проекта — с дисциплиной Empire. Зелёный `prime_check` из имён AC, мёртвых портов, ignored e2e или exclude composition — **не** done.

**Tier:** PRIME+ только для **multi-user/PII/payments/FSM/side-effect jobs/external mutations**; single-user auth без чужих данных → **STANDARD**. **Security:** baseline (§0.5) обязателен на **любом** tier (включая LITE); масштабируется только *глубина* — без гипер-защиты на простых скриптах.

**v6.5+ (senior pass):** senior-протоколы **по всему файлу (один файл)** — Doctrine **Ask first**, self-вопросы у ролей, **questions block** у суб-агентов, **Domain Elicitation** (§1.12), **Senior Debugging** 12 шагов (§4.12), **Architecture Decision** 7 шагов (§4.13), **Senior Thinking Checklist** (§4.14), **Cross-Service** (§4.15), **Feedback Loop** post-mortem→gate (§4.16), **Self-Sufficiency** (§4.17 — AI решает всё сам, без человека). **v6.5 (backend + дыры закрыты):** **A60 Webhooks · A61 Upload safety · A62 Load/soak · A63 Privacy/retention · A64 Notifications · A54 Budgets · A55–A59** (GraphQL/WS/Search/i18n/PCI) +11 гейтов (138) · per-language concurrency · failure modes 20→30. **Дыры:** enforcement глубины через **файлы** (`docs/reasoning/`, `docs/reviews/`, `docs/adr/`) · честные **`steps_registered/green/skipped` + `skip_reasons`** · **merge conflict rules** · **§5.7 inline (один файл)** · §3.3 слит в §0.7 · flaky N=10/20 · `critical_scope` определён · алиасы A49→A20, A51→B03, A52→B04, A53→A14. **v6.4:** A48–A53 + FOCUS 30. **v6.3:** Enough-vs-too-much · sub-agent hardening · standards mapping.

**v6.5 открыт в репо** для чтения/форка/личного использования. **Корп / команда / клиентский прод** → разовая лицензия ($50/сотрудник) → [@ExcitedSkam](https://t.me/ExcitedSkam).

---

## Файлы

| Файл | Содержание | Доступ |
|------|------------|--------|
| `Mawyxx Prime V3.0.md` | Паттерны · ~220 строк | **MIT** |
| `Mawyxx Prime V6.5.md` | **Один файл** · Unified Constitution · **§0–§5** · **A01–A64** · **B01–B14** · §5.7 standards mapping (inline) | **Открыт в репо** · корп = платно |
| `Mawyxx-Security.md` | Отдельный security-аудит mega-prompt (§1.1 Surface Matrix S01–S23 · 19 сабагентов) | **Открыт в репо** |
| `scripts/prime_check/` | Агент создаёт FOCUS→CORE→FULL по **§3.2** | **Не в репо** — агент bootstrap |

Норматив — **только** в `Mawyxx Prime V6.5.md`. Этот README = карта, не второй SSOT.

---

## Столпы честности (A34–A47)

| Столп | Правило · gates | Убивает |
|-------|-----------------|---------|
| **Intent lock** | **A34** · `intent-lock-gate` | AC↔имя теста; AC без оракула |
| **Contract Surface** | **A35** · port-surface · composition/Fake | Concrete в UC · мёртвые порты |
| **Live Surface** | **A36** · `live-surface-gate` | Порт в yaml без вызова · unread поле |
| **No swallow** | **A10** · no-swallow · err-variant | `let _ =` на I/O · dump-bucket Err |
| **Checker integrity** | **A22** · `checker-integrity-gate` | Театр `return GREEN` · existence-only |
| **Behavior SSOT** | **A39** · `behavior-ssot-gate` | Клоны алгоритма · fake-split |
| **Secure Continuum** | **A40** · ci-harden · channel-secret · headers · cors-csrf · iac | Зелёный zta + `write-all` · `.env` в чат |
| **Trust Pipeline** | **A41** · trust-pipeline · idor · mass-assign · path · session | «залогинен ⇒ любой id» · `update(**body)` |
| **Parameter Bounds** | **A42** · `param-bounds-gate` | `digest[i]` без bounds · difficulty без clamp |
| **Idempotency & Atomicity** | **A14** · idempotency-matrix · atomicity | replay → 2 side-effects · claim без release |
| **Dependency Isolation** | **A44** · `dep-isolation-gate` | hot-path зависит от cold dep |
| **Config Guard** | **A46** · `prod-guard-gate` | `if TESTING` без env-guard · fail-open |
| **Contracts & Spec Parity** | **A21** · api-contract-drift · snapshot · spec-parity | поле без version · спека ≠ код |

Также: **A05a** cohesion · **A12a** taxonomy (24 family) · Anti-N/A (Doctrine) · **A25** coverage honesty · **A33** blast · rich domain (**A05**/**B06**).

---

## Карта правил

```text
§0 IDENTITY & ROUTER   0.3 Task router · 0.4 Tier · 0.5 Default-secure 5Q · 0.6 Principles
§1 HOW TO WORK         1.1 Роли · 1.2 Фазы · 1.3 Design Artifact · 1.5 Conflict Matrix
                       1.6 Anti-N/A · 1.7 Failure modes · 1.9 3-strike · 1.10 Reasoning (PRIME+)
                       1.11 Sub-agent execution (spawn packs · контракты · merge)
§2 LAWS (A01–A47)  —  каждый с Why + чеклист (+ GOOD/BAD паттерны на 12 ключевых)
   A01 Context/tier      A13 DoD               A25 Coverage absolute   A37 alias→A10
   A02 Zero Trust        A14 Idempotency+Atom  A26 Evidence            A38 alias→A22
   A03 API contract      A15 Deterministic     A27 Test quality        A39 Behavior SSOT
   A04 Plugin boundary   A16 Secure-by-design  A28 Mutation            A40 Secure Continuum
   A05 Layer law         A17 Clean code        A29 ZTA matrix          A41 Trust Pipeline
   A05a Cohesion         A18 OWASP             A30 Anti-slack          A42 Param bounds
   A06 DI & ports        A19 Secrets SSOT      A31 Legacy              A43 alias→A14
   A07 Design-first      A20 Migrations        A32 Monorepo            A44 Dep isolation
   A08 Anti-fork         A21 Contracts+Parity  A33 Blast               A45 alias→A14
   A09 alias→A08         A22 Checker+integrity A34 Intent lock         A46 Config guard
   A10 Errors            A23 Docker/IaC        A35 Contract Surface    A47 alias→A21
   A11 Decomposition     A12 Tests             A12a Taxonomy           A24 TDD-LOCK
   B01 CQRS … B14 Human handoff
§3 GATES               3.0 группы · 3.1 алгоритмы · 3.2 prime_check (FOCUS 30 → CORE 70 → 138) ·
                       3.3 Depth gates · 3.4 P0–P3 · 3.5 evidence
§4 PROTOCOLS           4.1 Threat Model 10Q · 4.2 Two-Agent · 4.3 Bug→Gate · 4.4 Pre-Flight
                       4.5 Fix-until-green · 4.6 3-strike · 4.7 Decision Log ·
                       4.8 Diagnostic tree · 4.9 Testing recipes · 4.10 Adversarial · 4.11 Explain
§5 REFERENCE           5.1 Quality Constellation (7 AST gates) · 5.2 Pattern Catalog ·
                       5.3 Glossary · 5.4 Forbidden · 5.5 Rule families · 5.6 Changelog ·
                       5.7 Standards Traceability (конкретные ID)
```

Международные карты (ISO 25010 · CISQ · OWASP ASVS · CERT/MISRA): **Quality Constellation** в §5.1. Таблица OWASP Top 10: **только A18**.

---

## Checker = работа агента

**Роли — как суб-агенты (§1.11):** Orchestrator делегирует **Analyst · Builder · Guardian · Verifier** через Task tool, каждому — самодостаточный spawn-промпт (роль, tier, какие секции файла читать, handoff IN, гейты, output-контракт). Writer ≠ Verifier — adversarial-ревью в свежей сессии. Суб-агенты возвращают структурный `[OUTPUT]`; Orchestrator мержит, дедупит, строит chains и возвращает фиксы (fix-until-green).

На ≥PRIME агент создаёт `scripts/prime_check/`, реализует **FOCUS 30 (обязательный честный MVP)** первым → green → **затем** фича, и **ratchet** до CORE 70 / EXTENDED (138 всего) по trigger/tier. `standards-map-gate` — **FOCUS+CORE** и проверяет **ID↔gate в обе стороны** (ID заявлен ⇒ его gate green; security gate ⇒ есть ID). Семантический гейт, который нельзя реализовать корректно — `SKIPPED(ADR)`, **никогда не fake-green**. Гоняет `--diff` → FULL до `exit 0`, печатает `PRIME-VERIFY-EVIDENCE`. Пользователь не ставит и не запускает checker.

```text
PHASE 0    Analyst   Tier + adoption_mode
PHASE 0.5  Analyst   Design Artifact + Default-secure 5Q + Threat Model 10Q + maps + AC oracles + blast
PHASE 1–3  Builder   Research → TDD-lock → ports/adapters/composition root
PHASE 4    B↔G       Fix-until-green loop   (P0 перед P1 перед P2)
PHASE 4.5–4.6 Guardian Security audit + review
PHASE 4.7  Builder   Docs + ADR
PHASE 4.8  Verifier  Two-Agent adversarial (другая сессия/модель)
PHASE 5    Verifier  prime_check FULL + evidence block
```

**Skip rules:** LITE = PHASE 0–3, без checker. Threat Model MUST при любом Default-secure YES. Two-Agent MUST для PRIME+.

---

## Лицензия

| Использование | v3.0 | v6.5 |
|---------------|------|------|
| Читать / форк / учиться | MIT | Открыт в репо |
| Личное / hobby | Бесплатно | Бесплатно |
| Компания / команда / клиентский прод | MIT (v3) | **$50 / сотрудник · разово** → [@ExcitedSkam](https://t.me/ExcitedSkam) |

---

## Cursor — без загрязнения User Rules

Держи V6.5 **в workspace**; грузи по требованию. Короткий boot-rule:

```markdown
---
description: MAWYXX PRIME boot — short; full spec on demand
alwaysApply: true
---

Project Skin + Empire Engine. Читай `Mawyxx Prime V6.5.md` для архитектуры / merge.
Нет checker? Агент строит FULL по §3.2. Не проси пользователя гонять тесты.
На RED: fix-until-green (P0→P1→P2). Anti-N/A · Conflict Matrix · Default-secure 5Q · A34–A47 — coverage ≠ done.
Сомневаешься? §4.8 Diagnostic tree + §1.5 uncertainty table.
```

**Опционально — промпт для аудита:** [`Mawyxx-Security.md`](Mawyxx-Security.md) — отдельный standalone-файл для полного security-ревью (`@Mawyxx-Security.md` или project rule). Для Prime не обязателен; не заменяет A18/A41 в обычной разработке.

---

*MAWYXX PRIME · [@ExcitedSkam](https://t.me/ExcitedSkam)*
