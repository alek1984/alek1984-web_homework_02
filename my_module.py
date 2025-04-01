# Використовуємо базовий образ Python
FROM python:3.9-slim-buster

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо файли залежностей (якщо є)
COPY pyproject.toml poetry.lock ./

# Встановлюємо Poetry
RUN pip install poetry

# Встановлюємо залежності проекту
RUN poetry install --no-root

# Копіюємо файли проекту
COPY . .

# Встановлюємо змінну середовища, якщо необхідно
ENV APP_NAME "personal-assistant"

# Визначаємо команду для запуску застосунку
CMD ["poetry", "run", "python", "personal_assistant/main.py"]