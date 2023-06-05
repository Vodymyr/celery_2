import os
from celery.app import celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Student.settings')

app = celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


def celery():
    return None


def app():
    return None


def app():
    return None
