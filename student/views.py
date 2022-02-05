from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import StudentForm
from .models import Student


# Create your views here.

# create new student and list the students
def create_list(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            grade = form.cleaned_data['grade']
            major = form.cleaned_data['major']
            reg = Student(name=name, age=age, address=address, grade=grade, major=major)
            reg.save()
            form = StudentForm()
    else:
        form = StudentForm()
    students = Student.objects.all()

    return render(request, 'student/createlist.html', {'form': form, 'students': students})


# update student information
def update(request, id):
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'student/update.html', {'form': form})


# delete student information
def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect('/')





