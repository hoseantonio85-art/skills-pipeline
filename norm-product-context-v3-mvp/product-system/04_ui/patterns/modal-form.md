---
id: modal-form
title: Форма в модалке
status: draft
maturity: reference-backed
category: form
version: 0.1.0

implementation:
  type: guidance
  reusable_component: false

owners:
  design: needs-review
  frontend: needs-review

normative_scope:
  - modal-form anatomy and information hierarchy
  - draft, validation, submit and cancel lifecycle
  - modal-level form state model
  - integration between form body, feedback and footer actions

delegated_patterns:
  - modal-surface
  - form-section
  - form-field
  - validation-summary
  - workflow-footer
  - confirmation-modal
  - staged-form
  - attachment-field
  - auxiliary-drawer

last_reviewed: 2026-08-07
---

# Форма в модалке

## Назначение

Сфокусированная composition для создания или редактирования сущности в modal, когда сценарий важнее текущего page context и должен завершаться явным submit/cancel. Паттерн определяет lifecycle формы и связь регионов, но не schema полей, базовую modal surface, validation controls, footer component или wizard mechanics.

## Пользовательская задача

Заполнить или изменить данные сущности, понять обязательность и ошибки, безопасно сохранить результат либо выйти без случайной потери введённого.

## Pattern responsibility

### Owns

- anatomy Header → Feedback/Progress → Form Body → Footer;
- draft initialization, validation, submit, cancel и success lifecycle;
- distinction initial loading, submitting и recoverable failure;
- dirty-close boundary;
- contract между form sections, validation feedback и workflow actions;
- outcome для вызывающего context.

### Delegates

- overlay, focus trap, Escape, geometry и scroll lock modal surface;
- field types, formatting, dependencies и field-level accessibility;
- section layout и server-driven form rendering;
- action controls/order и confirmation UI;
- stepper/wizard transitions;
- attachments and uploads;
- auxiliary hints/drawers;
- product store, payload и navigation technology.

## Use when

- create/edit требует фокуса и явного завершения;
- форма достаточно содержательна, чтобы отдельная modal была оправдана;
- пользователь должен сохранить исходный page/modal context;
- UX solution утверждает modal, а не page или drawer.

## Do not use when

- действие короткое и вспомогательное — использовать auxiliary drawer/form;
- нужна только confirmation одного решения;
- работа длительная, многоэтапная или требует широкой workspace-навигации — рассмотреть page/staged workspace;
- форма состоит из одного простого необязательного поля и не требует modal focus.

## Anatomy

1. Modal surface — delegated контейнер и focus boundary.
2. Form header — create/edit intent и entity context.
3. Optional progress — completion или stage context, если полезен.
4. Feedback region — validation summary, recoverable errors и applicable warnings.
5. Form body — прокручиваемые semantic sections/fields.
6. Footer actions — cancel/secondary/primary submit intents.
7. Optional auxiliary-surface host — подсказка, lookup или attachment detail.
8. Outcome interface — success/cancel result для origin context.

## Slots

| Slot | Назначение | Обязательность | Допустимое содержимое | Constraints | При отсутствии | Delegated pattern |
|---|---|---|---|---|---|---|
| `modal-surface` | Изолировать form task | required | approved modal container | geometry/focus/overlay определяются отдельно | паттерн неприменим | `modal-surface` |
| `form-title` | Назвать действие и объект | required | create/edit title, optional entity identifier | одно основное heading; не заменяется progress | паттерн неприменим | — |
| `progress` | Показать completion или stage | optional | completion indicator либо current/total stage | только если progress понятен и вычислим; не обещает несуществующие steps | регион удаляется | `staged-form` или progress primitive |
| `feedback` | Объяснить общие ошибки/предупреждения | recommended | validation summary, server message, attachment warning | не дублирует field errors без пользы; ведёт к исправлению | field-level feedback остаётся | `validation-summary` |
| `form-sections` | Собрать редактируемые данные | required | semantic sections с fields | schema и field contract делегированы; порядок следует задаче | паттерн неприменим | `form-section`, `form-field` |
| `attachments` | Добавить связанные файлы | optional | upload/list intent | upload lifecycle не смешивается с form submit скрыто | секция отсутствует | `attachment-field` |
| `footer-actions` | Завершить form lifecycle | required | cancel, applicable secondary, primary submit/continue | одно постоянное место; permissions/pending учитываются; не дублировать в header | паттерн неприменим | `workflow-footer` |
| `auxiliary-surface` | Дать короткую подсказку/lookup | optional | help, reference, narrow supporting step | не хранит основной form draft; security/content contract отдельно | не занимает место | `auxiliary-drawer` |
| `outcome` | Сообщить origin context результат | required | saved entity identity/version, cancel или recoverable failure | transport не задаётся; success не выдаётся до подтверждённого commit | origin выполняет локальный contract | navigation/data adapter |

## Information hierarchy

Сначала пользователь понимает create/edit intent, затем видит применимый progress/feedback, заполняет логически сгруппированные sections и завершает сценарий footer actions. Ошибка не должна требовать ручного поиска: summary и focus ведут к первому проблемному field. Footer не конкурирует с полями и остаётся устойчивой точкой завершения.

## Behavior

- При открытии создаётся/загружается один draft, связанный с текущим form intent и permissions.
- Initial loading не показывает форму предыдущей сущности как текущую.
- Field changes обновляют draft; applied entity не считается сохранённой до успешного submit.
- Submit запускает полную применимую validation. При ошибке commit не выполняется, feedback становится доступным, focus/scroll ведёт к первой ошибке.
- Во время submit повторный primary action блокируется; введённые значения сохраняются.
- Recoverable server error сохраняет draft и позволяет retry.
- Cancel/close при dirty draft требует осознанного discard contract; конкретная confirmation surface делегирована.
- После success возвращается explicit outcome. Close, переход к entity view или следующий stage определяется UX solution.
- Refresh dependent field options не приравнивается к submit и по возможности блокирует только затронутую часть.

## Actions

- `submit/save` — validate → pending → commit → success outcome либо recoverable error.
- `cancel/close` — выйти; dirty draft проходит discard confirmation.
- `continue` — optional staged intent; валидирует текущий scope и передаёт управление `staged-form`.
- Secondary actions допускаются только если относятся к текущей form task.
- Placement и visual ordering controls определяет `workflow-footer`; modal-form нормирует footer как единственное постоянное место form actions.

## Required states

- `default`: draft загружен, editable fields и разрешённые actions согласованы.
- `loading`: загружается schema/data; shell/title сохраняют orientation, submit недоступен.
- `refreshing`: dependent data/options обновляются без потери draft; блокируется минимальный scope.
- `empty`: schema/entity недоступны или нет редактируемых fields; объяснить причину и дать close/retry, не показывать raw fallback.
- `recoverable error`: draft сохраняется, ошибка submit/load объяснена, доступен retry/close.
- `validation error`: field errors и summary связаны; focus/scroll ведёт к первой ошибке; submit не коммитит.
- `pending action`: повтор submit/continue блокируется; cancel/close следует consequence contract.
- `success feedback`: commit подтверждён; outcome и следующий шаг однозначны.
- `disabled`: field/action имеет объяснимую permissions/dependency причину; disabled form целиком не остаётся без сообщения.
- `nested surface open`: form draft сохраняется; верхний auxiliary/confirmation layer владеет interaction и возвращает focus по surface-stack contract.

## Variants

- `create`: новый draft, success возвращает identity созданной сущности.
- `edit`: draft инициализирован текущей версией; success обновляет существующую сущность.
- `single-step`: один submit охватывает всю форму.
- `staged`: reference-backed intent с Continue/Save, но transitions, cross-step validation и resume принадлежат `staged-form`.

Короткая comment/action form в Drawer не является вариантом modal-form: это auxiliary-form pattern с другим surface intent.

## Delegated patterns

- `modal-surface` — dialog semantics, focus, overlay, geometry и close mechanics.
- `form-section` — section heading/help/layout.
- `form-field` — control, value, validation, dependency и accessibility.
- `validation-summary` — aggregate errors and navigation.
- `workflow-footer` — action ordering, controls, pending и outcomes.
- `confirmation-modal` — dirty discard/consequential confirmation.
- `staged-form` — step model, progress, transitions и resume.
- `attachment-field` — upload/list/error lifecycle.
- `auxiliary-drawer` — hints/lookups/supporting detail.

Пока child pattern отсутствует или не approved, использовать UX Solution, общие UX/UI/frontend rules и relevant production reference; store/API/props reference не становятся нормой.

## Responsive behavior

- Sections переходят из side-label layout в последовательный label/help → fields order.
- Footer actions остаются достижимыми и не перекрывают последнюю ошибку/field.
- Title, feedback и close сохраняются; progress адаптируется без потери current/total meaning.
- Modal geometry и full-screen threshold принадлежат `modal-surface`.
- Staged flow не скрывает critical Save/Cancel только из-за mobile layout.

## Accessibility

- Modal имеет dialog semantics и accessible title; background inert.
- Labels, required state, descriptions и errors программно связаны с fields.
- Submit с validation error переводит focus к summary/первой ошибке предсказуемо.
- Pending объявляется, не меняя accessible name действия произвольно; duplicate submit предотвращён.
- Close/Escape учитывает dirty/pending state и не теряет draft без confirmation.
- Footer следует после body в reading order; sticky presentation не меняет DOM order.
- Progress сообщает current/total semantics; декоративные segments скрыты от assistive tech.

## UI Kit dependencies

Проверены по текущему `component-index.yaml`; props не нормируются.

```yaml
- component: Row
  purpose: form sections and responsive regional layout
  api_status: verified
- component: Col
  purpose: optional section grouping
  api_status: verified
- component: Title
  purpose: form heading
  api_status: verified
- component: Text
  purpose: section help, progress and feedback copy
  api_status: verified
- component: Button
  purpose: explicit form action intents when composing a verified footer
  api_status: verified
- component: Loader
  purpose: initial and submit progress
  api_status: verified
- component: LinearProgress
  purpose: optional completion indication
  api_status: verified
- component: Alert
  purpose: applicable warning or recoverable feedback
  api_status: verified
- component: ScrollBar
  purpose: bounded form-body scrolling
  api_status: verified
```

`WorkflowActions`, `ConfirmationModal`, `ViewMessages`, `Drawer` и validation helpers в references импортируются из `@sber-orm/components` или local code и не зарегистрированы как обязательные UI Kit dependencies.

## Design tokens

- Использовать реальные UI Kit/theme tokens для surface, spacing, text, validation, focus, progress и footer separation.
- Не переносить fixed section widths, padding, loader z-index/radius, raw rgba или custom step geometry.
- Validation и warning colors используют semantic tokens, не локальную palette.

## Constraints

- Form schema, business validation, permissions и payload остаются domain/data layer.
- Pattern не является universal server-driven form renderer.
- Create/edit могут разделять shell, но не обязаны иметь одинаковую business logic.
- Staged form не нормируется по одному реализованному step.
- Нельзя вставлять unsanitized HTML hints; content/security contract делегирован.
- Modal form не используется автоматически для любого CRUD action.

## Content and UX writing

- Title называет действие: «Создать …» или «Редактировать …».
- Section heading описывает группу данных, help объясняет зачем, а не повторяет label.
- Primary action отражает outcome: «Сохранить», «Создать», «Продолжить».
- Validation говорит, что исправить; server error — что произошло и что можно сделать.
- Dirty-close confirmation ясно различает «остаться» и «выйти без сохранения».
- UI copy локализуется; domain/runtime values остаются данными.

## Anti-patterns

- Submit выполняется до validation либо ошибки невозможно найти.
- Loading, saving и dependent refresh представлены одним глобальным blocker без необходимости.
- Cancel/close молча теряет dirty draft.
- Actions дублируются в header/body/footer или вынесены в page floating dock.
- Raw «No data» заменяет empty/recoverable state.
- Один store/component смешивает create, edit, steps, fields, uploads, navigation и analytics без boundary.
- Drawer с одним comment field объявляется modal-form только по имени компонента.
- Fixed geometry, `WorkflowActions` props или product schema копируются как standard.

## Implementation guidance

- Разделить modal shell, form orchestration, domain adapter, sections/fields, feedback и footer actions.
- Моделировать draft, dirty, valid, loading, refreshing, submitting и outcome отдельно.
- Submit pipeline сделать явным: validate → focus/summary on error → commit → outcome.
- Не сбрасывать draft при recoverable error; защищать от stale responses/unmount.
- Child fields возвращают values/errors через typed contract, а не знают navigation/store shell.
- Тестировать create/edit, initial load failure, validation, double submit, server retry, dirty close, success and nested auxiliary surface.
- Проверять UI Kit exports/types; shared facade APIs не переносить по памяти.

## Evidence

| Repository | Revision | File | Что подтверждает | Ограничения |
|---|---|---|---|---|
| sberorm-enablers/sberorm-cloud-measures-front | 04d04bbdd29 | `src/pages/EditMeasureForm/EditMeasureForm.tsx`; `types.ts`; `styles.module.scss`; `components/EditDescription/EditDescription.tsx`; `src/pages/CreateMeasureView/CreateMeasureView.tsx`; router config | Наиболее полный create/edit modal form: title, progress, scroll body, sections, validation focus, messages, submit pending, footer actions, dirty-close confirmation, success navigation | Create/edit intertwined; shared APIs unverified; raw `No measure`; global overlay saving; HTML hint Drawer/security issue; fixed geometry/rgba |
| sberorm-enablers/sberorm-cloud-agent-risks-front | 741fa169e66 | `src/pages/CreateAgentRisksView/CreateAgentRisksView.tsx`; `styles.module.scss`; `components/EditDescription/EditDescription.tsx`; types; router config | Второй production form shell: initial loading, title, current/total progress, sections, validation, Save/Continue footer and success navigation | Проверен только step 1 of 3; custom step segments; error catch hides failure; no explicit dirty-close; shared WorkflowActions unverified |

## Reference implementation

Основной reference — Measures `EditMeasureForm.tsx` вместе с `EditDescription` и `CreateMeasureView`: наиболее полное покрытие form lifecycle. Дополнительный reference — Agent Risks `CreateAgentRisksView.tsx` для повторяемого shell и staged intent.

Reference implementation является доказательством и примером реализации. Его код, props, геометрия и локальные domain-specific решения не копируются автоматически и не становятся нормативными, если это отдельно не указано в паттерне.

## Conflicts and decisions

### Create и edit

**Found:** Measures переиспользует один form component для create/edit; Agent reference покрывает только create.

**Decision:** нормировать общий lifecycle и разные outcome contracts, не требовать один component/store.

**Classification:** normative lifecycle; implementation-specific reuse.

**Reason:** create/edit могут развиваться независимо при одинаковых form invariants.

**Evidence:** Measures `EditMeasureForm`/`CreateMeasureView`; Agent `CreateAgentRisksView`.

### Validation and feedback

**Found:** Measures валидирует fields/attachments, scrolls to error and shows messages; Agent validates template but не показывает полный error contract.

**Decision:** validation-before-commit, accessible error navigation and draft preservation обязательны; конкретный helper/summary делегирован.

**Classification:** normative with partial implementation evidence.

**Reason:** form cannot safely submit invalid data; implementation API may vary.

**Evidence:** both main files; prototype rules state matrix.

### Dirty close

**Found:** Measures uses confirmation flow; Agent create does not expose equivalent behavior in inspected file.

**Decision:** dirty draft requires explicit discard contract; confirmation UI delegated.

**Classification:** normative safety boundary; incomplete reference coverage.

**Reason:** silent data loss violates predictable form lifecycle.

**Evidence:** Measures confirmation integration; Agent absence noted.

### Staged flow

**Found:** Agent shows step 1/3 and Save/Continue; only one step implementation was inspected.

**Decision:** staged variant is reference-backed, but step model/transitions are delegated and not normalized here.

**Classification:** reference-backed / open.

**Reason:** evidence insufficient for a wizard contract.

**Evidence:** Agent `CreateAgentRisksView` and discovery concern.

### Surface boundary

**Found:** `ModalAction` is named modal but implemented as in-modal Drawer with one comment field.

**Decision:** exclude it as modal-form reference; classify as auxiliary form in Drawer.

**Classification:** implementation-specific naming; normative surface distinction.

**Reason:** intent and surface rules have priority over component name.

**Evidence:** Agent `ModalAction.tsx`; approved Modal/Drawer rules.

### Shared dependencies

**Found:** footer, confirmation, messages and Drawer come from shared facade; verified reusable composition export is absent.

**Decision:** keep guidance maturity and delegate child contracts; only list verified UI Kit primitives.

**Classification:** open implementation dependency.

**Reason:** frontend rules forbid invented or hidden APIs.

**Evidence:** imports, `component-index.yaml`, frontend rules.

## Open questions

- Product-specific требования не предоставлены: блок содержит placeholder.
- Какой approved modal-surface и workflow-footer package/API использовать?
- Каков единый validation-summary и server-error contract?
- Когда dirty-close confirmation обязательна и как учитывать autosave?
- Требуется ли отдельный approved `staged-form` pattern?
- Как согласовать attachments pending/error с основным submit?
- Какой success outcome: close, entity view, next step или stay-and-confirm?
- Как сохранять/resume draft и защищаться от version conflict?

## Acceptance checklist

- [ ] Form intent и create/edit context понятны из title.
- [ ] Draft не считается сохранённым до подтверждённого commit.
- [ ] Initial loading, refreshing и submitting различены.
- [ ] Validation блокирует commit и ведёт к первой ошибке.
- [ ] Recoverable error сохраняет draft и предлагает retry.
- [ ] Dirty close не теряет данные молча.
- [ ] Footer — единственное постоянное место form actions.
- [ ] Double submit предотвращён, success outcome однозначен.
- [ ] Responsive layout сохраняет labels, errors, footer и progress meaning.
- [ ] UI Kit exports проверены; shared APIs, geometry и product schema не нормированы.

