from django.shortcuts import render
from .tasks import send_sms

def send_sms_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        send_sms.delay(phone_number, message)

        return render(request, 'success.html')
    return render(request, 'sms_form.html')
