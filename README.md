## Зависимости
- Docker version 23.0.3
- Docker Compose version v2.17.2
- GNU Make 4.2.1

## Подготовительные работы
- make build
- Создаем .env файл и добавляем секреты для работы с БД (пример):
    ```
    POSTGRES_USER=test
    POSTGRES_PASSWORD=test
    POSTGRES_DB=test
    DB_HOST=localhost
    DB_PORT=5432
    SECRET_AUTH="SECRET"
    ```

## Запуск проекта
- make start
- make migration мигрируем готовые таблицы для БД

## Доп команды
- make stop - остановка сервисов
- make restart - рестарт сервисов
- make create_revision - создание версии миграции
- make migration hash=<указать hash миграции> - мигрировать таблицы
