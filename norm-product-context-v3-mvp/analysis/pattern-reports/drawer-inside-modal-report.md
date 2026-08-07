# Отчёт нормализации: drawer-inside-modal

## Scope

Паттерн владеет auxiliary intent внутри parent modal, сохранением parent context, nested-surface lifecycle, active-layer boundary и outcome interface. Он не владеет Drawer primitive, domain content, workflow footer, confirmation, parent modal или глубоким stack implementation.

Product-specific требования отсутствуют: исходный блок содержит placeholder.

## Implementations inspected

### Agent Risks — 741fa169e66

Просмотрены `ReadonlyAgentRisksForm.tsx`, `RiskCategories`, `FilesFooter`, их types/styles и непосредственные Drawer blocks. Подтверждает category/files intents, optional actions и сохранение modal context. Ограничения: multiple overlays, fixed width 749, shared props и domain workflow complexity.

### Measures — 04d04bbdd29

Просмотрены `ReadonlyMeasureForm.tsx`, `History.tsx`, `EmptyHistory` и colocated styles. Подтверждает чистый read-only history Drawer с local loading/empty. Ограничения: fixed width 850, domain history model, отсутствие доказанного focus/Escape contract.

### Risks — 029af7b6402

Просмотрены `FilesDrawer.tsx`, types/styles и parent `AssesmentTaskForm.tsx`. Подтверждает files/source transparency без ухода из task modal. Ограничения: narrow content, width 800, no empty/error surface и swallowed download error.

## Evidence comparison

| Решение | Agent Risks | Measures | Risks | System rule | Classification |
|---|---|---|---|---|---|
| Auxiliary intent | categories/files/actions | history | source files | Drawer для короткого шага | normative |
| Parent preserved | yes | yes | yes | без потери контекста | normative |
| Drawer header/title | dynamic/static | history title | sources title | auxiliary context | normative intent |
| Footer actions | conditional | absent | absent | зависит от task | optional/reference-backed |
| Local states | modes/pending external | loading + empty | file deleted only | применимые states | partial/open |
| Fixed width | 749 | 850 | 800 | geometry not approved | implementation-specific |
| `inModal` shared API | yes | yes | yes | UI Kit export unverified | open dependency |
| Stack/focus/Escape | not explicit | not explicit | not explicit | active layer must be clear | normative boundary/open API |
| Parent mutation | category/files | read-only | read-only download | explicit outcome preferred | reference-backed |

## What became normative

- only short auxiliary intent over parent modal;
- parent identity/state continuity;
- one active top interaction layer;
- explicit close/return boundary;
- local handling of Drawer states/errors;
- Drawer never substitutes full primary-object view.

## What remained reference-backed

- history, files/source and category-preview variants;
- optional footer actions;
- explicit outcome for targeted parent refresh;
- full-height nested presentation.

## What was delegated to child patterns

- `modal-surface`;
- `drawer-surface`;
- `auxiliary-content`;
- `workflow-footer`;
- `confirmation-modal`;
- `surface-stack`;
- `related-entity-preview`.

## What was rejected as implementation-specific

- widths 749/800/850;
- `position='absolute'`, `inModal`, `fullHeight`, `headerRevert` props;
- shared `@sber-orm/components` Drawer as automatically approved dependency;
- category/history/files schemas and services;
- file download implementation, store mutations and local visual details.

## Conflicts

- Repeated shared Drawer API is not verified by current UI Kit index.
- Multiple possible Agent overlays lack explicit stack/focus/Escape evidence.
- Footer actions exist only for some intents and cannot be required globally.
- State coverage differs: Measures has loading/empty, Risks lacks recoverable download feedback.

## Open questions

- Нет product-specific требований.
- Нужны approved Drawer export/API and surface-stack contract.
- Не решены maximum depth, mobile presentation, auto-close after success и typed parent outcome.
- Нужен общий partial error/retry contract.

## Readiness for stage 03

Готовность: **0.77 — ready with review gates**. Intent и continuity подтверждены approved UX rules и тремя production revisions. До production reuse требуются решения по Drawer dependency, focus/Escape/stack, mobile и action outcome/error contracts.

### Классификация для review

**Normative:** auxiliary scope; parent continuity; active top layer; close/return; local state boundary; no full-object substitution.

**Reference-backed:** history/files/category variants; optional footer; full-height presentation; targeted parent refresh.

**Delegated:** modal/drawer surfaces; content; workflow footer; confirmation; stack; related preview.

**Implementation-specific:** fixed widths; shared props; domain models/services; local styles/download/store code.

**Open:** user requirements; approved Drawer API; stack/focus/Escape; mobile; auto-close; typed outcome; partial errors.

