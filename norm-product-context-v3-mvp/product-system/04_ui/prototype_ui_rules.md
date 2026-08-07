# Compact UI rules for prototype stage

## 1. Не перепроектировать UX

`02_ux_solution.md` определяет flow, surfaces, information hierarchy, actions и states. Этап 03 выбирает композицию и UI Kit components, но не меняет бизнес-логику и пользовательский сценарий молча.

## 2. Управлять вниманием

- сначала главный вопрос, сигнал и summary;
- затем причины, связи и детали;
- приоритет важнее полноты;
- сложное раскрывается прогрессивно;
- интерфейс должен вести к следующему действию.

## 3. Surface roles

- page — обзор, список и продолжительная работа;
- object modal — полный просмотр объекта, фокус и решение;
- drawer — короткий вспомогательный шаг без потери контекста;
- action modal — подтверждение или критическое действие.

Не открывайте полный объект в drawer и не делайте drawer обязательной остановкой перед object modal.

## 4. Действия

- page-level primary actions следуют утверждённому page pattern;
- object modal actions находятся в footer;
- primary action не дублируется без причины;
- destructive action визуально и смыслово отделяется;
- результат значимого действия всегда имеет feedback.

## 5. Состояния

Для применимых surfaces реализуйте default/success, loading, empty, recoverable error, disabled/pending, validation и action success/failure. Empty и error states должны объяснять следующий шаг.

## 6. AI blocks

AI объясняет ситуацию, основания и рекомендуемое действие. Он не является декоративным баннером и не дублирует данные без новой ценности.

## 7. Visual language

Используйте продуктовый UI Kit и tokens. Не создавайте новую палитру, новую типографику или случайный dashboard-style. Минимализм достигается иерархией, spacing и точностью, а не отсутствием содержания.

Подробные основания находятся в `product-system/03_ux/ux_principles.md` и `ux_patterns.md`; stage 03 читает только релевантные разделы при споре.
