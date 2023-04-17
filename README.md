## Зависимости
- Docker version 23.0.3
- Docker Compose version v2.17.2
- GNU Make 4.2.1

## Подготовительные работы
- make build

## Запуск проекта
- make start

## Доп команды
- make stop - остановка сервисов
- make restart - рестарт сервисов
- make create_revision - создание версии миграции
- make migration hash=<указать hash миграции> - мигрировать таблицы