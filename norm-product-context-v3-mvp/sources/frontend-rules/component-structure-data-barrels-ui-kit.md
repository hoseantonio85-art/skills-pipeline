  

### 1. Target-first структура

Перед созданием новой страницы или сервиса необходимо изучить структуру актуальных продуктовых репозиториев того же типа. Абстрактные best practices не должны заменять фактически принятую в проекте архитектуру.

Для доменного микрофронтенда предпочтительна структура:

```javascript
```

```javascript
src/
├─ @types/
├─ components/
├─ data/
├─ helpers/
├─ i18n/
├─ pages/
├─ providers/
├─ stores/
└─ <service>-mf-app.tsx
```

Ответственность слоёв:

- 
  ```javascript
  pages
  ```

   — route-level композиция экрана;
- 
  ```javascript
  pages/<Page>/components
  ```

   — компоненты, используемые только конкретной страницей;
- 
  ```javascript
  components
  ```

   — действительно переиспользуемые между страницами компоненты;
- 
  ```javascript
  data
  ```

   — fixtures, mock-данные и воспроизводимые демонстрационные состояния;
- 
  ```javascript
  helpers
  ```

   — чистые преобразования и бизнес-вычисления;
- 
  ```javascript
  stores
  ```

   — состояние, derived values и actions;
- 
  ```javascript
  providers
  ```

   — router, store provider, runtime-обвязка;
- 
  ```javascript
  @types
  ```

   — доменные типы и стабильные идентификаторы;
- 
  ```javascript
  i18n
  ```

   — пользовательские интерфейсные строки.

Route-specific компонент нельзя помещать в общий 

```javascript
src/components
```

, если он используется только одной страницей.

### 2. Правило для 

```javascript
data
```

Большие массивы договоров, компаний, пользователей, модулей, тарифов и других mock-объектов не должны находиться внутри page или component.

Для них используется отдельный слой:

```javascript
```

```javascript
src/data/
└─ tariffFixtures.ts
```

В 

```javascript
data
```

 допустимо хранить runtime/mock content:

- ФИО и email;
- названия компаний;
- номера договоров;
- даты;
- описания тарифов и модулей;
- демонстрационные данные сценариев.

В 

```javascript
data
```

 нельзя хранить:

- CSS-классы;
- JSX;
- обработчики;
- визуальные цвета;
- локализованные UI-labels для кнопок, фильтров и системных сообщений.

Mock-данные должны использовать стабильные domain ids. Отображаемое локализованное название не должно становиться business id.

Правильно:

```javascript
```

```javascript
{
  roleIds: ["ORMCLOUD_RISKMANAGER"];
  status: "active";
}
```

Неправильно:

```javascript
```

```javascript
{
  role: "Риск-менеджер";
  status: "Активен";
}
```

### 3. 

```javascript
index.ts
```

 как публичный API компонента

В целевых frontend-репозиториях каждая самостоятельная папка компонента должна иметь 

```javascript
index.ts
```

.

```javascript
```

```javascript
components/
└─ UsersList/
   ├─ UsersList.tsx
   ├─ styles.module.scss
   └─ index.ts
```

Содержимое:

```javascript
```

```javascript
export { UsersList } from "./UsersList";
```

или, если компонент экспортирует несколько связанных сущностей:

```javascript
```

```javascript
export * from "./SystemAccessState";
```

Потребители должны импортировать компонент через публичный API папки:

```javascript
```

```javascript
import { UsersList } from "@/pages/TariffInfo/components/UsersList";
```

Не следует обходить barrel прямым импортом файла:

```javascript
```

```javascript
import { UsersList } from "@/pages/TariffInfo/components/UsersList/UsersList";
```


```javascript
index.ts
```

, который непосредственно экспортирует компонент своей папки, является штатным публичным API и не считается бесполезным re-export.

При этом запрещено создавать facade-файлы, которые импортируют внешнюю библиотеку и сразу переэкспортируют её только для сокрытия реальной зависимости:

```javascript
```

```javascript
// Запрещённый локальный facade
export { Button, Modal, Row } from "@sber-orm/ui-kit";
```

UI Kit должен быть виден в импортах потребляющего компонента.

### 4. UI Kit без скрывающих адаптеров

Компоненты UI Kit импортируются напрямую:

```javascript
```

```javascript
import {
  Button,
  Chips,
  Modal,
  Row,
  Switch,
  Text,
  Title,
} from "@sber-orm/ui-kit";
```

Запрещено без подтверждённой необходимости:

- копировать UI Kit в 

  ```javascript
  vendor
  ```

  ;
- создавать локальную библиотеку-дубль;
- скрывать UI Kit за универсальным adapter/facade;
- использовать Radix, shadcn или другой UI-фреймворк параллельно;
- создавать собственные 

  ```javascript
  ActionButton
  ```

  , 

  ```javascript
  BaseButton
  ```

   или 

  ```javascript
  CustomModal
  ```

  , если штатный компонент уже решает задачу;
- использовать сырой HTML 

  ```javascript
  button
  ```

  , 

  ```javascript
  input
  ```

  , 

  ```javascript
  select
  ```

  , 

  ```javascript
  textarea
  ```

   вместо компонентов UI Kit.

Технические HTML-обёртки допустимы, если UI Kit не предоставляет подходящего семантического элемента:

- divider;
- notification host;
- wrapper для ограничения ширины;
- wrapper для CSS-состояния.

Интерактивная карточка может оставаться карточкой, а не превращаться в визуальный 

```javascript
Button
```

, если:

- это явно требуется дизайном;
- присутствуют 

  ```javascript
  role
  ```

  , 

  ```javascript
  tabIndex
  ```

  , 

  ```javascript
  aria-label
  ```

  ;
- реализованы Enter и Space;
- внутри используется штатная видимая кнопка UI Kit;
- клавиатурное и pointer-поведение согласованы.

### 5. Layout, типографика и стили

Layout собирается через 

```javascript
Row
```

 и 

```javascript
Col
```

. Типографика — через 

```javascript
Text
```

 и 

```javascript
Title
```

.

Для каждого визуального компонента используется colocated непустой SCSS Module:

```javascript
```

```javascript
Component/
├─ Component.tsx
├─ styles.module.scss
└─ index.ts
```

Допустимый локальный импорт:

```javascript
```

```javascript
import classes from "./styles.module.scss";
```

В стилях используются только токены UI Kit. Hardcoded hex, RGB, локальная палитра и Tailwind color utilities запрещены.

### 6. i18n только в JSON

Пользовательские интерфейсные строки должны храниться в JSON:

```javascript
```

```javascript
src/i18n/locales/ru/tariff.json
```

```javascript
```

```javascript
{
  "toolbar": {
    "all": "Все",
    "tariff": "В тарифе",
    "notBillable": "Не тарифицируется"
  }
}
```

TypeScript допускается только для настройки i18next и подключения JSON-ресурсов:

```javascript
```

```javascript
import tariff from "@/i18n/locales/ru/tariff.json";

export const resources = {
  ru: { tariff },
} as const;
```

В TSX не должны оставаться пользовательские системные строки, названия кнопок, фильтров, статусов, уведомлений и ошибок.

ФИО, названия компаний, номера договоров и другой runtime content являются данными и не обязаны переноситься в i18n.

### 7. Разделение UI и бизнес-логики

Page должна оставаться композицией компонентов. Бизнес-правила нельзя реализовывать глубоко внутри JSX.

Пример разделения:

```javascript
```

```javascript
src/
├─ data/tariffFixtures.ts
├─ helpers/tariff.ts
├─ helpers/tariff.test.ts
├─ stores/TariffStore.ts
├─ stores/TariffStore.test.ts
└─ pages/TariffInfo/
```

В 

```javascript
helpers
```

 размещаются:

- определение тарифицируемой роли;
- подсчёт занятых слотов;
- фильтрация;
- вычисление stale-состояния;
- initials и детерминированный avatar tone;
- immutable-преобразования пользователей.

В 

```javascript
store
```

 размещаются:

- состояние фильтров;
- открытие modal/popover;
- активация и деактивация;
- проверка лимита;
- feedback;
- derived counters.

Новые и изменённые helpers/stores должны покрываться тестами.

### 8. Обработчики

Обработчики, которые передаются дочерним компонентам, участвуют в dependencies или заметно усложняют JSX, выносятся в 

```javascript
useCallback
```

.

Неправильно:

```javascript
```

```javascript
<TariffModal onClose={() => setOpen(false)} />
```

Правильно:

```javascript
```

```javascript
const handleClose = useCallback(() => setOpen(false), []);

<TariffModal onClose={handleClose} />;
```

MST-компонент, читающий observable store, должен быть обёрнут в 

```javascript
observer
```

.

### 9. Microfrontend runtime

Если эталонные сервисы используют Single-SPA, новый сервис не должен поставляться как отдельное самостоятельное React-приложение.

Нужно повторять target-паттерн:

- entrypoint с 

  ```javascript
  bootstrap
  ```

  , 

  ```javascript
  mount
  ```

  , 

  ```javascript
  unmount
  ```

  ;
- 
  ```javascript
  single-spa-react
  ```

  ;
- внутренний 

  ```javascript
  BrowserRouter
  ```

   с 

  ```javascript
  basename
  ```

   из host runtime;
- общий auth microfrontend;
- общий 

  ```javascript
  ClickStreamProvider
  ```

  ;
- externalized React, React DOM, router, UI Kit и общие runtime-зависимости;
- отсутствие собственного сайдбара и внешнего layout в production-handoff.

Preview-версия может иметь собственную оболочку только как отдельная ветка или отдельный режим для визуальной проверки.

### 10. Разделение Preview и frontend-handoff

Если корпоративные зависимости недоступны локально, рекомендуется разделять:

- 
  ```javascript
  preview
  ```

   — самостоятельно запускаемая версия для GitHub Pages, скриншотов и визуальных проверок;
- 
  ```javascript
  handoff
  ```

   — чистый целевой микрофронтенд для продуктовой команды.

В handoff-ветке не должно быть:

- vendored UI Kit;
- legacy-компонентов прототипа;
- favicon и демонстрационных assets, не относящихся к сервису;
- Radix/shadcn/Tailwind;
- самостоятельной внешней оболочки;
- локальных UI-фасадов;
- сгенерированных build-файлов;
- 
  ```javascript
  *.tsbuildinfo
  ```

  ;
- временных patch-файлов.

Handoff должен содержать инструкцию:

- какие зависимости предоставляет target runtime;
- какие версии нужно уточнить;
- какие fixtures заменить API;
- какие query-сценарии удалить;
- какие проверки выполнить после подключения корпоративного registry.

### 11. Проверка перед передачей

Обязательный статический аудит:

- у всех компонентных папок есть корректный 

  ```javascript
  index.ts
  ```

  ;
- нет обхода публичных component imports;
- нет скрывающих UI Kit re-exports;
- нет hardcoded colors;
- нет пустых или неиспользуемых SCSS Modules;
- нет пользовательских строк вне i18n;
- нет больших fixtures внутри components/pages;
- нет компонентов больше 400 строк без обоснования;
- нет inline JSX handlers, которые должны быть callbacks;
- нет dead code и запрещённых зависимостей;
- нет vendored и generated-файлов;
- 
  ```javascript
  git diff --check
  ```

   проходит;
- helpers/stores покрыты тестами;
- TypeScript, lint, test и build запускаются после подключения target dependencies.

  