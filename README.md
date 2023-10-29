# Менеджер паролей.

Приложение позволяет хранить название сервисов и пароли к ним. Пароли хвранятся в зашифрованном виде.
При запросе пароля, происходит расшифровка.

### Стэк: DRF, PostgreSQL, Docker
### Для удобства тестирования используется Swagger.

## Запуск приложения:
Для запуска приложения необходимо:
  1) Создать и активировать окружающую среду:
     ```
     python -m venv venv
     venv/scripts/activate
     ```
  2) Сбилдить контейнеры и запустить их:
     ```
     docker compose build
     docker compose up -d
     ```
  3) Провести миграции:
     ```
     docker exec -it django bash
     python manage.py migrate
     ```
## Тестирование.
Для ручного тестирования можно воспользоваться Swagger по адресу http://localhost:8000/swagger/
или Postman.
Для запуска тестов необходимо выполнить команду:
  ```
  docker compose run django python manage.py test
  ```
