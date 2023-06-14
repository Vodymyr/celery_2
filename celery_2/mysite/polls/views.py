import os
from twilio.rest import Client
from django.shortcuts import render
from .tasks import send_sms, count_publications
# from polls.tasks import count_publications

#
# account_sid = "ACbae224004e5a756308f9bf7847d3723c"
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#   body="Hello from Twilio",
#   from_="",
#   to="+34624420502"
# )
# print(message.sid)
# def send_sms_view(request):
#     count_publications.delay()
#     if request.method == 'POST':
#         phone_number = request.POST.get('phone_number')
#         message = request.POST.get('message')
#         send_sms.delay(phone_number, message)  # Асинхронно надсилаємо SMS за допомогою Celery.
#         return render(request, 'success.html')
#     return render(request, 'form.html')

def send_sms_view(request):
    count_publications.delay()
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        account_sid = "ACbae224004e5a756308f9bf7847d3723c"
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_="",
            to=phone_number
        )
        print(message.sid)

        send_sms.delay(phone_number, message)  # Асинхронно надсилаємо SMS за допомогою Celery.
        return render(request, 'success.html')
    return render(request, 'form.html')
