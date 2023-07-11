from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_name', 'get_age']


admin.site.register(Student, StudentAdmin)
