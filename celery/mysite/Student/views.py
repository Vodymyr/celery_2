from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Сторынка додатка Student")


def send_sms_view(request, send_sms=None):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        send_sms.delay(phone_number, message)

        return render(request, 'success.html')
    return render(request, 'sms_form.html')

