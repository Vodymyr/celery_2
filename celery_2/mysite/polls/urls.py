from django.urls import path

from . import admin
from .views import send_sms_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('send-sms/', send_sms_view, name='send_sms'),
    # Додайте інші URL-адреси, які вам потрібні.
]
