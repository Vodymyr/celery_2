from django.contrib import admin
from .models import Teacher
from .models import Group
from .models import Student, StudentsGroup

admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(StudentsGroup)


def site():
    return None
