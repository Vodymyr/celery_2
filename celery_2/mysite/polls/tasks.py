import os
from multiprocessing.connection import Client

from celery import Celery

from celery import shared_task

from .models import SMSMessage

from .models import Publication

app = Celery('hello', broker='amqp://guest@localhost//')

@shared_task
def send_sms(phone_number, message):
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    from_number = os.environ.get('TWILIO_PHONE_NUMBER')

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=from_number,
        to=phone_number
    )
    return message.sid

@shared_task
def count_publicatians():
    print("publication count", Publication.objects.count() )


@shared_task
def add_new_publication():
    print("Hello world")
    p = Publication.objects.create(title="New Publication")


def count_publications():
    return None