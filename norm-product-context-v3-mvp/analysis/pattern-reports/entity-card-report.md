# Отчёт нормализации: entity-card

## Scope

Паттерн владеет semantic anatomy одной decision-oriented карточки: identity, primary signal, 1–3 decision metrics, attention reason, optional supporting context и open-intent boundary. Он не владеет domain schema, status/metric formatting, details surface, item actions, selection, list ordering или virtualization.

Product-specific требования отсутствуют: исходный блок содержит placeholder.

## Implementations inspected

### Risks — 029af7b6402

Просмотрены `RiskCard.tsx`, `types.ts`, colocated styles и непосредственное использование в `RisksList.tsx`.

Подтверждает identity, status/level/new signals, decision metrics, secondary context и whole-card open. Ограничения: reason не выделена явно, raw button отключает outline, geometry и rgba локальны.

### Measures — 04d04bbdd29

Просмотрены `MeasureCard.tsx`, `types.ts`, `utils.ts`, styles и `MeasureList.tsx`.

Подтверждает metric-led anatomy, status/deadline signals, name/ID, description context, open intent и responsive collapse. Ограничения: domain-heavy fields, literal label, fixed grid/min sizes, raw hex и ambiguous attention reason.

### Agent Risks — 741fa169e66

Просмотрены `AgentRisksCard.tsx`, `types.ts`, styles и `AgentRisksList.tsx`.

Подтверждает compact third-repository skeleton: identity, level/status, supporting metadata и open intent. Не покрывает явные decision metrics и attention reason.

## Evidence comparison

| Решение | Risks | Measures | Agent Risks | System rule | Classification |
|---|---|---|---|---|---|
| Name + ID | оба | оба | name + business ID | обязательны | normative |
| Primary signal | level/status | status/deadline | level/status | обязательный signal | normative |
| 1–3 metrics | losses/strategy | dates/feature | metadata only | 1–3 решающих показателя | normative, partial evidence |
| Attention reason | implicit | implicit | absent | обязательна | normative, implementation gap |
| Supporting context | owner/source | description/department | version/stage/date | не задано | optional/reference-backed |
| Whole-card open | raw button | raw button | raw button | ведёт к просмотру/action | reference-backed intent |
| Route modal | yes | yes | yes | parent/surface concern | delegated/implementation-specific |
| Phone reduction | hides secondary fields | stacks/hides secondary | compact | сохранять смысл | priority normative; layout open |
| Fixed geometry/colors | local | local | local | tokens only | implementation-specific/conflict |

## What became normative

- identity through name + stable user-facing identifier;
- one primary signal understandable without color;
- 1–3 decision metrics or explicitly approved equivalent decision context;
- explicit attention reason;
- hierarchy and preservation of mandatory meaning on responsive layouts;
- accessible open-intent boundary without nested controls.

## What remained reference-backed

- whole-card open intent;
- supporting owner/source/date/description;
- signal-led and metric-led emphasis;
- responsive removal of secondary fields.

## What was delegated to child patterns

- `status-indicator`;
- `metric-display`;
- `entity-details-surface`;
- `item-actions`;
- `selectable-list-item`;
- `list-virtualization`.

## What was rejected as implementation-specific

- `FieldView` and product form schemas;
- raw button copies and route construction;
- domain field names and formatting helpers;
- fixed 160/512/660 px geometry, card heights and breakpoints;
- raw hex/rgba hover colors and exact shadows;
- tracking/test-ID generators.

## Conflicts

- Approved attention-reason rule is not explicitly implemented in all references.
- Agent Risks lacks clear decision metrics; repository repetition alone cannot lower the approved requirement.
- Whole-card raw button works only without nested actions and currently loses visible focus in some styles.
- Mobile references hide secondary content inconsistently; mandatory semantic minimum must be reviewed.

## Open questions

- Нет product-specific требований.
- Нужны content rules/ownership для attention reason.
- Нужен contract для non-numeric decision context и missing values.
- Не решены reusable component ownership, selection/bulk variant и virtualization accessibility.

## Readiness for stage 03

Готовность: **0.82 — ready with review gates**. Semantic anatomy утверждена UX rules и проверена на трёх production revisions. Основные review gates — фактическое покрытие attention reason, non-numeric decision context, focus semantics и future reusable ownership.

### Классификация для review

**Normative:** identity; primary signal; decision metrics/context; attention reason; semantic hierarchy; accessible interaction boundary.

**Reference-backed:** whole-card open; supporting context; signal/metric emphasis; removal of secondary mobile data.

**Delegated:** status; metric formatting; details surface; item actions; selection; virtualization.

**Implementation-specific:** `FieldView`; raw buttons/routes; domain fields; fixed geometry; local colors/shadows; tracking.

**Open:** user requirements; attention-reason ownership; non-numeric context; missing values; reusable component; selection/bulk; virtualization/focus.

