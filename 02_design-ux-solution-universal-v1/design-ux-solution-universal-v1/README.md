# design-ux-solution — Universal Skill v1

Второй skill AI PDLC:

```text
formulate-product-task
→ design-ux-solution
→ UI prototype skill
```

## Что делает

Принимает утверждённый Product Task Brief и создаёт `02_ux_solution.md`.

Учитывает:

- выбранный продуктовый контекст;
- текущий продукт;
- UX principles;
- UX patterns;
- сущности и данные;
- состояния;
- edge cases;
- роль AI;
- handoff для прототипа.

## Что не делает

- не рисует;
- не назначает цвета;
- не задаёт размеры;
- не выбирает UI Kit components;
- не пишет код;
- не создаёт прототип.

## Установка

Скопировать:

```text
skill/design-ux-solution/
```

в:

```text
~/.gigacode/skills/design-ux-solution/
```

Затем выполнить:

```text
/clear
```

Контекст NORM требует обновления manifest. Файлы находятся в:

```text
context-update/norm/
```
