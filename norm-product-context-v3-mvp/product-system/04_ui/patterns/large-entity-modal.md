---
id: large-entity-modal
title: Большая модалка сущности
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
  - entity-modal anatomy
  - hierarchy between identity, content, meta and actions
  - modal-level state and continuity contract
  - integration between modal regions

delegated_patterns:
  - entity-summary
  - entity-content-section
  - entity-meta
  - workflow-footer
  - related-entity-navigation
  - auxiliary-drawer
  - confirmation-modal
  - modal-surface

last_reviewed: 2026-08-07
---

# Большая модалка сущности

## Назначение

Сфокусированная крупная поверхность для полного просмотра одной сущности, понимания ситуации и принятия решения без потери исходного рабочего контекста. Паттерн задаёт modal-level композицию и интерфейсы регионов, но не внутренние контракты summary, domain content, meta, workflow footer, navigation или вложенных surfaces.

## Пользовательская задача

Идентифицировать объект, быстро понять его суть и значимость, изучить необходимые детали, выполнить доступное решение и вернуться в ожидаемый контекст.

## Pattern responsibility

### Owns

- anatomy Header → Body(Content + Meta) → Footer;
- иерархия identity, смыслового контента, служебных данных и действий;
- modal-level loading/error/close/continuity contract;
- размещение дочерних композиций по смысловым регионам;
- предотвращение дублирования действий между header и footer.

### Delegates

- summary и domain content blocks;
- состав и presentation meta fields;
- workflow action ordering, confirmation и async outcome;
- previous/next и related-entity navigation;
- focus trap, overlay, geometry и animation базовой modal surface;
- nested drawers и modal stack;
- chat/AI/report integrations.

## Use when

- полный объект нужно открыть поверх текущего рабочего контекста;
- пользователь должен понять ситуацию и принять решение, не переходя в длительную отдельную workspace-задачу;
- объект содержит достаточно content/meta для крупной структурированной поверхности;
- approved UX solution выбирает object modal как surface.

## Do not use when

- нужен короткий вспомогательный просмотр или одно лёгкое действие — использовать соответствующий auxiliary surface;
- сценарий требует длительной самостоятельной работы, сложной навигации или нескольких параллельных областей — рассмотреть entity page/workspace;
- требуется только подтверждение одного последствия — использовать confirmation/action modal;
- содержимое сводится к короткому сообщению или простой форме.

## Anatomy

1. Modal surface — delegated контейнер, overlay и modal semantics.
2. Header — идентификация сущности и modal controls.
3. Body — основная прокручиваемая область.
4. Content region — смысловой слой, начинающийся с понимания сути.
5. Meta region — компактный служебный слой.
6. Footer — действия текущего объекта/сценария.
7. Optional auxiliary-surface host — вход во вложенный короткий сценарий.

## Slots

| Slot | Назначение | Обязательность | Допустимое содержимое | Constraints | При отсутствии | Delegated pattern |
|---|---|---|---|---|---|---|
| `modal-surface` | Дать изолированную modal-поверхность | required | approved modal container | обеспечивает modal semantics; geometry и overlay не задаются здесь | паттерн неприменим | `modal-surface` |
| `identity-header` | Ответить «что это за объект?» | required | title, stable identifier, status, короткие признаки | без длинных описаний, аналитики и дублирующих actions | паттерн неприменим | header content может быть локальным либо будущим pattern |
| `content` | Ответить «что происходит и что с этим делать?» | required | summary intent, причины, последствия, показатели, evidence, связанные смысловые секции | начинается со смысла, не с необработанного набора полей | паттерн неприменим | `entity-summary`, `entity-content-section` |
| `meta` | Ответить «что это за объект формально?» | recommended | статус, тип, даты, источник, owner, IDs | компактно и вторично; без выводов, причин и рекомендаций | Body становится одноколоночным | `entity-meta` |
| `footer-actions` | Завершить решение в контексте сущности | required, если доступны действия | primary, secondary, destructive/reject intents | одно устойчивое место; не дублируются в header; permissions/state учитываются | footer не оставляет пустого контейнера | `workflow-footer`, `confirmation-modal` |
| `close` | Закрыть modal и восстановить ожидаемый контекст | required | close intent | dirty/pending guard делегирован; результат закрытия предсказуем | паттерн неприменим | `modal-surface`, `confirmation-modal` |
| `entity-navigation` | Перейти к соседней/связанной сущности без выхода из контекста | optional | previous/next/back/related intents | доступность и порядок согласованы с navigation contract | controls не занимают место | `related-entity-navigation` |
| `auxiliary-surface` | Открыть историю, источник или короткий вспомогательный шаг | optional | auxiliary intent/host | не заменяет полный просмотр основного объекта; stack behavior делегирован | слот отсутствует | `auxiliary-drawer` |

## Information hierarchy

Header быстро идентифицирует объект. Content имеет первый визуальный приоритет и начинает с summary/понимания ситуации. Meta отделена и вторична. Footer завершает сценарий действиями. Технические поля, история и вспомогательные детали не должны вытеснять summary и основной content.

## Behavior

- При открытии modal получает identity и релевантный origin context от вызывающей композиции.
- Первое содержательное представление объясняет суть до полного набора полей.
- Content и Meta могут прокручиваться в общей или согласованной области; footer остаётся доступен согласно `workflow-footer` contract.
- Close возвращает пользователя в ожидаемый origin context. Способ хранения контекста (URL, router state, local state) определяется navigation contract.
- Незавершённое редактирование или consequential pending action не теряется при закрытии молча; confirmation делегирована отдельному pattern.
- Previous/next и back являются optional reference-backed intents, а не обязательной частью каждой modal.
- Открытие auxiliary surface сохраняет modal context. Порядок Escape/back/focus для stack определяет surface-stack contract.
- Loading или refresh отдельной дочерней секции не должен блокировать всю modal без необходимости.

## Actions

- Object/workflow actions принадлежат footer-region по approved UX rule.
- Close/back/navigation controls могут находиться в header/control layer, но не конкурируют с workflow actions.
- Primary action не дублируется в header и footer.
- Конкретные labels, ordering, confirmation, permissions и async feedback делегированы `workflow-footer` и UX solution.
- Если действий нет, footer-region не рендерится пустым; modal остаётся полноценным read-only просмотром.

## Required states

- `default`: identity, смысловой content и доступные actions согласованы с одной сущностью.
- `loading`: modal shell и orientation сохраняются; первичная загрузка не показывает данные предыдущей сущности как текущие.
- `refreshing`: уже загруженный контекст сохраняется, обновляемая область обозначена локально.
- `empty`: применимо к отсутствующему/удалённому объекту или отсутствию содержательных данных; объясняет следующий шаг и не имитирует нормальный object view.
- `recoverable error`: сохраняет доступный identity/context, объясняет сбой и даёт retry/close.
- `pending action`: блокирует повтор только затронутого action и защищает от случайного close согласно action contract.
- `success feedback`: результат действия понятен; дальнейшее close/refresh/navigation определяется workflow outcome.
- `disabled`: отдельное action/section объяснимо недоступно; permissions не оставляют пустые controls.
- `nested surface open`: modal сохраняет identity и состояние; focus, Escape и возврат определяются верхней surface и stack contract.

Validation errors принадлежат дочернему form pattern, если modal используется для редактирования; large entity modal сам по себе не нормирует форму.

## Variants

- `read-only decision view`: основной вариант полного просмотра с optional actions.
- `content + meta`: desktop composition с отдельным служебным регионом; approved semantic structure.
- `single-column responsive`: те же регионы последовательно размещены на узкой ширине.
- `navigable set`: reference-backed вариант с previous/next или back, когда origin context задаёт упорядоченный набор.

Edit/create modal не является вариантом автоматически: его validation, dirty state и submit contract принадлежат отдельному modal-form pattern.

## Delegated patterns

- `entity-summary` — первый смысловой блок.
- `entity-content-section` — domain sections, anchors и progressive disclosure.
- `entity-meta` — состав и presentation служебных атрибутов.
- `workflow-footer` — actions, ordering, pending и outcome.
- `related-entity-navigation` — previous/next/back и linked objects.
- `auxiliary-drawer` — история, источники и короткие вспомогательные сценарии.
- `confirmation-modal` — защита consequential action или dirty close.
- `modal-surface` — overlay, focus trap, Escape, geometry, scroll lock и animation.

Пока дочерний pattern отсутствует или не approved, использовать UX Solution, общие UX/UI rules и релевантный production reference; локальный код не становится universal contract.

## Responsive behavior

- На узкой ширине Content и Meta переходят в последовательный logical order без потери смысловой иерархии.
- Header сохраняет identity и доступный close; вторичные признаки могут переноситься/сворачиваться.
- Footer actions остаются достижимыми и не перекрывают content; их responsive layout делегирован.
- Previous/next controls не должны просто исчезать, если navigation intent критичен; нужен утверждённый mobile path.
- Конкретные modal width, margins, radii и full-screen threshold определяет `modal-surface`, не этот pattern.

## Accessibility

- Modal имеет programmatic dialog semantics, accessible title и описываемый контекст.
- При открытии фокус входит в modal предсказуемо; background inert; при закрытии фокус возвращается инициатору либо в ожидаемую navigation target.
- Один основной heading идентифицирует сущность; landmark/heading order Content и Meta остаётся логичным.
- Close имеет accessible name; status не кодируется только цветом.
- Escape закрывает верхнюю доступную surface с учётом dirty/pending guard; stack order не неоднозначен.
- Previous/next controls являются настоящими keyboard-operable controls, а не clickable icons.
- Reduced motion соблюдается базовой modal surface.

## UI Kit dependencies

Проверены по текущему `component-index.yaml`; props из product references не нормируются.

```yaml
- component: Row
  purpose: modal header and regional layout
  api_status: verified
- component: Col
  purpose: content and meta layout when applicable
  api_status: verified
- component: Title
  purpose: entity and region headings
  api_status: verified
- component: Text
  purpose: identifiers, statuses and supporting copy
  api_status: verified
- component: Button
  purpose: close, back and action intents
  api_status: verified
- component: Icon
  purpose: supporting navigation iconography
  api_status: verified
- component: Loader
  purpose: modal or section loading indication
  api_status: verified
- component: ScrollBar
  purpose: bounded content scrolling where needed
  api_status: verified
```

`Portal`, `Drawer`, `WorkflowActions` и confirmation helpers в references приходят из `@sber-orm/components` либо локального кода. Они не включены как обязательные UI Kit dependencies. Хотя `Modal` является verified export UI Kit, пригодность его API для large entity composition не проверена и остаётся open.

## Design tokens

- Surface, overlay, text, border, spacing, radius, shadow и motion используют только реальные UI Kit/theme tokens.
- Не переносить `1320px`, `600px`, `24px`, `z-index: 999`, animation duration или локальные rgba/hex из references.
- Reduced-motion behavior определяется token/system contract базовой modal surface.

## Constraints

- Паттерн описывает composition guidance, не reusable React component.
- Domain fields, sections, status model, permissions и API остаются данными/adapters.
- Header/Content/Meta/Footer имеют смысловые границы; pattern не превращается в form renderer или dashboard.
- Nested surface depth, chat adjacency и report mode не входят в базовый contract.
- Route-backed implementation допустима, но не обязательна без navigation requirement.

## Content and UX writing

- Title однозначно называет сущность; identifier и status не подменяют title.
- Summary отвечает: что произошло, почему важно, насколько критично, какое действие возможно.
- Meta labels короткие и формальные; выводы и рекомендации остаются в Content.
- Actions называются глаголами и отражают outcome; destructive labels не маскируются общими словами.
- Loading/error/success copy локализованы и предлагают следующий шаг.

## Anti-patterns

- Modal начинается с длинного набора полей без понимания сути.
- Meta содержит выводы, рекомендации или длинные объяснения.
- Workflow actions дублируются в header и footer либо вынесены в page floating widget внутри modal.
- Drawer используется вместо полного просмотра основного объекта.
- Fixed geometry, chat MFE, query parameter names или store protocol reference объявлены стандартом.
- Весь shell блокируется из-за refresh одной независимой секции.
- Clickable icons используются как navigation controls без button semantics.
- Surface stack создан без определённого focus/Escape/back contract.

## Implementation guidance

- Разделить modal shell, header, body layout, content, meta, footer и navigation adapters.
- Parent shell принимает semantic slots и state intents, а не domain field schema.
- Loading текущей сущности отделить от refreshing секции и pending workflow action.
- Origin/return context хранить через approved navigation contract; URL использовать только для shareable/recoverable state по архитектуре.
- Не копировать локальный `ModalLayout` между repositories; сначала проверить утверждённую surface dependency.
- Для optional previous/next использовать stable entity identity и предотвращать показ stale content.
- Проверять UI Kit exports/types перед JSX; custom Portal/facade не считать нормой.

## Evidence

| Repository | Revision | File | Что подтверждает | Ограничения |
|---|---|---|---|---|
| sberorm-enablers/sberorm-cloud-agent-risks-front | 741fa169e66 | `src/components/ModalLayout/ModalLayout.tsx`; `withNavigation.tsx`; `styles.module.scss`; `src/pages/ReadonlyAgentRisksForm/ReadonlyAgentRisksForm.tsx`; router config | Наиболее полный shell: overlay, close/back, optional previous/next, loading, responsive content, nested-surface host | Локальная копия; chat/report/query protocol смешаны с shell; fixed geometry; clickable Icon navigation; content domain-heavy |
| sberorm-enablers/sberorm-cloud-measures-front | 04d04bbdd29 | `src/components/ModalLayout/ModalLayout.tsx`; `withNavigation.tsx`; `styles.module.scss`; `src/pages/ReadonlyMeasureForm/ReadonlyMeasureForm.tsx`; `components/Info/Info.tsx`; router config | Повтор route modal shell; Header/Body, content/meta regions, anchored content, workflow actions и history intent | Footer фактически принадлежит page content; desktop/mobile actions расходятся; shared Portal/Drawer/WorkflowActions API не проверены; raw colors |
| sberorm-enablers/sberorm-cloud-risks-front | 029af7b6402 | `src/components/ModalLayout/ModalLayout.tsx`; `withNavigation.tsx`; `styles.module.scss`; `src/pages/ReadonlyRiskForm/ReadonlyRiskForm.tsx`; `components/Summary/Summary.tsx`; router config | Rich content/meta split, summary-first, related sections, history intent, footer actions и list continuity | Большой domain-specific view; action placement конфликтует с current footer rule; implicit URL protocol; chat coupling; raw colors |

## Reference implementation

Основной reference — Agent Risks `src/components/ModalLayout/ModalLayout.tsx` вместе с `withNavigation.tsx` и `ReadonlyAgentRisksForm`: наиболее полный актуальный shell. Дополнительные references: Measures — для content/meta, anchors и action integration; Risks — для summary-first rich object view.

Reference implementation является доказательством и примером реализации. Его код, props, геометрия и локальные domain-specific решения не копируются автоматически и не становятся нормативными, если это отдельно не указано в паттерне.

## Conflicts and decisions

### Shell anatomy и content hierarchy

**Found:** три implementations повторяют крупную modal surface; content views различаются, но approved UX rule задаёт Header → Body(Content + Meta) → Footer и summary-first.

**Decision:** нормировать semantic regions и hierarchy, не конкретную DOM/grid implementation.

**Classification:** normative.

**Reason:** approved cross-product UX rule имеет приоритет над локальными layout differences.

**Evidence:** `ux_patterns.md`; три revisions.

### Footer actions

**Found:** product views используют `WorkflowActions`, но placement и mobile behavior различаются; shell сам footer не владеет.

**Decision:** large entity modal владеет footer slot и запретом дублирования; внутренний action contract делегировать `workflow-footer`.

**Classification:** normative boundary; conflicted implementation.

**Reason:** approved UX rule требует actions в modal footer, но локальная реализация не даёт единого reusable component contract.

**Evidence:** UX object-modal Footer rule; Measures/Risks/Agent readonly views.

### Route-backed navigation

**Found:** все три shells используют nested routes и query parameters для origin/back/related navigation.

**Decision:** continuity и предсказуемый возврат обязательны; route-backed modal — strong reference, но URL protocol не universal requirement.

**Classification:** reference-backed.

**Reason:** persistence technology может изменяться независимо при сохранении UX contract.

**Evidence:** router configs, `ModalLayout`, `withNavigation` трёх repositories.

### Previous/next navigation

**Found:** повторяется в трёх shell copies, скрывается на phone и при edit.

**Decision:** optional intent для упорядоченного набора; controls и mobile behavior делегировать navigation pattern.

**Classification:** reference-backed / open mobile.

**Reason:** полезно не каждому object modal; текущие clickable icons не удовлетворяют полной accessibility норме.

**Evidence:** три `ModalLayout.tsx` и `withNavigation.tsx`.

### Shared surface dependency

**Found:** custom shell использует `Portal` из shared facade; `Modal` есть в UI Kit index, но его suitability не проверена.

**Decision:** не регистрировать product-specific `ModalLayout` как implemented component; оставить `modal-surface` delegated и dependency open.

**Classification:** open.

**Reason:** frontend rules требуют verified API и запрещают скрывающие facade/copies.

**Evidence:** component index, three shell imports, frontend rules.

## Open questions

- Product-specific требования не предоставлены: блок содержит placeholder.
- Какой approved component/package реализует large `modal-surface` и его accessibility contract?
- Нужен ли единый reusable shell вместо трёх локальных `ModalLayout` copies?
- Каков утверждённый responsive contract Content/Meta/Footer и previous/next?
- Каков maximum nested-surface depth и порядок Escape/back/focus?
- Когда origin/navigation state обязательно хранится в URL?
- Как согласовать WorkflowActions placement в текущих views с approved footer rule?
- Как показывать partial section error и stale content при navigation между сущностями?

## Acceptance checklist

- [ ] Header идентифицирует объект без длинного content и дублирующих actions.
- [ ] Content начинается с понимания сути; Meta остаётся компактной и вторичной.
- [ ] Footer является единственным постоянным местом workflow actions.
- [ ] Loading, refreshing, empty, recoverable error и pending action различены.
- [ ] Close восстанавливает ожидаемый origin context и защищает dirty/pending state.
- [ ] Optional navigation не показывает stale entity и имеет доступные controls.
- [ ] Nested surface сохраняет modal context и следует явному stack contract.
- [ ] Responsive order сохраняет identity → content → meta → actions.
- [ ] Использованы только verified UI Kit exports; shared surface dependency подтверждена отдельно.
- [ ] Fixed geometry, chat, route parameter names и domain content references не нормированы.

