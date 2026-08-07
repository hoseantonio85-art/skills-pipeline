# Отчёт нормализации: modal-form

## Scope

Паттерн владеет modal-form anatomy, draft/validation/submit/cancel lifecycle, parent states и интеграцией body/feedback/footer. Он не владеет fields, sections, modal primitive, footer controls, confirmation, staged transitions, attachments или product store/API.

Product-specific требования отсутствуют: исходный блок содержит placeholder.

## Implementations inspected

### Measures — 04d04bbdd29

Просмотрены `EditMeasureForm.tsx`, types/styles, `EditDescription`, `CreateMeasureView.tsx` и router usage. Подтверждает полный create/edit lifecycle, progress, messages, validation navigation, pending submit, footer actions, dirty-close confirmation и success navigation. Ограничения: mixed create/edit logic, unverified shared APIs, raw empty fallback, global loader, unsafe HTML hint Drawer and local geometry.

### Agent Risks — 741fa169e66

Просмотрены `CreateAgentRisksView.tsx`, styles, `EditDescription`, types и router usage. Подтверждает repeated modal form shell, loading, sections, validation, Save/Continue footer and staged intent. Ограничения: only step 1/3, custom progress geometry, swallowed initial error and no visible dirty-close contract.

`ModalAction.tsx` просмотрен как boundary case и исключён из evidence count: это short form in Drawer, несмотря на имя.

## Evidence comparison

| Решение | Measures | Agent Risks | System rule | Classification |
|---|---|---|---|---|
| Header/body/footer shell | yes | yes | modal focus/actions in footer | normative |
| Draft edit | template | template | form lifecycle | normative intent |
| Initial loading | Loader | Loader | preserve structure | normative |
| Progress | completion percent | step 1/3 | only when meaningful | optional/reference-backed |
| Validation before submit | fields + attachments + focus | template validation | required for safe submit | normative |
| Feedback summary | ViewMessages | not evident | states must explain next step | normative intent/open component |
| Pending submit | saving overlay | loading overlay | prevent duplicate action | normative |
| Dirty close | confirmation | not evident | avoid silent loss | normative boundary/partial evidence |
| Save outcome | close/back/view | entity view/next step | UX-dependent outcome | reference-backed/open |
| Staged flow | no | partial 1/3 | insufficient | reference-backed/open |
| Shared components | facade | facade | verified APIs only | open dependency |

## What became normative

- Header → Feedback/Progress → Body → Footer composition;
- draft separate from committed entity;
- validation-before-commit and error navigation;
- loading/refreshing/submitting distinction;
- recoverable failure preserves draft;
- dirty-close boundary;
- footer as sole persistent form-action region;
- explicit success/cancel outcome.

## What remained reference-backed

- completion progress;
- Save plus Continue actions;
- route navigation after success;
- server-configured sections;
- staged create intent.

## What was delegated to child patterns

- `modal-surface`;
- `form-section`;
- `form-field`;
- `validation-summary`;
- `workflow-footer`;
- `confirmation-modal`;
- `staged-form`;
- `attachment-field`;
- `auxiliary-drawer`.

## What was rejected as implementation-specific

- MobX templates/stores, routes, tracking and payloads;
- `WorkflowActions`, `ViewMessages`, helpers and facade props as approved APIs;
- fixed section widths/padding, raw rgba and custom progress segments;
- `dangerouslySetInnerHTML` hint Drawer;
- raw `No measure` fallback;
- one-comment `ModalAction` Drawer as modal-form reference.

## Conflicts

- Dirty-close coverage exists only in Measures.
- Validation/feedback is complete in Measures and minimal in Agent.
- Agent staged UI claims three steps but inspected evidence covers one.
- Shared composition APIs are not verified UI Kit dependencies.
- Global overlay loader conflates submit blocking with local refresh.

## Open questions

- Нет product-specific требований.
- Нужны approved surface/footer/validation-summary APIs.
- Не решены autosave/dirty close, attachments lifecycle, staged contract, success destination, draft resume and version conflict.

## Readiness for stage 03

Готовность: **0.79 — ready with review gates**. Core lifecycle подтверждён двумя production implementations и modal/action rules. До production reuse требуются решения по shared dependencies, error summary, dirty/autosave, staged flow and outcome/version contracts.

### Классификация для review

**Normative:** shell hierarchy; draft lifecycle; validation; async state separation; draft preservation; dirty close; footer action boundary; explicit outcome.

**Reference-backed:** progress; Save/Continue; route outcome; configured sections; staged intent.

**Delegated:** modal surface; sections/fields; validation summary; footer; confirmation; staged form; attachments; auxiliary drawer.

**Implementation-specific:** stores/routes/tracking; facade props; fixed geometry; raw colors; HTML hint; raw fallback; ModalAction naming.

**Open:** user requirements; approved APIs; autosave; attachment coordination; wizard; success destination; resume/version conflict.

