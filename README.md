# PostTrackingBot

Бот для отслеживания почтовых отправлений через API Почты России с сохранением истории запросов в БД.

##  Функционал
- Отслеживание статуса отправлений по трек-номеру

##  Технологии
- `Python 3.10+`
- `Aiogram 3.x` (Telegram Bot API)
- `SQLAlchemy 2.0` (работа с БД)
- `Zeep` (SOAP-клиент для API Почты России)
- `PostgreSQL` ( БД)
- `Alembic` (миграции БД)
- `requests`
- `API`
  

##  Настройка (.env)
Создайте файл `.env` в корне проекта:
```ini
BOT_TOKEN=ваш_токен_бота_от_BotFather
DB_HOST=localhost
DB_PORT=DB_PORT
DB_USER=ваш_пользователь_db
DB_PASS=ваш_пароль_db
DB_NAME=имя_базы
LOGIN_POST=логин_от_ПочтыРоссии
PASS_POST=пароль_от_ПочтыРоссии
