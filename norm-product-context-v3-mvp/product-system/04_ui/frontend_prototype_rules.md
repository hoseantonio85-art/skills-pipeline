# Frontend prototype rules — compact stage 03 profile

## 1. Граница результата

Prototype — standalone React/TypeScript implementation на mock/fixture data. Он должен быть визуально точным и сценарно полным, но не считается production microfrontend и не обязан подключать реальные API, auth, analytics или Single-SPA runtime.

## 2. UI Kit

- импортируйте components напрямую из `@sber-orm/ui-kit`;
- сначала проверяйте фактические exports, props, enums и types версии package;
- не создавайте скрывающий facade и не копируйте UI Kit;
- не используйте параллельные base UI libraries;
- layout собирайте через `Row`/`Col`, typography — через `Text`/`Title`, когда API подходит;
- raw HTML controls допустимы только при отсутствии подходящего UI Kit component и с зафиксированным gap.

## 3. Структура

```text
src/
├── @types/
├── components/             # только реально переиспользуемые элементы
├── data/                   # fixtures и demo scenarios
├── helpers/                # pure transformations
├── i18n/locales/ru/        # JSON UI strings
├── pages/<Page>/components # route-specific UI
├── providers/
├── stores/                 # только при нетривиальном state
├── App.tsx
└── main.tsx
```

Не создавайте пустые папки и файлы. Page остаётся композицией и orchestration верхнего уровня.

## 4. Component contract

Самостоятельная папка component содержит implementation, непустой colocated `styles.module.scss` и `index.ts` как public API. Не обходите barrel глубоким импортом файла. Не создавайте facade, который только скрывает внешнюю dependency.

## 5. Styles и tokens

- только реальные UI Kit/theme tokens;
- запрещены hardcoded hex/rgb/hsl/named colors и локальная palette;
- CSS Modules colocated с component;
- inline style только для динамической геометрии, не для цвета;
- config не содержит CSS class strings и visual colors.

## 6. Data, IDs и i18n

- большие mock arrays находятся в `data`;
- domain values используют stable IDs;
- локализованный label не является business ID или guard;
- UI labels, buttons, statuses, notifications и errors находятся в JSON i18n;
- ФИО, компании, договоры, даты и другой runtime content остаются data.

## 7. State и scenarios

Scenario matrix формируется до JSX. Независимые flows не объединяются в god-hook. Пользователь должен переключать demo states без редактирования source code.

## 8. Размер и ответственность

Route page не содержит business calculations, большие fixtures или visual config. Файл component больше 400 строк является blocker без обоснования; целевой размер обычно 200–300 строк.

## 9. Tests

Каждый новый helper и нетривиальная store/model transformation покрываются тестом. Отсутствие component render tests само по себе не является нарушением.

## 10. Self-review

До handoff проверьте hardcoded colors, forbidden imports/re-exports, пустые style modules, file size, user strings, localized guards, dead files/exports, encoding и `git diff --check`. Runtime checks запускаются только если разрешены workspace instructions и dependencies доступны.

Полные нормативные источники находятся в `sources/frontend-rules/` и не читаются по умолчанию.
