# MAWYXX PRIME: Enterprise Vibe-Coding Standard (v5.7)

*«Build for Billions. Code for Vibe. Rule with Logic.»*

**Agent contract** — единый нормативный файл для ИИ-кодера.

> **v5.7** — **правда исхода**, не наличие артефактов. Contract Surface **живой** ([A36](#prime-a36--live-surface)) · AC = **оракул** ([A34](#prime-a34--intent-lock)) · no-swallow ([A37](#prime-a37--honest-errors--no-swallow)) · checker не театр ([A38](#prime-a38--checker-integrity)) · **Behavior SSOT** ([A39](#prime-a39--behavior-ssot)) · **Secure Continuum** ([A40](#prime-a40--secure-continuum)) · **Trust Pipeline** ([A41](#prime-a41--trust-pipeline)) · FFI на PRIME ([A16](#prime-a16--secure-by-design)) · coverage там, где OS ([A25](#prime-a25--coverage-absolute)).  
> **Не применять:** зелёный `prime_check` = 10/10 · AC↔имя теста без оракула · порт в yaml без вызова · `#[ignore]` e2e · exclude composition · stub `return GREEN` · copy-paste вместо вызова owner · разрезал файл = DRY · «framework = OWASP закрыт» · «CI secrets ок» · «в чат скинул .env» · `security.md` без gate · `permissions: write-all` · «просто залогинен = authorized» · `update(**body)` · client `user_id` as ownership · token in URL.

### Universal Doctrine — Project Skin · Empire Engine (read first)

> **Форма = проект. Дух = всегда Empire.**  
> Не «как принято в репо, но получше где надо». Не «enterprise только на платежах».  
> **Всегда:** пишешь **на языке и в стиле проекта** — но с дисциплиной Empire: taxonomy с **оракулом**, **живые** порты, **богатый домен**, честный error (не swallow), **один owner на алгоритм**, FFI-дисциплина When unsafe, coverage на I/O/composition, **честные When/N/A**, **минимальный blast**, checker без театра.  
> **Default-secure:** любой вход снаружи = враг, пока schema + authz не сказали иначе. CRUD с id/PATCH — тоже security surface, не «потом A41».

| Принцип | Правило |
|---------|---------|
| **Project Skin** | Стек/папки/naming/test runner/DI/lint/logs **как в репо**; capability-пакеты ([A05a](#prime-a05a--package-cohesion)); формы портов = Pattern Catalog; виды тестов = Engine. |
| **Empire Engine** | Слои · cohesion · **живой** contract surface · **rich domain** · taxonomy с оракулом · anti-N/A · blast · no-swallow · **behavior SSOT** · **secure continuum** (app·CI·chat·ops) · **trust pipeline** (schema→authz→allowlist→safe sink) · FFI When · честный coverage · **checker integrity** — **всегда** для tier. Law без step = ложь. Артефакт без исхода = ложь. |
| **Default-secure** | До кода — 5 вопросов PHASE 1. Любой «да» → [A18](#prime-a18--owasp-input-hygiene)/[A40](#prime-a40--secure-continuum)/[A41](#prime-a41--trust-pipeline) в **этом** PR. Все «нет» → честный `N/A(…)` ([Conflict Matrix](#conflict-matrix-при-сомнении--читать-это-не-конкурирующие-абзацы)). |
| **WHEN** | Триггер включает family (тесты **или** контракты); `N/A` только с reason — иначе FAIL ([A12a](#prime-a12a--test-taxonomy), [A35](#prime-a35--contract-surface)). |
| **Minimal blast** | Минимум файлов/capabilities ([A33](#prime-a33--blast-radius)); качество и порты не режутся. |
| **Никогда** | «потом тесты» · N/A без причины · coverage vanity · AC без оракула · порт без вызова · `let _ =` на I/O · ignored e2e без skipped_steps · exclude composition на greenfield · театральный checker · дубль алгоритма · секрет вне vault/ref · IDOR / mass-assign · «обычный CRUD = без trust pipeline» · учебник `domain/entities`. |

### Conflict Matrix (при сомнении — читать это, не конкурирующие абзацы)

| Tension | Correct | Wrong |
|---------|---------|-------|
| Сомнение в **When-trigger** taxonomy/security | **Включи** family/gate | skip forever / «потом» |
| «Обычный CRUD / не CRITICAL» vs A41 | Default-secure: id/PATCH/body → Trust Pipeline **сейчас** | «security touch только CRITICAL» |
| Сомнение «наплодить порт / test_err_* / SecurityPort» | **Не плоди** ([A35](#prime-a35--contract-surface), [A36](#prime-a36--live-surface)) | unused Port / vanity names |
| YAGNI vs [A39](#prime-a39--behavior-ssot) | N=1 local OK; **N≥2** extract owner | never extract **или** god-util на N=1 |
| YAGNI vs [A40](#prime-a40--secure-continuum) / [A41](#prime-a41--trust-pipeline) | When surface exists → gate **MUST** | «CSRF/IDOR/ci-harden later» |
| [A33](#prime-a33--blast-radius) vs A39/A41 | touch shared owner = **correct** blast | copy-paste to keep blast «small» |
| Skin vs Engine | keep Nest/Rails/Go folders | rewrite to `domain/entities` |
| [A40](#prime-a40--secure-continuum) vs [A41](#prime-a41--trust-pipeline) | A40 = channels (CI/chat/ops); A41 = in-process trust cut | «security = only CI» **или** «only handlers» |

### Anti-N/A (SSOT — один раз)

- **MUST:** `N/A` только с reason = **absent When-trigger** (`N/A(no auth)`, `N/A(no I/O)`, `N/A(no FSM)`…).
- **MUST NOT:** `N/A`, `N/A()`, `N/A(потом)`, `N/A(skip)`, `N/A(одна реализация)`, `N/A(framework DI)`.
- **Enforced by:** `test-taxonomy-gate` · `port-surface-gate`. Details: [A12a](#prime-a12a--test-taxonomy), [A35](#prime-a35--contract-surface). Conflict Matrix above for «при сомнении».

### Spec Law Shape (как писать законы в этом файле)

Каждый `PRIME-A*` / `PRIME-B*`: *why* → **Min tier / When / Enforced by** → Outcome → MUST/MUST NOT → Enough vs too much (When agents cheat) → See. Не дублировать OWASP/Anti-N/A таблицы — ссылка на SSOT. Эталон плотности: [A36](#prime-a36--live-surface)–[A41](#prime-a41--trust-pipeline).

### Agent failure modes (30 секунд — читать до кода)

Типовой самообман ИИ → чем бить:

| Самообман | FAIL / rule |
|-----------|-------------|
| Happy-path only | [A12a](#prime-a12a--test-taxonomy) negative + boundary |
| Flat layer-dump | [A05a](#prime-a05a--package-cohesion) |
| N/A-spam / пустой reason | [Anti-N/A SSOT](#anti-na-ssot--один-раз) · `test-taxonomy-gate` · `port-surface-gate` |
| E2E-only / unit-only при API+DB | Pyramid [A12](#prime-a12--tests--coverage) |
| Coverage vanity | [A25](#prime-a25--coverage-absolute) ≠ taxonomy green |
| «Acceptance понял» / тест только по имени AC | [A34](#prime-a34--intent-lock) behavior-lock — нет оракула |
| Порт в yaml, в `run()` не вызывается | [A36](#prime-a36--live-surface) · `live-surface-gate` |
| `let _ =` / `.ok()` / empty catch на I/O | [A37](#prime-a37--honest-errors--no-swallow) · `no-swallow-gate` |
| `#[ignore]` / `xtest.skip` без skipped_steps | [A12a](#prime-a12a--test-taxonomy) · `ignored-test-gate` |
| exclude composition/adapters + 100% fakes | [A25](#prime-a25--coverage-absolute) · `exclude-honesty-gate` |
| Checker: `return GREEN` / path.exists / `"AC{i}" in text` | [A38](#prime-a38--checker-integrity) · `checker-integrity-gate` |
| unsafe без SAFETY; `safety_profile: false` при FFI | [A16](#prime-a16--secure-by-design) FFI profile · `ffi-safety-gate` |
| Разнёс half-repo | [A33](#prime-a33--blast-radius) |
| Скопировал handler/retry/mapper в новый файл, чтобы не трогать shared | [A39](#prime-a39--behavior-ssot) · [A11](#prime-a11--decomposition) · [A33](#prime-a33--blast-radius) · `behavior-ssot-gate` |
| A11 разрезал god-file на два клона | [A11](#prime-a11--decomposition) fake-split · [A39](#prime-a39--behavior-ssot) |
| Зелёный zta, но `write-all` workflow | [A40](#prime-a40--secure-continuum) · `ci-harden-gate` |
| `.env` / JWT / private key в Cursor/Telegram | [A40](#prime-a40--secure-continuum) · [A19](#prime-a19--supply-chain--secrets) · `channel-secret-gate` |
| Helmet в package.json, middleware не подключён | [A40](#prime-a40--secure-continuum) · `security-headers-gate` · [A36](#prime-a36--live-surface) spirit |
| Authorize скопирован в 12 контроллеров | [A39](#prime-a39--behavior-ssot) · [A02](#prime-a02--zero-trust) · [A40](#prime-a40--secure-continuum) |
| Dockerfile non-root, Helm privileged / open TF | [A23](#prime-a23--infra--docker-security) · `iac-scan-gate` · [A40](#prime-a40--secure-continuum) |
| `security.md` / OWASP checklist без Enforced-by gate | Law→Gate + [A38](#prime-a38--checker-integrity) · [A40](#prime-a40--secure-continuum) |
| ZTA green, но `/orders/{id}` отдаёт чужой заказ (IDOR) | [A41](#prime-a41--trust-pipeline) · [A02](#prime-a02--zero-trust) · `idor-ownership-gate` |
| PATCH принимает `is_admin` / `role` из JSON | [A41](#prime-a41--trust-pipeline) · `mass-assign-gate` |
| `filename` = user input → `open(path)` | [A41](#prime-a41--trust-pipeline) · `path-escape-gate` |
| JWT в query + `console.log(token)` | [A41](#prime-a41--trust-pipeline) · [A19](#prime-a19--supply-chain--secrets) · `session-token-gate` |
| Authz после `charge()` / `delete()` | [A41](#prime-a41--trust-pipeline) · `trust-pipeline-gate` |
| Law в спеке, step-заглушка **или** existence-only step | Law→Gate + [A38](#prime-a38--checker-integrity) |
| Evidence без families | [A26](#prime-a26--evidence-block) |
| Concrete infra в UC / нет `contract_surface_map` | [A35](#prime-a35--contract-surface) · `port-surface-gate` |
| «Одна реализация → без порта» при I/O | [A35](#prime-a35--contract-surface) · [A06](#prime-a06--di--ports) |
| Mock concrete вместо Fake на Port | [A35](#prime-a35--contract-surface) · `port-test-double-gate` |
| Wiring concrete вне composition root | [A35](#prime-a35--contract-surface) · `composition-root-gate` |
| `user.status = 'active'` / публичный сеттер без инварианта | [A05](#prime-a05--layer-law) Anti-Anemic · [B06](#prime-b06--fsm) · `anemic-mutation-gate` |
| try/catch на каждые две строки; глотать DB-down в UC | [A10](#prime-a10--result) expected vs unexpected |
| «Идеальное дерево» `domain/entities` вместо Skin репо | [A01](#prime-a01--context--risk-tier) · [A05a](#prime-a05a--package-cohesion) · Pattern Catalog |

### Checker = 100% работа агента (не пользователя)

На ≥PRIME человек **не** настраивает checker. Агент создаёт `scripts/prime_check/` + ~50 steps + yaml + CI + deps, гоняет `--only`/`--diff`/FULL, чинит код **и** checker до `exit 0`. Нет checker → STOP фичу → [AGENT-5](#agent-5--prime-check) bootstrap → green → потом задача.

**Цель:** правда исхода — A34–A41 + cohesion + rich domain + честный coverage. Не зелёные имена · не ISO ради таблиц · не копии вместо owner · не «безопасный код + дырявый CI» · не «залогинен ⇒ любой id».

**Applicability keywords (RFC 2119 + WHEN):**

| Keyword | Meaning |
|---------|---------|
| **Always** | Любой tier, любой стек |
| **STANDARD+** / **PRIME+** / **CRITICAL** | Tier floor |
| **When \<trigger\>** | Только если условие в задаче/дизайне |
| **Stack-native** | Реализация = конвенция проекта; gate проверяет outcome |

**Сквозные инварианты (outcomes — вшиты в правила, не отдельный модуль):**

| Invariant | Outcome | Where | When | Gate |
|-----------|---------|-------|------|------|
| **Explicit errors** | Нет silent `null`/`None` как «ошибка» в core logic | [A10](#prime-a10--result) | PRIME+ core/UC | `anti-null-gate` |
| **Immutability** | Нет in-place mutation shared/concurrent state | [A05](#prime-a05--layer-law) · [B06](#prime-b06--fsm) | When races / FSM / shared aggregate | `immutability-gate` |
| **Injectable nondeterminism** | time/ID/random тестируемы | [A06](#prime-a06--di--ports) · [A15](#prime-a15--deterministic-time) | PRIME+ testable core | `deterministic-runtime` |
| **Idempotent mutations** | Повтор = тот же эффект, не дубль | [A14](#prime-a14--idempotency) | When state-changing + retry risk | `idempotency-matrix-gate` |
| **Module isolation** | Нет импорта чужих **private** domain types | [A04](#prime-a04--integration--plugin-boundaries) | When multi-module / service split | `context-leak-gate` |
| **Package cohesion** | Код одного capability рядом (slice / feature package); нет flat layer-dump | [A05a](#prime-a05a--package-cohesion) · [A05](#prime-a05--layer-law) | STANDARD+ · When ≥2 capabilities / growing domain | `package-cohesion-gate` (soft) |
| **Test taxonomy** | Применимые виды тестов написаны; **N/A только с валидным reason** | [A12a](#prime-a12a--test-taxonomy) · [A12](#prime-a12--tests--coverage) | STANDARD+; full matrix PRIME+ | `test-taxonomy-gate` · matrix gates |
| **Behavior lock** | Каждый AC несёт **оракул** — наблюдаемый факт; тест обязан его сломать, если поведение соврало | [A34](#prime-a34--intent-lock) | PRIME+ features | `intent-lock-gate` (oracle, не substring) |
| **Live surface** | Объявленный порт/поле **вызывается**; identity/todo impl = FAIL | [A36](#prime-a36--live-surface) | PRIME+ · When ports/DTO/settings | `live-surface-gate` |
| **No swallow** | Result на границе процесса mapped или ADR; dump-bucket Err запрещён | [A37](#prime-a37--honest-errors--no-swallow) | PRIME+ | `no-swallow-gate` · `err-variant-gate` (provoke path) |
| **Checker integrity** | Step не existence-only, не безусловный GREEN, не `"AC{i}" in text` | [A38](#prime-a38--checker-integrity) | PRIME+ | `checker-integrity-gate` |
| **Behavior SSOT** | Политика/алгоритм имеет **одного owner** в `runtime_scope`; остальные CALL, не копируют | [A39](#prime-a39--behavior-ssot) · [A08](#prime-a08--anti-fork--policy-facades) | PRIME+ · When N≥2 copies (body above threshold) | `behavior-ssot-gate` · `anti-fork-gate` |
| **Secure Continuum** | Секрет/trust не живут вне vault+allowlist на **всех** каналах (app · CI · chat · ops); контроль = gate, не `security.md` | [A40](#prime-a40--secure-continuum) · [A16](#prime-a16--secure-by-design) · [A19](#prime-a19--supply-chain--secrets) | PRIME+ · When network/auth/PII/deploy/CI | `ci-harden-gate` · `channel-secret-gate` · `security-headers-gate` · `cors-csrf-gate` · `iac-scan-gate` |
| **Trust Pipeline** | На protected op trust режется в порядке schema→authn→authz(resource)→allowlisted command→UC→safe sink; attack class = gate+oracle | [A41](#prime-a41--trust-pipeline) · [A02](#prime-a02--zero-trust) · [A39](#prime-a39--behavior-ssot) | PRIME+ · When exposed op / auth / multi-user / upload | `trust-pipeline-gate` · `idor-ownership-gate` · `mass-assign-gate` · `path-escape-gate` · `session-token-gate` |
| **Blast radius** | Минимум файлов/capabilities на фичу | [A33](#prime-a33--blast-radius) | STANDARD+ | soft `blast-radius-gate` + DoD |
| **Contract surface** | Core/app зависит только от контрактов; concrete в adapters / composition root | [A35](#prime-a35--contract-surface) · [A06](#prime-a06--di--ports) · [A04](#prime-a04--integration--plugin-boundaries) | PRIME+ · When I/O / boundary / multi-entry | `port-surface-gate` · `composition-root-gate` · `port-test-double-gate` |
| **Rich domain** | Lifecycle/status меняет **метод сущности** с инвариантом; не публичный сеттер / field assign | [A05](#prime-a05--layer-law) · [B06](#prime-b06--fsm) | When entity has status/lifecycle | `anemic-mutation-gate` · `fsm-transition-gate` |
| **Expected vs unexpected errors** | Бизнес-отказ = named Err/Result в core; infra-сбой = adapter + presentation handler — не try/catch-лес в UC | [A10](#prime-a10--result) | PRIME+ | `err-variant-gate` · `no-transport-in-domain` |
| **Observable failures** | trace + invariant_id + safe context; **assert в тестах** | [A10](#prime-a10--result) · [B03](#prime-b03--sre--observability--events) · [A12a](#prime-a12a--test-taxonomy) | PRIME+ | `error-context-gate` |

### Quality Constellation — ISO · CISQ · OWASP · CERT (constitutional layer)

**Empire Engine** — не «наш внутренний чеклист». Это **операционализация** международных стандартов качества и безопасного кодинга: измеримые outcomes + machine gates, не PDF на полке.

| Standard | Role in PRIME | How enforced |
|----------|---------------|--------------|
| **ISO/IEC 25010** | Модель качества ПО — 9 характеристик | Каждая → правила Part A/B + gates (таблица ниже) |
| **ISO/IEC 5055** (CISQ) | Автоизмерение **структурных** дефектов в исходниках | **AST Prosecutor** + static steps — 4 столпа CISQ |
| **OWASP Top 10 · ASVS** | Веб-безопасность и verification levels | [A18](#prime-a18--owasp-input-hygiene) · [A02](#prime-a02--zero-trust) · security steps |
| **SEI CERT** | Безопасный системный код (C/C++/Java…) | Forbidden constructs · concurrency · memory safety **When** native/unsafe stack |
| **MISRA C/C++** | Safety-critical предсказуемость | **CRITICAL** / embedded profile — запрет UB-конструкций, динамики без ADR |

**Agent rule:** не цитируй стандарт «для галочки». Каждый MUST в PRIME = **конкретный** gate или test matrix. Нет gate → агент пишет step при bootstrap ([AGENT-5](#agent-5--prime-check)).

#### ISO/IEC 25010 → PRIME mapping (9 characteristics)

| ISO 25010 | Sub-characteristic (examples) | PRIME rules | Gates / evidence |
|-----------|------------------------------|-------------|------------------|
| **Functional suitability** | completeness, correctness | [A07](#prime-a07--design-first) · [A12](#prime-a12--tests--coverage) · [A12a](#prime-a12a--test-taxonomy) · [A24](#prime-a24--tdd-lock) | `test-matrix-gate` · `test-taxonomy-gate` · `route-matrix-gate` · `err-variant-gate` · scenario/acceptance |
| **Performance efficiency** | time behaviour, resource use | [B10](#prime-b10--performance) | perf budget ADR · load smoke When SLA |
| **Compatibility** | coexistence, interoperability | [A21](#prime-a21--semver--contracts) · [B05](#prime-b05--inter-service-contracts) | `api-contract-drift` · `snapshot-contract` · contract tests |
| **Usability** | learnability, operability (UI) | [B11](#prime-b11--client-apps) | `frontend-quality` · E2E/scenario When UI |
| **Reliability** | maturity, availability, fault tolerance, recoverability | [A12](#prime-a12--tests--coverage) · [A12a](#prime-a12a--test-taxonomy) · [A25](#prime-a25--coverage-absolute) · [B04](#prime-b04--resilience) · [A14](#prime-a14--idempotency) | 100% coverage · path/boundary · mutation · property · negative · idempotency |
| **Security** | confidentiality, integrity, non-repudiation, accountability | [A02](#prime-a02--zero-trust) · [A16](#prime-a16--secure-by-design) · [A18](#prime-a18--owasp-input-hygiene) · [A19](#prime-a19--supply-chain) · [A29](#prime-a29--zta-matrix) · [A40](#prime-a40--secure-continuum) · [A41](#prime-a41--trust-pipeline) · [A12a](#prime-a12a--test-taxonomy) | `zta-matrix-gate` · `idor-ownership-gate` · `trust-pipeline-gate` · `mass-assign-gate` · `injection-fuzz` · continuum gates · `gitleaks-history` · `dependency-audit` |
| **Maintainability** | modularity, reusability, analysability, modifiability, testability | [A05](#prime-a05--layer-law) · [A05a](#prime-a05a--package-cohesion) · [A35](#prime-a35--contract-surface) · [A11](#prime-a11--decomposition) · [A17](#prime-a17--clean-code) · [A39](#prime-a39--behavior-ssot) · [B09](#prime-b09--adr) | **7 AST gates** · `package-cohesion-gate` · `port-surface-gate` · `anemic-mutation-gate` · `cyclomatic-gate` · `anti-fork-gate` · `behavior-ssot-gate` · ADR |
| **Portability** | adaptability, installability | stack adapters · [A32](#prime-a32--monorepo-scope) | `stack-detect` · per-path tier |
| **Operational** (25010 ops view) | deploy, monitor, restore | [B13](#prime-b13--ops--runbook) · [B03](#prime-b03--sre--observability--events) | `health-gate` · `prod-config` · trace_id |

#### ISO/IEC 5055 (CISQ) — 4 pillars → AST Prosecutor

AST Prosecutor = локальный CISQ-аналог (агент пишет сам).

| CISQ pillar | Structural defects (examples) | PRIME enforcement |
|-------------|------------------------------|-------------------|
| **Reliability** | unhandled paths, complexity hotspots, nondeterminism in core | `anti-null-gate` · `deterministic-runtime` · `err-variant-gate` · `cyclomatic-gate` |
| **Security** | injection sinks, hardcoded secrets, weak crypto, CI privilege, open CORS, IDOR, mass-assign | `no-string-sql` · `gitleaks-history` · `bandit` · `no-debug-bypass` · continuum gates · `idor-ownership-gate` · `mass-assign-gate` · `trust-pipeline-gate` |
| **Performance efficiency** | algorithmic hotspots, resource leaks in hot path | `cyclomatic-gate` · `dead-code-gate` · [B10](#prime-b10--performance) budgets |
| **Maintainability** | coupling, god files, duplicate policy, layer violations, flat dumps, concrete-in-core, anemic status writes, algorithm clones | **7 AST gates** · `import-graph-gate` · `package-cohesion-gate` · `port-surface-gate` · `anemic-mutation-gate` · `anti-fork-gate` · `behavior-ssot-gate` · `file-size-guard` |

**MUST:** architecture steps в `prime_check` документируют в step header: `cisq_pillar: Reliability|Security|…` — для traceability в отчёте.

#### OWASP Top 10 · ASVS → tier-scaled verification

**SSOT closure table:** [A18](#prime-a18--owasp-input-hygiene) (не дублировать здесь).  
**Channels / in-process:** [A40](#prime-a40--secure-continuum) · [A41](#prime-a41--trust-pipeline).

**OWASP ASVS** depth by tier:

| Tier | ASVS target | Agent MUST |
|------|-------------|------------|
| **LITE** | hygiene — no secrets, validate input | [A16](#prime-a16--secure-by-design) basics |
| **STANDARD** | V1 + V2 partial | boundary validation · no secrets |
| **PRIME+** | V1–V4 for exposed web/API | Threat Model mini · ZTA + Trust Pipeline · injection fuzz · continuum When CI |
| **CRITICAL** | all applicable chapters | Threat Model full · `mutation-critical` · `injection-fuzz` |

#### SEI CERT · MISRA — native / FFI profile (PRIME+ When FFI — не только CRITICAL)

**When** в `src` есть FFI: Rust `unsafe` · JNI · ctypes/`cffi` · Win32/GDI · raw pointers · C/C++ · embedded.  
**MUST** на этом When включить `ffi_profile: true` (и `safety_profile: true` на CRITICAL / embedded).  
**FAIL:** `safety_profile: false` **и** `ffi_profile: false` при `unsafe`/JNI/ctypes/Win32 в src.

**CRITICAL** / avionics/automotive/medical — полный MISRA denylist дополнительно.

| Family | CERT / MISRA intent | PRIME rule |
|--------|---------------------|------------|
| **Memory safety** | no unchecked buffer arithmetic; no use-after-free | каждый `unsafe` / FFI блок — `// SAFETY:` с инвариантом; native handle = RAII/Drop; raw ptr в TLS только рядом с documented owner |
| **Concurrency** | no data races; defined locking order | [A05](#prime-a05--layer-law) immutability · `immutability-gate` · FSM atomic transitions [B06](#prime-b06--fsm) |
| **Predictability** | no undefined behaviour; bounded execution | `deterministic-runtime` · no `eval`/`exec` · no unbounded recursion without ADR |
| **Forbidden language subset** | MISRA banned constructs | extend `forbidden_patterns` in config: `goto`, `setjmp`, unchecked casts, VLAs (C) |
| **Dynamic allocation** | minimize heap in hot/safety path | **SHOULD:** arena/pool patterns; heap in ISR/real-time loop → ADR + review |

**When** safety profile: wire `clang-tidy` / `cppcheck` / `clippy` / MISRA denylist.

### ZERO-TOLERANCE doctrine (tier ≥ PRIME)

Gates ниже — **outcome checks**. Шаг `N/A` только с ADR, если триггер не применим (нет Docker, нет FSM в design artifact, LITE script…).

| Запрет | Enforcement | Applicability |
|--------|-------------|---------------|
| Непокрытая строка в `runtime_scope` / diff | `coverage-line-100` → exit 1 | PRIME+ |
| Непокрытая ветка (branch) | `coverage-branch-100` → exit 1 | PRIME+ |
| Coverage упал vs `main` | `coverage-ratchet` → exit 1 | PRIME+ |
| `# pragma: no cover` без ADR | `no-pragma-no-cover` → exit 1 | PRIME+ |
| Пустой / trivial test | `no-empty-test` → exit 1 | PRIME+ |
| Непротестированный error variant | `err-variant-gate` → exit 1 | PRIME+ |
| Exposed operation без contract-тестов | `route-matrix-gate` → exit 1 | PRIME+ · When API/CLI/RPC surface |
| Protected operation без auth matrix | `zta-matrix-gate` → exit 1 | PRIME+ · When auth |
| Применимый вид теста из taxonomy отсутствует | `test-taxonomy-gate` → exit 1 | PRIME+ · [A12a](#prime-a12a--test-taxonomy) |
| `N/A` без trigger-reason / «потом» | `test-taxonomy-gate` → exit 1 | PRIME+ · Anti-N/A |
| AC без оракула / тест только по имени | `intent-lock-gate` → exit 1 | PRIME+ · [A34](#prime-a34--intent-lock) |
| Порт/поле объявлены, не живут | `live-surface-gate` → exit 1 | PRIME+ · [A36](#prime-a36--live-surface) |
| Swallowed Result на I/O границе | `no-swallow-gate` → exit 1 | PRIME+ · [A37](#prime-a37--honest-errors--no-swallow) |
| `#[ignore]` / skip без per-test skipped_steps | `ignored-test-gate` → exit 1 | PRIME+ |
| exclude composition/I/O adapters (greenfield) | `exclude-honesty-gate` → exit 1 | PRIME+ greenfield · [A25](#prime-a25--coverage-absolute) |
| Checker step = existence / `return GREEN` | `checker-integrity-gate` → exit 1 | PRIME+ · [A38](#prime-a38--checker-integrity) |
| Дубль одного алгоритма/политики в ≥2 местах без единого owner | `behavior-ssot-gate` → exit 1 | PRIME+ · body above threshold ([A39](#prime-a39--behavior-ssot)) |
| Secret / long-lived cloud key in CI with fork-PR trust · `write-all` | `ci-harden-gate` → exit 1 | PRIME+ · When CI ([A40](#prime-a40--secure-continuum)) |
| Open CORS+credentials или missing CSRF When cookie session | `cors-csrf-gate` → exit 1 | When browser-facing ([A40](#prime-a40--secure-continuum)) |
| Raw secret in evidence / chat handoff | `channel-secret-gate` → exit 1 · agent refuse | Always ([A40](#prime-a40--secure-continuum)) |
| Security checklist / ADR without Enforced-by gate | Law→Gate + [A38](#prime-a38--checker-integrity) | PRIME+ · [A40](#prime-a40--secure-continuum) |
| Client-supplied owner/tenant id trusted for access | `idor-ownership-gate` → exit 1 | multi-user ([A41](#prime-a41--trust-pipeline)) |
| Full request bag bound onto entity | `mass-assign-gate` → exit 1 | patch/create ([A41](#prime-a41--trust-pipeline)) |
| User path without root jail | `path-escape-gate` → exit 1 | uploads ([A41](#prime-a41--trust-pipeline)) |
| Token in query/logs or homemade crypto | `session-token-gate` → exit 1 | token auth ([A41](#prime-a41--trust-pipeline)) |
| Mutation before authz / raw body in UC | `trust-pipeline-gate` → exit 1 | protected ops ([A41](#prime-a41--trust-pipeline)) |
| unsafe без `// SAFETY:` / native handle без Drop | `ffi-safety-gate` → exit 1 | When FFI in src · [A16](#prime-a16--secure-by-design) |
| Happy-path-only (нет negative/boundary) | `negative-path-gate` / `boundary-value-gate` → exit 1 | PRIME+ · When validators / state-changing |
| Evidence без taxonomy APPLIED\|N/A list | `evidence-block` → invalid | PRIME+ · [A26](#prime-a26--evidence-block) |
| Secret в repo / history / логах | `gitleaks-history` → exit 1 | Always (network tier+) |
| Core logic импортирует I/O layer | `import-graph-gate` → exit 1 | PRIME+ · When layered/monolith |
| Flat layer-dump при ≥2 capabilities | `package-cohesion-gate` → WARN→FAIL per config | STANDARD+ · When growing domain ([A05a](#prime-a05a--package-cohesion)) |
| `Date.now` / `uuid4` в testable core | `deterministic-runtime` → exit 1 | PRIME+ · When testable core exists |
| Silent null как failure path | `anti-null-gate` → exit 1 | PRIME+ core |
| In-place mutation shared state | `immutability-gate` → exit 1 | When FSM / concurrent aggregate |
| Публичный assign/setter статуса вне метода сущности | `anemic-mutation-gate` → exit 1 | When lifecycle/status entity ([A05](#prime-a05--layer-law), [B06](#prime-b06--fsm)) |
| Double-apply мутации | `idempotency-matrix-gate` → exit 1 | When state-changing + retry risk |
| Cross-module private type leak | `context-leak-gate` → exit 1 | When multi-module |
| Concrete infra type в signature / deps testable core | `port-surface-gate` → exit 1 | PRIME+ · When I/O in core/app ([A35](#prime-a35--contract-surface)) |
| `new ConcreteAdapter` вне composition root | `composition-root-gate` → exit 1 | PRIME+ · [A35](#prime-a35--contract-surface) |
| Outbound port без Fake/InMemory (или ADR) | `port-test-double-gate` → exit 1 | PRIME+ · When outbound port |
| `N/A(одна реализация)` / `N/A(потом)` на outbound при I/O | `port-surface-gate` → exit 1 | PRIME+ · Anti-N/A contracts |
| Failure без observable context | `error-context-gate` → exit 1 | PRIME+ |
| Catch-all в UC, глотающий infra как Ok | `err-variant-gate` + [A10](#prime-a10--result) expected vs unexpected → FAIL / B08 | PRIME+ |
| Небезопасный Docker/compose | `docker-security` → exit 1 | When containerized |
| CVE в dependencies (high/critical) | `dependency-audit` → exit 1 | Always (deps) |
| «Готово» без evidence block | `evidence-block` → invalid response | PRIME+ |
| Merge без quality gate green | **запрещён** | PRIME+ |

**Нет «норм сойдёт».** `99.99%` = `0%`. Tier ≥ PRIME = **чинить до green**, не сдавать задачу.

### FIX-UNTIL-GREEN (главный закон агента)

- **MUST:** `prime_check` red → **чинить код/тесты → re-run** → повторять до `exit 0`.
- **MUST NOT:** останавливаться с красным gate и говорить «готово» / «не получилось» / «запустите сами».
- **MUST NOT:** бросать задачу пользователю с exit ≠ 0 — **ты** доводишь до green.
- **MUST NOT:** переключаться на другую фичу, пока текущая не green (кроме bootstrap `prime_check` по AGENT-5).
- **Stop-the-line** = не **наращивать** сломанный фундамент новым кодом; **не** = «бросить и уйти». Сломано → чини → green → продолжай.

**Empire wins** over «сойдёт для этого проекта». Нет checker → [AGENT-5](#agent-5--prime-check). Red → fix until green + evidence.

---

## AGENT-OMEGA — Execution phases (before any code)

**MUST** выполнить фазы **в порядке** на tier ≥ PRIME. На LITE/STANDARD — **SHOULD** checklist (пропуск с обоснованием в ответе).

### PHASE 0 — LOCK

```text
assign tier → tier ≥ PRIME?
  → quality gate exists + config + CI? NO → STOP all feature work
      → agent bootstraps FULL checker (AGENT-5): scaffold, ~50 steps, yaml, CI, deps
      → agent runs FULL → green (or legacy ratchet ADR) → ONLY THEN feature
  → adoption_mode? greenfield | legacy (A31) — agent sets in config
  → stack? agent detects → picks adapter → wires tools in checker
```

### PHASE 1 — DESIGN ARTIFACT (в ответе до кода)

**Default-secure (MUST до кода — ответить явно):**

```text
1. untrusted input? (HTTP/CLI/WS/file/upload/webhook)     → yes | N/A(no I/O)
2. principal / session / token?                           → yes | N/A(no auth)
3. resource id / multi-user / tenant / чужой id?          → yes | N/A(single-user)
4. client body / PATCH / privileged fields?               → yes | N/A(no write body)
5. secret · cookie · CI · HTML · path/upload?             → list | N/A(none)
Any YES → fill trust_pipeline_map + secure_continuum_map this PR; enable matching A18/A40/A41 gates.
All N/A → keep reasons; do NOT silently skip. «CRUD ≠ security» = FAIL reading.
```

```text
tier + triggers: [STANDARD | PRIME — why]
default_secure: [answers 1–5 above]
stack + existing_patterns: [detected — MVC | hexagonal | FP | framework-native]
capability_slices: [orders | billing | auth | …]   # package map — [A05a](#prime-a05a--package-cohesion)
package_form: [mirrored_slices | feature_packages | Nx_lib | Nest_module | …]
files_to_touch: [...]
new_error_variants: [...]
new_operations: [HTTP route | RPC method | GraphQL field | CLI cmd → statuses/outcomes]
fsm_transitions: [...]                    # only When entity has status
acceptance_criteria:                  # [A34](#prime-a34--intent-lock) — каждый AC = id + statement + oracle
  - id: AC1
    statement: "process does not create a visible overlapped window"
    oracle: { kind: hwnd|pixels|fs|order|error_id|toast|state, assert: "FakeOverlay.shown==false until hotkey" }
    test: test_ac1_no_visible_window
  # empty on PRIME+ feature → STOP; имя теста без oracle = FAIL
blast_radius: [capabilities…, files…]     # minimal set — [A33](#prime-a33--blast-radius)
test_matrix: behavior × input × expected outcome
test_taxonomy_map:                        # [A12a](#prime-a12a--test-taxonomy) — N/A MUST cite When-trigger absent
  unit: [test names…]
  integration: […] | N/A(no I/O)
  e2e_or_contract: […] | N/A(no UI / no exposed op)
  regression: […] | N/A(no bug fix)
  mutation: APPLIED on critical_scope (PRIME greenfield MUST) | N/A(legacy & mutation ADR)
  skipped_steps: [{step, test, trigger, adr, sunset}]   # one skip = one trigger; NEVER one ADR for 15 N/A
  property: […] | N/A(no pure invariant)
  injection: […] | N/A(no untrusted input)
  access_control: […] | N/A(no auth)
  contract: […] | N/A(no API surface)
  scenario: […] | N/A(single-step)
  bdd_acceptance: [GWT ↔ each AC]
  path_boundary: […]
  state_transition: […] | N/A(no FSM)
  negative: […]
  observability: […] | N/A(no new Err/log path)   # assert log/trace fields
  fuzz_logic: […] | N/A
contract_surface_map:                     # [A35](#prime-a35--contract-surface) — N/A MUST cite absent When
  outbound_ports: [IOrderRepo, IClock, …] | N/A(no I/O)
  inbound_ports:  […] | N/A(single HTTP entry)
  dto_acl:        […] | N/A(single capability)
  api_contracts:  […] | N/A(no exposed op)
  event_contracts:[…] | N/A(no events)
  strategies:     […] | N/A(no swap)
  composition_root: [main.py | app.module.ts | …]
behavior_owners:                      # [A39](#prime-a39--behavior-ssot) — empty OK if no repeated behavior yet
  - id: money-round | retry-http | authorize | …   # When second copy appears → MUST fill this session
    owner: path::symbol
    callers: [...]
secure_continuum_map:                 # [A40](#prime-a40--secure-continuum) — Anti-N/A on absent surfaces
  surfaces: [http, ci, iac, chat] | subset
  threat_channels: […]                # MUST include ci/chat When those channels exist
  header_policy: APPLIED | N/A(reason)
  cors_csrf: APPLIED | N/A(reason)
  ci_permissions_owner: path::workflow | N/A(no CI)
  authz_owner: path::symbol | N/A(no auth)   # A39 link
trust_pipeline_map:                   # [A41](#prime-a41--trust-pipeline) — Anti-N/A on absent surfaces
  ops: [{id, pipeline: schema>authn>authz>command>uc, authz_owner, command_type}] | N/A(no protected op)
  idor_cases: [{op, victim_resource, oracle_test}] | N/A(single-user)
  privileged_fields_stripped: [role, is_admin, balance, …]
  session_model: cookie | bearer | mtls | N/A
```

### PHASE 2 — TDD-LOCK ([A24](#prime-a24--tdd-lock) · [A12a](#prime-a12a--test-taxonomy))

Failing tests first (greenfield); same PR (legacy). Каждая applicable family / AC — named test или `N/A(reason)`. No happy-path-only.

### PHASE 3 — IMPLEMENT

Минимальный scope на фичу; максимальный на качество. Ports/contracts before adapters ([A35](#prime-a35--contract-surface), [A07](#prime-a07--design-first)). Status/lifecycle → entity methods, not field-assign ([A05](#prime-a05--layer-law)). Existing behavior → **call owner**, do not clone ([A39](#prime-a39--behavior-ssot)).

### PHASE 4 — VERIFY LOOP · FIX UNTIL GREEN ([AGENT-VERIFY](#agent-verify--you-run-prime_check))

```text
edit → prime_check --only <step> → RED → FIX → re-run → … → GREEN
all touched → prime_check --diff → RED → FIX → re-run → … → GREEN
session end → prime_check FULL → RED → FIX → re-run → … → exit 0  (mandatory)
print PRIME-VERIFY-EVIDENCE block ([A26](#prime-a26--evidence-block))
```

**Нет легального выхода с exit ≠ 0.** Агент **не останавливает задачу** — итерирует fix → re-run до green.

### Forbidden phrases (MUST NOT в ответе)

«~99%» · «запустите тесты» · «checker потом» · «установите pytest» · «edge без теста» · «тесты в другом PR» · «хватит unit» · «happy path достаточно» · «E2E/негатив потом» · naked `N/A` · «acceptance в голове» · «потрогал соседние на всякий» · «не могу починить / оставим красным» · «перепишу под domain/entities» · «скопировал чтобы не трогать shared» · «разрезал файл = DRY».

### 3-strike rule ([A30](#prime-a30--anti-slack))

Один step падает **3 раза** с **тем же патчем** → redesign + ADR → continue fix loop. Не бросать задачу.

---

## AGENT-0 — Boot (read first)

Skin + Engine. До кода: tier ([A01](#prime-a01--context--risk-tier)) · **Default-secure 5Q** · [Conflict Matrix](#conflict-matrix-при-сомнении--читать-это-не-конкурирующие-абзацы) · [failure modes](#agent-failure-modes-30-секунд--читать-до-кода) · OMEGA 0–4.

- **MUST:** родной синтаксис; slices ([A05a](#prime-a05a--package-cohesion)); maps + AC + blast ([A12a](#prime-a12a--test-taxonomy), [A35](#prime-a35--contract-surface), [A34](#prime-a34--intent-lock), [A33](#prime-a33--blast-radius)).
- **MUST:** Default-secure 5Q в PHASE 1. Любой YES на untrusted/auth/id/PATCH/secret → [A18](#prime-a18--owasp-input-hygiene)/[A40](#prime-a40--secure-continuum)/[A41](#prime-a41--trust-pipeline) **в этом PR** (не «security потом»).
- **MUST:** нет/битый checker на PRIME+ → bootstrap [AGENT-5](#agent-5--prime-check) → green → потом фича.
- **MUST:** `--only` после edit; перед done — `--diff` + FULL + evidence ([A26](#prime-a26--evidence-block)).
- **MUST NOT:** happy-path / N/A-spam / concrete I/O в core / «запусти тесты» / done при exit ≠ 0 / «обычный CRUD без trust pipeline».
- Red → fix-until-green ([A30](#prime-a30--anti-slack)). No new feature on red.

**Не применять (кратко):** pure-fn Port · CQRS на 3 поля · учебник `domain/entities` · port в yaml без вызова · AC-имя без оракула · coverage без taxonomy · Helmet-in-package.json · `.env` в чат · `write-all` · IDOR «просто залогинен» · `update(**body)` · «не CRITICAL → без A41». Полный список самообмана → failure modes; «при сомнении» → **Conflict Matrix**.

**Global FORBIDDEN (Engine):** concrete I/O в core · policy в adapters · clone auth/validate/algorithm · trust localhost/CI/chat as auth · nondeterminism в core · secrets в repo/evidence/chat · string SQL · DDL вне migrations · `write-all` CI · flat dump ≥2 caps · swallow I/O Result · skip без `skipped_steps` · `eval`/unsanitized HTML · tokens in `localStorage` без ADR · debug auth bypass. See [A02](#prime-a02--zero-trust)·[A08](#prime-a08--anti-fork--policy-facades)·[A15](#prime-a15--deterministic-time)–[A20](#prime-a20--migrations)·[A35](#prime-a35--contract-surface)–[A41](#prime-a41--trust-pipeline).

---

## AGENT-1 — Task router

| Task | Tier | PRIME sections | After code, **you** run |
|------|------|----------------|-------------------------|
| **No prime_check in repo** | ≥PRIME | AGENT-5, A22 | **WRITE prime_check first** → full green |
| Legacy repo bootstrap | ≥PRIME | A31, AGENT-5 | `adoption_mode: legacy` + diff gates |
| Monorepo path | varies | A32 | per-path tier in config |
| Any runtime code change | ≥PRIME | A01–A41 (+ Default-secure 5Q); When I/O/auth/id/PATCH → **A18/A40/A41** | `prime_check --diff` then **full** |
| New/changed exposed operation (HTTP/gRPC/GraphQL/CLI) | ≥PRIME | A02, A03, A18, A29, A12a, **A41**, **A40** When web | `route-matrix-gate` + `zta-matrix-gate` + `trust-pipeline-gate` + contract/negative |
| New feature / provider | ≥PRIME | A04–A07, **A05a**, **A12a**, **A35**, **A39**, **A40**, **A41**, A12, A24 | TDD → ports + taxonomy → Fake → adapter → full; **call owners**; Default-secure then continuum/pipeline |
| Auth / session | ≥PRIME | A02, A16, A29, A12a, A35, **A39**, **A40**, **A41** | `zta-matrix-gate` + `idor-ownership-gate` + one authorize owner + session-token |
| Security / OWASP surface | ≥PRIME | A16, A18, A02, A29, A12a, **A40**, **A41** | injection + access_control + trust pipeline + continuum |
| CRUD / resource id / PATCH body (даже «простая фича») | ≥PRIME | **A41**, A02, A18, A12a | schema→authz→allowlist; IDOR oracle When multi-user; `mass-assign-gate` |
| Docker / compose / deploy | ≥PRIME | A16, A23, **A40** | `docker-security` + `prod-config` + `ci-harden` / `iac-scan` When present |
| DB schema / persistence | ≥PRIME | A20, B06, A12a | integration + boundary + negative + `schema-drift` |
| New dependency | any | A19 | `dependency-audit` + lockfile |
| Idempotency / retries | ≥PRIME | A14, A09, A12a | integration + contract + negative + double-submit |
| Stateful entity (status) — When in design artifact | ≥PRIME | A05, B06, A14, A12a | `anemic-mutation-gate` + `fsm-transition-gate` + state_transition family |
| Client UI | ≥PRIME | B11, A18, A12a, **A40** | E2E/scenario + unit + `frontend-quality` + headers/CORS When browser |
| Financial / compliance | CRITICAL | All + B09 + A12a | full + mutation + property + injection-fuzz |
| Safety-critical (C/C++/embedded) | CRITICAL | A16, A15, B06 + CERT/MISRA profile | `clang-tidy`/`cppcheck`/`clippy` + immutability + forbidden_patterns |
| Ops / deploy / health | ≥PRIME | B13, A23, **A40** | `health-gate` + `prod-config` + rotate/revoke on leak |
| Script only (no network) | LITE | B07 | smoke only — no prime_check required |

---

## AGENT-2 — Pre-commit checklist (merge gate)

*Полный DoD = [A13](#prime-a13--definition-of-done). Здесь — core ≤25.*

```text
[ ] OMEGA 0–4 + Default-secure 5Q + design maps (taxonomy · contracts · behavior_owners · secure_continuum · trust_pipeline · AC · blast)
[ ] prime_check exists (bootstrap AGENT-5 if missing); adoption_mode set
[ ] Anti-N/A ([SSOT](#anti-na-ssot--один-раз)); [Conflict Matrix](#conflict-matrix-при-сомнении--читать-это-не-конкурирующие-абзацы)
[ ] A34 oracles · A36 live ports · A37 no-swallow · A38 checker integrity
[ ] A39 no clone / owner · A40 continuum GREEN|N/A · A41 trust pipeline GREEN|N/A (+ IDOR When multi-user)
[ ] A35 ports + Fake + composition root · A05/A05a rich domain + cohesion
[ ] A12a applicable families · coverage-diff-100 + ratchet · err-variant / zta / route When triggered
[ ] A19 secrets + audit · continuum CI/headers When triggered · A23 docker When touched
[ ] `prime_check --diff` then FULL → exit 0 · evidence (A26) · CI ≡ local
[ ] Threat Model When CRITICAL **or** any Default-secure YES (incl. CI/chat When present)
```

**Coverage ZERO (PRIME+):** line+branch 100% scope/diff · 0 uncovered Err on touch · matrix gaps 0 — details [A25](#prime-a25--coverage-absolute) / table in A13 evidence path.

**LITE only:** smoke; no 100% gate. Else red → fix until green.

---

## AGENT-VERIFY — You run the quality gate

Tier ≥ PRIME: **ты** создаёшь/гонишь checker. User не в цепочке.

```text
exists? NO → AGENT-5 bootstrap → green
loop: --only <step> → RED → FIX PLAN batch → re-run
done: --diff → FULL → exit 0 → --evidence → paste block
```

**MUST NOT:** skip hard gates; `--only unit` as final; ask user to run; done without evidence.

---

## AGENT-5 — PRIME-CHECK (agent enforcement engine)

**Quality gate** — **единственный** merge gate на tier ≥ PRIME.  
**Владелец: агент на 100%.** Создаёт · настраивает · дописывает steps · вешает CI · ставит dev-deps · запускает · чинит до green. **Пользователь не трогает checker.**

**Reference implementation:** Python `scripts/prime_check/` — reference scaffold; на другом стеке агент делает эквивалент (`npm run prime:check`, `make prime-check`…) с **тем же контрактом** (steps, Finding, evidence, exit 0).

### Agent ownership checklist (MUST — агент делает сам)

```text
[ ] Detect stack → pick adapter row (lint, types, unit, coverage, security)
[ ] Scaffold orchestrator + reporter + finding + evidence + steps/
[ ] Implement ALL applicable steps for tier (~50 — не заглушки)
[ ] Law→Gate: каждый PRIME MUST с Enforced by → real step (не return [])
[ ] Write prime_check.config.yaml: tier, adoption_mode, runtime_scope, capabilities, cohesion_mode, ports, composition_root_scope, port_mode
[ ] Wire CI job — identical command to local
[ ] Add dev-deps to project (pytest, ruff, eslint… — что нужно gates)
[ ] Run --list → all steps registered
[ ] Run FULL → fix checker bugs → fix codebase → exit 0
[ ] Document entrypoint in README fragment if project has no docs
```

### Law→Gate rule (MUST — не плодить мёртвые MUST)

**Любой новый / изменённый Empire law** с `Enforced by:` **обязан** в той же сессии bootstrap/правки checker иметь:

| Артефакт | Требование |
|-----------|------------|
| `steps/<gate>.py` (или stack equiv) | Реальная проверка, не `return []` |
| Finding example | rule ID · file:line · hint · rerun в спеке или docstring step |
| Config knobs | если gate soft/configurable — поля в `prime_check.config.yaml` |
| Step map row | AGENT-5 FULL step map обновлён |
| Evidence field | если law про honesty/taxonomy — поле в evidence block |

**MUST NOT:** добавить Axx в markdown и оставить gate «потом». Это тот же класс лжи, что coverage vanity.

### Gate algorithms — Package cohesion & Test taxonomy (агент реализует)

#### `package-cohesion-gate` ([A05a](#prime-a05a--package-cohesion))

```text
1. Read architecture.package_form, capabilities[], cohesion_mode
2. If package_form=flat_ok OR len(capabilities)<2 → SKIP (ADR sunset if temporary)
3. For each changed file in core_scope|application_scope|presentation_scope:
   - path must contain /<capability>/ OR feature-package root matching capabilities
   - else Finding P2/P1 per cohesion_mode (warn|fail)
4. Hint: move to mirrored slice or features/<cap>/…
```

#### `intent-lock-gate` ([A34](#prime-a34--intent-lock) — behavior-lock)

```text
1. acceptance_criteria empty on PRIME+ feature change → FAIL STOP
2. Each AC MUST have: id, statement, oracle.kind, oracle.assert, test ref
3. FAIL if oracle missing | oracle.kind empty | test body has no assert/expect matching oracle.assert tokens
   (HWND/pixels/fs/error_id/toast/shown/style — Skin-native API OK)
4. FAIL if lock is only: AC id in test name / "AC{i}" in docstring / inventory.yaml exists
5. Hint: write the observable fact first; name the test after the fact, not AC1
```

#### `test-taxonomy-gate` + Anti-N/A ([A12a](#prime-a12a--test-taxonomy))

```text
1. Load test_taxonomy_map (or tests/taxonomy_inventory.yaml)
2. Infer triggers from diff + design
3. For each A12a family:
   - trigger present → ≥1 test whose BODY has a non-trivial oracle assert (see A27)
   - trigger absent → N/A(<absent-trigger>) — one reason per skip, not one ADR for 15 families
4. FAIL: missing family | N/A spam | N/A while trigger detected | APPLIED but only name exists (no oracle)
5. Cross-check AC oracles ([A34](#prime-a34--intent-lock))
```

#### `live-surface-gate` ([A36](#prime-a36--live-surface))

```text
1. For each port in architecture.ports / contract_surface_map.outbound:
   - AST: type is constructed in composition_root_scope AND a method is called from application_scope
   - else FAIL (declared-not-lived)
2. Serialized Settings/DTO field never read outside serde/schema → FAIL (unread field)
3. impl Trait for T whose methods are identity / todo!() / Ok(()) / pass without ADR+sunset → FAIL
4. Adapter type name contains a crate/feature token (Wgc, DXGI, BitBlt, Stripe, Redis…)
   not referenced in src except the name → FAIL (lying adapter)
5. Port listed but zero call sites in application → FAIL (port spam)
```

#### `no-swallow-gate` ([A37](#prime-a37--honest-errors--no-swallow))

```text
1. AST in composition + presentation + application: let _ = expr; .ok(); .unwrap_or_default() on Result
   from I/O register/save/capture/autostart/hotkey — FAIL unless skipped_steps ADR+sunset on that line
2. Empty catch / except: pass / catch {} on those calls → FAIL
3. One Err variant used as dump-bucket (≥3 distinct failure sites map to same variant without alias+ADR) → FAIL
```

#### `err-variant-gate` ([A10](#prime-a10--result) · [A37](#prime-a37--honest-errors--no-swallow))

```text
1. Collect named Err variants in core/app
2. Each variant → test that CALLS production path (UC/adapter Fake) and observes that variant
3. FAIL if test only assert_eq!(err.invariant_id(), "…") / Display / enum name without invoking producer
4. Coverage of the return site required — not regex on test name test_err_*
```

#### `ignored-test-gate` ([A12a](#prime-a12a--test-taxonomy) · [A25](#prime-a25--coverage-absolute))

```text
1. Collect #[ignore] / xtest.skip / it.skip / pytest.mark.skip / .skip(
2. Each MUST have skipped_steps row: {step, test, trigger, adr, sunset} — unique trigger, not shared ADR-N/A(desktop)
3. FAIL if ignored without row
4. e2e-ui: family APPLIED only if at least one e2e test actually runs (not all ignored)
5. AC oracle kind hwnd|pixels|ui cannot be closed by unit-only while e2e is ignored
```

#### `exclude-honesty-gate` ([A25](#prime-a25--coverage-absolute))

```text
1. greenfield + PRIME: exclude_coverage MUST NOT contain composition_root_scope, infrastructure adapters, presentation command handlers
2. ALLOW: generated/, vendor/, OS glue WITH an integration test of that adapter (real PNG, real mutex) + ADR+sunset
3. FAIL: empty fakes-only 100% while composition.rs excluded
```

#### `ffi-safety-gate` ([A16](#prime-a16--secure-by-design))

```text
1. If src has unsafe / JNI / ctypes / winapi / raw ptr → ffi_profile MUST be true
2. FAIL: ffi_profile false while those tokens exist in src
3. FAIL: safety_profile false when tier CRITICAL or embedded with FFI
4. Each unsafe block: preceding SAFETY comment with invariant (aliasing, HWND lifetime, GDI ownership)
5. Native handle type without Drop/RAII/finalizer → FAIL
6. clippy::undocumented_unsafe_blocks deny (Rust) or analog; geiger/unsafe budget ratchet when tool exists
```

#### `checker-integrity-gate` ([A38](#prime-a38--checker-integrity))

```text
1. AST scripts/prime_check/** (and stack equiv):
   FAIL: return GREEN / return [] / if False: FAIL else GREEN / always-pass
   FAIL: gate whose only check is path.exists() / file read without parse
   FAIL: lock "AC{i}" in text / inventory filename exists
2. no-trivial-assert implementation MUST flag more than assert!(true) (see A27)
3. This gate runs on the checker itself every FULL run
```

#### `behavior-ssot-gate` ([A39](#prime-a39--behavior-ssot) · [A08](#prime-a08--anti-fork--policy-facades))

```text
1. Scope: runtime_scope minus generated/vendor — presentation + application + core + adapters
2. Fingerprint functions/methods: strip identifiers/comments; keep control-flow + call-kinds
   + business literals (status enums, error codes). Body < behavior_ssot.min_body_stmts (default 8) → skip
3. Cluster near-duplicates (same shape, renamed vars)
4. Cluster size ≥2 AND no single exported owner that the others CALL → FAIL
   Hint: extract canonical fn / facade / entity method; replace copies with calls
5. Cross-check design artifact behavior_owners: [{id, owner_symbol, callers[]}]
   — new clone without updating the map → FAIL
6. ALLOW: ADR allowlist {hash, reason, sunset} for coincidental similarity (different invariants)
7. MUST NOT: path.exists("utils/") / helpers.rs exists. MUST parse AST. [A38](#prime-a38--checker-integrity)
```

#### `ci-harden-gate` ([A40](#prime-a40--secure-continuum))

```text
1. When: .github/workflows | .gitlab-ci.yml | Jenkinsfile | equiv in repo; else N/A(no CI)
2. Parse workflow YAML/AST — MUST NOT path.exists only ([A38](#prime-a38--checker-integrity))
3. FAIL if default/job permissions is write-all OR absent when secrets/deploy present
   — require explicit least set (Skin map in config: contents:read, id-token:write When OIDC…)
4. FAIL if pull_request_target (or equiv) runs untrusted checkout with secrets without ADR+sunset
5. FAIL if actions/uses unpinned (@v4 floating) When secure_continuum.ci_harden.pin_actions true
6. FAIL if curl|sh / wget|bash install without checksum ADR
7. ALLOW: allowlist [{path, reason, sunset}]
```

#### `channel-secret-gate` ([A40](#prime-a40--secure-continuum) · [A19](#prime-a19--supply-chain--secrets))

```text
1. Extend gitleaks/no-secrets patterns to docs, examples, evidence templates
2. FAIL if evidence-block / design paste contains raw secret-shaped tokens
3. FAIL if committed examples look like real keys (sk-…, BEGIN PRIVATE KEY, Bearer eyJ…)
4. Agent discipline (spec): refuse to echo user-pasted secrets — rewrite to env var names;
   on leak in chat → B14 rotate/revoke steps — MUST NOT ignore
5. MUST NOT: existence of SECURITY.md as PASS
```

#### `security-headers-gate` ([A40](#prime-a40--secure-continuum) · [A18](#prime-a18--owasp-input-hygiene))

```text
1. When: web UI or public HTTP API; else N/A(api-json-only|no HTTP) with Anti-N/A reason
2. Detect framework Skin (Express/Nest/FastAPI/Axum…)
3. Assert CSP · HSTS(prod) · X-Content-Type-Options · frame deny — via middleware registration AST
   or config snapshot test — MUST NOT «Helmet in package.json»
4. ALLOW ADR for intentional omit with sunset
```

#### `cors-csrf-gate` ([A40](#prime-a40--secure-continuum) · [A18](#prime-a18--owasp-input-hygiene))

```text
1. When: browser-facing; else N/A(bearer-only|no browser) with reason
2. CORS: allowlist origins — FAIL `*` with credentials
3. CSRF: token or SameSite strategy When cookie session; N/A(bearer-only) OK with reason
4. Parse config/code AST — FAIL open CORS + cookies
```

#### `iac-scan-gate` ([A40](#prime-a40--secure-continuum) · [A23](#prime-a23--infra--docker-security))

```text
1. When: k8s/helm/terraform/pulumi/cloudformation present; else N/A(no IaC)
2. Soft→fail per secure_continuum.iac.mode: privileged pods, hostNetwork, public * IAM,
   open security groups (denylist + one Skin linter: checkov|tfsec|kube-linter)
3. MUST NOT require all scanners — one GREEN
4. MUST NOT: Dockerfile-only harden while cluster wide open
```

#### `trust-pipeline-gate` ([A41](#prime-a41--trust-pipeline))

```text
1. When: protected / state-changing ops in design artifact / route matrix; else N/A
2. Infer call chain Skin-native (handler → middleware → UC)
3. FAIL if raw request/body reaches UC/repo without schema type boundary
4. FAIL if authz runs after mutation / after side-effect write
5. FAIL if UC reads untyped dict/map from transport as business input
6. Cross-check secure_continuum_map.authz_owner OR behavior_owners id=authorize
7. MUST NOT: path.exists("auth.ts"). MUST parse AST/call graph. [A38](#prime-a38--checker-integrity)
```

#### `idor-ownership-gate` ([A41](#prime-a41--trust-pipeline) · [A02](#prime-a02--zero-trust) · [A29](#prime-a29--zta-matrix))

```text
1. When: resource id in path/body + multi-user/tenant; else N/A(single-user)
2. Require test oracle: principal A cannot read/mutate principal B's resource (403/404)
3. Production path: authz uses server-side ownership/tenant — NOT client-supplied owner id
4. Extend zta-matrix rows OR trust_pipeline_map.idor_cases — one skip = one ADR
5. FAIL if only «anonymous vs logged-in» without cross-user When multi-user
```

#### `mass-assign-gate` ([A41](#prime-a41--trust-pipeline))

```text
1. When: update/patch/create from external input
2. AST: entity/ORM update from full request / **body / Object.assign(entity, req) → FAIL
   unless allowlisted fields / explicit Command / schema strips privileged keys
3. Privileged fields (config denylist: role, is_admin, balance, password_hash, tenant_id…)
   MUST NOT be optional client DTO fields without separate admin op + authz
```

#### `path-escape-gate` ([A41](#prime-a41--trust-pipeline) · [A18](#prime-a18--owasp-input-hygiene))

```text
1. When: file path / upload / download
2. Detect path joins with user strings
3. FAIL if no canonicalization + root prefix check (or Skin-safe API)
4. Require negative test: `../` rejected
```

#### `session-token-gate` ([A41](#prime-a41--trust-pipeline) · [A19](#prime-a19--supply-chain--secrets))

```text
1. When: session or token auth; bearer-only → N/A(cookie flags) OK with reason
2. FAIL token in query string / logged fragment
3. FAIL cookie session without Secure+HttpOnly (prod) unless ADR
4. FAIL custom crypto / homemade JWT verify when stack has standard lib
5. FAIL secrets/tokens in logs (pair pii-log-scan)
```

#### `port-surface-gate` + Anti-N/A contracts ([A35](#prime-a35--contract-surface))

```text
1. Load contract_surface_map (design artifact or architecture.ports in config)
2. Infer triggers: banned_imports / I/O in testable_core_scope? multi-entry? cross-cap? API? events?
3. For each A35 family:
   - If trigger present → require named Port/Protocol/iface (or schema path) in map + type exists
   - If trigger absent → require N/A(<absent-trigger>)
4. FAIL if: concrete infra type in core/app param/annotation | N/A("одна реализация"|"потом"|"framework DI")
5. Hint: introduce Protocol/iface; move concrete to adapters/
```

#### `composition-root-gate` ([A35](#prime-a35--contract-surface))

```text
1. Read architecture.composition_root_scope
2. AST: new ConcreteAdapter / client constructors / SDK init
3. Outside composition_root_scope + outside tests → FAIL
4. Hint: wire in main / AppModule / DI config only
```

#### `port-test-double-gate` ([A35](#prime-a35--contract-surface))

```text
1. For each outbound port in contract_surface_map / architecture.ports
2. Require Fake|InMemory|Stub type that implements the port (AST implements/extends)
3. Or ADR allowlist mock-exception with sunset
4. FAIL if unit tests only mock concrete adapter class
```

#### `anemic-mutation-gate` ([A05](#prime-a05--layer-law) · [B06](#prime-b06--fsm))

```text
1. If no status/lifecycle field AND no fsm_transitions in design → SKIP
2. AST in testable_core_scope + presentation: Assign to .status/.state/.lifecycle
   OR call public setStatus/set_state on an entity type — outside that type's methods
3. FAIL: use-case / handler / service does user.status = 'active' | user.setStatus('active')
4. ALLOW: User.activate() / Order.transition(...) that owns the invariant inside the type
5. ALLOW: persistence hydrate/mapper reconstructing entity from row (infra) — not a business write
6. Hint: move mutation into entity/VO method; pair fsm-transition-gate for legal/illegal edges
```

### Если скрипта нет

STOP фичу → scaffold per ownership checklist above → ALL steps → FULL green → then feature.

### Stack adapter matrix (universal — pick detected stack)

| Stack | lint | types | unit | coverage | security |
|-------|------|-------|------|----------|----------|
| **Python** | ruff | mypy | pytest | coverage.py | bandit |
| **TS/Node** | eslint | tsc | vitest/jest | c8/istanbul | npm audit |
| **Rust** | clippy | rustc | cargo test | llvm-cov | cargo audit |
| **Go** | golangci-lint | — | go test | go tool cover | govulncheck |
| **Kotlin** | detekt | — | junit | jacoco | dependency-check |
| **Swift** | swiftlint | — | xctest | xccov | — |

Агент **адаптирует имена шагов**, не правила. `pytest-unit` → `vitest-unit` и т.д.

### AST Prosecutor — не CI-обёртка

**Проблема:** pytest+coverage alone = CI-обёртка; агент «готов» словами.  
**Решение:** агент **пишет** AST/import-graph steps в `scripts/prime_check/` (не shipped). Exit 0 = правда. CISQ/CERT map → [Quality Constellation](#quality-constellation--iso--cisq--owasp--cert-constitutional-layer). Scopes = Skin paths in config; Engine = outcomes.

**MUST:** architecture gates = real AST/import graph (не stub `return []`); FAIL → Finding (rule · file:line · hint · rerun).  
**MUST NOT:** «import-graph failed» без file:line + chain + hint.

**Role scopes** (agent fills at bootstrap) — see Config yaml `architecture.*` below.  
**Gate inventory:** FULL step map + algorithms above (`import-graph` · `di-purity` · `deterministic-runtime` · `anti-null` · `handler-purity` · `cyclomatic`/`file-size` · `anti-fork` · `behavior-ssot` · `package-cohesion` · `port-surface` · `composition-root` · `port-test-double` · `live-surface` · `no-swallow` · continuum · trust-pipeline · `ffi-safety` When FFI).

**Stack AST tooling (agent wires):** Python `libcst`/`ast` · TS `@typescript-eslint`/`madge` · Rust `syn` · Go `go/ast` · Kotlin detekt · Swift SourceKit.

```text
FAIL PRIME-A05 [import-graph-gate] P1
  file: src/core/order.py:4
  issue: core imports sqlalchemy.orm
  hint: move persistence to adapters/; core depends on port only
  rerun: python -m scripts.prime_check --only import-graph-gate
```

### AI MUST maintain

Cross-platform entrypoint; structured Findings; `--list/--only/--diff/--evidence/--json`; local ≡ CI; no stub steps; no «настройте сами».

### Report output

FULL = **collect all** findings. Batch-fix P1→P3. Finding shape above. Report: EXEC SUMMARY → FIX PLAN → FINDINGS → COVERAGE/MATRIX gaps → exit footer.

### Config (`prime_check.config.yaml`)

```yaml
project_tier: PRIME
adoption_mode: greenfield          # greenfield | legacy
stack: auto                      # auto-detect → adapter row
runtime_scope: [src/**, lib/**, app/**]
tests_scope: [tests/**, __tests__/**]
critical_scope: [src/domain/**, src/application/**]
monorepo_scopes:                 # optional — A32
  - path: services/api/
    tier: PRIME
  - path: tools/script/
    tier: LITE
exclude_coverage: []             # EMPTY default; greenfield MUST NOT exclude composition/adapters (A25)
skipped_steps: []                # [{step, test, trigger, adr, sunset}] — one skip = one trigger
ffi_profile: false               # MUST true When unsafe/JNI/ctypes/Win32 in src
safety_profile: false            # true When CRITICAL/embedded; FAIL false if ffi in src and ffi_profile false
zero_tolerance: true
agent_evidence_required: true
coverage:
  line: 100.0
  branch: 100.0
  diff_only_on_pr: true          # legacy: mandatory
  ratchet: true
mutation:
  min_kill_rate_prime: 85          # PRIME greenfield MUST on critical_scope (A28)
  min_kill_rate_critical: 95
  enabled_prime_greenfield: true   # MUST NOT set false to dodge A27 weak tests
forbidden_patterns:
  - "pragma: no cover"
  - "istanbul ignore"
  - "assert True"
  - "expect(1).toBe(1)"
docker_files: [Dockerfile, docker-compose.yml, compose*.yml]
architecture:                      # AST Prosecutor — agent maps Skin → scopes
  core_scope: [domain/**, src/core/**]
  application_scope: [application/**, usecases/**]
  presentation_scope: [api/**, routes/**, controllers/**]
  testable_core_scope: [domain/**, application/**]
  handler_max_logic_lines: 15
  cyclomatic_max: 10
  file_max_lines: 300
  banned_imports_in_core: {python: [sqlalchemy, fastapi], node: [express, pg]}
  package_form: mirrored_slices          # A05a — Skin form
  capabilities: [orders, billing, auth]  # A05a — empty only if flat_ok / single capability
  cohesion_mode: warn                    # off | warn | fail
  ports: [IOrderRepository, IClock]      # A35 — outbound ports
  composition_root_scope: [src/main.py, src/di/**]
  port_mode: fail                        # warn | fail
behavior_ssot:                           # A39 — Anti-Clone
  mode: fail                             # warn | fail — PRIME+ fail
  min_body_stmts: 8
  allowlist: []                          # [{hash, reason, sunset}] ADR coincidental similarity
secure_continuum:                        # A40 — Anti-Theatre
  mode: fail                             # PRIME+ fail
  ci_harden:
    pin_actions: true
    forbid_pull_request_target: true
    allowlist: []                        # [{path, reason, sunset}]
  headers:
    mode: fail
  cors_csrf:
    mode: fail
  iac:
    mode: warn                           # fail when manifests present on PRIME+
  channel_secret:
    mode: fail
trust_pipeline:                          # A41 — Hardened App Code
  mode: fail
  privileged_field_denylist: [role, is_admin, balance, password_hash, tenant_id]
  idor_mode: fail
  mass_assign_mode: fail
  path_escape_mode: fail
  session_token_mode: fail
forbidden_patterns:                  # extend per safety_profile / ffi_profile
  - "goto"
  - "setjmp"
  - "eval("
  - "exec("
```

### FULL step map — ~50 steps (mandatory at PRIME+)

Агент реализует **все** применимые. `N/A` только с ADR + `--list` shows `SKIPPED(ADR-xxx)`.

| Step | What it does | Rule |
|------|--------------|------|
| **PREFLIGHT** | | |
| `stack-detect` | auto stack + adapter | A22 |
| `config-valid` | yaml schema, scopes, tier | A22 |
| `ci-parity` | CI cmd ≡ local cmd | A22 |
| **STATIC** | | |
| `lint` | formatter/linter zero issues | A17 |
| `typecheck` | mypy/tsc — zero errors | A17 |
| `format-check` | no unformatted diff | A17 |
| `dead-code-gate` | vulture/knip — no unused export | A11 |
| `file-size-guard` | >300 fail; >200 allowlist | A11 |
| `cyclomatic-gate` | function complexity >10 fail | A11 |
| **ARCHITECTURE — AST Prosecutor (7 gates + soft cohesion)** | | |
| `import-boundaries` | quick role import check | A05 |
| `import-graph-gate` | **AST** import DAG; core ↛ infra/presentation/banned | A05 |
| `package-cohesion-gate` | capability folders / no flat layer-dump (soft→fail per config) | A05a |
| `deterministic-runtime` | **AST** nondeterminism ban in testable_core_scope | A06, A15 |
| `anti-null-gate` | **AST** + types: no silent null as failure path | A10 |
| `immutability-gate` | domain/app entities immutable; no in-place mutation | A05, B06 |
| `anemic-mutation-gate` | status/lifecycle mutated only via entity methods (not public assign/setter) | A05, B06 |
| `context-leak-gate` | no cross-bounded-context import of domain entities | A04, A05, B05 |
| `idempotency-matrix-gate` | state-changing UC has key + ledger + double-submit test | A14, A09, A12 |
| `error-context-gate` | every Err type: rule_id + state_snapshot + trace_id | A10, B03 |
| `no-transport-in-domain` | no HTTPException/throw in domain | A10 |
| `di-purity` | **AST** no hardcoded infra `new`/`()` in core/app | A06, A35 |
| `di-graph-gate` | wiring only in composition root | A06, A35 |
| `port-surface-gate` | core/app deps are Ports; Anti-N/A on contract_surface_map | A35, A06 |
| `composition-root-gate` | concrete adapters constructed only in composition_root_scope | A35 |
| `port-test-double-gate` | each outbound port has Fake/InMemory impl | A35 |
| `dto-boundary-gate` | cross-capability imports only contracts/DTO/primitives | A35, A04 |
| `inbound-port-gate` | soft: multi-entry → UC behind inbound port | A35 |
| `plugin-boundary-gate` | new provider via SPI/port; no Core edit for swap | A35, A04 |
| `event-contract-gate` | soft: published events have versioned schema | A35, B03 |
| `handler-purity-gate` | **AST** presentation handler ≤15 logic lines, no business if | A05 |
| `anti-fork-gate` | **AST** fingerprint: `*_v2`, duplicate policy blocks + near-dup algorithms | A08 · A39 |
| `behavior-ssot-gate` | **AST** cluster same algorithm ≥2 without one owner all call; `behavior_owners` map | A39 |
| `no-string-sql` | no f-string SQL | A18 |
| `no-ddl-in-app` | DDL only migrations/ | A20 |
| **SECURITY** | | |
| `gitleaks-history` | secrets in full git history | A19 |
| `no-secrets` | regex scan working tree | A19 |
| `bandit` / `npm-audit` / `cargo-audit` | static security | A16, A18 |
| `dependency-audit` | zero high/critical CVE | A19 |
| `sbom` | SBOM generated + stored | A19 |
| `no-debug-bypass` | `if True:`, `SKIP_AUTH`, test flags | A16 |
| `pii-log-scan` | email/phone/card in log strings | A16 |
| `injection-fuzz` | fuzz inputs on boundaries | A18, A12a, B12 |
| `ssrf-gate` | outbound URL allowlist | A18 |
| `zta-matrix-gate` | route × anon/valid/forbidden/expired | A02, A29, A12a |
| `ci-harden-gate` | **YAML/AST** workflow: least permissions, pin actions, no privileged fork PR | A40 |
| `channel-secret-gate` | no raw secrets in evidence/docs/examples; agent refuse echo | A40 · A19 |
| `security-headers-gate` | CSP/HSTS/… registered in middleware — not package.json | A40 · A18 |
| `cors-csrf-gate` | CORS allowlist; CSRF When cookie session | A40 · A18 |
| `iac-scan-gate` | When k8s/tf/helm: privileged/public * IAM denylist + one Skin scanner | A40 · A23 |
| `trust-pipeline-gate` | schema→authn→authz→command before UC; no raw body in UC; authz before mutation | A41 |
| `idor-ownership-gate` | cross-user oracle; no client owner id as proof | A41 · A02 · A29 |
| `mass-assign-gate` | no request-bag→entity; privileged fields stripped | A41 |
| `path-escape-gate` | path under root jail; `../` negative test | A41 · A18 |
| `session-token-gate` | no token in query/logs; cookie flags or bearer N/A | A41 · A19 |
| **TESTS** | | |
| `test-taxonomy-gate` | families APPLIED only with non-trivial oracle; Anti-N/A; one skip = one trigger | A12a |
| `intent-lock-gate` | each AC has oracle; test body asserts it — not `"AC{i}" in name` | A34 |
| `live-surface-gate` | declared ports/fields live (called, not identity/unread) | A36 |
| `no-swallow-gate` | no swallowed Result on process I/O | A37 |
| `checker-integrity-gate` | AST of prime_check: no unconditional GREEN, no existence-only | A38 |
| `e2e-ui` | UI journeys **actually run**; ignored → skipped_steps | A12a, B11 |
| `flaky-detector` | same test ×3 in one invocation — not «ran cargo test twice» | A27 |
| `no-trivial-assert` | no tautology, no same-file constant, no enum-name/invariant_id-only | A27 |
| `ignored-test-gate` | #[ignore]/skip without per-test skipped_steps → FAIL | A12a, A25 |
| `err-variant-gate` | each Err provoked via production path + Fake — not name regex | A10, A37 |
| `exclude-honesty-gate` | greenfield must not exclude composition/I/O adapters | A25 |
| `ffi-safety-gate` | SAFETY comments, RAII, ffi_profile vs src | A16 |
| `blast-radius-gate` | soft: diff vs declared blast_radius | A33 |
| `pytest-unit` / stack equiv | all unit pass | A12, A12a |
| `pytest-integration` | real DB/Redis/queue | A12, A12a |
| `pytest-contract` | full HTTP stack / contract@boundary | A12, A12a |
| `pytest-property` | hypothesis/proptest | A12a, B12 |
| `no-empty-test` | test must have real assert | A27 |
| `e2e-only-anti-pattern` | E2E without unit base fail | A12 |
| `test-matrix-gate` | design matrix ≡ tests + AC oracles (not `"AC{i}" in text`) | A12, A12a, A24, A34 |
| `boundary-value-gate` | validators/ranges: 0,-1,null/empty,max edges | A12a |
| `negative-path-gate` | reject/rollback/invalid for state-changing + auth | A12a |
| `scenario-matrix-gate` | multi-step business flows covered | A12a |
| `route-matrix-gate` | route × method × status | A03, A12, A12a |
| `fsm-transition-gate` | every legal + illegal FSM edge | B06, A12a |
| `regression-lock` | bug fix = `test_regression_*` | A12, A12a |
| **COVERAGE** | | |
| `coverage-line-100` | 100.00% line | A25 |
| `coverage-branch-100` | 100.00% branch (= path coverage) | A25, A12a |
| `coverage-diff-100` | 100% on changed files | A25, A31 |
| `coverage-ratchet` | no drop vs main | A25 |
| `no-pragma-no-cover` | pragma without ADR fail | A25 |
| **DATA & CONTRACTS** | | |
| `migration-path-only` | DDL only migrations/ | A20 |
| `schema-drift` | DB ≡ migrations | A20 |
| `api-contract-drift` | OpenAPI/proto ≡ code | A21, A12a |
| `snapshot-contract` | golden responses ≡ runtime | A21, A12a |
| **INFRA & OPS** | | |
| `docker-security` | non-root, no privileged | A23 |
| `compose-security` | no public DB without auth | A23 |
| `prod-config` | required env; no debug prod | A23 |
| `health-gate` | /health /ready probes exist + tested | B13 |
| `tls-min-version` | prod TLS < 1.2 fail | A23 |
| `iac-scan-gate` | IaC beyond Docker When present | A40 · A23 |
| **SAFETY — When FFI in src / CRITICAL** | | |
| `ffi-safety-gate` | SAFETY comments · RAII · ffi_profile | A16 |
| `cert-forbidden-gate` | AST/denylist: goto, unchecked cast, eval, VLAs (config) | A16 · CERT/MISRA profile |
| `concurrency-race-gate` | shared mutable + missing sync in safety scope | A05 · B06 · CERT |
| `clang-tidy` / `cppcheck` / `clippy-deny` | stack-native safety linter zero violations | A16 · ISO 5055 Security/Reliability |
| **CLIENT** | | |
| `frontend-quality` | lint + types + unit | B11 |
| **CRITICAL / PRIME greenfield** | | |
| `mutation-critical` | kill rate on critical_scope — PRIME greenfield MUST; CRITICAL ≥95% | A28 |
| **OUTPUT** | | |
| `evidence-block` | PRIME-VERIFY-EVIDENCE valid | A26 |

### Execution order (full run)

```text
stack-detect → config-valid → ci-parity →
lint → typecheck → format-check → dead-code-gate → architecture gates →
security scans → test pyramid → test-taxonomy-gate → coverage gates → matrix gates →
data/contract gates → docker/ops gates →
[mutation-critical if CRITICAL or PRIME greenfield] → evidence-block
```

### Coverage gates — ZERO untested code ([A25](#prime-a25--coverage-absolute))

```yaml
coverage-line-100:
  line: 100.0
  scope: runtime_scope | changed_files (legacy)
coverage-branch-100:
  branch: 100.0
coverage-diff-100:
  scope: git diff vs main
coverage-ratchet:
  baseline: main branch report
no-pragma-no-cover:
  scan: AST + regex; allow only with adr_ref in config
```

**MUST NOT:** `# pragma: no cover` без ADR. **MUST NOT:** 99.9%. **MUST:** новая строка = новый тест в том же PR.

### zta-matrix-gate — full auth scenarios ([A29](#prime-a29--zta-matrix))

Per protected route contract tests **MUST** exist:

| Scenario | Expected |
|----------|----------|
| No credentials | 401 |
| Wrong/expired token | 401 or 403 |
| Valid but insufficient scope | 403 |
| Valid authorized | 2xx |

localhost / docker **не** exempt.

### Evidence block format ([A26](#prime-a26--evidence-block))

```text
PRIME-VERIFY-EVIDENCE
tier: PRIME
adoption_mode: legacy
stack: python
prime_check: exit 0
steps_green: 47/47
coverage_line: 100.00%
coverage_branch: 100.00%
coverage_delta_vs_main: +1.2%
taxonomy_families: unit=APPLIED · integration=APPLIED · contract=APPLIED · negative=APPLIED · access_control=N/A(no auth) · …
contract_surface: outbound=APPLIED:IOrderRepo · inbound=N/A(single HTTP entry)
rich_domain: APPLIED:Order.submit | N/A(no status entity)
error_split: expected=named Err · unexpected=global handler
acceptance_criteria: AC1→test_place_order_ok · AC2→test_place_order_rejects_invalid
blast_radius: capabilities=[orders] files=[application/orders/…, tests/…]
changed_files: [src/uc.py, tests/test_uc.py]
tests_added: 8
uncovered: NONE
risks: NONE
rollback: git revert <sha>
last_cmd: python -m scripts.prime_check
```

### Bootstrap checklist

Ownership checklist + Law→Gate + config scopes (ports, composition_root) + CI parity + evidence fields (taxonomy/contract_surface/rich_domain/error_split/AC/blast). First run green or legacy ADR.

### Commands

```bash
python -m scripts.prime_check --list
python -m scripts.prime_check --only coverage-diff-100
python -m scripts.prime_check --only zta-matrix-gate
python -m scripts.prime_check --diff                # changed files — mandatory before full
python -m scripts.prime_check --json                # machine-readable report
python -m scripts.prime_check --report reports/     # persist JSON + coverage HTML
python -m scripts.prime_check --evidence              # print evidence block
python -m scripts.prime_check                         # FULL — mandatory before «done»
```

---

## AGENT-3 — Rule index

| ID | Topic | Min tier |
|----|-------|----------|
| [A01](#prime-a01--context--risk-tier) | Context & Risk Tier | all |
| [A02](#prime-a02--zero-trust) | Zero Trust | PRIME+ |
| [A03](#prime-a03--api-response-contract) | API response contract | PRIME+ |
| [A04](#prime-a04--integration-boundaries) | Integration & plugin boundaries | PRIME+ |
| [A05](#prime-a05--layer-law) | Layer law / separation roles | STANDARD+ |
| [A05a](#prime-a05a--package-cohesion) | Package cohesion / capability packaging | STANDARD+ |
| [A06](#prime-a06--di--ports) | DI & ports | PRIME+ |
| [A07](#prime-a07--design-first) | Design-first order | PRIME+ |
| [A08](#prime-a08--anti-fork--policy-facades) | Anti-fork & policy facades | PRIME+ |
| [A09](#prime-a09--policy-facades) | Policy facades (→ A08) | PRIME+ |
| [A10](#prime-a10--result) | Result & errors by tier | PRIME+ |
| [A11](#prime-a11--decomposition) | File size / complexity | STANDARD+ |
| [A12](#prime-a12--tests--coverage) | Tests & pyramid / coverage | STANDARD+ |
| [A12a](#prime-a12a--test-taxonomy) | Test taxonomy — kinds of tests MUST write | STANDARD+ / PRIME+ |
| [A13](#prime-a13--definition-of-done) | Definition of Done | PRIME+ |
| [A14](#prime-a14--idempotency) | Idempotency | PRIME+ |
| [A15](#prime-a15--deterministic-time) | Time/ID/random | PRIME+ |
| [A16](#prime-a16--secure-by-design) | Secure-by-design | all* |
| [A17](#prime-a17--clean-code) | Clean code & patterns | STANDARD+ |
| [A18](#prime-a18--owasp-input-hygiene) | OWASP Top 10 · ASVS · input hygiene | PRIME+ |
| [A19](#prime-a19--supply-chain--secrets) | Supply chain & secrets | all |
| [A20](#prime-a20--migrations) | Data & migrations | PRIME+ |
| [A21](#prime-a21--semver--contracts) | SemVer & contracts | PRIME+ |
| [A22](#prime-a22--prime-check) | Prime Check merge gate | PRIME+ |
| [A23](#prime-a23--infra--docker-security) | Infra & Docker security | PRIME+ |
| [A24](#prime-a24--tdd-lock) | TDD-LOCK — tests before code | PRIME+ |
| [A25](#prime-a25--coverage-absolute) | Coverage absolute — 100% + ratchet | PRIME+ |
| [A26](#prime-a26--evidence-block) | Evidence block — verify transcript | PRIME+ |
| [A27](#prime-a27--test-quality) | Test quality — no empty/trivial/flaky | PRIME+ |
| [A28](#prime-a28--mutation-prime) | Mutation testing | PRIME greenfield MUST; CRITICAL ≥95% |
| [A29](#prime-a29--zta-matrix) | ZTA auth scenario matrix | PRIME+ |
| [A30](#prime-a30--anti-slack) | Anti-slack — no partial PR | PRIME+ |
| [A31](#prime-a31--legacy-adoption) | Legacy adoption — diff-100 + ratchet | PRIME+ |
| [A32](#prime-a32--monorepo-scope) | Monorepo per-path tiers | PRIME+ |
| [A33](#prime-a33--blast-radius) | Blast radius — minimal feature scope | STANDARD+ |
| [A34](#prime-a34--intent-lock) | Behavior lock — AC oracle ↔ test body | PRIME+ |
| [A35](#prime-a35--contract-surface) | Contract Surface — ports · DTO · API/event · composition root | PRIME+ |
| [A36](#prime-a36--live-surface) | Live Surface — declared ports/fields must be used | PRIME+ |
| [A37](#prime-a37--honest-errors--no-swallow) | Honest errors — no swallow, no dump-bucket, provoke path | PRIME+ |
| [A38](#prime-a38--checker-integrity) | Checker integrity — no theatrical steps | PRIME+ |
| [A39](#prime-a39--behavior-ssot) | Behavior SSOT — one owner per algorithm; Anti-Clone | PRIME+ |
| [A40](#prime-a40--secure-continuum) | Secure Continuum — app · CI · chat · ops; Anti-Theatre | PRIME+ |
| [A41](#prime-a41--trust-pipeline) | Trust Pipeline — hardened app code; IDOR/mass-assign/path/token | PRIME+ |
| [B01](#prime-b01--cqrs) | CQRS | PRIME+ |
| [B02](#prime-b02--solid--grasp) | SOLID & GRASP | STANDARD+ |
| [B03](#prime-b03--sre--observability--events) | SRE, observability, events | PRIME+ |
| [B04](#prime-b04--resilience) | Resilience | PRIME+ |
| [B05](#prime-b05--inter-service-contracts) | Inter-service contracts | optional |
| [B06](#prime-b06--fsm) | FSM | PRIME+ |
| [B07](#prime-b07--yagni) | YAGNI | all |
| [B08](#prime-b08--agent-self-review) | Agent self-review | all |
| [B09](#prime-b09--adr) | ADR | CRITICAL |
| [B10](#prime-b10--performance) | Performance | PRIME+ |
| [B11](#prime-b11--client-apps) | Client apps (web/mobile/desktop) | STANDARD+ |
| [B12](#prime-b12--fuzz--property) | Fuzz & property invariants | PRIME+ |
| [B13](#prime-b13--ops--runbook) | Ops, health, rollback | PRIME+ |
| [B14](#prime-b14--human-handoff) | Human handoff after agent done | PRIME+ |

\*Security never exempted by YAGNI when code touches network/secrets/input.  
\*Empire Engine outcomes в Part A/B. **Skin** = Pattern Catalog. **Engine** = всегда для tier; **When** = только механизм (FSM/ledger/Docker), не «можно хуже».

---

# Part A — Code quality rules

## PRIME-A01 — Context & Risk Tier

**Min tier:** all **Enforced by:** DoD-only (tier in design artifact → applicable gates for that tier)  
**Applicability:** Always

- **MUST:** read project structure, stack, patterns, CI **before** writing. **Repo conventions = default form.**
- **MUST:** classify tier. **App / API / service / lib с I/O = минимум STANDARD.** LITE — одноразовые скрипты без сети.
- **MUST:** elevate to **PRIME** when **any** trigger fires:
  - authn/authz, PII, payments/money, external API mutations, background jobs with side effects
  - entity with **status/lifecycle** (→ FSM When applicable · **rich domain** — [A05](#prime-a05--layer-law))
  - multi-module monorepo or service split (→ context isolation When applicable)
  - operations where **retry/double-submit** is dangerous (→ idempotency When applicable)
- **MUST:** elevate to **CRITICAL** for finance, compliance, irreversible data loss.
- **MUST:** if tier ≥ PRIME and no quality gate → bootstrap first ([AGENT-5](#agent-5--prime-check)).
- **MUST:** set `adoption_mode`: greenfield (full scope) or legacy (diff-100 + ratchet) ([A31](#prime-a31--legacy-adoption)).
- **MUST:** PRIME defines **quality outcomes**, not one universal folder tree or framework — outcomes align with **ISO/IEC 25010** for assigned tier ([Quality Constellation](#quality-constellation--iso--cisq--owasp--cert-constitutional-layer)). Outcomes **include** layer separation ([A05](#prime-a05--layer-law)) **and** package cohesion ([A05a](#prime-a05a--package-cohesion)) — «не диктуем DDD-дерево» ≠ «плоский dump OK».
- **MUST NOT:** downgrade tier to avoid tests or gate bootstrap.
- **MUST NOT:** impose Clean/DDD/UseCase/Result **or** a textbook `domain/entities` + `use-cases` + `tests/unit|e2e` tree if the project already uses another proven Skin — map to [Pattern Catalog](#pattern-catalog--stack-native-equivalents).
- **MUST:** **минимальный scope** на фичу ([A33](#prime-a33--blast-radius)); **максимальный scope** на качество — тесты/security/taxonomy не режутся.
- **MUST NOT:** add a second capability as orphan files in a flat layer bag when the repo already has (or needs) capability packages.
- **SHOULD:** document tier triggers + `capability_slices` + `acceptance_criteria` + `blast_radius` in design artifact.

---

## PRIME-A02 — Zero Trust (ZTA)

**Min tier:** PRIME+ **When:** exposed operation requires auth **Enforced by:** `zta-matrix-gate`, contract tests  
**Aligns:** OWASP Top 10 **A01 Broken Access Control** · **A07 Identification & Auth Failures** · ASVS V2/V4 · ISO 25010 **Security**

- **MUST:** authn + authz on **every** protected **operation** (HTTP route, RPC method, GraphQL field, CLI with credentials) **before** application logic.
- **MUST:** localhost, docker network, `127.0.0.1`, sidecar, `/internal`, `/debug` — **те же правила** что и public internet в prod/staging.
- **MUST:** CI job identity / deploy token / chat-ops bot ≠ trusted substitute for authz — same deny-by-default ([A40](#prime-a40--secure-continuum)).
- **MUST NOT:** `LIME_TESTING=1`, compose network, reverse proxy, VPN как substitute auth.
- **MUST NOT:** trust «мы внутри кластера» — [A23](#prime-a23--infra--docker-security).
- **MUST:** allow/deny in Application layer — not «header present ⇒ OK»; **one authorize owner** When N≥2 call sites ([A39](#prime-a39--behavior-ssot)).
- **MUST:** authz is **resource-scoped** — principal may act on **this** resource (IDOR closed); not only «has valid token» ([A41](#prime-a41--trust-pipeline), `idor-ownership-gate`).
- **MUST:** validate input at boundary before UC ([A18](#prime-a18--owasp-input-hygiene)); Trust Pipeline order ([A41](#prime-a41--trust-pipeline)).
- **MUST:** least privilege — minimal scopes, DTO fields, per-role secrets, **CI workflow permissions** ([A40](#prime-a40--secure-continuum)).
- **MUST:** deny-by-default; DB/Redis/cache **не** на public без TLS+auth.
- **MUST:** `zta-matrix-gate` — full auth scenario matrix per **protected operation** ([A29](#prime-a29--zta-matrix), taxonomy **access_control** in [A12a](#prime-a12a--test-taxonomy)). HTTP — один частный случай.
- **MUST:** When multi-user/tenant resources — matrix includes **cross-user/IDOR** oracle ([A41](#prime-a41--trust-pipeline)).
- **MUST:** split metrics/admin from product API at ingress.

---

## PRIME-A03 — API response contract

*Stable response shape — contract tests can assert status + error codes without guessing.*

**Min tier:** PRIME+ **When:** exposed HTTP/RPC/GraphQL/CLI operation **Enforced by:** `route-matrix-gate` · `api-contract-drift` · `snapshot-contract`  
**Aligns:** [A12a](#prime-a12a--test-taxonomy) contract · [A18](#prime-a18--owasp-input-hygiene) · [A21](#prime-a21--semver--contracts) · [A41](#prime-a41--trust-pipeline) When auth

### Outcome (Engine)

One envelope/error shape per surface; real status codes; every exposed op × outcome in matrix.

### MUST / MUST NOT

- **MUST:** consistent response format per API surface (envelope, status, error codes).
- **MUST:** real HTTP/RPC status codes; documented error shapes.
- **MUST NOT:** mix formats across endpoints of the same surface.
- **SHOULD:** health/metrics endpoints ([B03](#prime-b03--sre--observability--events)).

### See

[A12](#prime-a12--tests--coverage) · [A21](#prime-a21--semver--contracts) · [A29](#prime-a29--zta-matrix) When protected

---

## PRIME-A04 — Integration & plugin boundaries

**Min tier:** PRIME+ **When:** I/O swap / plugin / multi-module **Enforced by:** `context-leak-gate` · `port-surface-gate` · `plugin-boundary-gate` (When plugin)  
**See also:** [A35](#prime-a35--contract-surface) (SSOT for *which* contracts) · [A06](#prime-a06--di--ports)

- **MUST (outbound I/O):** any I/O / side-effect / nondeterminism from application/core → **explicit port** (Protocol/interface/trait/Skin equiv) — **even if one impl**. «Одна реализация» ≠ license for concrete in core ([A35](#prime-a35--contract-surface)).
- **MUST (plugin / strategy):** extend via **abstraction** + adapter — When 2+ impl **или** plan to swap provider (payment, storage, notifications, auth) without Core edits.
- **MUST:** **plugin boundary** — new provider adds via SPI/port; **no edits to existing Core** for wiring swap.
- **MUST:** modules communicate through **published API** (public types, events, RPC contract) — not private internals.
- **MUST NOT:** duplicate policy across DI, API, infrastructure.
- **MUST NOT:** nest I/O inside core/application packages (concrete clients).
- **SHOULD:** keep adapters and published ports **capability-local** inside a deployable ([A05a](#prime-a05a--package-cohesion)); A04 isolation is for **cross-module private types**, A05a is for **where files live**, A35 is for **contract families**.

### Module isolation (PRIME+) — When multi-module / service split

ИИ склеивает модули микро-импортами private types → распределённый монолит. **Запрещено импортировать чужие private domain types.**

- **When:** single-package app / trivial script → isolation gate **N/A**.
- **When:** multi-module monorepo or microservices → **MUST** isolate.
- **MUST:** каждый модуль владеет **своими** internal types.
- **MUST NOT:** import/re-export **private** entity/aggregate/VO другого модуля.
- **MUST:** cross-module data — **DTO / primitives / public contract types / events**:
  - primitives (`user_id: UUID`, `amount_cents: int`);
  - Domain Events (`UserRegistered`) — async ([B03](#prime-b03--sre--observability--events));
  - published interfaces — не concrete internal types ([A06](#prime-a06--di--ports), [A35](#prime-a35--contract-surface)).
- **MAY:** **shared kernel** (общие types) — **только** с ADR + explicit `shared/` или `contracts/` package; gate allowlists ADR path.
- **Enforced by:** `context-leak-gate` · `dto-boundary-gate` — import private type из `module_a` в `module_b` → exit 1 (unless ADR shared kernel).

```python
# BAD:  from users.domain import User  # private type in payments/
# GOOD: charge(user_id: UserId, amount: Money)  # primitive/DTO at boundary
# GOOD: shared kernel ADR → contracts/user_id.py — both modules import contracts only
```

---

## PRIME-A05 — Layer law

*Separation roles — not one mandatory universal tree. Form = repo-native ([Pattern Catalog](#pattern-catalog--stack-native-equivalents)). Package topology = [A05a](#prime-a05a--package-cohesion).*

**Min tier:** STANDARD+ **Applicability:** separation of business logic from I/O — **форма = repo-native**  
**Aligns:** ISO 25010 **Maintainability** (modularity, analysability) · CISQ **Maintainability** · ISO 5055 coupling defects  
**Enforced by (PRIME+):** `import-boundaries` · `anemic-mutation-gate` (When status entity) · `immutability-gate` (When applicable) · `context-leak-gate` (When multi-module) · paired with `package-cohesion-gate` ([A05a](#prime-a05a--package-cohesion))

| Role | MUST | MUST NOT |
|------|------|----------|
| **Core / Domain** | business rules, invariants, **rich entity methods**, domain errors; abstractions for I/O | direct I/O, frameworks, DB, HTTP, time/uuid in core; god-classes; **anemic public status writes** |
| **Application** | orchestration entry; explicit error handling per stack | direct DB/HTTP in orchestration when project separates adapters; transport exceptions in core |
| **Infrastructure** | I/O impls, persistence, clients, resilience | business policy |
| **Presentation** | validate input, invoke application entry, map response | business logic; manual wiring without project DI |

- **MUST NOT:** business logic in UI components, fat route handlers, CLI `main`, mobile Views.
- **MUST:** folder names and entry naming = **project convention** (UseCase, Handler, Service, Command, plain `fn` — см. Pattern Catalog).
- **MUST:** inside each role, group by **capability** when ≥2 directions exist — [A05a](#prime-a05a--package-cohesion). Layer purity alone is **not** done.
- **MUST:** one application entry = one process (thin orchestrator); status mutation delegated to entity methods — not a second god-procedure.
- **SHOULD NOT:** CQRS / extra layers for trivial CRUD ([B01](#prime-b01--cqrs), [B07](#prime-b07--yagni)).
- **MUST NOT:** ORM types / SQL in core/domain ([A35](#prime-a35--contract-surface) · `import-graph-gate`).
- **MUST NOT:** порт без вызова из application — dead abstraction ([A36](#prime-a36--live-surface)).

**Thin transport:** route/handler validates → calls injected application entry → maps outcome. (Stack samples: [Pattern Catalog](#pattern-catalog--stack-native-equivalents).)

**MAY:** validation types as data-only (Pydantic, zod) — not framework coupling in core.

### Rich domain / Anti-anemic (PRIME+) — When entity has lifecycle/status

**Outcome:** инвариант живёт **в типе**, который владеет данными — не в сеттере снаружи и не в UC-процедуре.

| | Rich (PASS) | Anemic (FAIL) |
|--|-------------|---------------|
| Status | `user.activate()` / `order.submit()` проверяет граф переходов | `user.status = 'active'` в UC / handler / «service» |
| Invariant | метод сущности/VO бросает named Err или возвращает Result | публичный `setStatus` без правил; «валидация потом в сервисе» |
| Persistence | adapter гидрирует сущность из ряда; **бизнес-запись** всё равно через метод | ORM entity с public fields, UC пишет колонки напрямую |

- **MUST:** entity/VO with lifecycle **exposes behavior methods** that enforce invariants ([B02](#prime-b02--solid--grasp) Information Expert · [B06](#prime-b06--fsm)).
- **MUST NOT:** public field-assign or anemic setter of status/state from application/presentation.
- **MUST NOT:** treat «слои зелёные» as done while the entity is a DTO bag.
- **MAY:** data-only DTO at **boundary** (request/response/ORM row) — map into rich type before mutation.
- **When NOT:** CRUD DTO without lifecycle; primitive config structs; generated OpenAPI models at the edge.
- **Enforced by:** `anemic-mutation-gate` · `fsm-transition-gate` (When status graph) · `immutability-gate` (When shared aggregate).

### Immutability (PRIME+) — When races / FSM / shared aggregate

- **When:** single-threaded script, DB-only state, no shared in-memory aggregate → **N/A** (persist in repo layer OK).
- **When:** concurrent access, FSM, in-memory shared state → **MUST** immutable transitions or equivalent (new instance, copy, persistent data structure).
- **MUST NOT:** in-place mutation of shared aggregate passed between threads/tasks without synchronization + ADR.
- **Enforced by:** `immutability-gate` · [B06](#prime-b06--fsm) (When status entity).

---

## PRIME-A05a — Package cohesion

*High Cohesion as **package topology** — thematic folders by capability. Complements layer roles ([A05](#prime-a05--layer-law)); does **not** replace them. SSOT for this vibe.*

**Min tier:** STANDARD+ **MUST** when ≥2 capabilities or domain is growing; LITE / single-capability spike → **N/A** or `package_form: flat_ok` + sunset ADR  
**Aligns:** ISO 25010 **Maintainability** (modularity, analysability, modifiability) · CISQ **Maintainability** (coupling / scattered change)  
**Enforced by (PRIME+):** `package-cohesion-gate` (`architecture.cohesion_mode`: `off` | `warn` | `fail`) · design artifact `capability_slices`

### Outcome

One capability together (mirrored slices or feature package). Flat dump + green import-graph = **FAIL**.

### Two Skin-native forms

| Form | Shape | When |
|------|-------|------|
| **Mirrored slices** | `domain/<cap>/`, `application/<cap>/`, `infrastructure/<cap>/`, `api/<cap>/` | Horizontal layers already exist — add capability subfolders |
| **Feature packages** | `features/<cap>/{domain,app,infra,api}/` · Nest module · Nx lib · Go `internal/<cap>` | Vertical packaging is Skin |

**MUST NOT** invent a third universal tree if Skin already chose one of these.

**Catalog sample — not a third MUST form.** Textbook Clean/hex is **one** Skin equivalent in [Pattern Catalog](#pattern-catalog--stack-native-equivalents). Nest/Rails/Go Skin stays; husky/Prettier/Pino = Skin tooling — not Empire MUST brands.

### Rules

- **MUST:** new capability → own package/slice (or extend existing capability package) — not orphan files in flat `domain/` / `services/` / `ports/`.
- **MUST:** when introducing a **second** capability into a formerly flat dump → introduce package boundaries in the **same** change set (or ADR + tracked move PR); do not widen the dump.
- **MUST:** layer law still holds **inside** packages ([A05](#prime-a05--layer-law)) — feature folder is not an excuse for domain→SQL.
- **MUST:** cross-capability dependencies only via public contracts / DTO / events / primitives ([A04](#prime-a04--integration--plugin-boundaries)).
- **MUST:** design artifact lists `capability_slices` + `package_form` before code ([AGENT-OMEGA](#agent-omega--execution-phases-before-any-code) PHASE 1).
- **MUST:** `prime_check.config.yaml` → `architecture.capabilities` + `package_form` reflect reality (agent fills at bootstrap / when slices appear).
- **SHOULD:** co-locate capability-owned ports/adapters with that capability; **MAY** keep a thin shared `ports/` / `contracts/` only for truly shared abstractions (+ ADR if non-obvious).
- **MUST NOT:** treat «roles, not mandatory folder tree» ([A05](#prime-a05--layer-law)) as license for **thematic flat dump**.
- **MUST NOT:** over-split (one micro-package per file / premature Nx for CRUD) — [B07](#prime-b07--yagni).
- **MUST NOT:** confuse with [A04](#prime-a04--integration--plugin-boundaries): A04 = no **private type** leaks across modules/services; A05a = **where files live** inside one deployable.
- **MUST NOT:** treat textbook Clean folder names as the only legal Skin.

### Good / Bad

```text
# BAD — flat dump        # GOOD — mirrored / feature
domain/order.py          domain/orders/…  OR  features/orders/{domain,app,…}
domain/invoice.py        domain/billing/…
ports/  # every port bag # capability-local ports
# BAD — rewrite Nest/Rails/Go into textbook domain/entities «для PRIME»
```

### When N/A

- LITE scripts; single-capability app that fits one package; greenfield spike with `flat_ok` + sunset date in ADR.
- **When** growing past one capability → cohesion becomes **MUST**; ratchet `cohesion_mode` toward `fail` at PRIME+.

---

## PRIME-A06 — DI & ports

*Injectable dependencies via **explicit contracts** — framework DI OK for wiring; does **not** cancel Port requirement. SSOT for contract families: [A35](#prime-a35--contract-surface).*

**Min tier:** PRIME+ **Enforced by:** `di-purity` · `port-surface-gate` · `composition-root-gate` · `port-test-double-gate` · `deterministic-runtime` (with [A15](#prime-a15--deterministic-time))

- **MUST:** external deps (DB, HTTP, time, ID, random, config, mail, queue, payments…) — **injectable** через **явный Port** (Protocol / interface / trait / abstract / Skin token) — даже при **одной** реализации.
- **MUST:** application/core signatures принимают **port types**, не concrete infra (`PostgresOrderRepo`, `StripeClient`, `httpx.AsyncClient`).
- **MUST:** one canonical impl per policy — SSOT, not duplicate helpers ([A08](#prime-a08--anti-fork)).
- **MUST:** cross-module via published API — DTO/primitives/events ([A04](#prime-a04--integration--plugin-boundaries)).
- **MUST:** tests substitute via **Fake/InMemory against Port** — not mock of concrete adapter class ([A35](#prime-a35--contract-surface)).
- **MUST:** concrete adapters constructed / bound **only** in composition root (`main`, DI module, Nest module, Spring config) — [A35](#prime-a35--contract-surface).
- **SHOULD:** place capability-owned port + adapter **with that capability** ([A05a](#prime-a05a--package-cohesion)); shared kernel ports only when truly shared.
- **MUST NOT:** `new ConcreteRepo()` / hardcoded clients inside testable core.
- **MUST NOT:** service locator, globals, hidden mutable state in core.
- **MUST NOT:** treat «framework `@Injectable` concrete» as substitute for Port in core/app type signatures.
- **MAY:** framework-native DI (Nest `@Injectable`, Spring `@Autowired`, FastAPI `Depends`) — **wires Port → Adapter**; Port type still required.

---

## PRIME-A07 — Design-first order

**Min tier:** PRIME+ **When:** any PRIME+ feature **Enforced by:** DoD-only ([A13](#prime-a13--definition-of-done) + OMEGA PHASE 1 — order is process, not an AST step)  
**Applicability:** logical order — names = repo-native

0. Tier + triggers + existing patterns + **capability_slices / package_form** ([A05a](#prime-a05a--package-cohesion)).  
1. Contract/DTO + invariants; SemVer if breaking ([A21](#prime-a21--semver--contracts)); fill **`contract_surface_map`** ([A35](#prime-a35--contract-surface)).  
2. Core rules + **outbound/inbound ports** — **in the capability package**, not flat dump. Status entities get **behavior methods**. If this **behavior already exists** → **call owner**; do not clone ([A39](#prime-a39--behavior-ssot)). For touched protected ops → declare `trust_pipeline_map` ([A41](#prime-a41--trust-pipeline)).  
3. Application entry + explicit errors (expected vs unexpected, [A10](#prime-a10--result)) + deps typed as **ports**.  
4. Versioned migration if schema ([A20](#prime-a20--migrations)).  
5. Infrastructure **adapters** implementing ports — capability-local when possible; wire in composition root.  
6. Presentation — transport only — same capability slice.  
7. Tests: unit **against Fake ports** → integration against real adapters → contract/E2E + **applicable A12a families** ([A12](#prime-a12--tests--coverage), [A12a](#prime-a12a--test-taxonomy)) + ADR if contracts change.

---

## PRIME-A08 — Anti-fork & policy facades

**Min tier:** PRIME+ **Enforced by:** `anti-fork-gate` · `behavior-ssot-gate` ([A39](#prime-a39--behavior-ssot))

- **MUST NOT:** second auth validator / idempotency handler / error mapper / `*_v2` fork; copy-paste validation.
- **MUST:** structural clone of a policy/algorithm (renamed vars, extra log line) **is a fork** even without `*_v2` — one owner, N call sites ([A39](#prime-a39--behavior-ssot)).
- **MUST:** authorize / validate / safe_path facades preferred owners for Trust Pipeline ([A41](#prime-a41--trust-pipeline)).
- **MUST:** extend canonical facade; auth/payments/state-changing — via facades (When applicable).
- **MUST NOT:** bypass facade from endpoint/UC «for convenience».
- **See:** [A14](#prime-a14--idempotency) · [A39](#prime-a39--behavior-ssot) · [A41](#prime-a41--trust-pipeline).

## PRIME-A09 — Policy facades

*Index alias — **merged into [A08](#prime-a08--anti-fork--policy-facades).** No separate body.*

**Min tier:** PRIME+ **When:** same as A08 **Enforced by:** `anti-fork-gate` · `behavior-ssot-gate` (via A08)  
**See:** [A08](#prime-a08--anti-fork--policy-facades) · [A14](#prime-a14--idempotency) · [A39](#prime-a39--behavior-ssot)

---

## PRIME-A10 — Result & errors by tier

*Explicit failure paths — stack-native; `Result` is one option ([Pattern Catalog](#pattern-catalog--stack-native-equivalents)).*

**Min tier:** varies — see table **Enforced by (PRIME+):** `anti-null-gate` · `err-variant-gate` · `error-context-gate` · `no-transport-in-domain` · `no-swallow-gate` ([A37](#prime-a37--honest-errors--no-swallow))

### Expected vs unexpected (PRIME+)

| Kind | Examples | Where | Form |
|------|----------|-------|------|
| **Expected business** | `EmailTaken`, illegal FSM | **core/app** named Err | tested (`err-variant-gate`) |
| **Unexpected infra** | DB down, timeout | **adapter** → **one** presentation handler | **MUST NOT** try/catch forest in UC / swallow as Ok |

- **MUST:** expected failures **named** in contract; unexpected I/O propagates to single presentation handler.
- **MUST NOT:** transport exceptions in core; catch-all that hides infra crash.

### Error handling by tier

| Tier | Approach |
|------|----------|
| **LITE** | Clear messages; fail-fast |
| **STANDARD** | Typed errors; do not swallow |
| **PRIME+** | Named domain errors; explicit failure paths (Pattern Catalog) |
| **Boundary** | User-friendly message; details in log only |

### Explicit errors (PRIME+)

**Outcome:** caller always knows success vs failure — no silent `null` as error.

Acceptable forms = Skin: `Result`/`Either`/`(T,error)`/sealed/typed exception — see Pattern Catalog.  
- **MUST:** presentation maps outcome → response **or** GUI toast; log with `invariant_id` When log sink (`N/A(no log sink)` + toast OK on tray).
- **MUST:** every expected Err **provokes production path** (`err-variant-gate`) — not id-string assert alone.
- **MUST NOT:** swallow process-boundary Result — [A37](#prime-a37--honest-errors--no-swallow).

### No silent null (`anti-null-gate`)

- **MUST NOT:** nullable return in application/core as sole error/absence signal.
- **MUST:** explicit branch (`match` / `if err` / checked exception).
- **MAY:** `Option` for optional data; nullable in ORM glue + ADR.

### Observable failures

- **MUST** at failure: `invariant_id` + safe context (no PII); `correlation_id` When log sink ([B03](#prime-b03--sre--observability--events)).
- **MUST (desktop/tray):** mapped error → user-visible toast ([B11](#prime-b11--client-apps)).

---

## PRIME-A11 — Decomposition

**Min tier:** STANDARD+ **Enforced by:** `file-size-guard` · `cyclomatic-gate` · `dead-code-gate` · `behavior-ssot-gate` (fake-split) · `package-cohesion-gate` When flat dump  
**Aligns:** ISO 25010 **Maintainability** · CISQ **Maintainability** · [A39](#prime-a39--behavior-ssot)

- **SHOULD:** ≤120 lines per file.
- **MUST:** file >200 → decompose or document exception; >300 → block.
- **MUST:** function >40 → extract; cyclomatic >10 → refactor.
- **MUST:** if code is hard to test — violates PRIME; split until testable ([A12](#prime-a12--tests--coverage)).
- **MUST:** if change set touches unrelated capabilities in one flat bag → split into capability packages ([A05a](#prime-a05a--package-cohesion)) — decomposition is **packages**, not only smaller files.
- **MUST:** decompose by extracting the repeated **behavior** to **one owner**, then shrink leftovers ([A39](#prime-a39--behavior-ssot)). **Compress ≠ split.**
- **MUST NOT:** satisfy file-size / cyclomatic by **cloning** logic into a new file (fake-split → `behavior-ssot-gate` FAIL).
- **MUST NOT:** interpret >40 lines as «copy into helpers **and** keep original» without deleting the duplicate.
- **MUST NOT:** fake split duplicating policy into utils.
- **MUST NOT:** «decompose» by dumping more files into the same flat layer root.

---

## PRIME-A12 — Tests & coverage (ZERO untested code)

**Min tier:** PRIME+ for 100% gate; STANDARD+ for pyramid **Enforced by:** `coverage-*` · `test-taxonomy-gate` · matrix gates ([A12a](#prime-a12a--test-taxonomy))  
**Kinds of tests:** [A12a](#prime-a12a--test-taxonomy) = SSOT.

**Doctrine:** нет непокрытых строк/веток в scope **и** нет applicable family без named test / `N/A(reason)`. Coverage без taxonomy = vanity. Unit (**against Fake ports**) → integration (**real adapters**) → E2E UI **или** contract@boundary (API-only).

| Tier | Coverage |
|------|----------|
| LITE | Smoke only |
| STANDARD | ≥80% + unit/boundary; migrate to PRIME |
| **PRIME greenfield** | **100%** line+branch `runtime_scope` + taxonomy green |
| **PRIME legacy** | **100%** changed files + ratchet ([A31](#prime-a31--legacy-adoption)) |
| **CRITICAL** | PRIME + `mutation-critical` ≥95% + fuzz/property When |

- **MUST:** unit first; regression `test_regression_*` per bug fix; TDD ([A24](#prime-a24--tdd-lock)); quality ([A27](#prime-a27--test-quality)).
- **MUST NOT:** E2E-only; browser E2E на API-only; 99.x%; тесты «потом»; happy-path-only.

---

## PRIME-A12a — Test Taxonomy

*SSOT for **which** tests Empire requires. Coverage % ≠ taxonomy complete. Form of runner = Skin; families below = Engine.*

**Min tier:** STANDARD+ (core families); **full matrix PRIME+** per When-column  
**Aligns:** ISO 25010 Functional suitability · Reliability · Security · Maintainability  
**Enforced by:** `test-taxonomy-gate` · `test-matrix-gate` · `route-matrix-gate` · `zta-matrix-gate` · `boundary-value-gate` · `negative-path-gate` · `scenario-matrix-gate` · `fsm-transition-gate` · `regression-lock` · `injection-fuzz` · `pytest-property` · `mutation-critical` · `coverage-branch-100`

### Doctrine

Агент **MUST** перед кодом заполнить `test_taxonomy_map` в design artifact ([AGENT-OMEGA](#agent-omega--execution-phases-before-any-code)). Для каждого family: **named tests** **или** `N/A(<trigger absent>)`.  
**MUST NOT:** «напишу unit — остальное потом».  
**MUST NOT:** требовать *все* families на каждый CRUD — колонка **When** нормативна.  
**MUST:** если When сработал — family **обязателен** и **APPLIED только с нетривиальным оракулом** (тело теста ломается, если поведение соврало). Имя `test_err_*` без вызова продакшен-пути ≠ APPLIED.

### Anti-N/A

**SSOT:** [Doctrine Anti-N/A](#anti-na-ssot--один-раз). Taxonomy-specific: `N/A(no auth|no FSM|no I/O|…)`. «При сомнении» → [Conflict Matrix](#conflict-matrix-при-сомнении--читать-это-не-конкурирующие-абзацы) (триггер → включи family; vanity names → не плоди).

### 1. Пирамида — логика и стабильность

| Family | Outcome (что проверяет) | Min tier | When (trigger) | Gate / naming |
|--------|-------------------------|----------|----------------|---------------|
| **Unit** | Отдельные функции/компоненты в изоляции; крайние значения; **Fake ports**, не mock concrete | STANDARD+ | Always for new/changed logic | `pytest-unit` / jest · most tests |
| **Integration** | Связка компонентов; реальная БД; внешние API/clients (**real adapters**) | PRIME+ | UC/touch touches DB, queue, HTTP client, filesystem | `pytest-integration` · real infra |
| **E2E** | Действия пользователя; цепочки UI; развилки сценариев | PRIME+ | **UI / client app** in scope ([B11](#prime-b11--client-apps)) | `e2e-ui` **runs** (not `#[ignore]`); else `skipped_steps` per test + ADR. AC with hwnd/pixels oracle **cannot** close via unit name while E2E ignored |
| **Contract@boundary** | Полный API/CLI/RPC stack без браузера | PRIME+ | Exposed operation, **no UI** (or in addition to E2E) | `pytest-contract` · `route-matrix-gate` |

**API-only:** Contract@boundary **заменяет** browser E2E (тот же уровень пирамиды). **MUST NOT** добавлять Selenium «для галочки».

**Test layout = Skin.** `tests/unit|integration|e2e` vs colocate (`__tests__/`, `*_test.go`, `foo_spec.rb` рядом с кодом) — Engine = **families** в таблице, не имена папок. Lint/format/log/CI hooks (husky, Prettier, Pino, Winston, ruff) = Skin-native ([A17](#prime-a17--clean-code), [B03](#prime-b03--sre--observability--events), [A22](#prime-a22--prime-check)) — **не** Empire MUST-бренды.

### 2. Надёжность — чтобы код не сломался

| Family | Outcome | Min tier | When | Gate / naming |
|--------|---------|----------|------|---------------|
| **Regression** | Старый баг не возвращается; гоняется на каждом обновлении | STANDARD+ | **Every bug fix** | `regression-lock` · `test_regression_*` |
| **Mutation** | Качество *самих* тестов; слепые зоны | **PRIME greenfield MUST** on `critical_scope`; CRITICAL ≥95% | FSM, parsers, money, hotkey/crop/naming core | `mutation-critical` ([A28](#prime-a28--mutation-prime)). `enabled: false` на greenfield PRIME = FAIL |
| **Property-based** | Случайные входы; математические/инвариантные свойства | PRIME+ | Parsers, crypto, money, serialization, idempotency invariants | `pytest-property` / hypothesis / fast-check ([B12](#prime-b12--fuzz--property)) |

### 3. Безопасность — защита от взлома

| Family | Outcome | Min tier | When | Gate / naming |
|--------|---------|----------|------|---------------|
| **Injection (SQLi / XSS / cmd)** | Фильтрация опасного ввода; эмуляция атак | PRIME+ | Untrusted input surface (HTTP body/query, uploads, HTML) | `injection-fuzz` · `no-string-sql` ([A18](#prime-a18--owasp-input-hygiene)) |
| **Access control** | Роли/права; нет доступа к чужим данным | PRIME+ | Authn/authz / multi-tenant / protected ops | `zta-matrix-gate` ([A02](#prime-a02--zero-trust), [A29](#prime-a29--zta-matrix)) |
| **Contract (schema)** | Строгий формат данных; защита от подмены структуры API | PRIME+ | Public/API schema or inter-service contract | `api-contract-drift` · `snapshot-contract` · `route-matrix-gate` ([A03](#prime-a03--api-response-contract), [A21](#prime-a21--semver--contracts)) |

### 4. Бизнес-сценарии

| Family | Outcome | Min tier | When | Gate / naming |
|--------|---------|----------|------|---------------|
| **Scenario** | Сквозные цепочки (напр. auth → выбор → оплата) | PRIME+ | Multi-step business flow / checkout / onboarding | `scenario-matrix-gate` · `test_scenario_*` |
| **BDD** | Сценарий человеческим языком **Given → When → Then** | PRIME+ | Same as scenario/acceptance — **форма** описания | Skin: Cucumber/Behave **или** GWT в имени/docstring теста — **не** обязателен отдельный фреймворк |
| **Acceptance** | Критерии готовности фичи из задачи/PRD выполнены | PRIME+ | Любая user-facing / API feature с acceptance criteria | Каждый criterion → named test; `test-matrix-gate` |

### 5. Разветвления и логика

| Family | Outcome | Min tier | When | Gate / naming |
|--------|---------|----------|------|---------------|
| **Path coverage** | Все ветки if/else; редкие комбинации; нет мёртвого кода | PRIME+ | Always on `runtime_scope` / changed files | `coverage-branch-100` ([A25](#prime-a25--coverage-absolute)) |
| **Boundary value** | Стыки условий: `0`, `-1`, `null`/empty, max, `>` vs `>=` | STANDARD+ | Validators, ranges, lengths, money, dates, statuses | `boundary-value-gate` · `test_*_boundary_*` / parametrize edges |
| **State transition** | Легальные/запрещённые переходы статусов; нет тупиков | PRIME+ | Entity with lifecycle / `fsm_transitions` in design | `fsm-transition-gate` ([B06](#prime-b06--fsm)) · legal + illegal edges |

### 6. Устойчивость бизнес-логики

| Family | Outcome | Min tier | When | Gate / naming |
|--------|---------|----------|------|---------------|
| **Negative** | Намеренно ломает процесс; обрыв связи; откат транзакции; invalid input | PRIME+ | State-changing ops, I/O, auth, payments | `negative-path-gate` · `test_*_rejects_*` / `test_*_rollback_*` |
| **Fuzz (logic / input)** | Хаотичные комбинации действий/входов; стресс логики | PRIME+ SHOULD; CRITICAL MUST on boundaries | Complex branching, parsers, external input | `injection-fuzz` · property/fuzz suites ([B12](#prime-b12--fuzz--property)) |
| **Observability** | Failure path пишет/проверяет trace + invariant_id + safe context | PRIME+ | New/changed Err variant or failure log path | `error-context-gate` · test asserts log/span fields ([B03](#prime-b03--sre--observability--events)) |

### Enough vs too much (нормирующие примеры)

| Задача | Достаточно (APPLIED) | Слишком / запрещено |
|--------|----------------------|---------------------|
| CRUD поле без auth, API-only | unit + boundary + contract + negative(invalid) + path; N/A(no auth, no FSM, no UI) | Playwright + mutation + full fuzz «на всякий» |
| Checkout: auth → cart → pay | unit + integration + scenario + BDD/AC **oracles** + access_control + negative | Только unit happy-path |
| Status entity | state_transition + entity methods | `user.status =` в UC + только happy-path |
| Desktop + hotkey + capture | integration adapter (real PNG/mutex) + E2E **running** or skipped_steps; AC hwnd oracle | 14 `test_err_*` string tests + unused port + `#[ignore]` e2e |
| Bugfix off-by-one | regression + boundary + path; N/A(no new API) | Новый E2E suite без `test_regression_*` |
| New Err variant | UC/Fake **провоцирует** вариант + observability | `assert_eq!(id, "CaptureTimeout")` без вызова адаптера |

### Agent algorithm (MUST)

```text
1. List triggers from task (auth? I/O? UI? FSM? money? bugfix? multi-step?)
2. Mark each A12a family applicable | N/A(reason) in test_taxonomy_map
3. For each applicable family → ≥1 failing test (TDD) with naming from table
4. Implement → keep tests red→green
5. prime_check: test-taxonomy-gate + related matrix gates → exit 0
```

### Anti-patterns (MUST NOT)

Only unit при API/DB/auth · only E2E без unit · happy-path без negative/boundary · coverage 100% + empty taxonomy map · naked N/A ([SSOT](#anti-na-ssot--один-раз)) · mutation skip на PRIME greenfield · Cucumber-as-MUST · browser E2E на API-only · AC closed by test **name** ([A34](#prime-a34--intent-lock)) · 14 err-string + unused port + ignored e2e · `#[ignore]` без skipped_steps · blast outside [A33](#prime-a33--blast-radius) · force `tests/unit|e2e` tree when repo colocates.

---

## PRIME-A13 — Definition of Done

**Min tier:** PRIME+ **Enforced by:** `prime_check` FULL exit 0 + evidence ([A22](#prime-a22--prime-check), [A26](#prime-a26--evidence-block)) — AGENT-2 is a **subset** of this checklist

- **MUST NOT:** duplicate policy/mapper/facade **or** second copy of the same algorithm without calling owner ([A08](#prime-a08--anti-fork--policy-facades), [A39](#prime-a39--behavior-ssot)).
- **MUST:** thin transport + injected application entry typed against **ports** + explicit error mapping ([A35](#prime-a35--contract-surface)).
- **MUST:** new/changed code in correct **capability package/slice** ([A05a](#prime-a05a--package-cohesion)); design artifact lists slices.
- **MUST:** `test_taxonomy_map` complete; Anti-N/A green ([A12a](#prime-a12a--test-taxonomy), [SSOT](#anti-na-ssot--один-раз)).
- **MUST:** `contract_surface_map` complete **and live** ([A35](#prime-a35--contract-surface), [A36](#prime-a36--live-surface)).
- **MUST:** every AC has **oracle** + test body asserts it ([A34](#prime-a34--intent-lock)).
- **MUST:** no swallowed process I/O; err-variant provokes production path ([A37](#prime-a37--honest-errors--no-swallow)).
- **MUST:** `checker-integrity-gate` green ([A38](#prime-a38--checker-integrity)).
- **MUST:** `behavior-ssot-gate` GREEN or `N/A(no cluster)` ([A39](#prime-a39--behavior-ssot)).
- **MUST:** Secure Continuum gates GREEN or honest N/A; no secrets in evidence ([A40](#prime-a40--secure-continuum)).
- **MUST:** Trust Pipeline gates GREEN or honest N/A; IDOR oracles When multi-user ([A41](#prime-a41--trust-pipeline)).
- **MUST:** diff inside declared `blast_radius` or justified expansion ([A33](#prime-a33--blast-radius)).
- **MUST:** update API docs / ADR if contracts changed; breaking → major + contract + migration tests ([A21](#prime-a21--semver--contracts)).
- **MUST:** tests per [A12](#prime-a12--tests--coverage) + [A12a](#prime-a12a--test-taxonomy); formatters green; migrations versioned ([A20](#prime-a20--migrations)).
- **MUST:** Threat Model mini if security-sensitive ([A16](#prime-a16--secure-by-design)).

**Coverage ZERO (PRIME+):**

| Metric | Greenfield | Legacy (A31) |
|--------|------------|--------------|
| Line + branch | **100.00%** `runtime_scope` | **100.00%** changed files |
| Ratchet vs `main` | must not decrease | must not decrease |
| Uncovered `Err` / matrix / auth gaps on touch | **0** | **0** |

**LITE only:** smoke; no 100% gate.

---

## PRIME-A14 — Idempotency

**Min tier:** PRIME+ **When:** state-changing operation + retry/double-submit risk **Enforced by:** `idempotency-matrix-gate`

**Outcome:** повторный вызов с тем же intent → **тот же результат**, без дубля side-effect.  
**Не обязательна форма:** ledger class — достаточно unique index, dedup table, Stripe-style key store, saga idempotency token.

### When REQUIRED

- payments, charges, posts, orders, webhooks, any mutation user can trigger twice (double-click, retry, at-least-once delivery)
- **NOT required:** idempotent reads, pure deletes with no money, internal batch with exactly-once framework guarantee + ADR

### Implementation options (pick one + test)

| Approach | Where |
|----------|-------|
| `Idempotency-Key` header + server dedup store | HTTP APIs |
| Unique DB constraint on `(idempotency_key)` | Persistence layer |
| Ledger / WAL table `(key → outcome)` | Application layer |
| Client-generated stable token per user action | Mobile/UI |

- **MUST:** stable key per user action across retries — не random per retry.
- **MUST:** dedup check **before** irreversible side-effect (or transactional outbox).
- **MUST (CRITICAL):** all financial mutations idempotent.
- **MUST (PRIME+):** каждый state-changing UC — `test_double_submit_*` / `test_idempotency_replay_*` ([A14](#prime-a14--idempotency), `idempotency-matrix-gate`) — taxonomy **negative** + integration.
- **Enforced by:** `idempotency-matrix-gate` — double-submit test: два вызова, один key → один side-effect, второй = same outcome.

---

## PRIME-A15 — Deterministic time

**Min tier:** PRIME+ **Enforced by:** `deterministic-runtime` · `port-surface-gate`  
*Side-Effect Injection — сквозной инвариант вместе с [A06](#prime-a06--di--ports) · [A35](#prime-a35--contract-surface).*  
**Aligns:** ISO 25010 **Reliability** · CISQ **Reliability** · MISRA/CERT **predictability**

`now()` / `uuid4()` / `random()` в testable core → flaky tests. **Outcome:** same inputs + fixed clock/ID/random in tests → same output.

- **MUST NOT:** direct `Date.now()`, `uuid4()`, `random()` in **testable core** (scope from config — not necessarily `domain/` path).
- **MUST:** inject via **outbound ports** — `IClock` / `IIdGenerator` / `IRandom` (or Skin equiv) — listed in `contract_surface_map.outbound_ports`.
- **MAY:** framework test utilities (`vi.setSystemTime`, frozen clock) **in tests**; production core still depends on port.
- **MUST NOT:** global singleton clock/random on core path without test override.

**`deterministic-runtime`:** ban direct nondeterminism calls in configured `testable_core_scope` paths.

---

## PRIME-A16 — Secure-by-design

**Min tier:** all* — full at PRIME+ **Enforced by:** `no-debug-bypass` · `pii-log-scan` · `gitleaks-history` · `dependency-audit` · `bandit`/`npm-audit` · Threat Model in design artifact (DoD) · [A18](#prime-a18--owasp-input-hygiene) · [A40](#prime-a40--secure-continuum) · [A41](#prime-a41--trust-pipeline)  
**Aligns:** ISO 25010 **Security** · OWASP Top 10 **A04 Insecure Design** · ASVS V1 Architecture

### Threat Model mini (CRITICAL / security touch / **any Default-secure YES**)

- **MUST:** assets, untrusted boundaries, verify points, top-5 threats, failure scenarios — When CRITICAL **or** any Default-secure 5Q answer is YES (CRUD with id/PATCH counts).
- **MUST:** map each threat → OWASP Top 10 category + PRIME rule ID + gate that closes it ([A18](#prime-a18--owasp-input-hygiene), [A40](#prime-a40--secure-continuum)).
- **MUST:** When CI or chat/agent channels exist — list **CI compromise** and **secret-exfil via chat** as threats with closing gates (`ci-harden-gate`, `channel-secret-gate`).
- **MUST:** When app surface — map top threats to [A41](#prime-a41--trust-pipeline) gates (IDOR, mass-assign, injection, path, token).
- **MUST (CRITICAL):** ASVS-relevant chapters listed in design artifact (auth, session, access control, data protection).
- **SHOULD:** STRIDE or equivalent lightweight frame — outcome = traceable threats, not slide deck.
- **MUST NOT:** «не CRITICAL → Threat Model N/A» при exposed op / resource id / client body.

### Security rules (all tiers)

- **MUST:** secrets via env/vault only — never in code, **evidence, chat, or CI logs** ([A40](#prime-a40--secure-continuum)).
- **MUST:** validate/sanitize input at boundary; authorize/sanitize = one owner When N≥2 ([A39](#prime-a39--behavior-ssot)).
- **MUST:** least privilege for services, users, API keys, **and CI workflows**.
- **MUST NOT:** log PII, passwords, tokens, full PAN/card numbers.
- **MUST NOT:** ignore known **high/critical** CVE — `dependency-audit` blocks merge ([A19](#prime-a19--supply-chain)).
- **MUST:** `gitleaks` + `bandit`/`npm-audit` green in prime_check before merge.
- **MUST NOT:** treat `security.md` checklist without Enforced-by gate as done ([A38](#prime-a38--checker-integrity), [A40](#prime-a40--secure-continuum)).

### Security MUST NOT

- Roll-your-own crypto; secrets in git; debug auth bypass (`no-debug-bypass` gate).
- New auth/payment path without docs/ADR + contract tests.
- Implicit network trust ([A02](#prime-a02--zero-trust), [A23](#prime-a23--infra--docker-security), [A40](#prime-a40--secure-continuum)).
- **MUST:** every security invariant = test from taxonomy (**injection** + **access_control** + **negative**) ([A12a](#prime-a12a--test-taxonomy)); every auth route = ZTA matrix ([A29](#prime-a29--zta-matrix)).
- **MUST NOT:** insecure code «пофиксим потом» — prime_check red → **fix until green**.
- **MUST NOT:** ship auth/payment without contract + access_control + negative families.

---

## PRIME-A17 — Clean code & patterns

**Min tier:** STANDARD+ **Enforced by:** `lint` · `typecheck` · `format-check` · `handler-purity-gate` · `anti-fork-gate` · `behavior-ssot-gate`  
**See:** [B02](#prime-b02--solid--grasp) · [A39](#prime-a39--behavior-ssot) · [A41](#prime-a41--trust-pipeline) Fail-Fast = Trust Pipeline step 1

### Core patterns

- **Fail-Fast** — validate at system **boundary** (API, CLI, form / DTO schema) = Trust Pipeline step 1 ([A41](#prime-a41--trust-pipeline)); data trusted inside the use-case. Presentation validates → UC; UC does **not** re-parse / re-trust the HTTP body.
- **No Magic Values** — constants in config, env, domain enum/type.
- **Generic DRY** — When **N≥2** of the **same behavior** (policy/algorithm), extract to one owner is **MUST** ([A39](#prime-a39--behavior-ssot)). When **N=1**, local OK — **MUST NOT** premature abstraction ([B07](#prime-b07--yagni)).
- **Rich types** — behavior with the data ([A05](#prime-a05--layer-law) Anti-Anemic); DTO bags stay at the edge.

### SOLID & GRASP — see [B02](#prime-b02--solid--grasp)

- **MUST:** ~10–15 orchestration lines per application entry (use case / handler / service method) — **delegate** to owners; do not re-implement.
- **MUST:** DRY for **policy**; duplicate wiring OK ([A08](#prime-a08--anti-fork--policy-facades)).
- **MUST:** project formatters before commit.
- **MUST NOT:** god-class; feature envy; god-`utils/` mixing unrelated behaviors ([A08](#prime-a08--anti-fork--policy-facades), [A05a](#prime-a05a--package-cohesion)).
- **MUST NOT:** unrelated capabilities in one god-package / flat layer dump ([A05a](#prime-a05a--package-cohesion)).

**Good:** thin `OrderService.place()` + `Order.submit()` + injectable `OrderRepository` **under `…/orders/`**.  
**Good:** one `retry_with_backoff` called from HTTP adapter **and** job runner.  
**Bad:** 400-line god-service — SQL, validation, HTTP mapping in one class.  
**Bad:** «правильные слои», но `domain/` = свалка Order+Invoice+Session без папок.  
**Bad:** `order.status = 'paid'` в сервисе при живом lifecycle.  
**Bad:** same money-round / authorize / hit-test copied into two UCs «чтобы не трогать shared».

---

## PRIME-A18 — OWASP input hygiene

**Min tier:** PRIME+ (validation STANDARD+)  
**Aligns:** OWASP Top 10 (2021) · OWASP ASVS V5 · ISO 25010 **Security** · CISQ **Security** pillar  
**Enforced by:** `no-string-sql` · `injection-fuzz` · `ssrf-gate` · `security-headers-gate` · `cors-csrf-gate` · `zta-matrix-gate` · `mass-assign-gate` · `path-escape-gate` · `session-token-gate` · `idor-ownership-gate` · `trust-pipeline-gate` · [A40](#prime-a40--secure-continuum) · [A41](#prime-a41--trust-pipeline)

- **MUST:** all external input untrusted until schema + auth + policy pass (HTTP, CLI args, WebSocket, file upload, webhooks, GraphQL variables…).
- **MUST:** schema at boundary (Pydantic, zod, Joi, protobuf validate…).
- **MUST:** parameterized SQL / prepared statements only — **no** string-built queries ([`no-string-sql`](#full-step-map--50-steps-mandatory-at-prime)).
- **MUST:** encode HTML output; CSP When web UI; allowlist redirects; validate uploads (type, size, path).
- **MUST:** path traversal blocked on file/upload paths When applicable.
- **MUST:** close **every applicable** OWASP Top 10 item for the surface — table below is normative, not checklist decoration.

| OWASP Top 10 | PRIME closure | Gate / test |
|--------------|---------------|-------------|
| **A01** Broken Access Control | [A02](#prime-a02--zero-trust) deny-by-default; **resource-scoped** authz; **one authorize owner** ([A39](#prime-a39--behavior-ssot)) | `zta-matrix-gate` · `idor-ownership-gate` · [A41](#prime-a41--trust-pipeline) |
| **A02** Cryptographic Failures | no custom crypto; TLS ≥1.2 prod; secrets not in code | `tls-min-version` · [A19](#prime-a19--supply-chain) |
| **A03** Injection | parameterized SQL; no shell with user input; fuzz | `no-string-sql` · `injection-fuzz` · taxonomy **injection** ([A12a](#prime-a12a--test-taxonomy)) |
| **A04** Insecure Design | Threat Model · design artifact · CI/chat threats When present | [A16](#prime-a16--secure-by-design) · [A07](#prime-a07--design-first) · [A40](#prime-a40--secure-continuum) |
| **A05** Security Misconfiguration | hardened docker; no debug prod; env validation; **CI least privilege**; headers When web | [A23](#prime-a23--infra--docker-security) · `prod-config` · `ci-harden-gate` · `security-headers-gate` |
| **A06** Vulnerable Components | lockfile; zero high/critical CVE | `dependency-audit` · `sbom` |
| **A07** Auth Failures | full scenario matrix per protected op | [A29](#prime-a29--zta-matrix) · `zta-matrix-gate` |
| **A08** Integrity Failures | signed deps policy; immutable deploy artifacts; pin CI actions When PRIME+ | [A19](#prime-a19--supply-chain) · `ci-harden-gate` |
| **A09** Logging Failures | structured logs; no PII/secrets; err context | [B03](#prime-b03--sre--observability--events) · `pii-log-scan` · `error-context-gate` · `channel-secret-gate` |
| **A10** SSRF | outbound URL allowlist; block metadata IPs | `ssrf-gate` |

**ASVS depth by tier** — см. [Quality Constellation](#quality-constellation--iso--cisq--owasp--cert-constitutional-layer). PRIME+ web/API **MUST** satisfy applicable ASVS L1–L3 verification items via gates above — not manual pen-test excuses.

- **MUST:** contract tests for malformed/hostile input on **every** boundary declared in design artifact.
- **MUST:** browser-facing → `cors-csrf-gate` GREEN or honest N/A ([A40](#prime-a40--secure-continuum)).
- **MUST:** Trust Pipeline for protected ops — mass-assign / path-escape / session-token / IDOR gates When triggers ([A41](#prime-a41--trust-pipeline)).
- **MUST NOT:** «мы используем framework → OWASP закрыт» без `zta-matrix-gate` / `injection-fuzz` / continuum / trust-pipeline gates green.

---

## PRIME-A19 — Supply chain & secrets

**Min tier:** all **Enforced by:** `gitleaks-history` · `no-secrets` · `dependency-audit` · `sbom` · `channel-secret-gate` · `ci-harden-gate` (When CI)

- **MUST:** deps via lockfile; no ad-hoc install without update + justification.
- **MUST:** secrets from env/store; never commit `.env`, keys, tokens.
- **MUST NOT:** hardcode `sk-…`, `Bearer …`, passwords in source/tests/**evidence/chat**.
- **MUST:** stop-the-line if secret committed **or leaked via CI log / chat** — rotate + revoke ([B14](#prime-b14--human-handoff), [A40](#prime-a40--secure-continuum)).
- **MUST:** `dependency-audit` — **zero high/critical CVE**; medium/low — fix or ADR with expiry.
- **MUST:** `gitleaks` in prime_check on every run.
- **MUST (PRIME+ When CI):** pin actions by SHA (or ADR); treat CI action supply chain as deps ([A40](#prime-a40--secure-continuum)).
- **MUST (When publish artifacts):** Skin-native provenance/attestation or ADR — not unsigned «потом».
- **MUST:** token handling follows `session-token-gate` — no token in query/logs ([A41](#prime-a41--trust-pipeline)).

---

## PRIME-A20 — Migrations

**Min tier:** PRIME+ **When:** persistence schema **Enforced by:** `migration-path-only` · `no-ddl-in-app` · `schema-drift`

- **MUST:** DDL only in versioned migrations; additive, numbered, idempotent.
- **MUST NOT:** DDL from UC/handlers; ORM `create_all()` on prod.
- **MUST:** multi-step mutations in one transaction (or outbox); FSM transitions atomic under concurrency ([B06](#prime-b06--fsm)).
- **MUST NOT:** long business logic in open transaction.

---

## PRIME-A21 — SemVer & contracts

**Min tier:** PRIME+ **Enforced by:** `api-contract-drift` · `snapshot-contract` · `route-matrix-gate`  
**Aligns:** taxonomy **contract** ([A12a](#prime-a12a--test-taxonomy)) · **API contract** family ([A35](#prime-a35--contract-surface)) · [A03](#prime-a03--api-response-contract)

### Contract sources

| Boundary | Tools (use what project has) |
|----------|------------------------------|
| **External API** | OpenAPI, GraphQL schema, JSON Schema, zod, pydantic |
| **Inter-service** | protobuf, shared types, codegen, gRPC/REST |
| **Internal ports** | Protocol/iface/trait — see [A35](#prime-a35--contract-surface) (not SemVer of public API, but still a contract) |

- **MUST:** public schema = contract; breaking = **MAJOR** + ADR + deprecation window.
- **MUST:** list API contracts in `contract_surface_map.api_contracts` when exposed ops change.
- **MUST (breaking):** contract tests + consumer migration note/tests in **same PR** — не «docs later».
- **MUST NOT:** silently change status/error codes / field types / auth requirements.

| Change | SemVer | Action |
|--------|--------|--------|
| Add optional field | MINOR | Docs + contract test |
| New endpoint | MINOR | Docs + contract test |
| Remove field / change auth | MAJOR | ADR + deprecation + migration test + contract |
| Rename error code | MAJOR | Migration guide + tests |

---

## PRIME-A22 — Prime Check (merge gate)

*Quality gate contract — stack-native entrypoint; Python `prime_check` = reference. Spec: [AGENT-5](#agent-5--prime-check).*

**Min tier:** PRIME+ **Enforced by:** AGENT-5 FULL step map (Law→Gate) · [A38](#prime-a38--checker-integrity)

### MUST / MUST NOT

- **MUST:** gate exists + config + CI; else agent bootstraps FULL **before** feature; agent owns steps/deps/run/fix.
- **MUST:** Law→Gate; FULL matrix + `--diff` + evidence before done; CI ≡ local.
- **MUST:** coverage 100% line+branch+diff+ratchet; architecture + port/live/no-swallow/checker/behavior-ssot; OWASP via [A18](#prime-a18--owasp-input-hygiene); continuum/trust When triggers ([A40](#prime-a40--secure-continuum), [A41](#prime-a41--trust-pipeline)); `ffi-safety-gate` When FFI on **PRIME**.
- **MUST NOT:** done with exit ≠ 0 · stub `pass` steps · ask user to run/configure · 99.x% · exclude without ADR+sunset · CI≠local.

**LITE scripts only:** exempt.

---

## PRIME-A23 — Infra & Docker security

**Min tier:** PRIME+ **When:** containerized deploy or Docker files in repo **Enforced by:** `docker-security`, `compose-security`, `prod-config`, `iac-scan-gate` (When broader IaC), `ci-harden-gate` (When CI)

### Docker MUST

- **MUST:** run as **non-root** `USER` in Dockerfile.
- **MUST NOT:** `--privileged`, `cap_add: [SYS_ADMIN]`, mount `/var/run/docker.sock`.
- **MUST NOT:** secrets as `ARG`/`ENV` in image — runtime injection only.
- **MUST NOT:** `latest` tag in prod without pin digest ADR.

### Compose / runtime MUST

- **MUST NOT:** Postgres/Redis/MQ на `0.0.0.0:5432` без password + TLS в prod/staging.
- **MUST:** deny-by-default network — only required ports exposed.
- **MUST:** prod profile: `debug=false`, no test bypass env vars.
- **MUST:** `prod-config` step validates required env vars exist and are non-default.

### Zero Trust infra

- **MUST NOT:** «internal» service-to-service без mTLS or signed token where data is sensitive.
- **MUST:** secrets from vault/env — never committed compose overrides with real passwords.
- **MUST:** `docker-security` + `compose-security` in prime_check when Docker files exist.
- **MUST:** When k8s/helm/terraform/pulumi/cloudformation present → `iac-scan-gate` GREEN — Dockerfile-only harden while cluster open = FAIL ([A40](#prime-a40--secure-continuum)).
- **MUST:** treat CI as infra — least workflow permissions ([A40](#prime-a40--secure-continuum)).

---

## PRIME-A24 — TDD-LOCK

**Min tier:** PRIME+ **Enforced by:** agent phase + `test-matrix-gate` + `test-taxonomy-gate`

- **MUST (greenfield):** PHASE 2 — failing test **before** production code — for **each applicable taxonomy family** ([A12a](#prime-a12a--test-taxonomy)) **и** each acceptance criterion ([A34](#prime-a34--intent-lock)).
- **MUST (legacy):** tests in **same PR**; test_matrix + `test_taxonomy_map` + AC mapping — order flexible.
- **MUST:** test_matrix покрывает behaviors/errors/operations **и** acceptance criteria (GWT).
- **MUST NOT:** «тесты потом» / «в следующем PR» / «сначала happy path» / «AC потом».
- **MUST NOT:** naked N/A ([Anti-N/A SSOT](#anti-na-ssot--один-раз)).

---

## PRIME-A25 — Coverage absolute

**Min tier:** PRIME+ **Enforced by:** `coverage-*` steps  
**Aligns:** ISO 25010 **Reliability** + **Maintainability** · CISQ **Reliability** — fault paths must be exercised  
**Note:** branch 100% = **path coverage** family in [A12a](#prime-a12a--test-taxonomy). Coverage **does not** replace scenario/security/mutation families.

- **MUST:** 100.00% line + 100.00% branch — `99.99%` = fail. Это **Reliability** characteristic, не KPI ради KPI.
- **MUST:** `coverage-diff-100` на каждый PR (legacy + greenfield).
- **MUST:** `coverage-ratchet` — coverage never drops vs `main`.
- **MUST NOT:** `# pragma: no cover` / `istanbul ignore` без ADR + config entry + sunset.
- **MUST NOT (greenfield PRIME):** `exclude_coverage` на composition root, I/O adapters, presentation command handlers — это спрятать 80% риска за 100% fakes (`exclude-honesty-gate`).
- **ALLOW exclude:** generated/; vendor/; OS glue **with** an integration test of that adapter (real PNG, real mutex) + ADR + sunset + owner.
- **MUST NOT:** declare done on coverage green if `test-taxonomy-gate` red or E2E all-ignored.
- **MUST:** unit vs Fake **does not replace** adapter integration When filesystem/DB/OS ([A12a](#prime-a12a--test-taxonomy)).

---

## PRIME-A26 — Evidence block

**Min tier:** PRIME+ **Enforced by:** `evidence-block` step + agent discipline  
**Honesty:** evidence без taxonomy/intent = невалиден (тот же класс, что «готово» без exit 0).

- **MUST:** перед «done» — `python -m scripts.prime_check --evidence` → paste block.
- **MUST:** block contains:
  - tier, adoption_mode, stack, exit 0, steps_green
  - coverage line/branch %
  - `taxonomy_families:` each family → `APPLIED:<tests>` \| `N/A:<reason>` (полный список A12a)
  - `contract_surface:` each A35 family → `APPLIED:<ports>` \| `N/A:<reason>` ([A35](#prime-a35--contract-surface))
  - `rich_domain:` `APPLIED:<entity.methods>` \| `N/A(no status entity)` ([A05](#prime-a05--layer-law))
  - `error_split:` expected=named Err · unexpected=presentation handler ([A10](#prime-a10--result))
  - `acceptance_criteria:` each AC → oracle.kind + test ref ([A34](#prime-a34--intent-lock))
  - `live_surface:` ports called \| unread fields none ([A36](#prime-a36--live-surface))
  - `no_swallow:` process I/O mapped ([A37](#prime-a37--honest-errors--no-swallow))
  - `checker_integrity:` `checker-integrity-gate` green ([A38](#prime-a38--checker-integrity))
  - `behavior_ssot:` `APPLIED:<owners>` \| `N/A(no repeated behavior)` ([A39](#prime-a39--behavior-ssot))
  - `secure_continuum:` `APPLIED:<gates>` \| `N/A(<reasons>)` ([A40](#prime-a40--secure-continuum))
  - `trust_pipeline:` `APPLIED:<ops/gates>` \| `N/A(<reasons>)` ([A41](#prime-a41--trust-pipeline))
  - `blast_radius:` capabilities + files ([A33](#prime-a33--blast-radius))
  - changed_files, uncovered: NONE, fix_plan_executed: ALL
- **MUST:** если был RED в сессии — evidence **не** печатается пока full run не green.
- **MUST NOT:** «готово» без evidence; evidence с пустым taxonomy / пустым contract_surface / скрытыми N/A — **невалиден**.
- **MUST:** `rich_domain` и `error_split` заполнены на PRIME+ (или честный N/A).

---

## PRIME-A27 — Test quality

**Min tier:** PRIME+ **Enforced by:** `no-empty-test`, `no-trivial-assert`, `flaky-detector`, `ignored-test-gate`

**Trivial (FAIL)** — не только `assert True`:

| Pattern | Why it is theatre |
|---------|-------------------|
| `assert True` / `expect(1).toBe(1)` | tautology |
| assert on a constant defined in the **same** test file | not production |
| `assert_eq!(err.invariant_id(), "X")` / Display / enum **name** without calling the producer | err-variant vanity ([A37](#prime-a37--honest-errors--no-swallow)) |
| `assert!(!name.contains("Window"))` as the only AC oracle | synonym lock, not behavior ([A34](#prime-a34--intent-lock)) |
| `assert!(!user_message().is_empty())` | non-empty ≠ correct |

- **MUST:** every APPLIED test has a **non-trivial oracle** — a fact that fails if production lies.
- **MUST:** `flaky-detector` = **same test ×3 in one gate invocation**. `cargo test` twice in the chat ≠ flaky-detector.
- **MUST NOT:** `#[ignore]` / skip without `skipped_steps` row (unique trigger; **MUST NOT** one ADR covering 15 N/A).
- **MUST NOT:** E2E-only without unit foundation (`e2e-only-anti-pattern`).
- **MUST NOT:** happy-path-only when negative/boundary When fired ([A12a](#prime-a12a--test-taxonomy)).
- **MUST:** each test maps to a taxonomy family so gates can inventory.

---

## PRIME-A28 — Mutation testing

**Min tier:** **PRIME greenfield MUST** on `critical_scope`; CRITICAL ≥95%  
**Taxonomy family:** Mutation ([A12a](#prime-a12a--test-taxonomy))  
**Enforced by:** `mutation-critical`

- **MUST (PRIME greenfield):** mutation on `critical_scope` (FSM, parsers, money, hotkey/crop/naming — the core that fakes don't prove). `mutation.enabled_prime_greenfield: false` = FAIL.
- **MUST (CRITICAL):** ≥95% kill rate on `critical_scope`.
- **SHOULD (PRIME legacy):** ≥85% when enabled; ADR if skipped with sunset.
- **MUST NOT:** merge with surviving mutants on domain invariants — strengthen the **test**, not weaken config.
- **MUST:** mutation exists so A27 cannot be gamed by weak oracles.

---

## PRIME-A29 — ZTA matrix

**Min tier:** PRIME+ **Enforced by:** `zta-matrix-gate` · `idor-ownership-gate`  
**See:** [A02](#prime-a02--zero-trust) · taxonomy access_control ([A12a](#prime-a12a--test-taxonomy)) · [A41](#prime-a41--trust-pipeline)

- **MUST:** per protected op: anon→401; bad token→401/403; wrong scope→403; valid→2xx; **IDOR/cross-user→403/404 When multi-user/tenant**.
- **MUST:** IDOR oracle in test body — principal A cannot access B's resource ([A41](#prime-a41--trust-pipeline)).
- **MUST NOT:** localhost/docker exempt. Matrix in test_matrix + taxonomy map + `trust_pipeline_map.idor_cases` When applicable.
- **MUST NOT:** only «logged-in vs anon» when resources are multi-user.

---

## PRIME-A30 — Anti-slack · Fix until green

**Min tier:** PRIME+ **Enforced by:** DoD-only (process — agent loop until `prime_check` exit 0; [A22](#prime-a22--prime-check))

- **MUST:** red gate → **fix loop** (edit → re-run) until `exit 0` — **никогда не бросать задачу**.
- **MUST NOT:** partial PR (код без taxonomy/AC mapping, API без contract, infra без docker gates, happy-path-only, N/A-spam, diff вне blast без reason).
- **MUST NOT:** delegate verify or fixes to user.
- **MUST NOT:** respond «готово» / «blocked» / «cannot fix» while prime_check is red.
- **MUST:** 3-strike → same patch fails 3× → **redesign**, then **continue fixing** until green.
- **MUST:** checker truth > agent words; Law→Gate — stub steps = anti-slack violation.

---

## PRIME-A31 — Legacy adoption

**Min tier:** PRIME+ **When:** existing codebase, not greenfield **Enforced by:** `coverage-diff-100` · `coverage-ratchet` · config `adoption_mode: legacy`

- **MUST:** `adoption_mode: legacy` in config.
- **MUST:** 100% coverage on **changed files only** — not whole repo day one.
- **MUST:** `coverage-ratchet` — each PR improves or maintains baseline.
- **MAY:** grandfather debt via ADR + ticket + sunset — **not** silent excludes.
- **MUST NOT:** use legacy mode to avoid tests on **new** files.

---

## PRIME-A32 — Monorepo scope

**Min tier:** PRIME+ **When:** monorepo **Enforced by:** `config-valid` (monorepo_scopes) · `prime_check --diff` path scope · [A33](#prime-a33--blast-radius)

- **MUST:** `monorepo_scopes` in config — per-path tier.
- **MUST:** `prime_check --diff` respects path scope.
- **MUST NOT:** apply LITE gates to `services/api/` because `tools/` is LITE.
- **MUST:** blast radius не пересекает чужие scopes без явной задачи ([A33](#prime-a33--blast-radius)).

---

## PRIME-A33 — Blast radius

*Минимальный scope на фичу. Качество (тесты/security) не режется — режется ширина diff.*

**Min tier:** STANDARD+ **Enforced by:** soft `blast-radius-gate` · DoD · design artifact  
**Aligns:** ISO 25010 Maintainability · [A05a](#prime-a05a--package-cohesion) · [A11](#prime-a11--decomposition)

- **MUST:** в PHASE 1 объявить `blast_radius`: capabilities + expected files.
- **MUST:** edits stay inside radius; выход за радиус → обновить artifact + reason (или split PR).
- **MUST NOT:** «заодно» рефакторить соседние capabilities / shared bags без задачи.
- **MUST NOT:** keep blast small by **duplicating** behavior that belongs in an existing owner ([A39](#prime-a39--behavior-ssot)). Touching the owner + replacing copies = **correct** blast, not «half-repo» — includes shared **authorize/sanitize** ([A40](#prime-a40--secure-continuum)).
- **MUST NOT:** путать с YAGNI на тесты — малый blast **не** отменяет [A12a](#prime-a12a--test-taxonomy) / [A34](#prime-a34--intent-lock).
- **SHOULD:** один capability на PR, если задача не требует cross-cut.
- **Good:** `orders` slice only. **Bad:** touched `orders`+`billing`+`auth`+DI root «на всякий».  
**Bad:** copy-paste retry into the new file «чтобы не трогать shared».

---

## PRIME-A34 — Intent lock (behavior-lock)

*Смысл задачи измерим **оракулом**, не именем теста. `AC1 ↔ test_acceptance_ac1_*` без наблюдаемого факта — таблица синонимов.*

**Min tier:** PRIME+ **When:** user-facing / API / behavioral feature (не typo-fix)  
**Enforced by:** `intent-lock-gate` · `test-matrix-gate`  
**Aligns:** ISO 25010 Functional suitability · taxonomy Acceptance/BDD ([A12a](#prime-a12a--test-taxonomy))

Каждый AC в design artifact:

| Field | MUST |
|-------|------|
| `id` | stable (`AC1`…) |
| `statement` | человеческий критерий |
| `oracle.kind` | `hwnd` · `pixels` · `fs` · `order` · `error_id` · `toast` · `state` · Skin analog |
| `oracle.assert` | факт, который **ломается**, если поведение соврало |
| `test` | named test whose **body** asserts that fact |

```text
# FAIL — synonym lock
AC1 ↔ test_acceptance_ac1_no_window
  assert!(!state.name().contains("Window"))

# PASS — behavior lock
AC1: process does not create a visible overlapped window
  oracle: hwnd / FakeOverlay.shown==false until hotkey
  test reads style HWND / GetWindowLong / fake.shown
```

- **MUST:** empty `acceptance_criteria` на PRIME+ feature → **STOP**.
- **MUST:** test body contains an assert matching `oracle.assert` tokens (Skin-native API OK).
- **MUST NOT:** lock = AC id in test name / docstring / `"AC{i}" in inventory.yaml`.
- **MUST NOT:** close hwnd/pixels/ui oracles with unit-only names while E2E is `#[ignore]` ([A12a](#prime-a12a--test-taxonomy)).
- **MUST NOT:** «и так понятно» / acceptance только в chat.
- **See:** Anti-N/A — нельзя `N/A` на acceptance family при наличии AC.

---

## PRIME-A35 — Contract Surface

*SSOT for **which** contracts Empire requires. Core/app depends on **contracts only**; concrete lives in adapters / composition root. Form of Protocol/iface/trait = Skin; families below = Engine. Complements [A06](#prime-a06--di--ports) (how to inject) · [A04](#prime-a04--integration--plugin-boundaries) (boundaries) · [A21](#prime-a21--semver--contracts) (external API).*

**Min tier:** PRIME+ (outbound + composition root); STANDARD+ SHOULD for new I/O  
**Aligns:** ISO 25010 Maintainability (modularity) · Compatibility · CISQ Maintainability  
**Enforced by:** `port-surface-gate` · `composition-root-gate` · `port-test-double-gate` · `live-surface-gate` · `dto-boundary-gate` · `inbound-port-gate` (soft) · `plugin-boundary-gate` · `event-contract-gate` (soft) · `di-purity` · `di-graph-gate` · `api-contract-drift`

### Doctrine

Агент **MUST** перед кодом заполнить `contract_surface_map` в design artifact ([AGENT-OMEGA](#agent-omega--execution-phases-before-any-code)). Для каждого family: **named ports/contracts** **или** `N/A(<trigger absent>)`.  
**MUST NOT:** «одна реализация → без порта» при I/O в testable core.  
**MUST NOT:** требовать *все* families на каждый CRUD — колонка **When** нормативна.  
**MUST:** если When сработал — family **обязателен**.  
**MUST NOT:** «при сомнении наплоди порт» — [Conflict Matrix](#conflict-matrix-при-сомнении--читать-это-не-конкурирующие-абзацы). Порт только если application **вызывает** его и есть Fake. Иначе `N/A(no I/O)` или concrete **только** в composition ([A36](#prime-a36--live-surface), [B07](#prime-b07--yagni)). Enough vs too much = **FAIL**.

### Anti-N/A

**SSOT:** [Doctrine Anti-N/A](#anti-na-ssot--один-раз). Contract-specific reasons: `N/A(no I/O|single HTTP entry|no events|…)`. Триггер сомнителен → Conflict Matrix row 1; «наплодить порт» → row 2.

### Contract families

| Family | Outcome | Min tier | When (trigger) | Gate / naming |
|--------|---------|----------|----------------|---------------|
| **Outbound port (driven)** | Repo, Clock, IdGen, Mailer, PaymentGateway, FileStore, Cache, Queue, HTTP client | PRIME+ | Application/core touches I/O / side-effect / nondeterminism | `port-surface-gate` · `di-purity` · `IOrderRepo` / Protocol / trait |
| **Inbound port (driving)** | Application entry as contract (UseCase/Command/Query iface) | PRIME+ soft | Multi-adapter entry (HTTP+CLI+job) **or** multiple callers / explicit UC test seam | `inbound-port-gate` · `IPlaceOrder` / handler port |
| **DTO / ACL contract** | Boundary types between capabilities/modules | PRIME+ | Cross-capability or multi-module | `dto-boundary-gate` · `context-leak-gate` · `contracts/` |
| **Policy / Strategy port** | Swappable business policy | PRIME+ | 2+ strategies **or** payment/auth/pricing branch families | `anti-fork-gate` · [A08](#prime-a08--anti-fork--policy-facades) |
| **SPI / Plugin contract** | Provider extension without Core edit | PRIME+ | New provider (payment, storage, notify, auth…) | `plugin-boundary-gate` · [A04](#prime-a04--integration--plugin-boundaries) |
| **API contract** | HTTP/RPC/GraphQL/CLI public shape | PRIME+ | Exposed operation | `api-contract-drift` · `route-matrix-gate` · [A21](#prime-a21--semver--contracts) |
| **Event contract** | Published domain/integration events | PRIME+ soft | Domain events / outbox / cross-module async | `event-contract-gate` · versioned event schema |
| **Query/Command contract** | CQRS message shapes | PRIME+ | When CQRS ([B01](#prime-b01--cqrs)) | design artifact Command/Query types |
| **Method contract (DbC)** | Pre/post + invariants on public core API | CRITICAL MUST; PRIME+ SHOULD | Money / security / irreversible ops | typed preconditions · err-variant tests |
| **Test double vs port** | Fake/InMemory implements **Port**, not mock concrete | PRIME+ | Always when outbound port exists | `port-test-double-gate` |
| **Composition root only** | Wiring concrete → port | PRIME+ | Always when adapters exist | `composition-root-gate` · `di-graph-gate` |

- **MUST:** external write input enters as **allowlisted Command/DTO** — never transport entity / request-bag → persistence ([A41](#prime-a41--trust-pipeline) mass-assign).

### Enough vs too much

| Задача | Достаточно (APPLIED) | Слишком / запрещено |
|--------|----------------------|---------------------|
| Pure `calculateTax(a,b)` | без порта; `N/A(no I/O)` | `ITaxCalculator` ради галочки |
| PlaceOrder + DB | `IOrderRepo` + Fake + **вызов из UC** + adapter + composition root | 12 портов на private method · identity mapper · port in yaml never called |
| HTTP-only CRUD | outbound ports + API contract; inbound `N/A(single HTTP entry)` | UseCase iface + 3 adapters «на будущее» |
| Working Nest/Rails/Go Skin | keep Skin folders; ports + rich entities inside | rewrite to textbook `domain/entities` «для PRIME» |
| One I/O adapter, used | Port + Fake + call from UC | Stub `InstanceCommandSink` / `todo!()` impl without ADR sunset |
| Settings DTO field | field read by runtime **or** removed from AC | `notify_on_save` serialized, never read |
| Checkout + Stripe | `IPaymentGateway` + SPI/plugin | Hardcode Stripe SDK в UC |
| Cross-capability charge | DTO/ACL + outbound ports | Import private `User` entity |

### Anti-patterns (MUST NOT)

Concrete in UC signature · «одна impl → без порта» при I/O · god-port · flat `ports/` bag ≥2 caps · mock concrete · empty marker iface · OpenAPI «в голове» · framework DI as excuse · rewrite Skin · port without call ([A36](#prime-a36--live-surface)) · identity/`todo!()` without ADR · adapter name for missing crate.

### Agent algorithm (MUST)

```text
1. List triggers (I/O? multi-entry? cross-cap? API? events? strategy? money?)
2. Mark each A35 family applicable | N/A(reason) in contract_surface_map
3. Declare ports/DTOs/API schemas before adapters
4. Implement adapters + Fake/InMemory; wire only in composition root
5. Unit tests against Fake ports; integration against real adapters
6. prime_check: port-surface-gate + composition-root + port-test-double + **live-surface-gate** → exit 0
```

### Stack-native forms (Skin)

| Family | Python | TS/Node | Go | Rust | Nest/Spring |
|--------|--------|---------|-----|------|-------------|
| Outbound port | `Protocol` / ABC | `interface` | iface | trait | interface + token / Spring iface |
| Inbound port | Protocol on UC | interface | iface | trait | command handler iface |
| Composition root | `main` / DI container | `container.ts` | `main.go` wire | `main` / DI | `AppModule` / `@Configuration` |
| Test double | InMemory implements Protocol | Fake class | fake struct | mock trait obj | test double bean |

---

## PRIME-A36 — Live Surface

*Объявленный контракт должен **жить**. Порт в yaml без вызова — тот же класс лжи, что coverage vanity.*

**Min tier:** PRIME+ **When:** ports / serialized settings / adapters exist  
**Enforced by:** `live-surface-gate`  
**Complements:** [A35](#prime-a35--contract-surface) (declare) · [A08](#prime-a08--anti-fork) (dead `*_v2`) · [B07](#prime-b07--yagni)

**FAIL если:**

- порт в `architecture.ports` / `contract_surface_map`, но нет construction в composition root **или** нет вызова из application;
- поле Settings/DTO сериализуется и нигде не читается рантаймом (`notify_on_save`);
- `impl Trait for T` — identity / `todo!()` / `Ok(())` / `pass` без ADR + sunset;
- имя адаптера врёт про механизм (токен технологии в имени ⊆ crate/feature, не используемых в `src`).

**Порт добавляй** только если: I/O из UC + Fake + **вызов**. Иначе `N/A(no I/O)` или конкретный адаптер только в composition. Fake считается вторым impl для теста — **не** требуй двух прод-адаптеров.

- **MUST NOT:** CoordinateMapper / PipeCommandSink / stitch() / OverlayPhase «на всякий».
- **MUST:** unread config field — выкинуть из AC **или** подключить к runtime в том же PR.

---

## PRIME-A37 — Honest errors & no swallow

*[A10](#prime-a10--result) запрещает silent null. Этот закон запрещает swallowed Result, dump-bucket Err и err-тест без продакшен-пути.*

**Min tier:** PRIME+ **Enforced by:** `no-swallow-gate` · `err-variant-gate` (provoke path)

- **MUST:** каждый `Result` на границе процесса (hotkey register, autostart, save, capture, bind port) либо mapped в named error + toast/log, либо явный `_ =` с **ADR + sunset на эту строку**.
- **MUST:** один вариант ошибки = один класс отказа пользователя. Dump-bucket (`CaptureTimeout` на GetDC==null **и** на hang) запрещён без `#[doc(alias)]` + ADR.
- **MUST:** `err-variant-gate` — тест **вызывает** UC/адаптер (Fake или real) и наблюдает вариант. `assert_eq!(err.invariant_id(), "…")` без producer = FAIL.
- **MUST NOT:** `let _ =` / `.ok()` / empty `catch {}` на I/O в composition и presentation.
- **MUST (desktop):** composition не глотает ошибки UI-команд — тост или mapped Err ([B11](#prime-b11--client-apps)).

---

## PRIME-A38 — Checker integrity

*Агент пишет checker и сам его зеленит. Step, который смотрит `path.exists()`, — театр. Law→Gate без этого закона всегда 7/10.*

**Min tier:** PRIME+ **Enforced by:** `checker-integrity-gate` (AST `scripts/prime_check/**`)

**MUST NOT** в step-модулях:

- `return GREEN` / `return []` / `if False: FAIL else GREEN`;
- единственная проверка — `path.exists()` / файл прочитан без parse содержимого;
- inventory/lock = `"AC{i}" in text` / filename exists;
- `no-trivial-assert`, который ловит только `assert!(true)` и пропускает tautology из [A27](#prime-a27--test-quality).

**MUST:** этот gate гоняется на каждом FULL run **по самому checker**. Красный checker = красный продукт.

---

## PRIME-A39 — Behavior SSOT

*Третий класс лжи: структурная многословность. Тот же алгоритм в двух методах — тот же класс, что `*_v2` и мёртвый порт. Форма owner = Skin; закон = один owner + call sites.*

**Min tier:** PRIME+ · **When:** growing domain / STANDARD+ with repeated policies  
**Enforced by:** `behavior-ssot-gate` · `anti-fork-gate`  
**Aligns:** [A08](#prime-a08--anti-fork--policy-facades) · [A11](#prime-a11--decomposition) · [A17](#prime-a17--clean-code) · [A33](#prime-a33--blast-radius) · [B07](#prime-b07--yagni) · [A36](#prime-a36--live-surface)

**Outcome (Engine):** a given policy/algorithm has **exactly one** implementation in `runtime_scope`; other sites **CALL** it.  
**Form (Skin):** plain `fn`, entity/VO method, A08 facade, strategy object, command/event dispatcher — **not** a mandatory UI `InputRouter` / `PaintPass` in every repo.

### When

| Trigger | Action |
|---------|--------|
| First occurrence of a behavior | **MAY** keep local (YAGNI) |
| Second independent copy in the same change set (or already in scope) | **MUST** extract/reuse **in that change set** |
| Body below `behavior_ssot.min_body_stmts` (default ~8) | skip cluster (trivial getters) |
| Same shape, **different** invariants | ADR allowlist `{hash, reason, sunset}` |

### MUST / MUST NOT

- **MUST:** callers orchestrate (~10–15 lines) and **delegate** — do not re-implement the policy.
- **MUST:** new mode/variant = data or strategy **plugged into** the owner ([B02](#prime-b02--solid--grasp)) — not a cloned method.
- **MUST:** when in doubt the **second** copy is appearing → extract. Do **not** extract on speculation of a future second caller (YAGNI / [A36](#prime-a36--live-surface)).
- **MUST NOT:** clone retry / map-error / validate / hit-test / draw / paginate / round-money / authorize / DTO-map / idempotency-key mint with only identifiers changed.
- **MUST NOT:** A11 split that moves the **same** logic into two files; A33 «didn’t touch shared so I duplicated».
- **MUST NOT:** new unused Port solely to «share» pure logic — share via `fn`/facade inside the capability; Port When I/O ([A35](#prime-a35--contract-surface), [A36](#prime-a36--live-surface)).
- **MUST NOT:** god-`helpers` mixing unrelated behaviors ([A08](#prime-a08--anti-fork--policy-facades), [A05a](#prime-a05a--package-cohesion)).
- **MUST NOT:** mandate UI-only types (HWND/paint/mouse Overlay) as the definition of this law — those are **examples**.

### Enough vs too much (FAIL table)

| Task | Enough | Too much |
|------|--------|----------|
| Two UCs need same money round | `Money.round()` / one fn | copy round into both UCs |
| Three widgets same hit-test | one HitTest in capability | three `on_mouse_move` copies |
| HTTP + job need same retry | one `retry_with_backoff(op)` | two copied backoff loops |
| HTTP + CLI same authz | one `authorize(op, principal)` | clone check in both entries |
| Same I/O from two UCs | existing Port + one mapper | new unused Port «to share» |
| One-off script parse | local parse | `IParser` + 4 strategies on N=1 |

**PASS examples:** one `Order.submit()` used by two UCs; Skin-native command/input dispatcher When the repo already has events/commands — **optional** form of A39, not a UI constitution.

**PHASE 1:** `behavior_owners: [{id, owner, callers[]}]` — empty OK until a shared behavior exists; introducing a second copy → map **MUST** name the owner in the same session.

---

## PRIME-A40 — Secure Continuum

*Четвёртый класс лжи: безопасный код + дырявые CI/chat/IaC. `security.md` без gate — тот же театр, что A38. Форма контролей = Skin; закон = секрет/trust не живут вне vault+allowlist на всех каналах.*

**Min tier:** PRIME+ · **When:** network-facing / auth / PII / payments / deploy / CI-present  
**Enforced by:** `ci-harden-gate` · `channel-secret-gate` · `security-headers-gate` · `cors-csrf-gate` · `iac-scan-gate`  
**Aligns:** [A02](#prime-a02--zero-trust) · [A16](#prime-a16--secure-by-design) · [A18](#prime-a18--owasp-input-hygiene) · [A19](#prime-a19--supply-chain--secrets) · [A23](#prime-a23--infra--docker-security) · [A38](#prime-a38--checker-integrity) · [A39](#prime-a39--behavior-ssot)

**Outcome (Engine):** every trust/secret/boundary decision has a **gate-enforced** owner across `runtime_scope` + `ci_scope` + `ops_scope` + agent channel policy — not a markdown checklist.  
**Form (Skin):** GitHub Actions / GitLab CI; Helmet / Nest middleware; Vault / GH Secrets — **not** a mandatory WAF product or textbook `security/` tree.

### Channel table (FAIL = Too much)

| Channel | Enough (PASS) | Too much / FAIL |
|---------|---------------|-----------------|
| App/API | schema@boundary · ZTA matrix · one authorize owner · headers/CORS/CSRF When web | «Nest defaults» without gate · clone authz per route |
| Secrets | env/vault refs; gitleaks GREEN; rotate on leak | `.env` in chat · secret in evidence · ARG in Dockerfile |
| CI/CD | least workflow permissions; pin actions by SHA When PRIME+; no secrets on fork PR; OIDC/short-lived When cloud | `write-all` · untrusted code + privileged secrets · `curl\|bash` |
| IaC | docker gates + When k8s/tf/helm → `iac-scan-gate` | only Dockerfile hardened, cluster wide open |
| Chat/agent | secret store / masked CI var; agent refuses echo into evidence | paste private key «to debug» |
| Supply chain | lockfile + audit + SBOM; When publish → provenance Skin-native | unsigned release «потом» |

### MUST / MUST NOT

- **MUST:** fill `secure_continuum_map` in PHASE 1; Anti-N/A on absent surfaces (LITE offline OK with reasons).
- **MUST:** When surface exists → enable the matching gate ([Conflict Matrix](#conflict-matrix-при-сомнении--читать-это-не-конкурирующие-абзацы): триггер → включи; unused SecurityPort → не плоди — [A36](#prime-a36--live-surface)).
- **MUST:** authorize / sanitize / CSRF token mint = **one owner** When N≥2 ([A39](#prime-a39--behavior-ssot)).
- **MUST:** Threat Model names CI compromise + chat exfil When those channels exist ([A16](#prime-a16--secure-by-design)).
- **MUST NOT:** `permissions: write-all` / absent permissions when secrets or deploy present.
- **MUST NOT:** treat framework defaults / Helmet-in-package.json / `security.md` as OWASP closed.
- **MUST NOT:** echo raw secrets into evidence, logs, or chat replies — rewrite to env names; on leak → rotate ([B14](#prime-b14--human-handoff)).
- **MUST NOT:** Dockerfile-only harden When broader IaC is open.
- **MUST NOT:** mandate Snyk/Wiz/Vault Enterprise/Cloudflare; one Skin-native scanner/control GREEN.
- **MUST NOT:** god-`SecurityService` on first use (N=1 local OK — [B07](#prime-b07--yagni)).

**LITE offline script:** `N/A(ci)` / `N/A(web headers)` with reasons — not silent skip.

**PHASE 1:** `secure_continuum_map` — surfaces, threat_channels, header/cors policies, `ci_permissions_owner`, `authz_owner`.

---

## PRIME-A41 — Trust Pipeline

*Пятый класс лжи: «фича» со слоями, но soft to own. Залогинен ≠ authorized на любой id. Form = Skin middleware; Engine = schema→authn→authz(resource)→allowlisted command→UC→safe sink. Attack class closed by gate+oracle — не «будь осторожен».*

**Min tier:** PRIME+ · **When:** exposed op / auth / PII / money / multi-tenant / file upload / HTML UI  
**Enforced by:** `trust-pipeline-gate` · `idor-ownership-gate` · `mass-assign-gate` · `path-escape-gate` · `session-token-gate`  
**Aligns:** [A02](#prime-a02--zero-trust) · [A18](#prime-a18--owasp-input-hygiene) · [A29](#prime-a29--zta-matrix) · [A39](#prime-a39--behavior-ssot) · [A40](#prime-a40--secure-continuum) · [A08](#prime-a08--anti-fork--policy-facades)

**Outcome (Engine):** for every protected/state-changing operation, trust is reduced in a **fixed order**; classic exploit classes closed by owners + gates.  
**Form (Skin):** Nest guards · FastAPI Depends · Axum layers · Spring filters — **not** mandatory IdP/WAF brand. Skin may merge steps into one middleware; **Engine order preserved**.

### Pipeline (MUST order)

| Step | Outcome | Typical Skin |
|------|---------|--------------|
| 1 Schema | untrusted bytes → typed DTO; unknown/privileged fields rejected | zod / pydantic / jsonschema |
| 2 Authn | principal established or deny | JWT / session / mTLS |
| 3 Authz | principal **may** act on **this resource** (IDOR closed) | one `authorize(op, principal, resource)` ([A39](#prime-a39--behavior-ssot)) |
| 4 Command | only allowlisted fields enter UC | explicit Command / patch DTO |
| 5 UC | business only; no raw body; no client id as ownership proof | thin orchestration |
| 6 Sink | parameterized SQL · path under root · HTML encoded · no shell+user | adapters ([A18](#prime-a18--owasp-input-hygiene)) |

### Attack → closure (FAIL table)

| Attack | Enough (PASS) | Too much / FAIL |
|--------|---------------|-----------------|
| IDOR | authz loads resource + ownership/tenant; cross-user oracle | client `user_id` / only «logged in?» |
| Mass assignment | Command / allowlist patch | `update(**body)` / bind full entity from request |
| Injection | parameterized / no shell / encode + fuzz | f-string SQL · raw `innerHTML` · `os.system(user)` |
| Path traversal | resolve under allowlisted root; reject `..` | concat user path to uploads |
| Session/token | httpOnly+Secure+SameSite **or** bearer header; no token in query/logs | token in localStorage w/o ADR · token in URL · homemade crypto |
| CSRF | [A40](#prime-a40--secure-continuum) `cors-csrf-gate` When cookies | cookies + no CSRF |
| Privilege escalate | role only from server claims/session | `body.role = admin` applied |
| SSRF | existing `ssrf-gate` | user URL → metadata IP |

### MUST / MUST NOT

- **MUST:** fill `trust_pipeline_map` in PHASE 1 for touched protected ops.
- **MUST:** authz **before** mutation/side-effect; schema **before** UC.
- **MUST:** When multi-user resources — IDOR oracle tests (principal A ↛ B's resource).
- **MUST:** authorize / validate / safe_path = one owner When N≥2 ([A39](#prime-a39--behavior-ssot)).
- **MUST:** privileged fields stripped from client DTOs (config denylist) unless admin op + authz.
- **MUST NOT:** treat «has token» as resource authorization.
- **MUST NOT:** request-bag → entity; client-owned id as proof of rights.
- **MUST NOT:** token in query/logs; reinvent JWT verify when stack has standard lib.
- **MUST NOT:** absolute «unhackable» claims — language is **attack class closed by gate+oracle**.
- **MUST NOT:** god-`SecurityService` on N=1; unused SecurityPort ([A36](#prime-a36--live-surface), [B07](#prime-b07--yagni)).
- **MUST NOT:** weaken [A40](#prime-a40--secure-continuum) — continuum = channels; this law = **inside the process**.

**LITE offline:** N/A with Anti-N/A reasons. CLI/desktop may N/A CSRF/cookies; IDOR/mass-assign/injection still When resources exist.

**PHASE 1:** `trust_pipeline_map` — ops, idor_cases, privileged_fields_stripped, session_model.

---

# Part B — Platform patterns

## PRIME-B01 — CQRS

**Min tier:** PRIME+ (SHOULD)

- **SHOULD:** commands/queries split when read/write complexity or load differs.
- **SHOULD NOT:** CQRS for simple CRUD ([B07](#prime-b07--yagni)).

## PRIME-B02 — SOLID & GRASP

**Min tier:** STANDARD+

| Principle | Enforcement |
|-----------|-------------|
| **S**RP | One UC/entity/policy — one reason to change; **also** one capability package ([A05a](#prime-a05a--package-cohesion)) |
| **O**CP | Extend via new UC, Strategy, Factory — not `if/elif` forests; **new variant = data/strategy on the owner**, not a cloned method ([A39](#prime-a39--behavior-ssot)) |
| **L**SP | Implementation fully replaces contract; subtypes honor invariants |
| **I**SP | Small ports (`IOrderRepository`, `ITimeProvider`) — no mega-interface; prefer capability-local ports ([A35](#prime-a35--contract-surface)) |
| **D**IP | Application → Protocol/Port; wiring in composition root only ([A35](#prime-a35--contract-surface), [A06](#prime-a06--di--ports)) |

**GRASP:**

- **Information Expert** — behavior on entity that owns data (**Anti-Anemic** — [A05](#prime-a05--layer-law)); shared algorithm → one Expert/owner, N callers ([A39](#prime-a39--behavior-ssot)); **ownership/authz rules** near the resource type or one authorize facade ([A41](#prime-a41--trust-pipeline)).
- **Creator / Low Coupling** — factories in DI; domain does not `new PostgresRepo()`; depends on Port.
- **High Cohesion** — files that change together live together (capability slice), not only «one class one job».
- **Controller** — one UC per story; ~10–15 orchestration lines; **does not** mutate entity fields directly; **does not** re-implement policy owned elsewhere; **does not** embed authz copies.
- **Pure Fabrication** — infra helpers only — not smuggling business rules out of domain; **not** a kitchen-sink util of unrelated policies.

- **MUST NOT:** «Service» classes accumulating unrelated static methods.
- **MUST NOT:** «ports/» mega-bag for every capability without slices ([A05a](#prime-a05a--package-cohesion)).
- **MUST NOT:** god-port `IUnitOfWorkEverything` — split by capability ([A35](#prime-a35--contract-surface)).
- **MUST NOT:** anemic entity + fat service that owns all invariants.
- **MUST NOT:** clone a method for a new mode when OCP says extend the owner ([A39](#prime-a39--behavior-ssot)).
- **MUST NOT:** Controller/handler that trusts client ids for ownership ([A41](#prime-a41--trust-pipeline)).

## PRIME-B03 — SRE, observability & events

**Min tier:** PRIME+

### Observability

- **MUST (PRIME+):** critical operations carry `trace_id` / `correlation_id` — one ID links request, logs, events.
- **MUST (PRIME+):** metrics on critical paths — latency, error rate, throughput.
- **MUST:** structured logging (JSON/structured) — not raw `console.log("error")`.
- **MUST (PRIME+):** при `Err` — log payload = `rule_id` + `state_snapshot` + `correlation_id` ([A10](#prime-a10--result)); prod debug ≤ 1 click from trace.
- **MUST (PRIME+ When new Err/failure path):** taxonomy **observability** — test asserts fields present ([A12a](#prime-a12a--test-taxonomy), `error-context-gate`).
- **MUST NOT:** PII, secrets, tokens in logs — в т.ч. в `state_snapshot`.
- **Enforced by:** `error-context-gate` (with [A10](#prime-a10--result)).

### Domain Events

- **SHOULD (PRIME+):** Domain publishes events (`OrderPlaced`, `PaymentFailed`, `UserRegistered`) with **event contract** in `contract_surface_map` ([A35](#prime-a35--contract-surface)).
- **MUST:** side effects (email, webhook, metrics) in Infrastructure subscribers — Domain does not know *how* delivery works; publish via port/event bus abstraction when I/O.
- **MUST NOT:** event bus for trivial CRUD ([B07](#prime-b07--yagni)).

### SRE

- **SHOULD:** **SLI** per critical path — latency, error rate, success rate.
- **SHOULD:** **SLO** targets (e.g. p99 < 3s, 99.9% success). SLO breach → stabilize before shipping features.
- **SHOULD:** **Error Budget** — exhausted → freeze features until root causes fixed.
- **SHOULD:** **Self-Healing** — jobs/integrations recover after transient failure (retry, reconnect, restart) without manual SSH.

## PRIME-B04 — Resilience

**Min tier:** PRIME+  
**Aligns:** ISO 25010 **Reliability** (availability, fault tolerance, recoverability) · CISQ **Reliability**

Assume external world **will** break.

- **SHOULD:** circuit breakers, timeouts, rate limits, bulkheads on external deps.
- **SHOULD:** **graceful degradation** — predictable partial failure:

| Failure | Degraded behavior |
|---------|-------------------|
| External data unavailable | Show UI without that data |
| Cache down | In-process fallback or fail-fast per ADR |
| RPC/API down | Last known good / cached snapshot |
| Queue down | Buffer locally or explicit error — not silent drop |

- **MUST NOT:** silent prod degradation without documented behavior.

## PRIME-B05 — Inter-service contracts

**Min tier:** optional (service split) **Enforced by:** `context-leak-gate` (cross-service)

- **SHOULD:** strict typed contracts; versioned (`v1`, `v2`).
- **SHOULD:** gRPC/proto or OpenAPI per project; see [A21](#prime-a21--semver--contracts).
- **MUST (service split):** сервисы общаются как **независимые государства** — DTO/proto messages / events, **не** shared domain entity libs ([A04](#prime-a04--integration--plugin-boundaries)).
- **MUST NOT:** monorepo shared `domain/User.ts` импортируемый payments + users — каждый сервис = свой bounded context + contract types.

## PRIME-B06 — FSM

**Min tier:** PRIME+ **When:** design artifact lists `fsm_transitions` OR entity has lifecycle status field **Enforced by:** `fsm-transition-gate` · `anemic-mutation-gate` · `immutability-gate` (When applicable)

**When NOT:** simple enum + validation sufficient; no status field; workflow engine (Temporal) owns graph — document in ADR, gate N/A.

- **MUST:** explicit transition graph when status/lifecycle matters (`Order`, `Job`, `Task`, `Subscription`, `Invoice`…).
- **MUST:** transitions live on the **entity** (`order.submit()`, `job.fail(reason)`) — not `order.status = …` in the use-case ([A05](#prime-a05--layer-law)).
- **MUST NOT:** illegal jumps (`DRAFT → COMPLETED` bypassing `PROCESSING`) — enforced in core, not scattered `if`.
- **MUST NOT:** status change from transport bypassing lifecycle rules.
- **MUST NOT:** public setter that accepts any status string/enum without the graph.
- **SHOULD:** transition returns new state instance when in-memory aggregate ([A05](#prime-a05--layer-law)); DB-only status OK with transactional update + ADR **if** the same invariant method is the only writer.
- **MUST:** transitions atomic at persistence under concurrency.
- **MUST:** tests for every **legal** edge + every **illegal** jump + concurrent transitions where applicable — taxonomy family **State transition** ([A12a](#prime-a12a--test-taxonomy), `fsm-transition-gate`).
- **MUST NOT:** only happy-path status updates without illegal-transition asserts.

## PRIME-B07 — YAGNI

**Min tier:** all

- **MUST:** full Part A for PRIME+ tasks.
- **MAY:** KISS for LITE without network/secrets/auth.
- **MUST NOT:** YAGNI exempts security ([A16](#prime-a16--secure-by-design)).
- **MUST NOT:** YAGNI exempts taxonomy / Anti-N/A / **oracles** / cohesion / **rich domain when status entity** — это Engine.
- **MUST NOT:** YAGNI «одна impl → без порта» при I/O из UC ([A35](#prime-a35--contract-surface)).
- **MUST NOT:** YAGNI наоборот — **плодить** порты/`test_err_*` «при сомнении» ([Conflict Matrix](#conflict-matrix-при-сомнении--читать-это-не-конкурирующие-абзацы)). Порт без вызова = dead abstraction ([A36](#prime-a36--live-surface)).
- **MUST NOT:** YAGNI as license to **keep the second/third copy** of the same algorithm ([A39](#prime-a39--behavior-ssot)).
- **MUST NOT:** YAGNI-extract a kitchen-sink util on **first** use (N=1 local OK).
- **MUST NOT:** new Port solely to share **pure** logic ([A35](#prime-a35--contract-surface) Enough vs too much).
- **MUST NOT:** YAGNI skip CSRF When cookie session / `ci-harden` When workflows ([A40](#prime-a40--secure-continuum)); skip IDOR/allowlist When multi-user/PATCH ([A41](#prime-a41--trust-pipeline)).
- **MUST NOT:** YAGNI rewrite Skin into textbook Clean folders · раздувать Part B без Law→Gate.

## PRIME-B08 — Agent self-review

**Min tier:** all

1. Risk Tier + [AGENT-1](#agent-1--task-router) sections applied.
2. Grep diff: swallowed `let _ =` / `.ok()` / empty catch on I/O; unused ports; `#[ignore]`; identity `impl`; unread config fields; `HTTPException` in domain, `Date.now`, secrets, f-string SQL, `.status =` outside entity, bare `except Exception` in UC; **duplicated blocks**; **workflow `permissions` / CORS `*` / secrets in md/evidence**; **`update(**` / `Object.assign` / `req.body.role` / path join / `localStorage` token**.
3. **Taxonomy + behavior-lock + blast:** families APPLIED with oracles? AC oracle in test body? Anti-N/A? one skip = one trigger?
4. **Live surface + honest errors:** every listed port called? err-variant provokes producer? toast/log on mapped failure?
5. **Behavior SSOT:** second copy of an algorithm? owner listed in `behavior_owners` or extracted this PR? ([A39](#prime-a39--behavior-ssot))
6. **Secure Continuum:** CI least privilege? no secret in evidence/chat? headers/CORS/CSRF or honest N/A? IaC when present? ([A40](#prime-a40--secure-continuum))
7. **Trust Pipeline:** schema before UC? authz before mutation? IDOR oracle When multi-user? no mass-assign? path jail? session-token hygiene? ([A41](#prime-a41--trust-pipeline))
8. **Checker:** no existence-only steps; `checker-integrity-gate` would pass on this repo's `prime_check`.
9. [AGENT-2](#agent-2--pre-commit-checklist).

## PRIME-B09 — ADR

**Min tier:** CRITICAL; SHOULD at PRIME+

- **MUST:** ADR in `docs/adr/` for non-trivial architecture/contract changes.
- **MUST:** template:

| Section | Content |
|---------|---------|
| **Контекст** | Problem and constraints |
| **Варианты** | Options considered and rejected |
| **Решение** | Choice and contract |
| **Последствия** | Pros, cons, cost of change |

- **SHOULD:** any engineer understands *why* in 5 minutes — without reading half the repo.

## PRIME-B10 — Performance

**Min tier:** PRIME+

- **MUST:** profile before optimizing — do not guess bottlenecks.
- **SHOULD:** correctness and readability first; optimize only proven hot paths.
- **SHOULD:** batching, caching, zero-alloc where metrics prove need.
- **MAY:** native module / separate service for proven bottlenecks if project supports it.

## PRIME-B11 — Client apps (web / mobile / desktop)

**Min tier:** STANDARD+ · **desktop PRIME MUST** below  
**Enforced by:** `e2e-ui` · `ignored-test-gate` · `no-swallow-gate` · `ffi-safety-gate` (When native)

- **SHOULD:** Presentation = UI only; logic in hooks/stores/services/use cases.
- **SHOULD:** server state on server; UI state local; **business invariants in Domain**.
- **MUST (desktop PRIME):** composition **не глотает** ошибки UI-команд — mapped Err + toast/balloon ([A37](#prime-a37--honest-errors--no-swallow)).
- **MUST (desktop PRIME):** E2E либо реально гоняется, либо каждая ignored-тест в `skipped_steps` с машиной/ADR. AC с hwnd/pixels **не** закрываются unit-именем.
- **MAY (desktop PRIME):** one dispatcher for input/commands **IF** that Skin fits — as **example** of [A39](#prime-a39--behavior-ssot), not a separate UI constitution. HTTP/CLI/jobs follow A39 the same way.
- **MUST:** settings, которые нельзя изменить в UI, **не** считаются настройками в AC ([A34](#prime-a34--intent-lock), [A36](#prime-a36--live-surface)).
- **MUST:** lint + format + typecheck before done.
- **MUST NOT:** `dangerouslySetInnerHTML`, `eval`, secrets in `localStorage` ([A18](#prime-a18--owasp-input-hygiene)) — without ADR; prefer httpOnly cookies or bearer ([A41](#prime-a41--trust-pipeline)).
- **MUST:** desktop/IPC commands follow Trust Pipeline When privileged ops ([A41](#prime-a41--trust-pipeline)).
- **MUST NOT:** three identical hit-test / paint / retry bodies across widgets — one owner ([A39](#prime-a39--behavior-ssot)).
- **MAY:** 20-line component — no DI; 200-line component with business logic — **violation**.

## PRIME-B12 — Fuzz & property

**Min tier:** PRIME+ **Enforced by:** `pytest-property`, `injection-fuzz`  
**Taxonomy families:** Property-based · Fuzz · Injection ([A12a](#prime-a12a--test-taxonomy))

- **MUST (PRIME+ When trigger):** property tests for parsers, crypto, money, serialization, idempotency invariants — not optional «nice to have» when those domains touched.
- **MUST (PRIME+ When untrusted input):** injection/fuzz on external input boundaries ([A18](#prime-a18--owasp-input-hygiene)).
- **SHOULD (CRITICAL):** fuzz + property on all external input + critical invariants.
- **SHOULD (PRIME+ When complex branching):** logic-fuzz / chaotic action sequences (negative + property combo).
- **MUST NOT:** property/fuzz tests that never fail on broken logic.
- **MUST NOT:** skip injection family with «у нас же schema validation» without fuzz evidence.

## PRIME-B13 — Ops & runbook

**Min tier:** PRIME+ **When:** long-running service / container / K8s deploy **Enforced by:** `health-gate`, `prod-config`

- **MUST:** liveness + readiness probe per deploy model (`/health` + `/ready`, Lambda ping, k8s probes, desktop N/A with ADR).
- **SHOULD:** graceful shutdown handler tested or documented in ADR.
- **SHOULD:** rollback steps in ADR for deploy-touching changes.
- **MUST:** 12-factor config — secrets env/vault only.
- **MUST:** runbook includes **revoke + rotate** on suspected secret leak (git/CI/chat) ([A40](#prime-a40--secure-continuum), [A19](#prime-a19--supply-chain--secrets)).

## PRIME-B14 — Human handoff

**Min tier:** PRIME+

- **MUST:** evidence block ([A26](#prime-a26--evidence-block)) is the handoff artifact — **no raw secrets**.
- **MUST:** list Secure Continuum status (`secure_continuum:` APPLIED|N/A) ([A40](#prime-a40--secure-continuum)).
- **MUST:** list Trust Pipeline status (`trust_pipeline:` APPLIED|N/A) ([A41](#prime-a41--trust-pipeline)).
- **MUST:** if leak suspected in session — handoff includes rotate/revoke steps ([B13](#prime-b13--ops--runbook)).
- **SHOULD:** list `risks`, `rollback`, `tests_added` for human reviewer.
- **MUST NOT:** hide failing steps or partial coverage in summary.
- **MUST NOT:** paste `.env` / keys into chat «для ревью».

---

## Pattern Catalog — stack-native equivalents

**Project Skin** — как назвать и разложить. **Empire Engine** — одинаковый для всех строк таблицы.  
Gates проверяют Engine, не заставляют одну колонку DDD.

| PRIME outcome | DDD / Clean (example) | Alternatives (equal if outcome met) |
|---------------|----------------------|-------------------------------------|
| Separation: core ↛ I/O | Domain / App / Infra / Presentation | MVC, Hexagonal, Onion, FP pure core + IO shell, Rails MVC, Nest modules |
| Package cohesion: capability together | Bounded context folders / vertical slice | Nest module, Nx lib, Go `internal/<cap>`, Rails engine, mirrored `…/<cap>/` under each layer |
| Folder tree (Skin sample) | textbook `domain/entities` · `use-cases` · `infra` · `presentation` · `tests/unit\|e2e` | **Same outcome** via Nest modules, Rails MVC, Go `internal/<cap>`, mirrored slices — **MUST NOT** rewrite Skin into the sample |
| Rich domain / Anti-anemic | `User.activate()` owns invariant | VO methods · FSM object · enum+validator **inside** the type — not `user.status =` in UC |
| Test taxonomy complete | Unit+Int+Contract + When families | Same outcomes via jest/pytest/go test; GWT names ≡ BDD; Playwright When UI; contract@boundary When API-only; **folders** = Skin (colocate OK) |
| Intent = tests | AC list ↔ **oracle in test body** | GWT docstring + hwnd/pixels/fs assert — not `"AC{i}" in name` |
| Live surface | Port constructed + called from UC | Fake as second impl; identity/todo impl = FAIL — [A36](#prime-a36--live-surface) |
| Honest errors | named Err **provoked**; no `let _ =` | toast/balloon on GUI; dump-bucket = FAIL — [A37](#prime-a37--honest-errors--no-swallow) |
| Behavior SSOT | one facade / one fn / entity method / dispatcher of the same kind of work | Nest injectable policy · Go func in package · Rust inherent method · FP shared pipeline — **NEVER** mandatory UI Router class — [A39](#prime-a39--behavior-ssot) |
| Secure Continuum | least CI permissions · registered headers · CORS allowlist · vault refs · one authorize owner | GHA `permissions:` · GitLab least · Helmet/Tower middleware · Vault/Doppler/GH Secrets — **NEVER** mandatory WAF product — [A40](#prime-a40--secure-continuum) |
| Trust Pipeline | schema→authn→authz(resource)→allowlisted command→UC→safe sink | Nest guards · FastAPI Depends · Axum layers · Spring filters — **NEVER** mandatory IdP brand — [A41](#prime-a41--trust-pipeline) |
| Minimal blast | one capability PR | stacked PRs; Nx affected; CODEOWNERS scope |
| Application entry | `*UseCase.execute()` | `*Handler`, `*Command`, `*Service.method`, MediatR, plain `fn`, Redux thunk, Effect |
| Explicit errors | `Result<Ok,Err>` | Rust `Result`, Go `(T,error)`, sealed exceptions, `Either`, discriminated union |
| Expected vs unexpected | named domain Err in core; infra → global presentation handler | Result/Err for business; middleware / exception filter / recover for DB-down — not try/catch forest in UC |
| Injectable I/O | `IOrderRepository` port | Spring iface + bean, Nest token+interface, trait bounds, constructor Protocol, `Clock` |
| Contract surface complete | Hexagonal ports + adapters | Protocol/ABC · TS interface · Go iface · Rust trait · Nest/Spring DI tokens — [A35](#prime-a35--contract-surface) |
| Composition root | `main` / DI container | Nest `AppModule`, Spring `@Configuration`, FastAPI lifespan, Go `wire` |
| Test double vs port | InMemory implements Port | Fake class · fake struct — not MagicMock(concrete) |
| Thin transport | FastAPI route → UC | Axum handler, Express router, gRPC servicer, GraphQL resolver, CLI subcommand |
| Module isolation | Bounded Context | Package-private, crate visibility, Nx libs, `internal/` Go, ADR shared `contracts/` |
| Idempotent mutation | Ledger table | Unique index, Redis SETNX, Stripe idempotency, outbox dedup |
| Lifecycle rules | Domain FSM **methods** on the entity | DB CHECK constraint, workflow engine, enum + validator **inside** the type + tests — not UC field-assign |
| Observable failure | Err struct fields | OTel span attrs, log middleware, structured `logger.error({...})` |
| Quality gate | `python -m scripts.prime_check` | `npm run prime:check`, `make prime-check`, `cargo xtask prime`, CI job contract |
| Safety-critical predictability | MISRA subset / CERT rules | `clang-tidy` profile · Rust deny `unsafe` w/o ADR · Go race detector in CI |
| Structural defect scan | CISQ / ISO 5055 automated measure | AST Prosecutor 7 gates + cohesion + **port-surface** + **anemic-mutation** + **behavior-ssot** + security static |
| OWASP verification | ASVS checklist per tier | `zta-matrix-gate` · `injection-fuzz` · Threat Model · **continuum gates** ([A40](#prime-a40--secure-continuum)) |

**Agent:** detect Skin → extend it → full Engine for tier → ADR only for **new** Skin pattern. Never: downgrade Engine · flat dump as «Skin» · skip Port for one-impl I/O · unused port · AC-name lock · existence-only checker · clone to avoid shared · mandatory InputRouter · framework/`security.md` as continuum · `write-all` · secrets in evidence/chat · logged-in as IDOR closed · `update(**body)` · client id as ownership.

---

## AGENT-4 — Glossary

| Term | Meaning |
|------|---------|
| Skin / Engine | форма репо / tier-дисциплина Empire |
| Anti-N/A | N/A только с absent-When reason ([SSOT](#anti-na-ssot--один-раз)); «при сомнении» → [Conflict Matrix](#conflict-matrix-при-сомнении--читать-это-не-конкурирующие-абзацы) |
| Conflict Matrix | единая таблица напряжений (When vs YAGNI vs blast vs A40/A41) — Doctrine |
| test_taxonomy_map | family → tests \| N/A(reason) |
| contract_surface_map | contract family → ports/schemas \| N/A(reason) ([A35](#prime-a35--contract-surface)) |
| Contract surface | core/app → contracts only; concrete in adapters/composition root |
| Rich domain / Anti-anemic | lifecycle/status via entity methods; not public assign ([A05](#prime-a05--layer-law)) |
| Expected vs unexpected | business Err in core; infra crash → presentation handler ([A10](#prime-a10--result)) |
| Outbound port | driven port: Repo, Clock, Gateway… |
| Inbound port | driving port: UseCase/Command iface When multi-entry |
| Composition root | only place concrete adapters are wired |
| Intent lock / behavior-lock | AC + **oracle** ↔ test **body** ([A34](#prime-a34--intent-lock)) |
| Live surface | declared port/field is constructed and called ([A36](#prime-a36--live-surface)) |
| No swallow | process-boundary Result mapped or ADR ([A37](#prime-a37--honest-errors--no-swallow)) |
| Checker integrity | no existence-only / unconditional GREEN steps ([A38](#prime-a38--checker-integrity)) |
| Behavior SSOT | one owner per policy/algorithm; others CALL ([A39](#prime-a39--behavior-ssot)) |
| Clone | near-duplicate body of the same algorithm (renames OK) without a shared call |
| Owner | canonical symbol (fn / method / facade / strategy / dispatcher) that callers invoke |
| Compress vs split | extract owner then shrink leftovers ≠ clone into a second file ([A11](#prime-a11--decomposition)) |
| Secure Continuum | secret/trust gated on app · CI · chat · ops — not code-only OWASP ([A40](#prime-a40--secure-continuum)) |
| Channel secret | secret in any durable text channel (git, CI log, chat, evidence, image layer) without vault/ref |
| CI least privilege | explicit minimal workflow permissions; no write-all / fork-PR secret trust |
| Security theatre | checklist/`security.md`/Helmet-in-package.json without Enforced-by gate |
| Trust Pipeline | ordered trust cut schema→authn→authz→command→UC→safe sink ([A41](#prime-a41--trust-pipeline)) |
| IDOR | access another user's resource by guessing/changing id |
| Mass assignment | binding full request onto entity including privileged fields |
| Allowlisted command | explicit fields/Command DTO — only those enter UC |
| Resource-scoped authz | principal may act on **this** resource — not merely authenticated |
| Oracle | observable fact the test must break if production lies |
| skipped_steps | one skip = one trigger + ADR + sunset — never one ADR for 15 N/A |
| Blast radius | min capabilities/files ([A33](#prime-a33--blast-radius)) |
| Law→Gate | MUST с Enforced-by → real step |
| Package cohesion | capability folders ([A05a](#prime-a05a--package-cohesion)) |
| Contract@boundary | API E2E-equivalent |
| Fix-until-green / Stop-the-line | red→fix→green; don't stack on broken base |
| AST Prosecutor | agent-written AST/import gates |
| Prime Check | merge gate exit 0 ([AGENT-5](#agent-5--prime-check)) |
| adoption_mode | greenfield \| legacy |

---

*Ни одного зелёного `prime_check` без правды исхода. Ни одного AC без оракула. Ни одного порта без вызова. Ни одного `let _ =` на I/O. Ни одного театрального step. Ни одного exclude composition на greenfield. Ни одного второго экземпляра того же алгоритма без вызова owner. Ни одного секрета вне vault/ref. Ни одного `write-all` ради удобства. Ни одного client-owned id как доказательства прав. Ни одного request-bag → entity.*

*End of MAWYXX PRIME v5.7 — Build for Billions. Code for Vibe. Rule with Logic.*
