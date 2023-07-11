from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import TeacherForm
from .models import Teacher

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

def new_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers:teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teachers/new_teacher.html', {'form': form})

def edit_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers:teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teachers/edit_teacher.html', {'form': form})

def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == "POST":
        teacher.delete()
        return redirect('teachers:teacher_list')
    return render(request, 'teachers/delete_teacher.html', {'teacher': teacher})
