# Статус UI-контекста

```yaml
status: ready_for_visual_html_mvp
supported_stages:
  - build-visual-html-prototype
  - build-ui-prototype
supported_modes:
  - standalone_concept
  - product_like_increment
visual_context_available: true
html_starter_available: true
verified_product_repositories:
  - sberorm-cloud-measures-front@04d04bbdd29
  - sberorm-cloud-risks-front@029af7b6402
ui_kit:
  package: "@sber-orm/ui-kit"
  version: "0.283.0"
  package_available: true
  docs_available: true
```

## Доступно

- продуктовые UX-принципы;
- обновлённые правила выбора surfaces;
- текстовый visual language NORM;
- подтверждённые двумя frontend-репозиториями layout и composition patterns;
- правила card registry, dashboard, filters, Object Modal, drawer и floating action dock;
- HTML starter для быстрого визуального прототипирования;
- документация и package UI Kit для последующего этапа реализации.

## Ограничения

- GigaCode не использует скриншоты как вход;
- visual context является MVP-аппроксимацией, а не полной дизайн-системой;
- HTML starter не имитирует API production UI Kit;
- visual regression baseline пока отсутствует.
