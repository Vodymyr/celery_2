"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import index
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from Student.views import *


app_name = 'celery'
@csrf_exempt
def celery_view(request):
    """

    :param request:
    :return:
    """
    return app.handle_task(request)

urlpatterns = [
    path("", include("Student.urls")),
    # path("Student/", index),
    # path("", index),
    # path("Student/", include("Student.urls")),
    path("admin/", admin.site.urls),
    #path('celery/', celery_view, name='celery'),
]
