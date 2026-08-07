---
id: drawer-inside-modal
title: Drawer внутри модалки
status: draft
maturity: reference-backed
category: surface
version: 0.1.0

implementation:
  type: guidance
  reusable_component: false

owners:
  design: needs-review
  frontend: needs-review

normative_scope:
  - auxiliary-drawer intent inside a parent modal
  - continuity between parent modal and nested drawer
  - nested-surface lifecycle and stack relationship
  - integration contract for drawer content and actions

delegated_patterns:
  - modal-surface
  - drawer-surface
  - auxiliary-content
  - workflow-footer
  - confirmation-modal
  - surface-stack
  - related-entity-preview

last_reviewed: 2026-08-07
---

# Drawer внутри модалки

## Назначение

Вложенная auxiliary surface для короткого просмотра, уточнения или действия без закрытия parent modal и потери контекста основной сущности. Паттерн определяет связь modal ↔ drawer, но не внутреннюю реализацию Drawer, domain content или workflow controls.

## Пользовательская задача

Открыть историю, источник, технические детали, краткий related preview или выполнить короткий вспомогательный шаг, затем вернуться к той же сущности и месту работы в modal.

## Pattern responsibility

### Owns

- допустимый auxiliary intent поверх parent modal;
- сохранение состояния и идентичности parent modal;
- open/close lifecycle и ожидаемый return target;
- отношение nested drawer к surface stack;
- интерфейс между drawer content/actions и parent modal.

### Delegates

- overlay, focus trap, Escape, geometry и animation базового Drawer;
- anatomy header/body/footer самого Drawer;
- history/files/category/related content;
- workflow actions, validation и confirmation;
- modal shell и его domain state;
- multi-layer stack policy глубже одного nested drawer.

## Use when

- пользователь должен сохранить текущий modal context;
- задача вспомогательная, короткая и уже относится к открытой сущности;
- нужен источник, история, техническая деталь, краткий preview или компактное действие;
- полный просмотр нового основного объекта не требуется.

## Do not use when

- Drawer подменяет полный просмотр основной сущности;
- пользователь должен принять самостоятельное важное решение, требующее action modal;
- содержимое требует длительного чтения или сложной workspace-навигации;
- Drawer добавлен как обязательный промежуточный шаг перед полным object view;
- нельзя определить однозначный возврат к parent modal.

## Anatomy

1. Parent-modal context — сохранённая основная сущность и рабочее состояние.
2. Drawer trigger/origin — элемент parent modal, задающий auxiliary intent.
3. Nested drawer surface — delegated верхний слой.
4. Auxiliary content slot — короткое содержимое текущего intent.
5. Optional drawer actions — действия только этого вспомогательного шага.
6. Close/return interface — возврат к trigger и неизменённому либо явно обновлённому parent context.
7. Surface-stack interface — порядок активных слоёв и владение вводом.

## Slots

| Slot | Назначение | Обязательность | Допустимое содержимое | Constraints | При отсутствии | Delegated pattern |
|---|---|---|---|---|---|---|
| `parent-context` | Сохранить основную сущность и modal state | required | identity, scroll/section, read/edit context | drawer не заменяет и не сбрасывает parent без явного outcome | паттерн неприменим | `modal-surface` |
| `trigger` | Открыть конкретный auxiliary intent | required | history/source/detail/preview/short-action intent | доступное имя; передаёт return target и нужный context | drawer не открывается | control принадлежит parent composition |
| `drawer-surface` | Создать вложенный верхний слой | required | approved Drawer container | focus/overlay/geometry делегированы; должен поддерживать in-modal stacking | паттерн неприменим | `drawer-surface`, `surface-stack` |
| `drawer-title` | Идентифицировать вспомогательный контекст | required | короткий title, optional parent-relative qualifier | не выдает preview за полный объект | паттерн неприменим | `drawer-surface` |
| `auxiliary-content` | Выполнить короткую задачу | required | history, files, source, technical detail, compact preview/form | scope ограничен intent; не копирует весь object modal | показать применимый empty/error state | `auxiliary-content`, `related-entity-preview` |
| `drawer-actions` | Завершить вспомогательный шаг | optional | apply/save/cancel/download/add или compact workflow intents | относятся только к Drawer; pending/outcome не блокируют parent без причины | footer не занимает место | `workflow-footer`, `confirmation-modal` |
| `close-return` | Закрыть верхний слой и восстановить interaction | required | close/cancel/back intent | результат, focus target и parent update предсказуемы | паттерн неприменим | `drawer-surface`, `surface-stack` |

## Information hierarchy

Drawer явно вторичен относительно parent modal. Title связывает auxiliary content с текущей сущностью. Внутри Drawer сначала показывается смысл/результат вспомогательного шага, затем детали; actions относятся только к этому слою. Parent modal остаётся визуальным и навигационным контекстом, но не принимает ввод, пока Drawer активен.

## Behavior

- Открытие Drawer не закрывает и не переинициализирует parent modal.
- В каждый момент один верхний слой владеет keyboard/pointer interaction; background layers не интерактивны.
- Drawer получает минимальный context, необходимый для auxiliary intent, а не полный mutable store parent surface.
- Закрытие без commit сохраняет parent state. Успешное действие возвращает явный outcome, после чего parent локально обновляет затронутые данные либо refreshes по contract.
- Ошибка Drawer не превращает parent modal в error state, если parent data остаётся валидной.
- Переход из Drawer к полному просмотру другой сущности не определяется этим pattern: intent передаётся approved entity-details/navigation pattern.
- Второй nested overlay не открывается автоматически. Если он необходим, порядок слоёв, Escape/back и focus определяются `surface-stack`.

## Actions

- `open` принадлежит trigger в parent modal.
- `close/cancel` завершает верхний auxiliary layer без скрытого commit.
- Optional `save/apply/add/download` относится только к drawer intent; placement и control API делегированы.
- Consequential action требует соответствующего confirmation/action pattern, а не превращает Drawer в modal решения.
- После success parent получает explicit outcome; закрывать Drawer автоматически или оставлять feedback определяет child workflow contract.

## Required states

- `default`: Drawer закрыт, trigger доступен, parent modal владеет interaction.
- `loading`: после открытия shell/title сохраняются, auxiliary content показывает ожидание.
- `refreshing`: доступный content остаётся видимым, обновление локально обозначено.
- `empty`: объясняет отсутствие history/files/details и не выглядит как parent-modal error.
- `recoverable error`: сохраняет parent context и drawer intent, предлагает retry или close.
- `validation error`: применимо только к delegated short form; commit не происходит, ошибка связана с control.
- `pending action`: повтор drawer action блокируется локально; close guard определяется consequence contract.
- `success feedback`: outcome понятен и передаётся parent; дальнейшее close/refresh явно задано.
- `disabled`: trigger или action объяснимо недоступны; пустой Drawer не открывается.
- `nested surface open`: Drawer является верхним активным слоем над modal; более глубокий слой допускается только с определённым `surface-stack` contract.

## Variants

- `read-only detail`: источник или техническая информация без footer actions.
- `history`: read-only chronological content с loading/empty.
- `related preview`: краткий контекст связанного объекта, не полный object view.
- `short auxiliary action`: компактный шаг с footer actions и optional validation.
- `files`: просмотр/download либо короткое add/save состояние.

Variants описывают intent, а не конкретные Risk Categories, Measure History или Assessment Files implementations.

## Delegated patterns

- `modal-surface` — parent shell и modal-level states.
- `drawer-surface` — header/body/footer anatomy, overlay, focus, Escape, scroll lock, geometry и responsive presentation.
- `auxiliary-content` — конкретный history/files/source/detail view.
- `workflow-footer` — actions, pending и outcome.
- `confirmation-modal` — consequential action/dirty close.
- `surface-stack` — ownership ввода, z-order, back/Escape и focus across layers.
- `related-entity-preview` — объём и переход из краткого preview.

Пока child pattern отсутствует или не approved, использовать UX Solution, общие surface rules и релевантный production reference; локальные props и размеры не становятся нормой.

## Responsive behavior

- Drawer presentation и width определяет `drawer-surface`; значения 749/800/850 px из references не нормативны.
- На узкой ширине сохраняются parent-relative title, close, content и применимые actions.
- Drawer не должен создавать горизонтальный scroll parent modal или недоступную область между слоями.
- Если mobile presentation перестаёт быть Drawer, semantic auxiliary intent и return contract сохраняются по UX solution.

## Accessibility

- Drawer имеет accessible name и связь с trigger/context.
- При открытии focus переходит в верхний слой; parent modal становится inert для interaction.
- Close возвращает focus trigger либо следующей логичной target после explicit parent update.
- Escape действует на верхний слой; dirty/pending confirmation не позволяет закрыть оба слоя одним событием.
- Screen reader не воспринимает одновременно два активных dialogs без определённой stack semantics.
- Loading/error/success объявляются в пределах Drawer без повторного чтения всего parent modal.

## UI Kit dependencies

Проверены по текущему `component-index.yaml`; props не нормируются.

```yaml
- component: Row
  purpose: integration layout for drawer title, content and actions
  api_status: verified
- component: Col
  purpose: optional responsive content grouping
  api_status: verified
- component: Title
  purpose: auxiliary-context heading
  api_status: verified
- component: Text
  purpose: supporting copy and state descriptions
  api_status: verified
- component: Button
  purpose: close and delegated drawer-action intents
  api_status: verified
- component: Loader
  purpose: auxiliary-content loading
  api_status: verified
- component: Alert
  purpose: applicable contextual notice or recoverable feedback
  api_status: verified
```

`Drawer` во всех references импортируется из `@sber-orm/components`, а не из подтверждённых UI Kit exports. Его concrete API (`inModal`, `position`, `fullHeight`, `width`) не нормируется; approved package/export остаётся open.

## Design tokens

- Surface, overlay, text, spacing, border, shadow, focus и motion используют реальные UI Kit/theme tokens.
- Z-order берётся из approved surface-stack scale, не из локальных magic numbers.
- Fixed widths и offsets references не переносятся.

## Constraints

- Drawer всегда auxiliary относительно открытой modal и не становится полным view основной сущности.
- Одновременно активный верхний слой должен быть однозначен.
- Parent identity/state не копируются в Drawer без необходимости.
- Domain data, services, file download, history model и actions schema не входят в pattern.
- Не создавать обязательную цепочку modal → drawer → modal без UX necessity.

## Content and UX writing

- Title называет auxiliary task: «История», «Источники», «Документы», а при неоднозначности — уточняет связь с сущностью.
- Empty сообщает, что именно отсутствует, без формулировки общей ошибки объекта.
- Error предлагает retry или close и не обещает, что parent data повреждены.
- Actions называют outcome: «Сохранить», «Добавить документы», «Скачать», «Отмена».
- UI copy локализуется; filenames, IDs и runtime values остаются данными.

## Anti-patterns

- Drawer используется для полного просмотра основной сущности или важного самостоятельного решения.
- Открытие Drawer уничтожает scroll, draft или identity parent modal.
- Parent и Drawer одновременно принимают keyboard/pointer input.
- Escape/back закрывает несколько слоёв непредсказуемо.
- Ошибка auxiliary content заменяет весь parent modal error screen.
- Второй overlay открывается без stack/focus policy.
- Width, `inModal` prop, file/history component или store reference объявлены общим API.

## Implementation guidance

- Parent хранит только open intent, selected auxiliary identity и outcome handler; content state принадлежит child adapter.
- Разделить drawer surface, auxiliary content и actions composition.
- При unmount/close отменять или игнорировать stale async responses.
- Обновлять parent только через typed outcome, не через скрытую взаимную mutation.
- Тестировать focus entry/return, Escape one-layer-at-a-time, dirty/pending guard и parent preservation.
- Проверять loading/empty/error независимо от parent states.
- Не копировать widths и `@sber-orm/components` props; сначала подтвердить approved Drawer API.

## Evidence

| Repository | Revision | File | Что подтверждает | Ограничения |
|---|---|---|---|---|
| sberorm-enablers/sberorm-cloud-agent-risks-front | 741fa169e66 | `src/pages/ReadonlyAgentRisksForm/ReadonlyAgentRisksForm.tsx`; `components/RiskCategories/RiskCategories.tsx`; `components/FilesFooter/FilesFooter.tsx`; colocated styles | Два drawer intents внутри entity modal: category detail/actions и files; parent context сохраняется; optional footer | Несколько overlays без доказанного stack policy; width 749 и shared Drawer props локальны; domain workflow/file modes сложны |
| sberorm-enablers/sberorm-cloud-measures-front | 04d04bbdd29 | `src/pages/ReadonlyMeasureForm/ReadonlyMeasureForm.tsx`; `components/History/History.tsx`; `components/History/components/EmptyHistory/EmptyHistory.tsx`; colocated styles | Чистый read-only history Drawer, локальные loading/empty states, возвращение к measure modal | Width 850; history content domain-specific; focus/Escape/return не видны; Drawer из shared facade |
| sberorm-enablers/sberorm-cloud-risks-front | 029af7b6402 | `src/pages/AssesmentTaskForm/components/FilesDrawer/FilesDrawer.tsx`; `types.ts`; `styles.module.scss`; `src/pages/AssesmentTaskForm/AssesmentTaskForm.tsx` | Read-only source/files Drawer без ухода из task modal; contextual alert и download intent | Narrow use case; нет footer actions/empty/error UI; width 800 и concrete `inModal` API локальны; download error проглатывается |

## Reference implementation

Основной reference — Measures `ReadonlyMeasureForm` + `History`: наиболее чистый auxiliary read-only Drawer с loading/empty внутри parent modal. Дополнительные references: Agent Risks — actions и два разных intents; Risks Assessment Files — source transparency без footer.

Reference implementation является доказательством и примером реализации. Его код, props, геометрия и локальные domain-specific решения не копируются автоматически и не становятся нормативными, если это отдельно не указано в паттерне.

## Conflicts and decisions

### Auxiliary scope

**Found:** history, files/source и category details/actions различаются по content, но сохраняют parent modal.

**Decision:** нормировать auxiliary intent и continuity, не конкретный content type.

**Classification:** normative.

**Reason:** соответствует approved Modal/Drawer distinction и повторяется в трёх production revisions.

**Evidence:** UX rules и три implementations.

### Drawer surface API

**Found:** все references используют shared `Drawer` с `inModal`, absolute/full-height и разными fixed widths; export отсутствует в UI Kit index.

**Decision:** делегировать surface contract и не переносить props/geometry.

**Classification:** open dependency; implementation-specific API.

**Reason:** frontend rules требуют verified exports; width может меняться независимо.

**Evidence:** three Drawer usages, `component-index.yaml`.

### Footer actions

**Found:** Agent drawers имеют conditional actions; Measures/Risks examples read-only.

**Decision:** `drawer-actions` optional; action internals принадлежат workflow/confirmation patterns.

**Classification:** optional / reference-backed.

**Reason:** наличие actions зависит от intent, не от nesting itself.

**Evidence:** Agent `ReadonlyAgentRisksForm`/`FilesFooter`; Measures History; Risks FilesDrawer.

### Stack and focus

**Found:** production code показывает несколько возможных overlay states, но не доказывает focus trap, return focus, Escape order или maximum depth.

**Decision:** один верхний слой владеет interaction; точный multi-layer contract делегировать и оставить open.

**Classification:** normative safety boundary; open implementation.

**Reason:** accessibility требует однозначного active layer, но evidence недостаточно для API/depth.

**Evidence:** Agent multiple Drawer/modal actions; discovery concerns.

### Parent update

**Found:** read-only drawers не меняют parent; file/category actions могут обновить данные.

**Decision:** close без commit сохраняет parent; successful mutation возвращает explicit outcome для targeted refresh.

**Classification:** reference-backed guidance.

**Reason:** предотвращает hidden cross-surface mutation, не навязывая store technology.

**Evidence:** Agent action handlers and file modes; Measures/Risks read-only cases.

## Open questions

- Product-specific требования не предоставлены: блок содержит placeholder.
- Какой approved package/export и API реализует Drawer внутри modal?
- Каковы maximum stack depth, z-order, Escape/back и focus-return rules?
- Может ли mobile использовать иной presentation при сохранении auxiliary intent?
- Когда successful drawer action автоматически закрывает surface?
- Нужен ли общий typed outcome contract для обновления parent modal?
- Как стандартизировать partial error/retry для downloads/history/actions?

## Acceptance checklist

- [ ] Intent короткий и auxiliary; Drawer не заменяет полный object view.
- [ ] Parent modal сохраняет identity, scroll и незатронутый state.
- [ ] Только верхний слой принимает interaction.
- [ ] Close/Cancel не делает скрытый commit и возвращает focus предсказуемо.
- [ ] Loading, empty и recoverable error локализованы внутри Drawer.
- [ ] Optional actions относятся только к drawer task и имеют pending/outcome contract.
- [ ] Deeper overlay не открывается без surface-stack rules.
- [ ] Responsive presentation сохраняет auxiliary intent и return path.
- [ ] Drawer dependency/API проверены; fixed widths/props references не скопированы.
- [ ] Domain history/files/category code не включён в composition contract.

