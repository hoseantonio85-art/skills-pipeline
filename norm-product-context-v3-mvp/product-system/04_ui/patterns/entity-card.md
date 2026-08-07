---
id: entity-card
title: Анатомия карточки сущности
status: draft
maturity: reference-backed
category: content
version: 0.1.0

implementation:
  type: guidance
  reusable_component: false

owners:
  design: needs-review
  frontend: needs-review

normative_scope:
  - entity-card semantic anatomy
  - information hierarchy inside one card
  - relationship between identity, signal, metrics and attention reason
  - card-level open intent and interaction boundary

delegated_patterns:
  - status-indicator
  - metric-display
  - entity-details-surface
  - item-actions
  - selectable-list-item
  - list-virtualization

last_reviewed: 2026-08-07
---

# Анатомия карточки сущности

## Назначение

Decision-oriented представление одной сущности внутри списка. Карточка помогает быстро идентифицировать объект, увидеть главный сигнал, оценить 1–3 решающих показателя, понять причину внимания и перейти к следующему действию. Паттерн задаёт смысловую anatomy, но не доменную схему полей, status-control API, поверхность полного объекта или list virtualization.

## Пользовательская задача

Просмотреть несколько объектов, понять, какие из них требуют внимания и почему, сравнить важные показатели и открыть выбранную сущность без чтения полного набора данных.

## Pattern responsibility

### Owns

- hierarchy identity → signal → decision metrics → attention reason;
- минимальная достаточность информации для выбора объекта;
- единый основной open intent карточки;
- правила отсутствия optional content и адаптивного сохранения смысла;
- card-level interactive semantics.

### Delegates

- visual/semantic contract конкретного статуса или уровня;
- форматирование денег, дат, длительностей и других метрик;
- тип surface полного объекта и navigation continuity;
- inline/item actions и их confirmation;
- selection, bulk actions и drag behavior;
- list virtualization, ordering и page-level states.

## Use when

- список помогает принимать решение, а не только просматривать реестр;
- сущности имеют различимые состояние, приоритет или причину внимания;
- пользователю достаточно компактного preview перед полным просмотром;
- несколько типов данных нужно связать в одну понятную единицу списка.

## Do not use when

- основной сценарий требует точного сравнения многих однородных колонок;
- элемент является простым navigation link без сигнала и decision context;
- нужен полный просмотр или редактирование объекта;
- информация не позволяет сформировать осмысленный signal/priority и карточка становится декоративной оболочкой строки.

## Anatomy

1. Identity region — название и ключевой идентификатор.
2. Signal region — главное состояние, уровень, изменение или проблема.
3. Decision metrics region — 1–3 показателя, влияющих на выбор.
4. Attention reason region — объяснение, почему объект важен сейчас.
5. Optional supporting context — краткие вторичные сведения.
6. Open intent — переход к полному представлению сущности.

## Slots

| Slot | Назначение | Обязательность | Допустимое содержимое | Constraints | При отсутствии | Delegated pattern |
|---|---|---|---|---|---|---|
| `entity-name` | Быстро идентифицировать объект | required | короткое название или главный описательный label | визуально первичен; не заменяется статусом | паттерн неприменим | — |
| `entity-id` | Отличить похожие объекты и дать стабильную ссылку | required | business/user-facing identifier | не локализованный label и не внутренний случайный key | паттерн неприменим | — |
| `primary-signal` | Показать главное состояние/приоритет | required | status, level, risk, change или problem state | один главный сигнал; доступен не только через цвет | паттерн теряет decision role | `status-indicator` |
| `secondary-signals` | Добавить редкие уточняющие признаки | optional | new/overdue/source-type markers | не конкурируют с primary signal и не превращаются в tag cloud | регион не занимает место | `status-indicator` |
| `decision-metrics` | Поддержать сравнение и выбор | required | 1–3 подписанных значения | только показатели, влияющие на решение; форматирование делегировано | нужен обоснованный content fallback либо паттерн неприменим | `metric-display` |
| `attention-reason` | Объяснить, почему объект стоит открыть | required | короткая причина, изменение или проблема | конкретна для текущего состояния; не повторяет status без объяснения | implementation не соответствует approved card anatomy | — |
| `supporting-context` | Дать минимум полезных вторичных данных | optional | owner, source, relevant date, короткое описание | удаляется раньше обязательных slots; не полный meta registry | layout уплотняется | domain view/formatter |
| `open-intent` | Открыть полное представление объекта | recommended | один card-level interaction intent | surface type не задаётся; вложенные controls не создают nested interactive elements | карточка должна явно объяснить иной следующий шаг | `entity-details-surface` |
| `item-actions` | Выполнить применимые действия элемента | optional | редкие secondary item intents | отделены от open intent; permissions/state учитываются | карточка целиком служит preview/open | `item-actions` |

## Information hierarchy

Пользователь сначала распознаёт объект, затем видит главный signal, далее сравнивает 1–3 metrics и понимает attention reason. Supporting context вторичен. Порядок может адаптироваться визуально, но чтение и accessibility tree сохраняют эту смысловую последовательность.

## Behavior

- Карточка получает уже подготовленную decision-oriented view model; бизнес-расчёты не выполняются внутри presentation composition.
- Primary signal и attention reason описывают текущее значимое состояние, а не общий постоянный профиль сущности.
- Вся карточка может быть одним open control, если внутри нет независимых interactive controls.
- При наличии item actions open intent и actions имеют раздельные доступные hit targets без вложенных кнопок/ссылок.
- Open intent передаёт stable identity и origin context вызывающей композиции; surface определяется `entity-details-surface` и UX solution.
- Отсутствующие optional slots удаляются без пустых separators и сохранения фиктивной высоты.
- Card height может быть измерена виртуализатором, но фиксированная высота не является semantic requirement.

## Actions

- Основное действие — открыть/продолжить работу с сущностью, если это предусмотрено родительским списком.
- Item actions optional и не должны вытеснять identity, signal или attention reason.
- Placement, overflow, destructive confirmation, pending и success behavior item actions делегированы.
- Карточка без доступного действия остаётся семантическим list item, а не disabled button.

## Required states

- `default`: обязательные slots относятся к одной сущности и имеют согласованную актуальность.
- `disabled`: применимо только когда open/action intent существует, но недоступен; причина должна быть понятна. Read-only карточка без action не считается disabled.
- `pending action`: применимо только при delegated inline action; карточка сохраняет identity/context, повтор действия блокируется локально.

Loading skeleton, empty list, refreshing results, list error и nested surface open принадлежат родительскому list/results pattern. Ошибка отдельного metric formatter должна иметь согласованный fallback, но не превращает карточку в page-level error state.

## Variants

- `signal-led`: главный signal расположен раньше metrics; подходит при срочной приоритизации.
- `metric-led`: 1–3 показателя визуально усилены после identity; signal остаётся доступным.
- `compact`: сохраняет identity, primary signal, минимальные metrics и attention reason; supporting context удаляется.
- `with-item-actions`: добавляет delegated actions при сохранении единственного open intent.

Variants описывают composition emphasis, а не отдельные продуктовые карточки Risks, Measures или Agent Risks.

## Delegated patterns

- `status-indicator` — семантика, цвет, iconography и label состояния.
- `metric-display` — формат, unit, missing/error value и comparison treatment.
- `entity-details-surface` — modal/page/другая approved поверхность полного объекта.
- `item-actions` — ordering, overflow, permissions, confirmation и async feedback.
- `selectable-list-item` — checkbox, multi-select и bulk interaction.
- `list-virtualization` — measurement, overscan, focus persistence и scroll restoration.

Пока child pattern отсутствует или не approved, использовать UX Solution, общие rules и релевантный production reference, не превращая локальный field renderer или geometry в стандарт.

## Responsive behavior

- На узкой ширине обязательные slots сохраняются; supporting context сокращается первым.
- Metrics переходят в последовательный layout и остаются подписанными.
- Signal и identifier не обрезаются так, чтобы терять различимость; длинное name допускает контролируемый wrap/truncation с доступом к полному значению по UX solution.
- Attention reason остаётся доступной, а не скрывается как desktop-only detail.
- Конкретные breakpoints, padding, columns и fixed heights не принадлежат паттерну.

## Accessibility

- Карточки находятся в semantic list; интерактивная карточка использует нативную button/link semantics согласно действию.
- Open intent доступен с клавиатуры и имеет видимый focus; hover не является единственным состоянием взаимодействия.
- Не использовать `outline: none` без равноценного focus indicator.
- Signal имеет текстовое значение; цвет, badge или position только поддерживают его.
- Название или доступное имя open control однозначно называет сущность.
- Nested interactive elements запрещены; item actions структурируются отдельно.
- DOM/read order соответствует identity → signal → metrics → reason, даже при CSS grid rearrangement.

## UI Kit dependencies

Проверены по текущему `component-index.yaml`; конкретные props не нормируются.

```yaml
- component: Row
  purpose: semantic regions and responsive metric layout
  api_status: verified
- component: Col
  purpose: optional responsive grouping
  api_status: verified
- component: Text
  purpose: entity identity, metric labels/values and attention reason
  api_status: verified
- component: Badge
  purpose: optional supporting signal marker
  api_status: verified
- component: Icon
  purpose: supporting iconography for a signal or metric
  api_status: verified
- component: Button
  purpose: explicit open or delegated item-action intent when appropriate
  api_status: verified
```

Product `FieldView`, format helpers and raw `<button>` implementations are not verified reusable composition dependencies and are not part of this contract.

## Design tokens

- Использовать реальные UI Kit/theme tokens для surface, border, text, status emphasis, spacing, radius, shadow и focus.
- Не переносить 16/24 px padding, fixed metric widths, raw hex/rgba hover colors или exact shadows.
- Status colors принадлежат semantic token contract delegated `status-indicator`.

## Constraints

- Обязательные смысловые slots не означают фиксированное число DOM-блоков или колонок.
- Карточка не содержит полный meta registry и не дублирует entity details.
- Не более 1–3 decision metrics без отдельного UX обоснования.
- Domain field names, `FieldView`, form schemas, route paths и tracking не входят в pattern.
- Selection и bulk actions не добавляются автоматически.
- Card composition не определяет ordering/priority всего списка.

## Content and UX writing

- Name и ID различимы и не повторяют друг друга без пользы.
- Metric всегда имеет label/unit или однозначный context.
- Attention reason формулируется конкретно: что изменилось, что пошло не так или почему объект важен сейчас.
- Не использовать общие фразы «требует внимания» без причины.
- Missing value имеет согласованный neutral fallback и не маскируется числом ноль.
- Labels локализуются; IDs и runtime values остаются данными.

## Anti-patterns

- Карточка является декоративной строкой реестра без signal и attention reason.
- Все доступные поля помещены в карточку «для полноты».
- Несколько равнозначных badges конкурируют за роль primary signal.
- Метрики не подписаны или не влияют на решение.
- Status/priority закодированы только цветом.
- Вся карточка — button, внутри которого размещены другие buttons/links.
- Desktop-only attention reason исчезает на mobile.
- Fixed height обрезает dynamic/localized content.
- Конкретный route/modal, `FieldView` API или product schema объявлены частью entity-card.

## Implementation guidance

- Создать domain adapter/view model отдельно от presentational card composition.
- View model предоставляет stable identity, name, primary signal, 1–3 metrics, attention reason и optional supporting context.
- Проверять согласованность временной актуальности signal, metrics и reason.
- Использовать semantic button/link только при реальном action; не эмулировать control через click handler на `div`.
- Виртуализатор измеряет реальную высоту и использует stable entity key; это интеграция, не card contract.
- Тестировать long names, missing optional data, localized labels, keyboard focus и coexistence open/item actions.
- Проверять UI Kit exports/types перед JSX; raw styles references не копировать.

## Evidence

| Repository | Revision | File | Что подтверждает | Ограничения |
|---|---|---|---|---|
| sberorm-enablers/sberorm-cloud-risks-front | 029af7b6402 | `src/pages/Risks/components/RiskCard/RiskCard.tsx`; `types.ts`; `styles.module.scss`; `src/pages/Risks/components/RisksList/RisksList.tsx` | Identity, level/status/new signals, decision metrics, supporting owner/source, whole-card open, responsive reduction | Attention reason не выделена явно; raw button теряет focus outline; hardcoded widths/gaps и rgba hover; `FieldView` локален |
| sberorm-enablers/sberorm-cloud-measures-front | 04d04bbdd29 | `src/pages/Measures/components/MeasureCard/MeasureCard.tsx`; `types.ts`; `utils.ts`; `styles.module.scss`; `src/pages/Measures/components/MeasureList/MeasureList.tsx` | Status, name/ID, date signals, 1–3 planning/actual metrics, description context, whole-card navigation, responsive columns | Attention reason смешана с overdue/description; raw button; literal label; fixed grid/min width/height и hex hover; domain-heavy |
| sberorm-enablers/sberorm-cloud-agent-risks-front | 741fa169e66 | `src/pages/AgentRisks/components/AgentRisksCard/AgentRisksCard.tsx`; `types.ts`; `styles.module.scss`; `src/pages/AgentRisks/components/AgentRisksList/AgentRisksList.tsx` | Третий repeat identity + signal + supporting metadata + open intent; компактный вариант | Нет явных 1–3 decision metrics и attention reason; raw button без visible focus; date/version/stage доменны |

## Reference implementation

Основной reference — Risks `src/pages/Risks/components/RiskCard/RiskCard.tsx`: наиболее близок к approved anatomy за счёт identity, нескольких signals и decision metrics. Дополнительные references: Measures — metric-led/content-rich вариант; Agent Risks — compact third-repository confirmation.

Reference implementation является доказательством и примером реализации. Его код, props, геометрия и локальные domain-specific решения не копируются автоматически и не становятся нормативными, если это отдельно не указано в паттерне.

## Conflicts and decisions

### Attention reason

**Found:** approved UX rules требуют явную причину внимания; Risks/Measures выражают её частично через status/deadline/description, Agent Risks не показывает явно.

**Decision:** сохранить `attention-reason` обязательным semantic slot и не придумывать product copy.

**Classification:** normative with implementation gap.

**Reason:** approved rule выше неполного repository coverage; без причины карточка не отвечает «почему открыть».

**Evidence:** `ux_patterns.md`, `ux_principles.md`, три card files.

### Decision metrics

**Found:** Risks и Measures показывают несколько показателей; Agent Risks — в основном version/stage/date metadata.

**Decision:** 1–3 decision metrics нормативны для decision-oriented entity card; если их нет, UX solution должен определить другой meaningful decision context или признать, что pattern не подходит.

**Classification:** normative with partial evidence.

**Reason:** approved card anatomy явно задаёт 1–3 показатели.

**Evidence:** rules; RiskCard, MeasureCard, AgentRisksCard.

### Whole-card interaction

**Found:** все три implementations используют raw `<button>` на всю карточку и открывают route modal; independent item actions отсутствуют.

**Decision:** нормировать единый open intent, но не raw button, route или modal. При item actions разделять targets.

**Classification:** reference-backed interaction; implementation-specific control/surface.

**Reason:** open intent повторяется, а surface делегирована и nested controls требуют иной semantics.

**Evidence:** три cards и list usages.

### Responsive content removal

**Found:** Risks/Measures скрывают часть supporting data на phone; обязательность отдельных данных различается.

**Decision:** optional supporting context можно сокращать, но identity, primary signal, decision context и attention reason сохраняются.

**Classification:** normative priority; responsive presentation open.

**Reason:** semantic hierarchy стабильна, конкретный mobile layout может меняться независимо.

**Evidence:** card TSX/styles трёх repositories.

### Visual/card primitive

**Found:** локальные raw buttons и SCSS повторяются, но используют разные grids, shadows, colors и focus treatment; reusable entity-card export не найден.

**Decision:** оставить implementation guidance; использовать verified primitives и token system, не объявлять local shell component.

**Classification:** implementation-specific / open reusable ownership.

**Reason:** повторение локального кода не равно reusable component; часть styles конфликтует с frontend rules/accessibility.

**Evidence:** три card styles; `component-index.yaml`; frontend rules.

## Open questions

- Product-specific требования не предоставлены: блок содержит placeholder.
- Как product teams должны формировать и локализовать `attention-reason`?
- Что считать достаточным decision context, если числовых metrics нет?
- Нужен ли approved reusable entity-card composition component?
- Какой общий contract у `status-indicator` и missing metric values?
- Нужны ли selection/bulk-action variants и отдельный `selectable-list-item` pattern?
- Как согласовать variable card height с accessibility и virtualization?

## Acceptance checklist

- [ ] Name и stable user-facing ID однозначно идентифицируют сущность.
- [ ] Один primary signal понятен без цвета.
- [ ] Показаны 1–3 подписанных decision metrics или согласованный meaningful decision context.
- [ ] Attention reason конкретно объясняет, почему объект важен сейчас.
- [ ] Supporting context не вытесняет обязательные slots.
- [ ] Open intent имеет нативную keyboard/focus semantics и не предписывает surface.
- [ ] Item actions не создают nested interactive controls.
- [ ] Mobile сохраняет identity, signal, decision context и reason.
- [ ] Missing/long/localized content не ломает layout.
- [ ] UI Kit exports проверены; product `FieldView`, geometry и routes не нормированы.

