
from django.urls import path

from . import views

app_name = 'university'

urlpatterns = [
    path("", views.index, name="index"),
    path("students/<int:id>", views.student_view, name="student_view"),
    path("student/", views.new_student, name="new_student"),
    path("student/delete/<int:id>", views.delete_student, name="delete_student"),
]