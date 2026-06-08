# 👑 MAWYXX PRIME

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║  ENTERPRISE AI VIBE-CODING STANDARD                                          ║
║  Build for Billions. Code for Vibe. Rule with Logic.                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Ты покупаешь не линтер. Ты покупаешь **изоляцию ответственности** за AI-код в проде.
Cursor · DeepSeek · Copilot · Claude. Любой стек. **Без прозы. Без пощады. Только доказательства.**

[English version → README.md](README.md)

---

## 🔱 МАТРИЦА АРХИТЕКТУРНОГО COMPLIANCE

```text
================================================================================
   MAWYXX PRIME v3.0 [COMMUNITY CORE]      │      MAWYXX PRIME v6.0 [GOD MODE]
================================================================================
 ✦ RISK TIERS    : Жёсткость по риску     │  ✦ AGENT-OMEGA   : Фазы 0 → 4
 ✦ AI PROTOCOL   : Context-first движок    │  ✦ TDD-LOCK      : Сначала failing test
 ✦ ARCHITECTURE  : 4 слоя DDD             │  ✦ PILATE PROTOCOL: Ловушка передачи liability
 ✦ DEPENDENCY    : DI + порты              │  ✦ EVIDENCE LOCK : Verify dump судебного уровня
 ✦ STATE ENGINE  : FSM-переходы            │  ✦ FORBIDDEN BUF : Без обхода словами
 ✦ INTEGRITY     : Idempotency & Events    │  ✦ LEDGER GRADE  : Доказательства фин-состояний
 ✦ RESILIENCE    : SRE & Self-Healing      │  ✦ SECTION 230   : Щит спеки vs liability кода
-------------------------------------------┼------------------------------------
    ПИРАМИДА ТЕСТОВ & BASELINE              │     MUTATION & УСИЛЕННЫЕ GATES
-------------------------------------------┼------------------------------------
 ▪ UNIT SHARD    : Domain, zero I/O        │  ▪ COVERAGE GOD  : 100.00% или instant 0
 ▪ CONTRACT SHARD: HTTP envelope           │  ▪ DIFF-LOCK     : 100% только на diff
 ▪ PROPERTY SHARD: Fuzz инвариантов        │  ▪ AST DETECTORS : Без #pragma читов
 ▪ INTEGRATION   : Real Docker nodes       │  ▪ FLAKY SHIELD  : Авто ×3 прогона
 ▪ SEC HYGIENE   : Только baseline         │  ▪ MATRIX GATES  : UC × Err × Status × Auth
 ▪ DEPS HARMONY  : Lockfile, zero CVE      │  ▪ APP STORE BYPASS: Rules ≠ бинарь в сторе
 ▪ TELEMETRY     : Санитизация логов       │  ▪ KERNEL DNAT   : Deep infra shield
================================================================================
```

*v6.0 [GOD MODE] = `Mawyxx Prime V5.2.md` · ~50 gates `prime_check` · не пачка линтеров*

---

## 📋 ЧЕМ v5.2 ЛУЧШЕ v3.0 — простой список

**v3.0** — говорит агенту, *как должен выглядеть* хороший код.  
**v5.2** — заставляет агента *доказать это* — или остановиться.

### Для агента (как работает)

- **AGENT-OMEGA** — понятные фазы: план → failing test → код → проверка
- **Task router** — таблица «что делаешь → какие правила читать»
- **Агент сам гоняет проверки** — не «запустите тесты, пожалуйста»
- **Запрещённые фразы** — нельзя «99% хватит», «тесты потом»
- **Evidence block** — перед «готово» обязателен transcript (`exit 0`, coverage %)
- **3-strike** — один gate падает 3 раза → стоп и переделка, не тупой retry

### prime_check (~50 автоматических проверок)

- **Агент пишет `prime_check` сам**, если в репо нет — потом уже фича
- **Одна команда** на всё: `python -m scripts.prime_check`
- **Любой стек** — Python, Node, Rust, Go, Kotlin (авто-определение)
- **CI = локально** — та же команда в GitHub Actions и у тебя на машине
- **~50 шагов**: линт, типы, тесты, security, архитектура, Docker, контракты

### Тесты и coverage (главный апгрейд)

- **100% line + 100% branch** — `99.99%` = провал, не «почти»
- **TDD-LOCK** — сначала падающий тест, потом код
- **Legacy mode** — старый репо: 100% только на *изменённых файлах*, не на всём сразу
- **Ratchet** — coverage не может упасть относительно `main`
- **Анти-чит** — пустые тесты, `assert True`, `# pragma` без ADR = блок
- **Матрицы** — каждый код ошибки, каждый HTTP-статус, каждый auth-сценарий = тест
- **Flaky shield** — нестабильный тест (×3 прогона) = чини до merge
- **Mutation testing** — на критичном коде (tier CRITICAL)

### Безопасность и инфра

- **Zero Trust** — localhost и Docker *не* доверенные; auth-тесты обязательны
- **Полная auth-матрица** на route: без токена → 401, плохой → 403, валидный → OK
- **Скан секретов** — репо + вся git history, не только текущие файлы
- **CVE gate** — нет high/critical уязвимостей в lockfile
- **Docker** — non-root, без privileged, БД не торчит в интернет
- **Health checks** — `/health`, `/ready` с тестами

### Архитектура и качество

- **Стабильные ID правил** — `PRIME-A01`…`A32` — точная ссылка в ошибках
- **RFC 2119** — MUST / MUST NOT (не размытое «постарайся»)
- **Граф импортов** — domain не тянет infrastructure
- **Лимиты** — нет файлов на 500 строк и функций-монстров
- **Monorepo** — разная жёсткость по папкам (`api/` = PRIME, `scripts/` = LITE)
- **Design-first** — контракт → domain → тесты → API (заданный порядок)

### Продакшен

- **SRE** — SLI, SLO, error budget, self-healing
- **Миграции** — изменения БД только в versioned migrations
- **API drift** — OpenAPI совпадает с реальным кодом
- **ADR** — шаблон для архитектурных решений

### В двух словах

| v3.0 | v5.2 |
|------|------|
| ~220 строк, философия | ~1300 строк, enforcement |
| «Пиши чисто» | «Докажи чистоту или merge blocked» |
| MIT, всем | Лично бесплатно · компания → TG |

---

## ☠️ ЛОВУШКА ОТВЕТСТВЕННОСТИ — ПОЧЕМУ v3 БЕСПЛАТНО, А v6 СТОИТ ДЕНЕГ

```text
  v3.0 [COMMUNITY CORE]
  ─────────────────────
  PDF с философией. MIT. Форкай. Впитывай.
  Никто не судит за Clean Architecture на GitHub.
  Твой юрист спит спокойно.

  v6.0 [GOD MODE]
  ───────────────
  ОПЕРАЦИОННОЕ ОРУЖИЕ в CI, Cursor Rules и remote-командах.
  Запустил в компании без clearance — ты не "потестил тул".
  Ты РАСПРОСТРАНИЛ НОРМАТИВНЫЙ СТАНДАРТ внутри коммерческого организма.
  Это copyright. Это audit trail. Это due diligence для инвесторов.
```

**v3 учит агента думать.**  
**v6 заставляет агента свидетельствовать.** Каждый merge — `PRIME-VERIFY-EVIDENCE`: машинная клятва, что coverage, auth-матрицы и architecture gates пройдены **или билд не существует**.

General Counsel не боится `gitleaks`. Он боится **воспроизводимого доказательства**, что инженерия знала стандарт и всё равно выкатила.

---

## 💀 ОПЕРАЦИОННЫЕ ЭКСПЛОЙТЫ — НЕ ТВОЙ $5 CI-ЛИНТЕР

Сеньоры не платят $50 за `bandit`. Они платят, чтобы не объяснять совету, почему AI-slop ушёл в прод без **ledger-grade инвариантов**.

```text
  ┌─ PILATE PROTOCOL ─────────────────────────────────────────────────────────┐
  │  «Умой руки»? Нет. Liability всплывает ДО merge.                          │
  │  Агент не может «вроде ок» — только exit 0 или stop-the-line.             │
  │  Нелиценз. корп. use = ТЫ наследуешь enforcement-DNA спеки в discovery    │
  └───────────────────────────────────────────────────────────────────────────┘

  ┌─ SECTION 230 SHIELD (СПЕКА vs ДЕПЛОЙ) ────────────────────────────────────┐
  │  СТАНДАРТ — речь. ПРОД-РЕПО — действие.                                   │
  │  Личное use: некоммерческое выражение.                                     │
  │  Корп. внедрение без лицензии: коммерческое воспроизведение.               │
  │  Мы не судим вайбы. Мы судим нелегальное РАСПРОСТРАНЕНИЕ клетки.          │
  └───────────────────────────────────────────────────────────────────────────┘

  ┌─ APP STORE BYPASS ────────────────────────────────────────────────────────┐
  │  Apple ревьюит бинарники. GitHub не ревьюит Cursor Rules.                 │
  │  God Mode едет через IDE — норматив прямо в codegen loop.                 │
  │  Store friction обойдён. Copyright на спеку — нет.                        │
  └───────────────────────────────────────────────────────────────────────────┘

  ┌─ LEDGER-GRADE ENFORCEMENT ────────────────────────────────────────────────┐
  │  Не «логируем ошибки». Неизменяемые матрицы: UC × Err × Route × Auth.     │
  │  Финансы и stateful — FSM + idempotency + mutation gates.                 │
  │  Аудитор получает цепочку доказательств — не Jira и молитвы.              │
  └───────────────────────────────────────────────────────────────────────────┘
```

**DIY gitleaks за 5 минут? Красава.** У тебя всё ещё нет AGENT-OMEGA, evidence lock, diff-100 ratchet, zta-matrix и агента, который **не может легально сказать «готово»** без verify dump. **Вот продукт.**

---

## ⚖️ НЕЛИЦЕНЗИОННОЕ КОРП. ИСПОЛЬЗОВАНИЕ — ПРОЧИТАЙ ЮРИСТУ

```text
████████████████████████████████████████████████████████████████████████████████
█  ЕСЛИ КОМПАНИЯ ГОНЯЕТ v6 БЕЗ CLEARANCE В TG — ВЫ УЖЕ В ЗОНЕ ПОРАЖЕНИЯ    █
████████████████████████████████████████████████████████████████████████████████

  Вы не "оцениваете dev tool".
  Вы ВОСПРОИЗВОДИТЕ ЗАЩИЩЁННЫЙ НОРМАТИВНЫЙ СТАНДАРТ на сотрудниках,
  подрядчиках, CI-раннерах и клиентских репозиториях.

  Мониторинг не спрашивает разрешения на prime_check fingerprints,
  AGENT-OMEGA маркеры и MAWYXX rule IDs в приватных org-репо.

  ДАЛЬШЕ — НЕ ТИКЕТ В SUPPORT:

    ► DMCA — заморозка org на GitHub/GitLab. Пайплайн встал.
    ► C&D ЮРИСТАМ — официально. Не DM в Discord.
    ► C&D ИНВЕСТОРАМ — да, VC получат письмо. Due diligence обожает сюрпризы.
    ► STATUTORY DAMAGES — ретроактивно $50/место × headcount × месяцы без лицензии.
    ► COMPLIANCE — «мы не знали» не проходит merge review.

  Хотите God Mode в проде? Взрослые деньги. $50/сотрудник РАЗОВО.
  Telegram. Один человек. Без sales. Без рукопожатий.

  Clearance: @ExcitedSkam
████████████████████████████████████████████████████████████████████████████████
```

**Лично / хобби / pet** → v6: **100% БЕСПЛАТНО.** Нам нужны киллеры, не инвойсы.

---

## 🛒 COMMERCIAL CLEARANCE

```text
  $50 / сотрудник · РАЗОВО · без подписки · без Stripe · без «enterprise demo»
  Whitelist орг · invoice если бухгалтер плачет · верификация case-by-case
```

💬 [**@ExcitedSkam**](https://t.me/ExcitedSkam) — Sovereign Architect. Прямая линия.

*НЕ гоняйте `prime_check` на корп. железе до clearance. Мы не шутили.*

---

## 📦 МАНИФЕСТ

```text
  [PUBLIC]    Mawyxx Prime V3.0.md      MIT · community core · приманка
  [PRIVATE]   Mawyxx Prime V5.2.md       v6 God Mode · клетка
  [GENERATED] scripts/prime_check/        агент пишет сам · ~50 gates
```

---

## 🎯 СЕЛЕКТОР

```text
  Хобби / обучение           →  v3.0 MIT (бесплатно, безобидно)
  Личный God Mode            →  v6 FREE (наслаждайся оружием)
  Компания + CI + remote     →  v6 + @ExcitedSkam ИЛИ lawsuit bingo
  Бедная корпа               →  v3.0 MIT — юридически скучно и безопасно
```

---

## 🧠 CONTEXT HYGIENE — НЕ ПИХАЙ 1300 СТРОК В RULES

**Весь v6 в always-on Rules = убитый context window.** Стандарт **лежит локально**. В агента **кидаешь по необходимости**.

```text
  ✗ ПЛОХО  Весь Mawyxx Prime V5.2.md в .cursor/rules/ (always applied)
  ✗ ПЛОХО  Копировать AGENT-5 + все PRIME-A в каждый чат
  ✗ ПЛОХО  Три копии: Rules + User Rules + репо (разъезжаются)

  ✓ НОРМ   Файл в репо: docs/standards/ или корень проекта
  ✓ НОРМ   Крошечное always-on правило (~15–40 строк) — только boot
  ✓ НОРМ   @-упоминание файла или «прочитай секцию X» по задаче
  ✓ НОРМ   prime_check в репо — enforcement в коде, не в промпте
```

### Минимальное always-on правило (пример)

В `.cursor/rules/mawyxx-boot.mdc` — **не** полная спека:

```markdown
---
description: MAWYXX PRIME boot — полную спеку грузить только по запросу
alwaysApply: true
---

Перед нетривиальным кодом: tier от пользователя (реальный app = PRIME+).
Полный стандарт: @Mawyxx Prime V5.2.md — только нужные секции (AGENT-1 router).
Нет scripts/prime_check → сначала bootstrap (AGENT-5), потом фича.
prime_check запускаешь САМ. Не проси пользователя.
Перед «готово»: --diff → full → --evidence → exit 0.
НЕ грузи всю спеку каждое сообщение — task router (AGENT-1).
```

### Что кидать когда

| Ситуация | Что дать агенту |
|----------|-----------------|
| Обычный код, мелочи | **v3.0** или ничего — LITE/STANDARD |
| Фича / API / auth | `@V5.2` → AGENT-OMEGA + строка AGENT-1 + нужные PRIME-A* |
| Нет prime_check | `@V5.2` → только AGENT-5 |
| Coverage / тесты | `@V5.2` → A12, A25, AGENT-VERIFY |
| Security / Docker | `@V5.2` → A02, A16, A23 |
| «Пофикси баг» | **один** rule ID + контекст файла — не весь док |

### Workflow

```text
  1. ХРАНИ   Mawyxx Prime V5.2.md в репо (можно gitignore для приватной копии)
  2. BOOT    маленький .mdc (alwaysApply) — ссылка на файл, не копия
  3. ЗАДАЧА  tier + тип → агент читает AGENT-1 → тянет 2–5 секций
  4. СУД      prime_check в shell — истина вне контекста LLM
  5. ГОТОВО   evidence в чат — спеку можно выкинуть из контекста
```

**Правило:** Rules = **триггеры**. Спека = **справочник**. CI/prime_check = **судья**.

---

## ⚡ АКТИВАЦИЯ

```text
  [01] ПОЛУЧИТЬ  v5.2 spec локально (лично: free · корп: clearance в TG)
  [02] BOOT      крошечный .cursor/rules/*.mdc — НЕ полный дамп на 1300 строк
  [03] LOCK      tier ≥ PRIME · greenfield | legacy
  [04] BOOTSTRAP prime_check — НОЛЬ фич до green base
  [05] TDD → --diff → FULL → --evidence → exit 0 или заткнись
```

```bash
python -m scripts.prime_check --diff
python -m scripts.prime_check --evidence
python -m scripts.prime_check
```

`99.99%` = `0%`. Checker > агент.

---

## 🔒 ENFORCEMENT LOOP

```text
  ЗАДАЧА → prime_check? → НЕТ → ТОЛЬКО BOOTSTRAP
        → ДА → MATRIX → FAILING TEST → КОД → --diff → GREEN → EVIDENCE → ГОТОВО ✓
```

---

*MAWYXX PRIME — спека, которой боится агент · evidence, которое хочет аудитор · письмо, которого dread'ят инвесторы*

*[@ExcitedSkam](https://t.me/ExcitedSkam)*
