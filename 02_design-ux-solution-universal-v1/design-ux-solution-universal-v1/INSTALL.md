# Установка design-ux-solution

## 1. Установить global skill

Скопировать папку:

```text
skill/design-ux-solution/
```

в:

```text
~/.gigacode/skills/design-ux-solution/
```

Итог:

```text
~/.gigacode/skills/design-ux-solution/
├── SKILL.md
├── references/
└── examples/
```

Не класть ZIP в `skills`. Архив сначала распаковать.

## 2. Выполнить

```text
/clear
```

## 3. Проверить context registry

Используется существующий файл:

```text
~/.gigacode/product-contexts.yaml
```

Отдельный registry для второго skill не нужен.

## 4. Обновить NORM context

Скопировать содержимое:

```text
context-update/norm/
```

в корень локального NORM context repository с заменой файлов.

Будут добавлены или обновлены:

```text
product-system/context-manifest.yaml
product-system/07_business_context/current_product_state.md
product-system/07_business_context/current_product_sources.yaml
```

## 5. Проверочный запуск

```text
Используй design-ux-solution.
Контекст: norm.
Вход: @increments/INC-001/01_product_brief.md
```
