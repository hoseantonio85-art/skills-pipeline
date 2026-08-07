# Universal Formulate Product Task Skill

Универсальный user-level skill для GigaCode, который помогает product owner превратить сырую идею, запрос бизнеса или предварительную user story в проверенный Product Task Brief.

Ключевой принцип:

> Skill знает, **как формулировать задачу**.  
> Подключаемый контекст знает, **для какого продукта формулируется задача**.

Skill не содержит знаний о конкретном продукте. Продуктовые знания подключаются через контекстные профили.

## Поддерживаемые контексты

- `norm` — контекст продукта NORM. В первой версии подключается как локальный репозиторий.
- `orm` — резервный профиль на будущее. В поставке помечен как `planned` и не считается подключённым.
- `none` — работа без продуктового контекста, только по вводным пользователя и приложенным материалам.

Если контекст не указан и не может быть однозначно определён, skill обязан спросить:

> Какой контекст использовать: `norm`, `orm` или работать без контекста?

## Что входит в пакет

```text
formulate-product-task-universal-v1/
├── skill/
│   └── formulate-product-task/
│       ├── SKILL.md
│       └── references/
│           ├── context-resolution.md
│           ├── output-template.md
│           ├── quality-checklist.md
│           └── source-policy.md
├── user-config/
│   └── product-contexts.yaml
├── project-config/
│   └── product-context.example.yaml
├── context-repository/
│   ├── context-manifest.template.yaml
│   ├── norm.context-manifest.yaml
│   └── orm.context-manifest.yaml
├── examples/
│   └── usage.md
└── INSTALL.md
```

## Важное ограничение

`product-contexts.yaml`, `product-context.yaml` и `context-manifest.yaml` — это соглашение данного skill, а не встроенный формат GigaCode.

GigaCode предоставляет механизм user-level skills, работу с локальными файлами и MCP. Этот пакет добавляет поверх них собственный минимальный контракт подключения продуктового контекста.

Позже локальный provider можно заменить на Confluence MCP, не меняя методику skill и формат Product Task Brief.
