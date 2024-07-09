# students/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print("Error")
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def edit_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form': form, 'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        student.delete()
        return redirect('index')
    return render(request, 'students/delete_student.html', {'student': student})

def search_student(request):
    query = request.GET.get('query')
    results = Student.objects.filter(id=query) if query else []
    return render(request, 'students/search_student.html', {'results': results})
