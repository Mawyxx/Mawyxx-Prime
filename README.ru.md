# MAWYXX PRIME — стандарт для AI-кодинга

*Build for Billions. Code for Vibe. Rule with Logic.*

[English version → README.md](README.md)

Нормативные спеки для ИИ-агентов, пишущих прод-код. Два уровня: **v3.0** (принципы, MIT) и **v5.2** (слой enforcement, в маркетинге v6 God Mode).

---

## Что в репозитории

| Файл | Что это |
|------|---------|
| `Mawyxx Prime V3.0.md` | ~220 строк · 10 разделов · философия и архитектура · **MIT · публично** |
| `Mawyxx Prime V5.2.md` | ~1300 строк · AGENT-0…5 · правила A01–A32 · B01–B14 · **приватно / коммерция** |
| `scripts/prime_check/` | Не в репо — **агент пишет сам** по AGENT-5 при tier ≥ PRIME |

**v3.0** — говорит агенту, *как должен выглядеть хороший код*.  
**v5.2** — добавляет *как агент обязан это проверить*: фазы, `prime_check`, закон coverage, evidence block.

---

## v3.0 vs v5.2 — в двух словах

```text
================================================================================
   v3.0 [ПРИНЦИПЫ]                        │   v5.2 [ENFORCEMENT]
================================================================================
 Risk tiers LITE → CRITICAL               │   Те же tiers · default PRIME для apps
 Контекст · минимальный scope             │   AGENT-OMEGA фазы 0 → 4 (строгий порядок)
 Self-review чеклист (§10)                 │   AGENT-2 + machine gates
 4 слоя · DI · FSM · idempotency          │   То же + import-graph · di-purity gates
 Security · тесты · SRE текстом           │   ~50 шагов prime_check под стек
 «Тесты на ключевое»                       │   100.00% line + branch (tier ≥ PRIME)
 «100% на CRITICAL»                        │   diff-100 · ratchet vs main · legacy mode
 Нет merge gate                           │   exit 0 = единственное валидное «готово»
================================================================================
```

*v6 / God Mode в маркетинге = `Mawyxx Prime V5.2.md` + agent-built `prime_check`*

---

## v3.0 — стандарт (кратко)

Универсальный стандарт качества для ИИ-кодеров. Жёсткость по **Risk Tier**:

| Tier | Когда |
|------|--------|
| **LITE** | Скрипты, утилиты — читаемость, без секретов |
| **STANDARD** | Обычные фичи — модули, ключевые тесты, понятные ошибки |
| **PRIME** | Auth, платежи, PII, API — слои, DI, FSM, observability |
| **CRITICAL** | Финансы, compliance — PRIME + ADR, resilience, макс. глубина тестов |

**Включает:** 4 слоя · DI · SOLID · typed errors · FSM · domain events · SRE/ADR · security · пирамида тестов · self-review.

**Не включает:** автоматический merge gate · обязательный % coverage · verify-loop агента · спеку `prime_check`.

---

## v5.2 — что добавляет стандарт

Та же архитектурная философия, что v3. **Плюс** agent contract и машинная верификация.

### Workflow агента (AGENT-OMEGA)

```text
PHASE 0  tier ≥ PRIME? → нет prime_check? → только bootstrap AGENT-5 (без фичи)
PHASE 1  design artifact: files · routes · Err · test_matrix
PHASE 2  TDD-LOCK: failing test до реализации
PHASE 3  реализация (минимум на фичу · максимум на качество)
PHASE 4  prime_check --only → --diff → full → exit 0 → PRIME-VERIFY-EVIDENCE
         RED → fix-until-green (агент не стопает · не просит юзера гонять тесты)
```

### prime_check (AGENT-5)

Один CLI, который агент создаёт и поддерживает: `python -m scripts.prime_check`

| Группа | Примеры шагов |
|--------|----------------|
| Static | lint · typecheck · format · dead-code · file-size · complexity |
| Architecture | import boundaries · DI purity · no SQL strings · no transport in domain |
| Security | gitleaks history · CVE audit · bandit · PII в логах · SSRF · ZTA matrix |
| Tests | unit · integration · contract · property · flaky ×3 · ban empty/trivial |
| Matrices | err-variant · route × status · FSM transitions · design test_matrix |
| Coverage | line 100% · branch 100% · diff-100 · ratchet · pragma только с ADR |
| Data/Ops | schema drift · API contract drift · docker security · health probes |
| Output | structured report · evidence block |

Stack adapters: **python · node · rust · go · kotlin · swift** — одни правила, локальные линтеры.

### Definition of Done (tier ≥ PRIME)

- `python -m scripts.prime_check` → **exit 0**
- блок **PRIME-VERIFY-EVIDENCE** в ответе агента
- без обоих — ответ **невалиден** по A26

---

## PRIME UPGRADE SCAN — дельта стандарта

```text
══════════════════════════════════════════════════════════════════════════════
 STANDARD DELTA                          v3.0 [MIT]  →  v5.2
══════════════════════════════════════════════════════════════════════════════
  Объём         10 разделов · ~220 строк          A01–A32 · B01–B14 · AGENT-0…5
  Язык          рекомендации                      RFC 2119 MUST / MUST NOT
  Модель        прочитал → код → self-review       AGENT-OMEGA 0 → 4
  «Готово»      агент заявил                      exit 0 + evidence block
  Merge gate    нет                               prime_check (~50 шагов)
──────────────────────────────────────────────────────────────────────────────

▸ ТОЛЬКО В v5.2
  prime_check · FIX-UNTIL-GREEN · TDD-LOCK (A24) · evidence block (A26)
  ~50 gates · 100% line+branch · матрицы ZTA/Err/Route/FSM
  legacy diff-100 + ratchet (A31) · monorepo tiers (A32) · mutation (A28)
  stack adapters · structured report · forbidden phrases · anti-slack (A30)

▸ БЫЛО В v3.0 — СТАЛО ПРОВЕРЯЕМЫМ В v5.2
  tiers · слои · DI · FSM · security §7 · tests §8 · SRE · ADR · docker
  → import-graph · err-variant · fsm-transition · gitleaks · schema-drift gates

▸ ЛИНИЯ COVERAGE
  v3.0   агент сам выбирает «ключевые пути» · 100% только для CRITICAL
  v5.2   99.99% = fail · pragma нужен ADR · coverage не падает vs main

▸ КОМАНДА ВЕРИФИКАЦИИ (только в v5.2)
  python -m scripts.prime_check --diff → full → --evidence → exit 0
══════════════════════════════════════════════════════════════════════════════
```

---

## Лицензия

| Использование | v3.0 | v5.2 |
|---------------|------|------|
| Лично / хобби / pet | MIT · free | **Бесплатно** |
| Компания / команда / клиентский прод | MIT только для v3 | **$50 / сотрудник · разово** → Telegram |

Корп. использование v5.2 без clearance: связаться до деплоя на раннерах компании или в клиентском коде.

💬 [**@ExcitedSkam**](https://t.me/ExcitedSkam)

---

## Быстрая справка

```text
  Хобби / обучение     →  Mawyxx Prime V3.0.md (MIT)
  Реальный app + агент →  Mawyxx Prime V5.2.md + bootstrap prime_check

  python -m scripts.prime_check --diff
  python -m scripts.prime_check --evidence
  python -m scripts.prime_check
```

---

## v5.2 в Cursor

Не вставляй все ~1300 строк в always-on Rules — enforcement теряет вес в контексте.

```text
  ✗ Весь V5.2 в alwaysApply на каждое сообщение
  ✓ Маленький boot rule (~20 строк) + @Mawyxx Prime V5.2.md по задаче
  ✓ prime_check в репо = верификация вне окна чата
```

`.cursor/rules/mawyxx-boot.mdc`:

```markdown
---
description: MAWYXX boot — спека по запросу
alwaysApply: true
---
Реальный app = PRIME+. Спека: @Mawyxx Prime V5.2.md (секции AGENT-1 по необходимости).
Нет prime_check? Сначала AGENT-5. Сам гоняешь prime_check. Чини до exit 0.
Перед готово: --diff → full → --evidence.
```

---

*MAWYXX PRIME — v3 принципы · v5.2 enforcement · [@ExcitedSkam](https://t.me/ExcitedSkam)*
