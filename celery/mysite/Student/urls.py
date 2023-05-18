from django.urls import path
from . import views
from .views import send_sms_view

app_name = 'students'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student_list'),
    path('send-sms/', send_sms_view, name='send_sms')
    # path('create/', views.StudentCreateView.as_view(), name='student_create'),
    # path('<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    # path('<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    # path('add_to_group/', views.AddStudentToGroupView.as_view(), name='add_student_to_group'),
]
