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
from django.urls import path, include

from school import admin

app_name = 'school'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('school.urls')),
    # path('students/', StudentListView.as_view(), name='student_list'),
    # path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    # path('students/new/', StudentCreateView.as_view(), name='student_create'),
    # path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_update'),
    # path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]
