from django.template.context_processors import static
from django.urls import path

import settings
from school.views import *

urlpatterns = [
    path('', index),
    # path('', views.StudentListView.as_view(), name='student_list'),
    # path('student/add/', views.StudentCreateView.as_view(), name='student_add'),
    # path('student/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    # path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    # path('group/<int:pk>/add_student/', views.add_student_to_group, name='add_student_to_group'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL)
