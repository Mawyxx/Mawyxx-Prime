# MAWYXX PRIME — Standard Audit (text-only scope)

**Тип:** рабочий документ репозитория. **Не часть агентного стандарта** и не
загружается агентом как правило.
**Аудит:** стандарт `Mawyxx Prime V6.7.md`, revision **v6.7**.
**Дата:** 2026-11-03.

**Главное ограничение:** стандарт **текстовый**. Он задаёт **обязанности агента**
и ничего не исполняет. Всё, что требует рантайм-контроля (контекст, инструменты,
аудит, бюджет, approvals), **не может быть обязанностью агента в тексте** —
это зона платформы/инструментов, а не стандарта. Поэтому такие предложения в
стандарт не добавляются.

**Status (v6.7):** в стандарт внесены text-only scope, performance/load contract и test
completeness — §0.0.2 boundary, §4.17 irreversible boundary, §1.11.8 all untrusted context,
§5.7.10 OWASP LLM / NIST AI RMF / ISO 42001 traceability, A12a performance + extended
families, A34 perf oracles, §1.3a axis 13, A62 Performance & Load Contract, PERF-LOCK,
Test Selection Matrix, edge-case sweep, §4.9a test data & environment.
Runtime-контроль остаётся вне scope; гейты не добавлены (SSOT 139).

---

## 0. TL;DR

- Стандарт силён в том, **как писать код**: Law→Gate, TDD-LOCK, anti-N/A, SSOT,
  traceability, sub-agent contracts.
- Он **не регулирует рантайм агента** — и не должен: текстовый стандарт не может
  заставить агента вести рантайм-журналы или
  контролировать контекст.
- Улучшать стандарт можно только **текстовыми обязанностями** (A/B): правила,
  чеклисты, evidence-артефакты, которые агент сам пишет.
- Рантайм-контроль (context/tools/audit/budget/approval) — **вне scope**;
  он принадлежит платформе, а не конституции.

---

## 1. Метод аудита

### 1.1 Петля развития стандарта

```
ДЫРА → КЛАСС → ЗАКОН → ГЕЙТ → ДОКАЗАТЕЛЬСТВО → КОНСОЛИДАЦИЯ → RATCHET
```

| Шаг | Что происходит | Пример v6.5 |
|---|---|---|
| Дыра | найден реальный failure class / пробел | «phases были чеками без артефакта» |
| Класс | новый класс или глубина старого | TDD-LOCK |
| Закон | `Axx` + Why + FAIL/PASS | A24 переписан |
| Гейт | `Enforced by` | `tdd-lock-gate` |
| Доказательство | файл-артефакт + evidence | `design/TDD-LOCK-<task>.md` |
| Консолидация | SSOT, alias, dedupe, счётчики | alias A49→A20 |
| Ratchet | FOCUS 31 → CORE 71 → 139 | `checker_maturity` |

### 1.2 Инструменты проверки

- `tools/doc_integrity_gate.py` — repo-only валидатор самого стандарта.
  На v6.6.2: **PASS** (`laws=81`, `aliases=10`, `registry_gates=114`).
- `tools/doc_integrity_gate.py --json` — машинный отчёт.

### 1.3 Keyword-аудит (факты вхождений)

| Понятие | Вхождений | Вывод |
|---|---|---|
| context budget / token / compaction | 0 | нет контекст-инженерии |
| tool safety / tool output / function call | 0 | нет безопасности инструментов |
| human approval / human-in-the-loop | 0 | нет точки человека |
| excessive agency / least agency | 0 | нет ограничения агентности |
| OWASP LLM / NIST AI RMF / ISO 42001 | 0 | нет AI-governance |
| agent cost / latency budget | 1 | только §1.11.6 (sub-agent) |
| eval / benchmark (агентные) | 0 | нет агентной проверки |
| model version / pin / temperature | 0 | нет контроля модели |
| replay / audit log (агентные) | 0 | нет аудита действий |
| sandbox | 6 | есть §1.11.7, без enforcement-гейта |
| prompt injection | 9 | только repo-контент (§1.11.8) |

---

## 2. Сильные стороны (не ломать)

1. **Law→Gate** и честный checker (`A22`), no-theatre, FOCUS→CORE→FULL.
2. **TDD-LOCK** (`design/TDD-LOCK-<task>.md`).
3. **Anti-N/A** + `N/A(absent-trigger)`.
4. **SSOT + Conflict Matrix + alias map**.
5. **Tier-aware depth** (§0.4/§0.7).
6. **Двухагентная верификация** (§4.2) + adversarial 8+3.
7. **Sub-agent contracts**: spawn-промпт, output JSON, merge rules, budget, sandbox.
8. **Standards traceability** OWASP/CWE/ASVS/ISO 25010/5055/CERT (§5.7).
9. **Bug→Gate + feedback loop** (§4.3/§4.16).
10. **Дедуктивный слой v6.6**: Axioms → Kernel → Law map → Policy Index →
    Gate registry.

---

## 3. Бенчмарк лучших систем

| Источник | Ключевая идея | У нас | Решение |
|---|---|---|---|
| Anthropic — Building effective agents | workflow vs agent | фазы/роли есть | текстовое дерево выбора — возможно (P2) |
| Anthropic — Context engineering | контекст — дефицитный ресурс | нет | **вне scope** (платформа) |
| Anthropic — Writing tools for agents | контракт инструмента | нет | **вне scope** (платформа) |
| OpenAI — Practical guide to agents | guardrails, human intervention | guardrails частично | **вне scope** (платформа) |
| OWASP LLM Top 10 | LLM01 prompt injection, LLM06 excessive agency | §1.11.8 + §5.7.10 | Done v6.7 |
| NIST AI RMF / ISO 42001 | risk management AI-систем | §5.7.10 | Done v6.7 |
| Google SRE / DORA | SLO, error budget | для кода есть | **вне scope** (платформа) |
| SWE-bench / τ-bench | benchmark | нет | **вне scope** (репозиторий/инструменты) |
| MCP / supply chain | provenance, least privilege | A19 частично | **вне scope** (платформа) |
| RFC/ADR/SemVer | версионирование решений | ADR/SemVer частично | migration policy (P2) |

---

## 4. Наблюдения (без предписаний)

| # | Наблюдение | Почему важно | Где решается |
|---|---|---|---|
| 1 | Нет контекст-инженерии | длинные задачи теряют нить | платформа/инструменты — **вне стандарта** |
| 2 | Нет tool trust | prompt injection / destructive tools | платформа — **вне стандарта** |
| 3 | Self-Sufficiency абсолютизирован (§4.17) | необратимые действия | Done v6.7 (§4.17 boundary) |
| 4 | Нет аудита действий | невоспроизводимость | платформа — **вне стандарта** |
| 5 | Нет бюджета прогона | перерасход | платформа — **вне стандарта** |
| 6 | Prompt injection покрыт частично | web/tool/RAG/MCP | Done v6.7 (§1.11.8) |
| 7 | Нет OWASP LLM / NIST / ISO 42001 | AI-governance | Done v6.7 (§5.7.10) |
| 8 | Нет model pin | дрейф модели | платформа — **вне стандарта** |
| 9 | Нет качества гейтов | FP/FN | repo-tooling — **вне стандарта** |
| 10 | Нет workflow-vs-agent decision | выбор подхода | **текстовое дерево §0.3** (P2) |
| 11 | Монолит ~236 KB | когнитивная нагрузка | 1-page card (P2), стандарт не сокращать |
| 12 | Нет migration guide | совместимость версий | `MIGRATION.md` (P2) |
| 13 | doc-integrity не в CI | дрейф | repo-only CI (P2) |
| 14 | 64 FAIL-примера на RU | язык | по политике допустимо |

---

## 5. Граница: что текст может и не может

| Текстовый стандарт **может** | Текстовый стандарт **не может** |
|---|---|
| задавать MUST/MUST NOT | исполнять команды |
| требовать артефакт, который агент пишет | вести журнал за агента |
| требовать evidence-файл | контролировать контекст/токены |
| задавать чеклист и FAIL/PASS | замерять стоимость/латентность |
| задавать порядок шагов | принудительно approval-ить действия |
| ссылаться на OWASP/CWE/ISO | проверять tool-output на injection |

**Следствие:** рантайм-контроль (контекст, инструменты, аудит, бюджет,
approval) **в стандарт не добавляется**. Это обязанность платформы/рантайма,
а не текста конституции.

---

## 6. Ограничения

- **Не сокращать стандарт** ради размера. Оптимизация — только точные копии и
  boilerplate с `→ ID`.
- **Не удалять правила** (No-rule-loss).
- **Не добавлять рантайм-законы** (context/tools/audit/budget/approval).
- **Не вводить метрики** в стандарт.
- **Не дублировать §3.2**: имена/счётчики гейтов остаются там; ownership — §3.0.1.

---

## 7. Remaining text-only work

- 1-page PRIME card + task cards (P2).
- `MIGRATION.md` + version policy (P2).
- repo-only CI for `tools/doc_integrity_gate.py` (P2).
- workflow-vs-agent decision tree in §0.3 (P2).
- optional full EN pass over FAIL examples.

---

## 8. Open questions (только текстовые)

- Нужен ли `MIGRATION.md` и 1-page card?
- Где проходит граница «стандарт» vs «платформа», чтобы не размывать оба?

---

*Рабочий документ. Не является вторым SSOT и не переопределяет
`Mawyxx Prime V6.7.md`. При конфликте побеждает стандарт.*
