## Project Structure

Структура проекта:
```text
service-name/
    pyproject.toml
    src/
        service_name/
            domain/
            application/
            infrastructure/
            presentation/
            core/
```

---

## Domain

Содержит только бизнес-логику

Не должен зависеть от:
- FastAPI
- Конкретной базы данных
- Pydantic моделей

---

## Application

Сценарии использования

Внутри:
- Services
- DTO

Может зависеть только от domain

---

## Infrastructure

Инфраструктурные зависимости:

- SQLAlchemy, ORM модели
- Репозитории
- Внешние API

---

## Presentation

HTTP интерфейс:

- FastAPI routers
- Request schemas
- Response schemas

Pydantic модели для API лежат здесь.

---

## Configuration

Используется pydantic-settings

Пример переменных окружения:

CASH_REGISTER__DATABASE__URL=sqlite:///data/app.db

Конфиги обычно:\
config/settings.py  
config/database.py
