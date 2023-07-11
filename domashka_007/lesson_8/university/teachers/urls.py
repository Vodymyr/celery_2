from django.urls import path
from . import views


app_name =  "teachers"  # Додайте цей рядок, якщо його ще немає

urlpatterns = [
    path("teachers/", views.teacher_list, name="teacher_list"),  # Шлях для листа вчителів
    path("teachers/new", views.new_teacher, name="new_teacher"),  # Шлях для створення нового вчителя
    path("teachers/<int:id>/edit", views.edit_teacher, name="edit_teacher"),  # Шлях для редагування вчителя
    path("teachers/<int:id>/delete", views.delete_teacher, name="delete_teacher"),  # Шлях для видалення вчителя
    path("", views.teacher_list, name="teacher_list"),
    path("new/", views.new_teacher, name="new_teacher"),
    path("edit/<int:id>", views.edit_teacher, name="edit_teacher"),
    path("delete/<int:id>", views.delete_teacher, name="delete_teacher"),
]