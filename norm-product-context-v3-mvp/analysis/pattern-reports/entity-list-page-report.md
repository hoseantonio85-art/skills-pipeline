# Отчёт нормализации: entity-list-page

## Объём и метод

Исследованы три production-кандидата из discovery registry. Для каждого просмотрены page component, colocated styles, list, card/empty/filter subcomponents, router usage, непосредственно влияющая async/navigation logic, package manifests и реальные imports UI Kit. Продуктовые архивы читались выборочно и не изменялись. Полный frontend review не выполнялся.

Пользовательский блок требований содержит placeholder, а не требования. Поэтому пользовательских product-specific решений нет; это явно оставлено open question, а синтез опирается на утверждённые правила и evidence.

## Исследованные реализации

### Risks, revision 029af7b6402

Взято: title + total, optional attention/summary перед карточками, quick filters + search + advanced filter drawer, виртуализация, различение исходного и filtered empty, route-backed list → modal, нижний dock, permission branch.

Отвергнуто как нормативное: magic button и chat MFE; фиксированная высота карточки 233; fade attention zone по scroll; доменная assessment-task ветка; raw button card; hardcoded dock geometry и rgba shadows; единый overlay loader для нескольких async фаз.

### Measures, revision 04d04bbdd29

Взято: наиболее чистый минимальный shell; quick/search/advanced filtering; draft/reset/apply behavior drawer; виртуализированный card list; empty/loading; route modal и optional page actions.

Отвергнуто: отсутствие summary как запрет summary; fixed 600 px dock; локальные rgba; конкретная card height 152; shared `Drawer` как автоматически допустимая UI Kit dependency.

### Agent Risks, revision 741fa169e66

Взято: третий независимый повтор shell, search-led variant, permission/config gating, virtual list, empty/loading и route-backed open.

Отвергнуто: отсутствие count и advanced filter как общая норма; hardcoded route; внешний analytics link как часть header anatomy; скрытие create action на mobile; фиксированная card height 233.

## Решения из требований пользователя

Product-specific требований не предоставлено. Из самого задания применены обязательные meta-решения: normalized composition вместо копии компонента; status `draft`; evidence 2–5 implementations; verified UI Kit exports only; явные conflicts/open questions; отсутствие изменений продуктовых repositories.

## Выводы из правил и repositories

- Устойчивый каркас: header → optional summary → filter toolbar → card list/states → optional bottom actions → nested route surface.
- Cards являются decision-oriented форматом; отдельный entity-card pattern должен определять внутреннюю anatomy.
- Summary — смысловой optional slot: обязателен при наличии полезной агрегированной картины, но не должен появляться формально.
- Quick filters, search и advanced drawer не являются одним обязательным toolbar preset.
- list → object modal и list → auxiliary drawer различаются по намерению.
- Виртуализация повторяется, но остаётся implementation option с accessibility contract.
- Initial loading, refreshing, empty и recoverable error нужно разделить нормативно; код полностью доказывает только loading и два empty.
- UI Kit exports `Row`, `Col`, `Title`, `Text`, `Button`, `Icon`, `FieldSearch`, `Loader`, `ScrollBar` подтверждены component index. Props из product code не объявлены нормативным API.

## Что требует подтверждения

- специальные пользовательские требования;
- допустимый shared/UI Kit Drawer и его версия/API;
- recoverable error/retry и stale-data contract;
- mobile placement quick filters и primary page action;
- focus return, live announcements и keyboard behavior виртуализатора;
- фактические UI Kit lock/resolution manifests трёх revisions.

## Готовность для этапа 03

`Ready with review gates`: паттерн пригоден как draft-каркас для выбора композиции на этапе 03, если команда не трактует optional slots как обязательные и не копирует props/геометрию references. Для production implementation сначала нужны design/frontend review и закрытие вопросов по Drawer, error/refresh и accessibility. Оценка готовности: **0.75**.

## Post-normalization correction

Первоначальная версия слишком жёстко включала решения самостоятельных дочерних композиций: фиксировала floating/bottom placement page actions и route-backed modal как универсальный способ открытия полного объекта. После корректировки `entity-list-page` нормирует только anatomy страницы, информационную иерархию, page-level states и взаимодействие slots.

В будущие или отдельные patterns делегированы:

- `entity-card` — внутренняя anatomy карточки;
- `filter-toolbar` — quick filters, search и advanced filtering;
- `entity-details-surface` — тип и контракт полного представления объекта;
- `page-actions` — placement и behavior действий страницы;
- `auxiliary-drawer` либо другой auxiliary-surface pattern — короткие вспомогательные сценарии.

Floating action placement и route-backed modal сохранены как сильные production references, но больше не являются универсальными требованиями. Исследование repositories и readiness **0.75** не изменены; вопросы по дочерним patterns, navigation contract, Drawer, errors и accessibility остаются открытыми.
