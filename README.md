# celery

# Инструкция по развертыванию проекта

Эта инструкция поможет вам развернуть проект с нуля и запустить основной веб-сервер и Celery для обработки задач. Проект включает в себя следующие задачи:
- Интеграция Celery с Django
- Использование RabbitMQ в качестве брокера сообщений
- Создание вида и формы, принимающих номер телефона и отправляющих SMS
- Отправка SMS через Celery задачу

## Шаги

1. Клонирование репозитория

git clone <URL_репозитория>
cd <название_папки_проекта>

2. Установка зависимостей
pip install -r requirements.txt

3. Создание и активация виртуальной среды (при необходимости)
python3 -m venv myenv
source myenv/bin/activate

4. Установка и настройка RabbitMQ

sudo apt-get install rabbitmq-server
### Запуск сервера RabbitMQ
sudo service rabbitmq-server start
### Создание пользователя и назначение прав доступа
sudo rabbitmqctl add_user <имя_пользователя> <пароль>
sudo rabbitmqctl set_permissions -p / <имя_пользователя> 

5. Настройка переменных окружения
Создайте файл .env в корневой папке проекта и установите следующие переменные окружения:
SECRET_KEY=your-secret-key
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token

6. Применение миграций базы данных
python manage.py migrate

7. Запуск основного веб-сервера
python manage.py runserver

8. Запуск Celery для обработки задач
celery -A <название_проекта> worker --loglevel=info
