import os
from celery.app import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Student.settings')

app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


def celery():
    return None


def app():
    return None