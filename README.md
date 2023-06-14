celery_2
Инструкция по развертыванию проекта

Шаг 1: Установка зависимостей python -m venv myenv 
  source myenv/bin/activate # Для Linux/Mac 
  myenv\Scripts\activate # Для Windows 
pip install -r requirements.txt

Шаг 2: Настройка RabbitMQ

Шаг 3: Настройка Celery В файл mysite/settings.py нужно добавить код CELERY_BROKER_URL = 'amqp://localhost' CELERY_RESULT_BACKEND = 'django-db'

Шаг 4: Создайте файл celery.py

Шаг 5: Создайте файл tasks.py
