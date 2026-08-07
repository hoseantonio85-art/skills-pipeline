# Отчёт нормализации: large-entity-modal

## Scope

Паттерн владеет semantic anatomy крупной object modal, hierarchy Header/Content/Meta/Footer, modal-level states и continuity contract. Он не владеет domain content, meta schema, workflow action internals, navigation controls, nested drawers, confirmation или базовой surface mechanics.

Product-specific требования отсутствуют: исходный блок содержит placeholder.

## Implementations inspected

### Agent Risks — 741fa169e66

Просмотрены `src/components/ModalLayout/ModalLayout.tsx`, `withNavigation.tsx`, colocated styles, router usage и `src/pages/ReadonlyAgentRisksForm/ReadonlyAgentRisksForm.tsx` как место наполнения shell.

Подтверждает overlay shell, close/back, previous/next, loading, responsive body и nested surface integration. Не нормированы chat/report coupling, query names, animation timing, fixed widths/z-index и product store.

### Measures — 04d04bbdd29

Просмотрены тот же shell set, `src/pages/ReadonlyMeasureForm/ReadonlyMeasureForm.tsx`, непосредственно используемый Info/history context и router config.

Подтверждает повторяемость shell, content/meta, anchors, workflow actions и auxiliary history intent. Ограничения: footer не принадлежит shell, mobile actions отличаются, shared APIs скрыты.

### Risks — 029af7b6402

Просмотрены shell set, `src/pages/ReadonlyRiskForm/ReadonlyRiskForm.tsx`, Summary usage и router config.

Подтверждает summary-first rich content, meta, related sections, workflow/history intents и return-to-list continuity. Ограничения: domain-heavy view, implicit URL protocol и action-placement conflict.

## Evidence comparison

| Решение | Agent Risks | Measures | Risks | System rule | Classification |
|---|---|---|---|---|---|
| Large modal shell | local `ModalLayout` | local copy | local copy | Object modal для полного просмотра | normative intent; implementation open |
| Header/Body/Footer | content supplies regions | content supplies regions | content supplies regions | Явная anatomy | normative |
| Content + Meta | present, domain-specific | clear split | clear split | Явное разделение | normative |
| Summary-first | narrative content | description-led | explicit Summary | Сначала смысл | normative |
| Footer actions | embedded view | `WorkflowActions` | `WorkflowActions` | Actions в footer | normative boundary; implementation conflicted |
| Route-backed origin | query protocol | query protocol | query protocol | Не требует URL | reference-backed |
| Previous/next | desktop | desktop | desktop | Не обязательны | optional / reference-backed |
| Nested Drawer | categories/files | history | history | Auxiliary allowed | optional; delegated |
| Chat | embedded shell | embedded shell | embedded shell | Не часть modal rule | implementation-specific |
| Geometry/motion | fixed local values | fixed/raw colors | fixed/raw colors | Tokens only | implementation-specific/conflict |

## What became normative

- object-modal intent для полного просмотра по текущему approved UX context;
- Header → Body(Content + Meta) → Footer;
- summary/meaning before raw details;
- Meta как компактный вторичный слой;
- workflow actions только в footer region без header duplication;
- close/continuity и modal-level state boundaries.

## What remained reference-backed

- route-backed origin and back-stack;
- previous/next navigation внутри упорядоченного набора;
- anchors для длинного content;
- auxiliary history/files/category intents;
- full-height responsive shell.

## What was delegated to child patterns

- `entity-summary`;
- `entity-content-section`;
- `entity-meta`;
- `workflow-footer`;
- `related-entity-navigation`;
- `auxiliary-drawer`;
- `confirmation-modal`;
- `modal-surface`.

## What was rejected as implementation-specific

- три локальные копии `ModalLayout` как reusable component;
- chat MFE и report mode;
- MobX/store adapters и query parameter names;
- 1320/600 px geometry, 24 px radius/padding, z-index 999;
- raw rgba/hex and exact animations;
- domain sections, field schemas and workflow labels;
- clickable `Icon` as navigation implementation.

## Conflicts

- Approved footer rule и фактический ownership/placement `WorkflowActions` не полностью согласованы.
- Repeated route protocol полезен, но implicit и duplicated.
- UI Kit `Modal` export подтверждён, но suitability для large composition не проверена; references используют shared `Portal`.
- Mobile скрывает previous/next и меняет actions без общего contract.
- Nested overlays существуют без доказанного focus/Escape/back policy.

## Open questions

- Нет product-specific требований.
- Требуются approved modal-surface package/API и reusable shell ownership.
- Требуются footer/mobile, nested stack и partial error contracts.
- Требуется решение URL versus local navigation state.
- Требуется accessibility verification focus trap, return focus и navigation controls.

## Readiness for stage 03

Готовность: **0.78 — ready with review gates**. Semantic composition хорошо подтверждена approved UX rules и тремя production revisions. Реализация остаётся guidance из-за отсутствия verified reusable shell и конфликтов footer, navigation, nested stack и accessibility.

### Классификация для review

**Normative:** modal intent; Header/Body(Content + Meta)/Footer; summary-first hierarchy; footer action boundary; continuity and parent state model.

**Reference-backed:** route backing; previous/next; anchors; auxiliary surface intents.

**Delegated:** summary; content sections; meta; workflow footer; related navigation; drawer; confirmation; base modal surface.

**Implementation-specific:** local shell copies; chat/report; stores/query names; fixed geometry; raw colors; animations; domain content.

**Open:** modal package/API; reusable ownership; footer/mobile; stack/focus/Escape; URL contract; partial errors; missing user requirements.

