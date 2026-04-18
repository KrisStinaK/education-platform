# Умный Кот — Образовательная платформа с чатом в реальном времени

Современная образовательная платформа на Django с поддержкой живых чатов через WebSocket.  
Идеально подходит для онлайн-курсов, вебинаров и группового обучения.

## 🚀 Основные возможности

- 📚 **Управление курсами** — создание уроков, модулей и тестов
- 👥 **Роли пользователей** — студент, преподаватель, администратор
- 💬 **Чат в реальном времени** — общение внутри курсов
- 🔔 **Уведомления** — о новых сообщениях и событиях в чате
- 📊 **Прогресс обучения** — отслеживание прохождения материалов
- 🧪 **Тестирование** — встроенные тесты с автоматической проверкой
- 📱 **Адаптивный дизайн** — работает на всех устройствах

## 🛠 Технологии

- **Backend:** Django 5.x, Django Channels
- **WebSockets:** Daphne / Redis
- **Database:** PostgreSQL / SQLtie (для разработки)
- **Frontend:** HTML5, CSS, JavaScript (WebSocket API)
- **Authentication:** Django Auth
- **Async:** ASGI, async views

## 📋 Требования

- Python 3.10+
- Django 5.x
- Redis (для production-окружения)

## 🏗 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/KrisStinaK/education-platform.git
cd education-platform
```
2. Настройка виртуального окружения
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows
```
3. Установка зависимостей
```
pip install -r requirements.txt
```