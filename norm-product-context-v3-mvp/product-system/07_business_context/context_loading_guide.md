# Руководство по загрузке контекста

## Общий принцип

Сначала читайте manifest и профиль текущего stage. Не передавайте модели весь repository.

## Этап 01 — Product Task

Автоматически: status, authority, mission, constraints, product philosophy, services map, roles, glossary, common rules и known capabilities.

По запросу: только релевантный service document и evidence, влияющее на feasibility.

Не читать: UX, UI, UI Kit и frontend rules.

## Этап 02 — UX Solution

Автоматически: stage 01 foundation в необходимом объёме, current product state/sources, UX principles и UX patterns.

По запросу: релевантные services и evidence текущего flow.

Не читать: UI Kit API, design tokens и frontend implementation rules.

## Этап 03 — UI Prototype

Автоматически: UI context status, compact prototype UI rules, compact frontend prototype rules, UI source registry и component index.

По запросу: только разделы выбранных UI Kit components/types, один relevant service document и один approved UI pattern.

Не читать: весь package, все services, полные frontend rules и product repositories.

## Длинные задачи

Progress и реально прочитанные sources фиксируются в increment-файле текущего stage. После `/clear` новая сессия продолжает работу по checkpoint, а не повторяет исследование.
