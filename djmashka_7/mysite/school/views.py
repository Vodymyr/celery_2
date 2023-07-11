from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Student
from django.http import HttpResponse


def index(request):
    return HttpResponse("Сторінка школи")


class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')
    success_message = "Студента успішно видалено."

    def post(self, request, *args, **kwargs):
        if request.POST.get('action') == 'delete':
            self.object = self.get_object()
            success_url = self.get_success_url()
            self.object.delete()
            messages.success(self.request, self.success_message)
            return redirect(success_url)
        else:
            return super().post(request, *args, **kwargs)


class StudentUpdateView:
    pass


class StudentCreateView:
    pass


class StudentDetailView:
    pass


class StudentListView:
    pass