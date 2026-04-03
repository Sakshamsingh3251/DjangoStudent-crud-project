from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all()
    count = students.count()

    return render(request, 'list.html', {
        'students': students,
        'count': count
    })

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'form.html', {'form': form})


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'form.html', {'form': form})


def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')


