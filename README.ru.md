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

*v3.0 говорит агенту, чего хотеть. v5.2 заставляет агента собрать судью, который говорит **нет**.*

```text
$ python -m scripts.prime_check --upgrade-scan v3.0→v5.2

══════════════════════════════════════════════════════════════════════════════
 PRIME UPGRADE SCAN — v3.0 [МЯГКИЙ ПРОМПТ]  →  v5.2 [GOD MODE / v6 маркетинг]
 спека: ~220 строк философии                 спека: ~1300 строк machine law
══════════════════════════════════════════════════════════════════════════════

▸ EXEC SUMMARY — почему твой v3.0 в `.cursorrules` всё ещё сливает деньги
──────────────────────────────────────────────────────────────────────────────
  P1  Агент написал «тесты green» — ничего не гонял           → evidence-block
  P1  «~80% coverage норм»                                    → coverage-line-100 + branch-100
  P1  `# pragma: no cover` / istanbul ignore                  → no-pragma-no-cover (AST)
  P1  Новый route без тестов 401/403                          → zta-matrix-gate
  P1  Err-коды есть, test_err_* нет                           → err-variant-gate
  P2  Секрет в git полгода назад                              → gitleaks-history
  P2  CVE в lockfile — «потом»                                → dependency-audit
  P2  Docker root в проде                                     → docker-security
  P2  Агент сдался на red: «не могу, в следующем PR»          → fix-until-green (no exit)

▸ v3.0 ГОВОРИЛ                         │ v5.2 ЗАСТАВЛЯЕТ (gate · реальный outcome)
───────────────────────────────────────┼──────────────────────────────────────────
 «Сначала прочитай контекст»           │ AGENT-OMEGA фазы 0–4 — пропуск = нарушение
 «Self-review перед done»              │ ~50 gates · агент сам гоняет CLI · 0 или чини
 «Тесты на ключевое»                   │ 100.00% line + branch · diff-100 · ratchet vs main
 «Границы слоёв»                       │ import-graph-gate · no-transport-in-domain · di-purity
 «Типизированные ошибки»               │ каждый Err → test_err_* или merge blocked
 «Auth на защищённых route»            │ матрица anon/expired/forbidden/valid
 «FSM для статусов»                    │ каждый переход протестирован или exit 1
 «Без секретов в репо»                 │ working tree + вся git history
 «Детерминированный domain»            │ Date.now / uuid4 / random в domain → fail
 «TDD когда можно»                     │ TDD-LOCK — failing test ДО кода, тот же PR
 «Done = чисто + протестировано»       │ PRIME-VERIFY-EVIDENCE — «готово» без него = invalid

▸ ЧТО v5.2 СТРОИТ, ЧЕГО v3.0 НИКОГДА НЕ МОГ
──────────────────────────────────────────────────────────────────────────────
  scripts/prime_check/     агент пишет ~50 gates если нет — PHASE 0 LOCK
  EXEC SUMMARY + FIX PLAN  на red — что чинить и в каком порядке
  COVERAGE MAP             file:line каждой непокрытой ветки — без гадания
  MATRIX GAPS              недостающие UC × Err × route × auth — списком
  stack adapters           python · node · rust · go · kotlin · swift — один закон
  legacy adoption          старый репо? diff-100 на diff + ratchet, не отмазка
  monorepo scopes          tier по пути — API=PRIME, scripts=LITE
  mutation-critical        CRITICAL: mutants must die ≥95%

▸ ОДНА КОМАНДА — У v3.0 АНАЛОГА НЕТ
──────────────────────────────────────────────────────────────────────────────
  python -m scripts.prime_check --diff      # только изменённое — не прятаться
  python -m scripts.prime_check               # full matrix — merge gate
  python -m scripts.prime_check --evidence    # handoff block под суд/борд

  v3.0 exit code: undefined.  v5.2 exit code: 0 = ship · 1 = агент чинит дальше.

▸ TIER FOOTER
──────────────────────────────────────────────────────────────────────────────
  v3.0 MIT · хобби-приманка · философия, которую вставляют и молятся
  v5.2/v6 · лично FREE · корп $50/место разово → @ExcitedSkam
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
