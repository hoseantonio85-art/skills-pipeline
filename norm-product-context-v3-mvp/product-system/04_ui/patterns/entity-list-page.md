---
id: entity-list-page
title: Страница списка сущностей
status: draft
maturity: reference-backed
category: page
version: 0.1.0
implementation:
  type: guidance
  reusable_component: false
normative_scope:
  - page anatomy
  - information hierarchy
  - page-level state model
  - interaction between page slots
delegated_patterns:
  - entity-card
  - filter-toolbar
  - entity-details-surface
  - page-actions
  - auxiliary-drawer
owners:
  design: needs-review
  frontend: needs-review
last_reviewed: 2026-08-07
---

# Страница списка сущностей

## Назначение

Страница для обзора множества однотипных сущностей, понимания приоритетов, сужения выборки и перехода к полному просмотру объекта. Паттерн задаёт композицию страницы, но не реализацию карточки, фильтра или object modal.

## Пользовательская задача

Понять общую картину и следующий приоритет, быстро найти нужный объект, открыть его без потери контекста списка и выполнить доступное действие уровня страницы.

## Use when

- пользователь регулярно работает с множеством однотипных объектов;
- объектам нужны сигналы, 1–3 решающих показателя и причина внимания;
- выборку нужно искать, фильтровать или приоритизировать;
- полный объект открывается как отдельный сфокусированный сценарий.

## Do not use when

- главный сценарий — сравнение большого числа однородных полей по строкам и столбцам;
- объектов мало и навигационного списка достаточно;
- экран является dashboard из независимых виджетов;
- пользователь проходит линейный процесс создания или редактирования;
- требуется только выбор значения внутри формы.

## Anatomy

1. Page header: идентифицирует раздел и состояние выборки.
2. Optional summary: показывает только верхнеуровневый сигнал и может сужать список.
3. Filter toolbar: быстрые фильтры, поиск и вход в расширенный фильтр.
4. List viewport: приоритизированная последовательность карточек.
5. State surface: loading, empty или recoverable error в контексте списка.
6. Optional page actions: действия уровня страницы или текущей выборки; их placement определяется отдельным паттерном или UX solution.
7. Entity details / auxiliary surface host: точка взаимодействия с полным представлением сущности или коротким вспомогательным сценарием без предписания конкретного surface type.

## Slots

| Slot | Назначение | Обязательность | Допустимое содержимое | Ограничения | При отсутствии |
|---|---|---|---|---|---|
| `title` | Назвать раздел | обязательно | короткий локализованный заголовок | одна смысловая строка | паттерн неприменим |
| `selection-status` | Показать объём/состояние выборки | рекомендуется | total, filtered total, краткий hint | не заменяет summary | header остаётся только с title |
| `summary` | Дать верхнеуровневую картину | опционально | KPI, распределение, зона внимания, краткий вывод | только данные, влияющие на решение; интерактивность должна фильтровать список предсказуемо | toolbar следует сразу за header |
| `quick-filters` | Дать частые сценарии сужения | рекомендуется при повторяемых сценариях | chips, toggles, segmented control | не полный набор параметров | остаются search/advanced filters либо нефильтруемый список |
| `search` | Найти объект по известному признаку | опционально | одно поисковое поле | debounce не должен скрывать текущий запрос; clear доступен | toolbar перераспределяет место |
| `advanced-filter-trigger` | Открыть точную настройку | опционально | кнопка с признаком активных фильтров | только если есть расширенный набор | быстрые фильтры не имитируют полный фильтр |
| `entity-list` | Показать приоритизированные сущности | обязательно | карточки одного типа, группы карточек | не плотная таблица; порядок объясним | state surface занимает область списка |
| `page-actions` | Действия уровня всей страницы или выборки | опционально | primary page action; применимые secondary actions | действие не дублируется в нескольких постоянных областях; placement выбирается по утверждённому `page-actions` pattern или UX solution; учитываются permissions и текущий state | пустой контейнер не рендерится |
| `entity-details-surface` | Открыть полное представление выбранной сущности, сохранив ожидаемый пользовательский контекст списка, если это требуется UX solution | опционально до взаимодействия | trigger/host утверждённой поверхности полного объекта | surface type не определяется этим паттерном; использовать `entity-details-surface` pattern и текущий UX solution | сущность не открывается с этой страницы либо используется иной утверждённый navigation flow |
| `auxiliary-surface` | Выполнить короткий вспомогательный сценарий | опционально | trigger/host вспомогательной композиции | тип поверхности определяется отдельными surface rules; не подменяет полное представление сущности | слот не занимает место |

## Information hierarchy

Сначала контекст и приоритет, затем инструменты сужения, затем карточки. В карточке сначала идентификация и сигнал, далее 1–3 решающих показателя и причина внимания. Служебная полнота не должна вытеснять смысл.

## Behavior

- Список имеет явный и устойчивый порядок; изменение фильтра, поиска или summary обновляет одну и ту же выборку.
- Поиск может применяться с задержкой, но введённое значение и состояние обновления остаются видимыми.
- Быстрый фильтр применяется непосредственно; расширенный фильтр редактируется отдельно и применяется явным действием.
- Закрытие расширенного фильтра без применения возвращает подтверждённые значения.
- Открытие сущности сохраняет или восстанавливает релевантный navigation context списка: фильтры, поиск, сортировку и позицию, если пользователь ожидает возврата к той же выборке.
- Способ открытия полного объекта определяется UX solution и утверждённым `entity-details-surface` pattern. Текущие production references подтверждают route-backed modal как распространённый вариант, но `entity-list-page` не нормирует его как единственно допустимый.
- Shareable/recoverable navigation state хранится в URL только там, где это соответствует архитектуре приложения и UX navigation contract.
- Для длинных списков допустима виртуализация, если сохраняются keyboard navigation, измерение динамической высоты и восстановление позиции.
- Summary интерактивен только когда действие однозначно сужает выборку; выбранное состояние отражается и в фильтрах.

## Actions

- Если у страницы есть постоянное основное действие уровня страницы, оно имеет одно устойчивое место и не дублируется одновременно в нескольких постоянных областях.
- Конкретный placement определяется отдельным `page-actions` pattern, UX solution или локальным product constraint.
- Открытие карточки — основное действие элемента списка.
- Reset и Apply расширенного фильтра имеют разные приоритеты; pending блокирует повторный submit.
- Недоступное по правам действие скрывается либо объяснимо disabled согласно модели разрешений; страница не оставляет пустой контейнер действий.

## Required states

- `default`: данные загружены, toolbar и карточки доступны.
- `loading`: первичная загрузка сохраняет header и ориентацию; область списка показывает Loader или эквивалентный placeholder.
- `refreshing`: текущие карточки и фильтры остаются видимыми, обновление обозначено ненавязчиво; не заменять всю страницу пустым состоянием.
- `empty`: различать исходно пустой список и нулевой результат фильтра/поиска; объяснить следующий шаг (создать, сбросить или изменить запрос).
- `recoverable error`: сохранить контекст и дать retry; не смешивать с отсутствием прав.
- `pending action`: отключить повторный запуск конкретного действия и показать прогресс рядом с ним.
- `disabled`: применимо к отдельным действиям/фильтрам с понятной причиной, не ко всей странице без объяснения.
- `entity/auxiliary surface open`: страница сохраняет необходимый контекст выборки; при закрытии overlay-поверхности фокус возвращается инициатору; при navigation-based переходе восстановление определяется navigation contract.

## Variants

- `minimal`: header, toolbar, список и states без отдельной summary-зоны.
- `summary-led`: перед toolbar или списком есть агрегированный сигнал; summary не обязателен для всех доменов.
- `search-led`: основной инструмент — поиск и небольшой набор быстрых фильтров; не запрещает advanced filtering при доказанной потребности.

Это composition variants, подтверждённые references, а не отдельные нормативные реализации продуктов Measures, Risks и Agent Risks.

## Delegated patterns

`entity-list-page` намеренно не определяет внутренний контракт следующих композиций:

- `entity-card` — anatomy одной сущности в списке;
- `filter-toolbar` — quick filters, search и advanced filtering;
- `entity-details-surface` — поверхность полного объекта;
- `page-actions` — placement и behavior действий уровня страницы;
- `auxiliary-drawer` или другой auxiliary-surface pattern — короткие вспомогательные сценарии.

Пока соответствующий паттерн отсутствует или не approved:

1. использовать требования текущего UX Solution;
2. использовать релевантный reference implementation;
3. следовать общим UX/UI rules;
4. не превращать локальную реализацию одного продукта в универсальную норму.

## Responsive behavior

- На узкой ширине header и toolbar переносятся без горизонтального скролла страницы.
- Быстрые фильтры могут сворачиваться в компактный control; ключевой текущий фильтр и способ очистки остаются доступны.
- Search занимает доступную ширину. Icon-only trigger обязан иметь accessible name.
- Карточка переходит в одну колонку и сохраняет порядок «идентификация → сигнал → показатели → причина».
- Если выбран overlay/floating placement page actions, он не перекрывает последнюю карточку, а list viewport получает необходимый safe area.
- Отсутствие desktop-действия на mobile не считается адаптацией: для разрешённого действия нужен мобильный путь.

## Accessibility

- Один `h1` на страницу; total объявляется рядом с понятной подписью.
- Список имеет list semantics, карточка — один понятный интерактивный entry point; вложенные действия не создают вложенных кнопок.
- Все icon-only controls имеют accessible name и видимый focus.
- Loading/refreshing объявляются без многократного шума; empty/error получают заголовок и следующий шаг.
- Изменение количества результатов сообщается через подходящий live region без перехвата фокуса.
- Overlay-поверхность управляет focus trap; при закрытии фокус возвращается карточке/trigger. Escape закрывает верхний surface согласно утверждённому surface contract.
- Виртуализация не должна делать элементы недоступными клавиатуре или ломать последовательность чтения.

## UI Kit dependencies

Проверены по `component-index.yaml`; props намеренно не нормируются без проверки конкретной установленной версии.

```yaml
- component: Row
  purpose: page, header and toolbar layout
  api_status: verified
- component: Col
  purpose: responsive card/layout regions when needed
  api_status: verified
- component: Title
  purpose: page and state headings
  api_status: verified
- component: Text
  purpose: counts, descriptions and status copy
  api_status: verified
- component: Button
  purpose: search/filter triggers, retry and page actions
  api_status: verified
- component: Icon
  purpose: supporting iconography; never the sole accessible label
  api_status: verified
- component: FieldSearch
  purpose: entity search
  api_status: verified
- component: Loader
  purpose: initial and incremental progress indication
  api_status: verified
- component: ScrollBar
  purpose: bounded long-list viewport when product shell requires it
  api_status: verified
```

`Drawer` из `@sber-orm/components` встречается в двух references, но не является подтверждённым export UI Kit в доступном component index; он не включён в нормативные зависимости до решения владельца shared layer.

## Design tokens

- Использовать только реальные theme/UI Kit tokens текущей версии для background, text, border, radius, shadow и spacing.
- Семантические размеры берутся из системной шкалы; численные значения из references (включая ширину dock и высоту карточек) не нормативны.
- Inline styles допустимы для вычисляемой геометрии виртуализатора, но не для цвета.

## Constraints

- Паттерн не является универсальным мегакомпонентом: page shell координирует, но не поглощает entity card, filter toolbar, entity details и auxiliary surfaces.
- Доменные поля, статусы, permissions и сортировка передаются данными/конфигурацией.
- Способ хранения восстанавливаемого navigation context определяется архитектурой и UX navigation contract.
- Виртуализация требуется только при измеренной необходимости.
- Нельзя зависеть от `@sber-orm/components` как скрытого facade без отдельного подтверждения.

## Content and UX writing

- Заголовок называет сущности во множественном числе.
- Count должен быть понятен: все результаты или отфильтрованные.
- Empty без фильтров объясняет, почему данных нет и как начать; filtered empty предлагает изменить или сбросить условия.
- Кнопки называют действие: «Применить», «Сбросить», «Повторить», «Создать …».
- Search placeholder указывает, по каким признакам ищут; labels и сообщения локализуются, runtime content остаётся данными.

## Anti-patterns

- Равнозначный реестр без приоритета и причины внимания.
- Таблица как автоматическая замена карточек для decision-oriented списка.
- Обязательный summary без полезного агрегированного сигнала.
- Все параметры как быстрые фильтры или постоянная боковая панель фильтров.
- Выбор surface для полного объекта без учёта намерения, объёма информации, continuity и утверждённых surface patterns.
- Spinner поверх пустого экрана при каждом обновлении.
- Один текст для исходного и filtered empty.
- Дублирование одного page-level action в нескольких постоянных областях.
- Копирование локальных card heights, raw button cards, rgba shadows и magic/chat integration как стандарта.

## Implementation guidance

- Разделить container orchestration, toolbar, list viewport, state rendering и entity card.
- Хранить подтверждённые фильтры отдельно от draft расширенного фильтра; shareable/recoverable navigation state синхронизировать с URL там, где это предусмотрено архитектурой и UX navigation contract.
- Запросы должны различать initial loading, refreshing и recoverable failure, сохраняя последние успешные данные при refresh.
- Для виртуализации использовать стабильный entity key, overscan и реальное измерение переменной высоты; предусмотреть non-virtual fallback для тестов/accessibility.
- Если выбран overlay/floating placement page actions, предусмотреть safe area, чтобы действия не перекрывали контент; не переносить фиксированную ширину 600 px из references.
- Проверять фактические exports/types установленного UI Kit перед написанием JSX; не переносить props из references по памяти.

## Evidence

| Repository | Revision | File | Что подтверждает | Ограничения |
|---|---|---|---|---|
| sberorm-enablers/sberorm-cloud-risks-front | 029af7b6402 | `src/pages/Risks/Risks.tsx`; `components/RisksList/RisksList.tsx`; `components/Filters/Filters.tsx`; `components/Empty/Empty.tsx`; `styles.module.scss`; router config | Полный shell, title/count, summary/attention, quick+advanced filters, virtual list, два empty, loading, route modal, dock | Summary и magic/chat feature-specific; raw card/button и hardcoded geometry не нормативны; refresh смешан с loading |
| sberorm-enablers/sberorm-cloud-measures-front | 04d04bbdd29 | `src/pages/Measures/Measures.tsx`; `components/MeasureList/MeasureList.tsx`; `components/Filters/Filters.tsx`; `components/Empty/Empty.tsx`; `styles.module.scss`; router config | Минимальный повторяемый shell, quick/search/drawer filters, virtual cards, empty/loading, modal navigation и actions | Нет summary; Drawer идёт через shared facade; локальные rgba и fixed dock width против frontend rules |
| sberorm-enablers/sberorm-cloud-agent-risks-front | 741fa169e66 | `src/pages/AgentRisks/AgentRisks.tsx`; `components/AgentRisksList/AgentRisksList.tsx`; `components/Filters/Filters.tsx`; `components/Empty/Empty.tsx`; `styles.module.scss`; router config | Третий независимый повтор shell, search-led variant, virtual cards, empty/loading, route modal и permissions | Нет count/advanced filter/summary; create скрыт на mobile; route partly hardcoded; не основной reference |

## Reference implementation

Основной reference — Measures `src/pages/Measures/Measures.tsx` вместе с `MeasureList`, `Filters` и `Empty`: это наиболее чистый минимальный каркас без доменного summary. Дополнительные references: Risks — для title/count, summary-led варианта и различения empty; Agent Risks — только для search-led варианта и подтверждения повторяемости.

Reference implementation подтверждает возможную реализацию паттерна, а не является кодом для прямого копирования и не превращает все локальные решения reference в нормативные правила.

## Conflicts and decisions

| Найденные варианты | Выбрано | Почему и основание |
|---|---|---|
| Summary обязателен в UX structure; отсутствует в 2 из 3 реализаций | Optional slot, обязательный только при доказанном агрегированном сигнале | UX требует summary-first по смыслу, но запрещает бессодержательную полноту; repository evidence показывает минимальный устойчивый shell без summary |
| Risks/Measures имеют advanced filter drawer; Agent Risks — только search | Search, quick и advanced — независимые optional slots по сложности домена | UX rules разделяют быстрый сценарий и точную настройку; единичное упрощение не отменяет drawer там, где он нужен |
| Overlay Loader используется и при загрузке, и при обновлении | Различать loading и refreshing, при refresh сохранять данные | prototype UI rules требуют states; overlay в коде не даёт устойчивого stale-content contract |
| Primary create + chat в fixed/absolute dock; mobile create скрыт | Сохранить это как reference-backed вариант, не как правило shell | Конкретный placement и mobile behavior принадлежат `page-actions` pattern или UX solution |
| Карточка открывает route modal; advanced filter открывает Drawer | Зафиксировать разные намерения полного и вспомогательного сценария без предписания surface type | Выбор поверхности делегирован соответствующим patterns и UX solution |
| Drawer импортируется из `@sber-orm/components`, UI primitives — из UI Kit | Нормировать только подтверждённые UI Kit exports; Drawer оставить open question | frontend rules запрещают скрытый facade; доступный component index не подтверждает этот export |
| Локальные tokens соседствуют с rgba shadows | Только theme/UI Kit tokens | Явное frontend-правило выше repository implementation |
| В references повторяется floating/bottom placement page actions | `entity-list-page` нормирует наличие и назначение `page-actions` slot, но не конкретную геометрию или placement | Placement — самостоятельная композиционная задача; её определяет отдельный pattern или UX Solution |
| Три исследованные реализации используют route-backed modal для полного объекта | Считать route-backed modal strong reference, но не universal requirement `entity-list-page` | Surface type зависит от пользовательского намерения и отдельного surface pattern |

## Open questions

- Пользовательский блок требований в задании пуст: design owner должен подтвердить, что специальных product constraints нет.
- Какой подтверждённый UI Kit/shared export использовать для advanced filter Drawer?
- Нужны утверждённые mobile rules для quick filters и placement page actions.
- Нужен контракт recoverable error/retry и сохранения stale data; текущие три реализации его не доказывают.
- Подтвердить focus return, live announcements и keyboard contract виртуализированного списка.
- Уточнить установленную версию UI Kit для трёх revisions: package manifests не дают надёжного прямого pin, поэтому API за пределами component index не фиксируется.
- Нужен ли отдельный approved `page-actions` pattern?
- Нужен ли общий `entity-details-surface` pattern или отдельные `entity-modal` / `entity-page`?
- Когда route state обязательно хранить в URL, а когда достаточно local navigation state?

## Acceptance checklist

- [ ] Title и состояние выборки понятны без чтения карточек.
- [ ] Список приоритизирован; карточки объясняют сигнал и причину внимания.
- [ ] Quick/search/advanced controls добавлены только при пользовательской потребности.
- [ ] Initial empty отличается от filtered empty.
- [ ] Loading, refreshing и recoverable error имеют отдельное поведение.
- [ ] Открытие объекта сохраняет или восстанавливает релевантные фильтры, поиск, сортировку и позицию согласно navigation contract.
- [ ] Page action не дублируется и не перекрывает список на desktop/mobile.
- [ ] Keyboard, screen reader и focus сценарии проверены, включая виртуализацию.
- [ ] Использованы только проверенные UI Kit exports и реальные tokens.
- [ ] Доменные summary, поля, permissions, chat и аналитика не зашиты в shell.
