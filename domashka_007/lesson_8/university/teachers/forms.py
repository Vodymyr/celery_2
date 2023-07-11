from django.forms import ModelForm

from teachers.models import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "subject"]
