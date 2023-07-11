from django import forms
from .models import Teacher, Group


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'date_of_birth', 'subjects']


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']