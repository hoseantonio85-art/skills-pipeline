---
name: build-visual-html-prototype
description: Создаёт быстрый интерактивный HTML/CSS/JavaScript-прототип по утверждённым Product Task Brief и UX Solution, используя визуальный язык, паттерны и HTML-заготовки выбранного продукта. Используй для проверки UX-концепции и визуальной композиции до переноса на UI Kit. Приоритеты — ясный сценарий, сходство с NORM, качество иерархии, правдоподобный контент и ключевые состояния; production-архитектура, настоящий UI Kit, API, i18n и строгая типизация не требуются.
---

# Build Visual HTML Prototype

## Input gate

Начинай, если доступны:

- Product Task Brief со статусом `READY_FOR_UX`;
- UX Solution со статусом `READY_FOR_PROTOTYPE`;
- выбранный product context;
- visual context и хотя бы базовый HTML starter.

Если UX Solution не определяет основной сценарий, surfaces или информационный приоритет, верни `BLOCKED_BY_UX_HANDOFF`.

## Context loading

Для NORM прочитай:

1. `04_ui/visual/visual-language.md`;
2. `04_ui/visual/layout-and-density.md`;
3. `04_ui/visual/pattern-selection.md`;
4. `04_ui/visual/modal-and-drawer.md` только при соответствующих surfaces;
5. только релевантные UX patterns и service context.

Не загружай документацию всего UI Kit. На этом этапе не подключай настоящий UI Kit, если пользователь явно не попросил иначе.

## Priorities

1. UX clarity.
2. Product likeness.
3. Visual hierarchy and composition.
4. Scenario completeness.
5. Plausible content.
6. Sufficient prototype code quality.

## Workflow

1. Прочитай brief и UX Solution; не меняй flow молча.
2. Выбери минимальный набор product patterns.
3. Начни с `assets/norm-html-starter`, если выбран NORM.
4. Составь короткий visual plan: shell, surfaces, hierarchy, density, states, interactions.
5. Создай правдоподобные fixtures на русском языке.
6. Реализуй happy path и критические альтернативные состояния.
7. Добавь только взаимодействия, необходимые для демонстрации решения.
8. Открой прототип в доступном browser/preview и проверь desktop layout.
9. Исправь очевидные проблемы композиции после первого render.
10. Сохрани прототип и короткий handoff.

## Implementation rules

- Предпочитай обычные HTML, CSS и JavaScript; React допустим, если уже есть подходящий starter или сложное состояние.
- Используй CSS variables визуального контекста.
- Допускай локальные prototype-компоненты без имитации API настоящего UI Kit.
- Не называй самодельные компоненты `@sber-orm/ui-kit` и не создавай ложный alias.
- Не добавляй production layers, stores, API clients, i18n и тесты без необходимости.
- Отделяй demo scenario controls от продуктовой поверхности.
- Не используй изображения как обязательный вход: GigaCode должен работать по текстовым правилам и assets.

## NORM rules

- Не используй классические таблицы как основной реестр.
- Используй card registry или row-cards с приоритетом, объяснением и действием.
- Dashboard допустим и желателен для обзора, мониторинга или зон внимания, если его агрегаты ведут к drill-down.
- Используй floating action dock, когда основное действие или AI/chat должно оставаться доступным при прокрутке.
- Используй emoji точечно, но не вместо системной визуальной семантики целиком.
- Не делай summary обязательной декоративной секцией: добавляй её, когда она сокращает работу интерпретации.

## Required states

Реализуй default и все состояния, критичные для UX acceptance criteria. Обычно это loading, empty, error и один action progress/success. Не создавай пять декоративных сценариев, если они не проверяют решение.

## Visual quality gate

Прототип готов, если:

- основной сценарий можно пройти;
- первый экран объясняет приоритет и следующий шаг;
- интерфейс выглядит частью выбранного продукта;
- контент правдоподобен;
- композиция не распадается на равнозначные блоки;
- card registry можно быстро сканировать;
- modal/drawer сохраняют контекст;
- floating dock не перекрывает содержимое;
- прототип был открыт и проверен после сборки.

Без runtime preview используй статус `READY_WITHOUT_VISUAL_REVIEW`, а не полный PASS.

## Output

Сохрани запускаемый проект и `03_visual_prototype.md` с разделами: sources, visual plan, реализованные сценарии, отклонения от UX Solution, проверенные viewport, ограничения и статус.
