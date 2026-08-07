# Отчёт нормализации: filter-bar-and-advanced-filter-drawer

## Scope

Паттерн владеет двухуровневой композицией фильтрации, applied/draft interaction, filter actions, active-state communication и контрактом обновления results surface. Он не владеет конкретными controls/fields, Drawer mechanics, result states, persistence transport или product store/API.

Product-specific требования отсутствуют: исходный блок содержит placeholder. Использованы approved UX/UI/frontend rules и production evidence.

## Implementations inspected

### Measures — 04d04bbdd29

Просмотрены `src/pages/Measures/components/Filters/Filters.tsx`, `QuickFilters/QuickFilters.tsx`, colocated styles, `src/components/FilterFieldView/FilterFieldView.tsx`, `src/stores/models/Filters.ts` и место использования `src/pages/Measures/Measures.tsx`.

Подтверждает neutral two-level composition, quick chips, disclosed search, Drawer, applied/template split, Apply/Reset, field groups и active indication. Локальны MobX, tracking, server-driven field renderer, exact props и geometry.

### Risks — 029af7b6402

Просмотрены соответствующие `Filters`, `QuickFilters`, styles, `FilterFieldView`, `Filters` model и page usage.

Подтверждает повторяемость, cancel restore, pending actions и dependent-option refresh. Локальны attention-zone fade/transform, доменные sections, immediate reset/search, analytics и concrete payload conversion.

Agent Risks рассмотрен только как discovery-backed контраст search/quick subset; он не включён в основную evidence table, потому что advanced drawer отсутствует.

## Evidence comparison

| Решение | Measures | Risks | System rule | Classification |
|---|---|---|---|---|
| Quick filters на странице | Radio/Checkbox chips | Radio/Checkbox chips | Частые состояния видны сразу | normative |
| Advanced filter | Drawer | Drawer | Полный набор в Drawer | normative intent |
| Search | раскрывается кнопкой, debounce | то же | Не задан как обязательный | optional / reference-backed |
| Draft отдельно от applied | `templateData` / `data` | `templateData` / `data` | Обратимость согласуется с UX | normative |
| Apply | search + close | search + close | Явное действие | normative |
| Close без Apply | restore template | restore template | Предсказуемая отмена | normative |
| Reset timing | неоднозначный commit | immediate search | Не определено | open |
| Active indication | локальная красная точка | та же | Не только цвет | intent normative; visual implementation-specific |
| Phone | quick filters скрыты | quick filters скрыты | Нет утверждённого правила | implementation-specific / open |
| Drawer package | shared facade | shared facade | Прямые verified UI Kit exports | open |

## What became normative

- двухуровневая иерархия quick filters + advanced Drawer для этого pattern;
- quick filters как приоритетный subset;
- applied/draft separation;
- explicit Apply и cancel-without-commit;
- согласованный results-update interface;
- доступная индикация applied criteria;
- preservation of structure и draft при применимых async/error states.

## What remained reference-backed

- раскрываемый search с debounce;
- group reset;
- pending indicator на Apply/Reset;
- группировка server-configured fields;
- route/query restoration как возможная интеграция.

## What was delegated to child patterns

- `quick-filter-control`;
- `search-field`;
- `filter-field`;
- `drawer-surface`;
- `results-surface`;
- `query-state-persistence`.

## What was rejected as implementation-specific

- MobX-State-Tree model и `templateData` naming;
- `@sber-orm/components` conversion/tracking facade;
- attention-zone animation and opacity;
- red active dot geometry;
- exact gaps/heights and phone hiding;
- specific UI Kit props and domain field formats.

## Conflicts

- Reset commit timing расходится и оставлен open.
- Drawer семантически задан approved UX rule, но его package/export не подтверждён UI Kit index.
- Mobile references скрывают quick filters, но этого недостаточно для universal rule.
- Dependent option refresh полезен, но не должен применять draft к results автоматически.

## Open questions

- Нет product-specific требований.
- Требуется approved Drawer/shared ownership.
- Требуется reset timing contract.
- Требуются accessible active-count и mobile behavior.
- Требуются validation/retry и URL/local persistence rules.

## Readiness for stage 03

Готовность: **0.80 — ready with review gates**. Композиция и state boundary подтверждены двумя production implementations и approved UX rule. До production reuse нужны design/frontend решения по Drawer dependency, Reset, mobile и accessibility. Это guidance, не reusable React component.

### Классификация для review

**Normative:** two-level hierarchy; quick-filter priority; applied/draft split; Apply/Cancel semantics; results interface.

**Reference-backed:** disclosed search; grouped fields; group reset; pending treatment.

**Delegated:** quick controls; search field; filter fields; Drawer mechanics; results states; query persistence.

**Implementation-specific:** stores, tracking, payload conversion, animations, active-dot geometry, fixed spacing.

**Open:** Drawer export/ownership; Reset timing; mobile access; accessible active indication; validation/retry; URL contract; missing user requirements.

