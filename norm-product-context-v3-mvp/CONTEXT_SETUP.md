# Подключение единого контекста NORM

## 1. Распаковать архив

Распакуйте repository в стабильную директорию, например:

```text
~/work/norm-product-context
```

Не размещайте его внутри каждого frontend-проекта: это отдельный источник знаний.

## 2. Зарегистрировать provider

Скопируйте:

```text
setup/product-contexts.yaml.example
```

в:

```text
~/.gigacode/product-contexts.yaml
```

Укажите абсолютный путь к распакованному repository.

## 3. Выбрать контекст в рабочем проекте

Создайте:

```text
<project>/.gigacode/product-context.yaml
```

```yaml
context_id: norm
```

## 4. Установить skills отдельно

В пользовательской директории GigaCode должны быть установлены:

```text
~/.gigacode/skills/formulate-product-task/
~/.gigacode/skills/design-ux-solution/
~/.gigacode/skills/build-ui-prototype/
```

После установки или обновления skill/context выполните:

```text
/clear
```

## 5. Как profiles используются

- этап 01: `loading.always` + `loading.for_product_task`;
- этап 02: `loading.always` + `loading.for_ux_solution`;
- этап 03: `loading.always` + `loading.for_ui_prototype`, затем только нужные фрагменты UI Kit.

Не передавайте модели весь архив целиком. Manifest и skill сами задают маршрут чтения.

## 6. Проверка

Из корня context repository:

```bash
python3 tools/validate_context.py
```

Для создания нового ZIP:

```bash
python3 tools/package_context.py
```
