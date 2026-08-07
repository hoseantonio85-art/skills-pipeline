---
id: filter-bar-and-advanced-filter-drawer
title: Панель фильтров с расширенным фильтром
status: draft
maturity: reference-backed
category: filtering
version: 0.1.0

implementation:
  type: guidance
  reusable_component: false

owners:
  design: needs-review
  frontend: needs-review

normative_scope:
  - hierarchy between quick filters, search and advanced filtering
  - applied and draft filter state interaction
  - filter actions and active-state communication
  - integration contract with a results surface

delegated_patterns:
  - quick-filter-control
  - search-field
  - filter-field
  - drawer-surface
  - results-surface
  - query-state-persistence

last_reviewed: 2026-08-07
---

# Панель фильтров с расширенным фильтром

## Назначение

Двухуровневая композиция фильтрации: частые сценарии доступны непосредственно в панели, а полный набор параметров раскрывается в отдельной drawer-поверхности. Паттерн координирует уровни фильтрации и их состояние, но не определяет внутренний API полей, Drawer или списка результатов.

## Пользовательская задача

Быстро сузить выборку по частым признакам, найти известный объект через поиск и при необходимости точно настроить полный набор условий без потери контекста результатов.

## Pattern responsibility

### Owns

- иерархия quick filters, search и advanced-filter trigger;
- связь applied state панели с draft state расширенного фильтра;
- семантика открытия, применения, отмены и сброса;
- индикация активной фильтрации;
- контракт обновления родительской results surface.

### Delegates

- внешний вид и доступность конкретных quick-filter controls;
- поиск как field/control и его query semantics;
- типы, validation и зависимости отдельных filter fields;
- focus trap, размеры, overlay и close mechanics Drawer;
- loading/empty/error и сортировка результатов;
- URL/local persistence query state.

## Use when

- есть несколько частых фильтров и более широкий набор редко используемых параметров;
- пользователь должен быстро менять выборку, не открывая полную форму;
- расширенные условия удобно редактировать как единый draft и применять осознанно;
- постоянная боковая панель не задана UX solution.

## Do not use when

- достаточно одного поиска или 1–2 простых controls без второго уровня;
- фильтрация является частью сложного построителя запросов;
- параметры меняют не выборку, а сам объект или workflow;
- UX solution явно требует иной approved surface или постоянную filter panel.

## Anatomy

1. Filter bar — постоянная зона управления выборкой.
2. Quick-filter region — наиболее важные частые сценарии.
3. Search intent — поиск по поддерживаемым признакам, если применим.
4. Advanced-filter trigger — вход в полный набор условий и индикатор applied state.
5. Advanced-filter surface — delegated Drawer с draft-настройкой.
6. Filter action region — apply/reset/cancel intents расширенного фильтра.
7. Results-update interface — передаёт подтверждённые критерии родительской композиции.

## Slots

| Slot | Назначение | Обязательность | Допустимое содержимое | Constraints | При отсутствии | Delegated pattern |
|---|---|---|---|---|---|---|
| `quick-filters` | Частые сценарии сужения | recommended | ключевые статусы, категории или сегменты | небольшой приоритетный набор; состояние согласовано с applied criteria | bar начинается с search/advanced trigger | `quick-filter-control` |
| `search` | Найти по известному признаку | optional | один поисковый intent | запрос и способ применения понятны; не дублирует advanced field без причины | остальные controls перераспределяют место | `search-field` |
| `advanced-filter-trigger` | Открыть точную настройку | required для этого варианта | label и признак активных applied filters | индикатор отражает applied, а не неподтверждённый draft | использовать более простой filter-bar pattern | control из UI Kit; surface делегирован |
| `advanced-filter-fields` | Полный релевантный набор параметров | required | сгруппированные domain-configured fields | только фильтры текущей выборки; зависимости и validation принадлежат field layer | advanced filter не открывается | `filter-field` |
| `filter-actions` | Управлять draft | required | apply, reset и close/cancel intents | apply не допускает повторной отправки; close/cancel не должен молча применять draft | паттерн неприменим | `drawer-surface` для placement |
| `results-interface` | Сообщить applied criteria родителю | required | stable filter values/IDs и change intent | labels не используются как IDs; transport/query format не задаётся паттерном | фильтрация не имеет эффекта | `results-surface`, `query-state-persistence` |

## Information hierarchy

Quick filters показывают самые важные пользовательские сценарии. Search служит известному запросу. Advanced trigger остаётся заметным, но вторичным входом к точной настройке. В расширенной поверхности поля группируются по смыслу; actions отделены от содержимого и остаются понятны при прокрутке.

## Behavior

- Quick filters применяют понятное изменение к текущей выборке непосредственно. Это normative по UX rules.
- Search может применяться с debounce; введённое значение остаётся видимым, а задержка не считается состоянием ошибки. Конкретная задержка implementation-specific.
- Advanced filter открывается с draft, совпадающим с последними applied criteria.
- Изменения advanced fields не меняют applied criteria до подтверждения, кроме явно спроектированных dependent-field data refresh, который не является применением фильтра к результатам.
- Apply валидирует применимые поля, фиксирует draft как applied state, запрашивает обновление результатов и закрывает surface после принятия действия.
- Close/cancel без Apply отбрасывает draft и восстанавливает applied state.
- Reset очищает доступные draft criteria. Момент применения reset к результатам должен быть единообразным в продукте; предпочтительно подтверждать его Apply, пока отдельный UX contract не решит иначе.
- Trigger и быстрые controls отражают applied state. Неподтверждённый draft не выдаётся за применённую фильтрацию.
- Если applied criteria изменены извне (например, summary или восстановлением navigation state), bar и следующий draft синхронизируются с ними.

## Actions

- `open advanced filters` — открыть delegated drawer-surface с текущим applied state.
- `apply` — подтвердить draft и обновить results surface.
- `reset all` — очистить доступные criteria с ясным commit behavior.
- `reset group` — optional intent для очистки одной смысловой группы.
- `close/cancel` — выйти без скрытого применения draft.
- Placement, размеры и visual priority actions внутри surface определяет `drawer-surface` pattern и UX solution.

## Required states

- `default`: applied criteria согласованы между bar, trigger и results interface.
- `loading`: загружается конфигурация/справочники фильтров; структура композиции сохраняется, недоступные controls не выглядят применимыми.
- `refreshing`: dependent options или результаты обновляются без потери введённого/applied состояния.
- `recoverable error`: ошибка конфигурации, options или Apply объяснена; draft сохраняется и доступен retry.
- `validation error`: относится к draft fields; Apply не коммитит некорректный draft, фокус/summary ведёт к ошибке.
- `pending action`: Apply/Reset защищены от повторного запуска; остальные разрешённые операции не блокируются без необходимости.
- `disabled`: отдельный control объяснимо недоступен из-за permissions, dependency или текущего контекста.
- `nested surface open`: bar сохраняет applied state; Drawer показывает draft; focus/close behavior делегирован `drawer-surface`.

Empty results и error загрузки списка принадлежат родительской `results-surface`, а не этому паттерну.

## Variants

- `quick + search + advanced`: полная reference-backed композиция.
- `quick + advanced`: поиск не нужен текущей выборке.
- `search + advanced`: устойчивых частых сценариев нет.
- `quick/search only`: упрощённая optional композиция без advanced drawer; это граница с более простым filter-bar pattern, а не обязательная реализация текущего варианта.

## Delegated patterns

- `quick-filter-control` определяет выбор control, keyboard behavior и presentation items.
- `search-field` определяет field semantics, clear и submission details.
- `filter-field` определяет типы значений, validation, dependencies и option loading.
- `drawer-surface` определяет overlay, focus trap, Escape, close affordance, width и responsive presentation.
- `results-surface` определяет loading/refreshing/empty/error результатов.
- `query-state-persistence` определяет URL, local navigation state и восстановление criteria.

Пока дочерний pattern отсутствует или не approved, использовать текущий UX Solution, общие UX/UI rules и релевантный production reference; локальный API или geometry не становятся универсальной нормой.

## Responsive behavior

- Bar переносит или сворачивает controls без горизонтального scroll всей страницы.
- При нехватке места сохраняются доступ к active state, advanced trigger и способ очистить критерии.
- Не переносить desktop-решение «скрыть все quick filters» как норму: mobile priority определяется UX solution.
- Presentation Drawer на малой ширине и его geometry принадлежат `drawer-surface`; filter content сохраняет logical order и доступные actions.

## Accessibility

- Каждый trigger имеет accessible name; icon-only search control не полагается только на иконку.
- Active/selected state quick filters и наличие applied advanced criteria доступны не только через цвет/точку.
- Результат изменения фильтра сообщается без неожиданного перемещения фокуса.
- Ошибки draft fields связаны с controls; Apply ведёт к первой ошибке или summary.
- Focus trap, возврат фокуса, Escape и screen-reader title advanced surface делегированы `drawer-surface`, но интеграция обязана передать trigger и понятный title.

## UI Kit dependencies

Проверены по текущему `component-index.yaml`; props не нормируются по product code.

```yaml
- component: Row
  purpose: filter bar and action-region layout
  api_status: verified
- component: Col
  purpose: responsive grouping when required
  api_status: verified
- component: Button
  purpose: search, advanced-filter and filter-action intents
  api_status: verified
- component: Icon
  purpose: supporting filter/search iconography
  api_status: verified
- component: Text
  purpose: labels and supporting state copy
  api_status: verified
- component: Title
  purpose: filter-group headings when needed
  api_status: verified
- component: FieldSearch
  purpose: optional search slot
  api_status: verified
- component: RadioChips
  purpose: optional single-choice quick filters
  api_status: verified
- component: CheckboxChips
  purpose: optional multi-choice quick filters
  api_status: verified
```

`Drawer` в references импортируется из `@sber-orm/components`, а не из подтверждённых exports UI Kit. Surface обязателен по approved UX rule, но конкретная dependency остаётся open до утверждения shared ownership/API.

## Design tokens

- Использовать только реальные UI Kit/theme tokens для цвета, spacing, typography, borders и state indication.
- Active state не кодируется произвольной красной точкой или hardcoded geometry.
- Конкретные gaps, heights, radii и offsets references не нормативны.

## Constraints

- Паттерн не владеет схемой domain filters или payload API.
- Stable IDs отделены от локализованных labels.
- Постоянная боковая filter panel не является вариантом по умолчанию без UX requirement.
- Quick filters — приоритетный subset, а не дубликат всех advanced fields.
- Analytics, MobX/store calls и server-driven form renderer не входят в composition contract.

## Content and UX writing

- Trigger называет действие или состояние понятно: «Фильтры», при необходимости — количество applied criteria.
- Search placeholder объясняет поддерживаемые признаки поиска.
- Группы advanced fields имеют короткие смысловые заголовки.
- Actions используют однозначные глаголы: «Применить», «Сбросить», «Отмена»/закрытие согласно surface contract.
- Labels, errors и status copy локализуются; значения сущностей остаются runtime data.

## Anti-patterns

- Все доступные параметры показаны как quick filters.
- Applied и draft state смешаны: закрытие молча меняет результаты либо trigger показывает неподтверждённые значения.
- Advanced filter открывается без текущих applied criteria.
- Reset имеет непредсказуемый commit behavior.
- Active state обозначен только цветом или декоративной точкой.
- Постоянная side panel введена только потому, что она удобна локальной реализации.
- Drawer API, field renderer, store или payload конкретного продукта объявлены частью общего паттерна.

## Implementation guidance

- Разделить composition orchestration, state adapter, quick controls, search, field rendering и delegated surface.
- Моделировать `appliedCriteria` и `draftCriteria` отдельно; тестировать open → edit → cancel и open → edit → apply.
- Stable IDs использовать для state/payload, localized labels — только для UI.
- Загрузку dependent options не путать с применением фильтра к results surface.
- Debounce, tracking, server payload conversion и store technology оставить adapters/helpers.
- Query state синхронизировать с URL только когда это предусмотрено navigation contract.
- Перед JSX проверять exports/types установленного UI Kit; не переносить props из references по памяти.

## Evidence

| Repository | Revision | File | Что подтверждает | Ограничения |
|---|---|---|---|---|
| sberorm-enablers/sberorm-cloud-measures-front | 04d04bbdd29 | `src/pages/Measures/components/Filters/Filters.tsx`; `QuickFilters/QuickFilters.tsx`; `src/components/FilterFieldView/FilterFieldView.tsx`; `src/stores/models/Filters.ts`; colocated styles; `src/pages/Measures/Measures.tsx` | Два уровня фильтрации; quick chips, disclosed search, advanced Drawer, draft/applied copies, group reset, Apply и active indication | Store/tracking встроены; reset commit не полностью ясен; Drawer через shared facade; размеры и красная точка локальны |
| sberorm-enablers/sberorm-cloud-risks-front | 029af7b6402 | `src/pages/Risks/components/Filters/Filters.tsx`; `QuickFilters/QuickFilters.tsx`; `src/components/FilterFieldView/FilterFieldView.tsx`; `src/stores/models/Filters.ts`; colocated styles; `src/pages/Risks/Risks.tsx` | Повтор той же композиции и draft restore; pending Apply/Reset; dependent-option refresh; связь с page/list | Attention-zone animation доменна; reset применяется немедленно; Drawer/shared field renderer не подтверждены как UI Kit; active dot недоступна сама по себе |

## Reference implementation

Основной reference — Measures `src/pages/Measures/components/Filters/Filters.tsx` вместе с `QuickFilters`, `FilterFieldView` и `Filters` model: наиболее нейтральная реализация двухуровневой фильтрации. Дополнительный reference — Risks для pending actions, dependent refresh и подтверждения повторяемости.

Reference implementation является доказательством и примером реализации. Его код, props, geometry, store, tracking и domain-specific решения не копируются автоматически и не становятся нормативными, если это отдельно не указано в паттерне.

## Conflicts and decisions

### Commit расширенного фильтра

**Found:** обе реализации разделяют applied data и template/draft; Close восстанавливает applied, Apply запускает поиск.

**Decision:** draft/applied separation, explicit Apply и cancel-without-commit — обязательный контракт.

**Classification:** normative.

**Reason:** повторяемый production evidence согласован с понятной обратимостью действия.

**Evidence:** Measures и Risks `Filters.tsx`, `src/stores/models/Filters.ts`.

### Reset

**Found:** Risks немедленно очищает и обновляет результаты; Measures очищает template/quick status, но commit path читается неоднозначно.

**Decision:** нормировать ясный reset intent и единообразный commit behavior; предпочтительный вариант — очистить draft и применить через Apply. Немедленный reset остаётся допустимым только при явном UX contract.

**Classification:** open / reference-backed.

**Reason:** implementations расходятся, а approved rule не задаёт commit timing.

**Evidence:** оба `Filters.tsx`.

### Advanced surface dependency

**Found:** approved UX rule задаёт Drawer; оба references используют `Drawer` из `@sber-orm/components`, которого нет среди проверенных UI Kit exports.

**Decision:** Drawer как surface семантически normative для текущего pattern, но package/export и внутренний surface contract делегированы.

**Classification:** normative intent; open implementation dependency.

**Reason:** UX rule выше repository facade; frontend rules требуют проверять export и не создавать facade.

**Evidence:** `ux_patterns.md`, оба `Filters.tsx`, `component-index.yaml`.

### Mobile quick filters

**Found:** оба references скрывают quick filters на phone и оставляют triggers; Agent Risks также использует упрощённую search-led панель.

**Decision:** не нормировать полное скрытие; сохранять доступ к важным criteria, конкретное responsive presentation определить UX solution.

**Classification:** implementation-specific / open.

**Reason:** mobile behavior может изменяться независимо и не подтверждено approved rule.

**Evidence:** Risks, Measures и вспомогательно Agent Risks filter components.

## Open questions

- Product-specific требования не предоставлены: блок содержит placeholder.
- Какой approved package/export реализует `drawer-surface`?
- Должен ли Reset ждать Apply или немедленно менять выборку?
- Как представлять applied filter count и active state доступно и единообразно?
- Какие quick filters сохраняются на mobile и где доступны скрытые?
- Каков общий validation/error/retry contract server-driven filter fields?
- Когда criteria обязательно синхронизировать с URL, а когда достаточно local state?

## Acceptance checklist

- [ ] Quick filters отражают только частые сценарии, а не полную схему.
- [ ] Applied и draft criteria разделены и синхронизируются при открытии.
- [ ] Apply коммитит draft; Close/Cancel не применяет его скрыто.
- [ ] Reset behavior понятен и одинаков во всех входах.
- [ ] Trigger доступно сообщает наличие applied criteria.
- [ ] Search, quick и advanced changes согласованно обновляют results interface.
- [ ] Loading, refreshing, validation, pending и recoverable error проверены.
- [ ] Responsive вариант сохраняет доступ к критичным критериям.
- [ ] UI Kit exports проверены; Drawer dependency не выдумана.
- [ ] Store, payload, geometry и domain fields references не стали нормативными.

