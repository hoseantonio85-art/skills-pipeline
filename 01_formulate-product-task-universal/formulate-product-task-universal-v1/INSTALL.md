# Установка

## 1. Установить глобальный skill

Скопировать папку:

```text
skill/formulate-product-task/
```

в пользовательскую директорию GigaCode:

```text
~/.gigacode/skills/formulate-product-task/
```

Итог:

```text
~/.gigacode/skills/formulate-product-task/
├── SKILL.md
└── references/
```

## 2. Установить реестр контекстов

Скопировать:

```text
user-config/product-contexts.yaml
```

в:

```text
~/.gigacode/product-contexts.yaml
```

Заменить в профиле `norm` значение `provider.root` на абсолютный путь к локальному клону репозитория с контекстом NORM.

Пример:

```yaml
provider:
  type: local_repository
  root: "/Users/name/work/AI-PDLC-Design"
  manifest: "product-system/context-manifest.yaml"
```

Профиль `orm` можно оставить со статусом `planned`. Skill не будет считать его подключённым.

## 3. Добавить manifest в репозиторий контекста NORM

Скопировать:

```text
context-repository/norm.context-manifest.yaml
```

в репозиторий NORM:

```text
<AI-PDLC-Design>/product-system/context-manifest.yaml
```

Проверить пути внутри manifest и отметить актуальность документов.

## 4. Опционально выбрать контекст на уровне проекта

Чтобы при работе в конкретном репозитории skill автоматически понимал продукт, скопировать:

```text
project-config/product-context.example.yaml
```

в:

```text
<project>/.gigacode/product-context.yaml
```

и указать:

```yaml
context_id: norm
```

Если такого файла нет и контекст не назван в запросе, skill спросит пользователя.

## 5. Перезагрузить skills

После установки или изменения skill выполнить в GigaCode:

```text
/clear
```

## 6. Проверить

```text
/skills formulate-product-task
```

Ожидаемое поведение при отсутствии явного контекста:

```text
Какой продуктовый контекст использовать?

1. norm — локальный репозиторий NORM
2. orm — профиль-заготовка, может быть не подключён
3. без контекста — использовать только ваши вводные и приложенные материалы
```

## Переход на Confluence в будущем

В `~/.gigacode/product-contexts.yaml` provider выбранного профиля меняется с:

```yaml
type: local_repository
```

на:

```yaml
type: confluence_mcp
```

При этом `SKILL.md`, шаблон brief и quality gate не меняются.
