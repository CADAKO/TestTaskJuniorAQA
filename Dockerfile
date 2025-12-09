# Используем официальный образ Playwright, который уже содержит Python и все зависимости браузеров
FROM mcr.microsoft.com

# Устанавливаем ваши дополнительные зависимости (Allure, pytest)
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем ваш код проекта
COPY . .

# Определяем команду запуска по умолчанию
ENTRYPOINT ["python", "-m", "pytest"]
