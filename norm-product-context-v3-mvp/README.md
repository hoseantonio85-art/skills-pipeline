# NORM Product Context v3 MVP

Единый локальный context repository для трёх GigaCode skills:

1. `formulate-product-task` — этап 01;
2. `design-ux-solution` — этап 02;
3. `build-ui-prototype` — этап 03 MVP.

Точка входа:

```text
product-system/context-manifest.yaml
```

Контекст отделён от skills и от task increments. Skills устанавливаются отдельно, а документы задачи (`01_product_brief.md`, `02_ux_solution.md`, `03_ui_prototype.md`) находятся в рабочем проекте.

## Принцип устройства

- `product-system/` — компактные нормализованные знания, которые разрешено загружать в контекст модели;
- `sources/` — полные первоисточники и пакеты для точечной проверки, но не для автоматической загрузки;
- `loading` в manifest определяет, какой объём получает каждый skill;
- отсутствующие UI patterns не блокируют этап 03: используется UX Solution, UI/UX rules и фактический API UI Kit.

## Поддерживаемая граница этапа 03

`build-ui-prototype` поддерживает только `standalone_greenfield`. Точечная модификация существующего продуктового интерфейса остаётся будущей capability.

См. `CONTEXT_SETUP.md`, `CONTEXT_MAINTENANCE.md` и `product-system/07_business_context/stage_access_matrix.yaml`.
