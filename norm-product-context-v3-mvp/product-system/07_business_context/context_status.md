# Статус продуктового контекста NORM

## Метаданные

| Поле | Значение |
|---|---|
| Context ID | `norm` |
| Package version | `3.0.0-mvp` |
| Статус | `partial` |
| Обновлено | 2026-08-06 |
| Product owner review | требуется |
| Business analyst review | не проводился |
| System analyst review | не проводился |
| UX owner review | требуется |
| Проверка production | не проводилась |

## Что присутствует

- product foundation, service map и шесть service documents;
- роли, glossary, общие business rules, capabilities, constraints и decisions;
- UX principles и UX patterns;
- профили загрузки для этапов 01, 02 и 03;
- нормализованные UI/frontend prototype rules;
- документация и package `@sber-orm/ui-kit` версии `0.283.0`;
- полный источник frontend standards и common components package в evidence layer;
- расширяемый registry для будущих composite patterns и surface templates.

## Что отсутствует или не подтверждено

- verified production behavior и authoritative release registry;
- полная permissions matrix и formal domain model;
- полный каталог business rules и analytics events;
- актуальные frontend/backend repositories как подключённые providers;
- утверждённый каталог composite components, pages и modal templates;
- режим prototype для изменения существующего product surface.

## Правило использования

Контекст пригоден для stages 01–03 в пределах их input gates. Он не является доказательством production behavior, фактических прав, API продукта или выпуска конкретной функции.
