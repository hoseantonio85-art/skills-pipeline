# Авторитетность источников

## 1. Product foundation

`01_product_foundation/` задаёт направление, принципы и миссию. Это не evidence выпущенной функции.

## 2. Services map

`02_services/services_map.md` — основной источник текущей продуктовой модели сервисов. При расхождении с отдельным service document конфликт фиксируется явно.

## 3. Service documents

`02_services/*.md` дают дополнительный контекст по конкретному сервису, но сами по себе не подтверждают production behavior.

## 4. Business context digest

`07_business_context/` — нормализованная выжимка для быстрого чтения. При споре возвращайтесь к источнику, указанному в source registry.

## 5. UX rules

`03_ux/` определяет принципы взаимодействия и утверждённые UX patterns. Эти документы не доказывают наличие UI в production и не подменяют task-specific UX Solution.

## 6. UI/frontend normalized rules

`04_ui/` определяет правила сборки prototype и маршрут к UI Kit. Task-specific `02_ux_solution.md` имеет приоритет в flow и information architecture; UI context определяет реализацию, а не заново проектирует UX.

## 7. UI Kit API

Для фактических exports, props, enums и types приоритет источников:

1. package/type declarations той же версии;
2. generated или проверенная документация той же версии;
3. component index;
4. общие упоминания в правилах.

Если документация расходится с package types, фиксируйте конфликт и используйте package types как API evidence.

## 8. Evidence layer

`sources/` хранит полные первоисточники. Он не загружается автоматически. Нормализованные документы используются для обычной работы, evidence — для проверки спорного правила или точного API.

## 9. Task increments

`01_product_brief.md`, `02_ux_solution.md` и `03_ui_prototype.md` описывают конкретное изменение. Они имеют приоритет для scope предлагаемого решения, но не подтверждают текущее production behavior.

## 10. Конфликты

Не разрешайте конфликт молча. Укажите источники, их revision/status и влияние на решение. Если конфликт меняет flow, права, бизнес-правило или необратимое действие, верните задачу на соответствующий предыдущий этап.
