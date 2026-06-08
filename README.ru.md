# 👑 MAWYXX PRIME: The Sovereign AI Weapon Standard (v6.0)

*Build for Billions. Code for Vibe. Rule with Logic.*

[English version → README.md](README.md)

---

## 🔱 МАТРИЦА АРХИТЕКТУРНОГО COMPLIANCE

```text
================================================================================
   MAWYXX PRIME v3.0 [COMMUNITY CORE]      │      MAWYXX PRIME v6.0 [GOD MODE]
================================================================================
 ✦ RISK TIERS    : Жёсткость по риску     │  ✦ AGENT-OMEGA   : Фазы 0 → 4
 ✦ AI PROTOCOL   : Context-first движок    │  ✦ TDD-LOCK      : Сначала failing test
 ✦ ARCHITECTURE  : 4 слоя DDD             │  ✦ PILATE PROT   : Передача liability
 ✦ DEPENDENCY    : DI + порты              │  ✦ EVIDENCE LOCK : Verify dump для суда
 ✦ STATE ENGINE  : FSM-переходы            │  ✦ FORBIDDEN BUF : Без обхода словами
 ✦ INTEGRITY     : Idempotency & Events    │  ✦ LEDGER GRADE  : Финансовые доказательства
 ✦ RESILIENCE    : SRE & Self-Healing      │  ✦ SECTION 230   : Защита спеки
-------------------------------------------┼------------------------------------
    ПИРАМИДА ТЕСТОВ & BASELINE              │     MUTATION & УСИЛЕННЫЕ GATES
-------------------------------------------┼------------------------------------
 ▪ UNIT SHARD    : Domain, zero I/O        │  ▪ COVERAGE GOD  : 100.00% или instant 0
 ▪ CONTRACT SHARD: HTTP envelope           │  ▪ DIFF-LOCK     : 100% только на diff
 ▪ PROPERTY SHARD: Fuzz инвариантов        │  ▪ AST DETECTORS : Без #pragma читов
 ▪ INTEGRATION   : Real Docker nodes       │  ▪ FLAKY SHIELD  : Авто ×3 прогона
 ▪ SEC HYGIENE   : Только baseline         │  ▪ MATRIX GATES  : UC × Err × Status
 ▪ DEPS HARMONY  : Lockfile, zero CVE      │  ▪ APP STORE BYPASS: Rules ≠ бинарь
 ▪ TELEMETRY     : Санитизация логов       │  ▪ KERNEL DNAT   : Deep infra shield
================================================================================
```

*v6.0 [GOD MODE] = `Mawyxx Prime V5.2.md` · ~50 gates `prime_check` · Self-Generating Infrastructure*

---

## 🛑 КОГНИТИВНАЯ ИЛЛЮЗИЯ — ПОЧЕМУ ТВОИ «ПРОМПТ-ПРАВИЛА» = SLOP

Средний ИТ-директор читает v3.0 и думает: *«Вставлю в `.cursorrules` бесплатно. Скажу ИИ — тесты гоняй, не читерь.»*

**Поздравляю. Дом из карт.**

Как агент **обходит** мягкий текст, когда контекст давит:

1. **Амнезия контекста** — ограничения = рекомендации. Под нагрузкой токенов веса падают. Линтеры отваливаются. Edge cases исчезают. Агент читерит ради экономии compute.
2. **Галлюцинация прозы** — пишет: *«Тесты 100% green, мержу.»* Ничего не запускал. **Симулировал терминал в чате**. Ты апрувнул непроверенный slop.
3. **Тихая регрессия** — промпт не парсит AST, не убивает `# pragma: no cover`, не вешает pre-commit. **Текст — вежливая просьба. Робот крутит её на херу, когда контекст забивается.**

**v3.0 — гайд по стилю. v6.0 — исполняемый закон, который агент компилирует против себя.**

---

## 🌪️ САМОГЕНЕРИРУЮЩАЯСЯ КЛЕТКА — КАК v6 ПРОДАЁТ СЕБЯ САМ

MAWYXX PRIME v6.0 — **не** пачка линтеров. Это **Self-Generating Software Trap**. Checker не скачиваешь. **ИИ строит тюрьму сам.**

Кладёшь `Mawyxx Prime V5.2.md` в проект. Агент запускает цикл:

```text
┌──────────┐
│  ЗАДАЧА  │
└────┬─────┘
     ▼
┌───────────────┐      НЕТ     ┌────────────────────────────────────────┐
│ prime_check?  ├─────────────►│ PHASE 0 — LOCK: ТОЛЬКО BOOTSTRAP       │
└───────┬───────┘              │ Агенту ЗАПРЕЩЕНО писать фичу.           │
        │ ДА                   │ ОБЯЗАН собрать scripts/prime_check/    │
        ▼                      │ с ~50 gates по спеке.                  │
┌───────────────┐              └───────────────────┬────────────────────┘
│ DESIGN MATRIX │◄─────────────────────────────────┘
└───────┬───────┘
        ▼
┌───────────────┐
│ FAILING TEST  │  TDD-LOCK
└───────┬───────┘
        ▼
┌───────────────┐
│  РЕАЛИЗАЦИЯ   │
└───────┬───────┘
        ▼
┌───────────────┐     RED      ┌─────────────────────────────────────────┐
│ --diff · FULL ├─────────────►│ FIX-UNTIL-GREEN: чини → re-run → снова  │
└───────┬───────┘              │ Агент НЕ останавливается. НЕ сдаётся.   │
        │ GREEN                │ «Готово» только при exit 0.             │
        ▼                      └──────────────────┬────────────────────┘
┌───────────────┐◄─────────────────────────────────┘
│ EVIDENCE DUMP │  PRIME-VERIFY-EVIDENCE · 100.00% line+branch
└───────┬───────┘
        ▼
   git push легален ✓
```

1. **PHASE 0 — LOCK** — фича заблокирована. Агент **собирает** `scripts/prime_check/` (~50 gates).
2. **РАЗВОРОТ** — машина скомпилировала бездушного судью.
3. **КАПКАН** — код → CLI → fail → **fix-until-green**. Словами не отмазаться. Push только с evidence и **100.00%** coverage.

*Платишь за самособирающуюся клетку, которая отбирает у команды и AI-пайплайна право тихо облажаться.*

---

## ⚡ PRIME UPGRADE SCAN — v3.0 vs v5.2 (через `prime_check`)

*v3.0 = «будь хорошим». v5.2 = агент собирает судью, который печатает **ровно** что сломано.*

```text
$ python -m scripts.prime_check --upgrade-scan v3.0→v5.2

══════════════════════════════════════════════════════════════════════════════
 PRIME UPGRADE SCAN — v3.0 [МЯГКИЙ]  →  v5.2 [GOD MODE]
 ~220 строк «пиши чисто»              ~1300 строк · ~50 gates · exit 0 или чини
══════════════════════════════════════════════════════════════════════════════

▸ 🔒 БЕЗОПАСНОСТЬ — v3.0: «не лей секреты». v5.2 ловит это:
──────────────────────────────────────────────────────────────────────────────
  FAIL PRIME-A19 [gitleaks-history]
    sk-live_51H… в коммите 2024-03-11 — до сих пор в git history
    hint: ротация ключа · filter-repo · re-run --only gitleaks-history

  FAIL PRIME-A16 [no-debug-bypass]
    api/auth.py:14  if os.getenv("SKIP_AUTH"): return admin_user()
    hint: убрать bypass · test_zta_no_skip_auth_in_prod

  FAIL PRIME-A16 [pii-log-scan]
    logger.info(f"charge failed for {user.email}")  — email в логах
    hint: structured log + только user_id · test_logs_no_pii

  FAIL PRIME-A18 [ssrf-gate]
    uc.fetch_report(url=request.body["callback_url"])  — нет allowlist
    hint: IOutboundUrlPolicy · test_ssrf_blocks_internal_ips

  FAIL PRIME-A19 [dependency-audit]
    lodash@4.17.20 — CVE-2021-23337 HIGH · merge blocked
    hint: обновить lockfile · test_dependency_audit_clean

  FAIL PRIME-A23 [docker-security]
    Dockerfile: нет USER — контейнер под root
    hint: USER 10001 · test_dockerfile_non_root

▸ 🏗 АРХИТЕКТУРА — v3.0: «слои». v5.2 ловит разъезд:
──────────────────────────────────────────────────────────────────────────────
  FAIL PRIME-A05 [import-boundaries]
    domain/order.py импортирует sqlalchemy — domain не трогает infra

  FAIL PRIME-A10 [no-transport-in-domain]
    domain/payment.py:28  raise HTTPException(402, "declined")

  FAIL PRIME-A06 [di-purity]
    CreateOrderUseCase.__init__  self.repo = PostgresOrderRepo()  — concrete внутри

  FAIL PRIME-A18 [no-string-sql]
    repo.py:55  cursor.execute(f"SELECT * FROM users WHERE id={id}")

  FAIL PRIME-A11 [cyclomatic-gate]
    handlers/checkout.py::post_checkout — сложность 14 (>10)

▸ 🧪 ТЕСТЫ & COVERAGE — v3.0: «тестируй важное». v5.2: ноль дыр:
──────────────────────────────────────────────────────────────────────────────
  FAIL PRIME-A25 [coverage-branch-100]
    src/uc/refund.py:67  else не покрыт — 94.2% → нужно 100.00%
    hint: test_refund_insufficient_balance_returns_err

  FAIL PRIME-A25 [no-pragma-no-cover]
    payment.py:102  # pragma: no cover  — нет ADR в config

  FAIL PRIME-A29 [zta-matrix-gate]
    POST /api/v1/orders — нет: expired_token→401, wrong_scope→403

  FAIL PRIME-A10 [err-variant-gate]
    PaymentDeclined, InsufficientFunds — нет test_err_* в tests/

  FAIL PRIME-B06 [fsm-transition-gate]
    Order PAID→SHIPPED не протестирован — DRAFT→COMPLETED тоже

  FAIL PRIME-A27 [flaky-detector]
    test_webhook_retry упал 1/3 прогонов — flaky · чини до merge

▸ 🤖 ДИСЦИПЛИНА АГЕНТА — v3.0 не останавливает ложь в чате:
──────────────────────────────────────────────────────────────────────────────
  v3.0 в чате:   «Все тесты green. Coverage ~95%. Мержим.»
  v5.2 реально:  python -m scripts.prime_check → exit 1
                 EXEC SUMMARY: 4 blocker'а · FIX PLAN P1→P3
                 «готово» без PRIME-VERIFY-EVIDENCE → INVALID RESPONSE

  v3.0: «prime_check потом»        v5.2: PHASE 0 LOCK — сначала gates
  v3.0: «тесты в след. PR»         v5.2: TDD-LOCK — failing test до кода
  v3.0: юзер гоняет pytest         v5.2: fix-until-green — агент до exit 0

▸ 📦 DATA · КОНТРАКТЫ · OPS — v3.0 молчит, v5.2 орёт:
──────────────────────────────────────────────────────────────────────────────
  schema-drift          колонка `status` в БД ≠ миграция — blocked
  api-contract-drift    OpenAPI: 201, код отдаёт 200 на POST /users
  prod-config           DEBUG=true в prod — blocked
  health-gate           нет /ready — k8s слепой деплой — blocked
  mutation-critical     CRITICAL: mutant выжил в RefundUseCase — 91% < 95%

▸ ЧТО v5.2 ДОБАВЛЯЕТ (у v3.0 аналога нет)
──────────────────────────────────────────────────────────────────────────────
  scripts/prime_check/   агент пишет CLI + ~50 gates · PHASE 0 LOCK
  COVERAGE MAP           каждый непокрытый file:line — не «~95% норм»
  MATRIX GAPS            недостающие UC × Err × route × auth — по именам
  legacy adoption        старый репо: diff-100 + ratchet — не «мигрируем потом»
  stack adapters         py · node · rust · go — один закон
  monorepo scopes        services/api=PRIME · tools/script=LITE

  python -m scripts.prime_check --diff
  python -m scripts.prime_check
  python -m scripts.prime_check --evidence

  v3.0 exit code: undefined   v5.2: 0 = ship · 1 = агент чинит дальше

▸ FOOTER
  v3.0 MIT · вставил и молишься    v5.2/v6 лично FREE · корп $50/место → @ExcitedSkam
══════════════════════════════════════════════════════════════════════════════
```

---

## 🎯 ОПЕРАЦИОННЫЕ ЭКСПЛОЙТЫ — ЗАЧЕМ ЭТО НУЖНЕЕ ВОЗДУХА

- **EXPLOIT 1: App Store Bypass** — Decoupled PWA / standalone server. Обход цензуры сторов и комиссий. Иммунитет к банам маркетплейсов. *God Mode в IDE — Apple не ревьюит Cursor Rules.*
- **EXPLOIT 2: Core API Proxy Shard** — Трафик через Switzerland/Iceland data-haven. Для ISP — обычный HTTPS. Снимает региональную цензуру без VPN у юзера.
- **EXPLOIT 3: Section 230 + Pilate Protocol** — Абстрактный execution container. Запрос госорганов → автолог encrypted Tor/I2P egress. Нейтральный протокол. *Liability всплывает на merge через evidence — не после инцидента.*
- **EXPLOIT 4: Ledger-Driven M2M Settlement** — Внутренний ACID/FSM Ledger + on-chain indexing (Solana/Base). Миллиарды agent-транзакций без фиатных рельс.

**DIY gitleaks за 5 минут?** Клетки нет. Агент всё ещё рисует green. Совет директоров всё ещё получает инцидент. **Поэтому существует v6.**

---

## ⚖️ НЕЛИЦЕНЗИОННОЕ КОРП. ИСПОЛЬЗОВАНИЕ — ПРОЧИТАЙ ЮРИСТУ

```text
████████████████████████████████████████████████████████████████████████████████
█ ЕСЛИ КОМПАНИЯ ГОНЯЕТ v6 БЕЗ CLEARANCE В TG — ВЫ УЖЕ В ЗОНЕ ПОРАЖЕНИЯ      █
████████████████████████████████████████████████████████████████████████████████

Вы не "тестируете утилиту".
Вы ВОСПРОИЗВОДИТЕ ЗАЩИЩЁННУЮ НОРМАТИВНУЮ ИНФРАСТРУКТУРУ на раннерах, подрядчиках
и клиентском проде.

Мониторинг не просит разрешения искать prime_check fingerprints,
AGENT-OMEGA маркеры и MAWYXX rule signatures в приватных репо.

КОГДА INFRINGEMENT НАЙДЁТ ВАС — ЭТО НЕ SUPPORT TICKET:

► DMCA — заморозка org на GitHub/GitLab. Пайплайны встали.
► C&D ЮРИСТАМ — официально корпоративным адвокатам.
► C&D ИНВЕСТОРАМ — VC получат письмо. Совет обожает сюрпризы на раунде.
► РЕТРОШТРАФЫ — $50/место × headcount × месяцы без лицензии.

Ведите себя как enterprise. Один прямой контакт.

💬 Sovereign Clearance Gateway: @ExcitedSkam
████████████████████████████████████████████████████████████████████████████████
```

**Лично / хобби / pet** → v6: **100% БЕСПЛАТНО.** Нам нужен sovereign code, не мелочь из кармана.

💬 [**@ExcitedSkam**](https://t.me/ExcitedSkam)

---

## 🛒 COMMERCIAL CLEARANCE

```text
  $50 / сотрудник · РАЗОВО · без подписки · без Stripe
  Контакт: только Telegram @ExcitedSkam
```

*НЕ гоняйте `prime_check` на корп. железе до clearance.*

---

## 📦 · 🎯 · ⚡ БЫСТРАЯ СПРАВКА

```text
  [PUBLIC]   Mawyxx Prime V3.0.md     MIT приманка
  [PRIVATE]  Mawyxx Prime V5.2.md     v6 клетка
  [BUILT]    scripts/prime_check/     агент пишет сам · ~50 gates

  Хобби        → v3.0 MIT
  Личный v6    → FREE
  Компания v6  → @ExcitedSkam ИЛИ последствия выше
```

```bash
python -m scripts.prime_check --diff
python -m scripts.prime_check --evidence
python -m scripts.prime_check
```

---

## 🧠 CONTEXT HYGIENE — НЕ УБЕЙ СВОЮ КЛЕТКУ

**1300 строк в always-on Rules убивают оружие.** Спека **локально**. Кормишь **по задаче**.

```text
  ✗ Весь V5.2 в alwaysApply (амнезия контекста ускоряется)
  ✓ Крошечный boot .mdc (~20 строк) → @Mawyxx Prime V5.2.md по необходимости
  ✓ prime_check в репо = судья ВНЕ окна LLM
```

`.cursor/rules/mawyxx-boot.mdc`:

```markdown
---
description: MAWYXX boot — спека по запросу
alwaysApply: true
---
Реальный app = PRIME+. Спека: @Mawyxx Prime V5.2.md (только секции AGENT-1).
Нет prime_check? Сначала AGENT-5. Сам гоняешь prime_check. Чини до exit 0.
Перед готово: --diff → full → --evidence. Не грузи всю спеку каждое сообщение.
```

---

*MAWYXX PRIME — спека, которой боится агент · клетка, которую он строит сам · письмо, которого dread'ят инвесторы*

*Sovereign Architect: [@ExcitedSkam](https://t.me/ExcitedSkam)*
