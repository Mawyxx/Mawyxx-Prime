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

## 📋 ЧЕМ v6 ЛУЧШЕ (коротко)

| v3.0 | v6.0 [God Mode] |
|------|-----------------|
| ~220 строк · философия | ~1300 строк · enforcement |
| «Пиши чисто» | «Чини до green — потом evidence» |
| Мягкие промпты | **~50 machine gates**, агент пишет сам |
| MIT · всем | Лично free · **$50/место** → TG |

**Апгрейд:** AGENT-OMEGA · TDD-LOCK · fix-until-green · 100% line+branch · legacy diff-100 · zta-matrix · evidence · любой стек · monorepo · mutation на CRITICAL.

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
