from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import StudentRegisterationForm, StudentLoginForm
from .models import Student
from django.contrib.auth import authenticate, login
# Create your views here.


def home(request):
    student_data = Student.objects.all()
    return render(request, 'school/home.html', context={'student_data': student_data})


def register(request):
    if request.method == "GET":
        form = StudentRegisterationForm()
    elif request.method == "POST":
        form = StudentRegisterationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            age = form.cleaned_data.get('age')
            add_data = Student(username=username, email=email,
                               password=password, age=age)
            add_data.save()
            return redirect('home')
    return render(request, 'school/register.html', context={'form': form})


def update_student_data(request, id):
    student_data = Student.objects.get(pk=id)
    if request.method == "POST":
        form = StudentRegisterationForm(request.POST, instance=student_data)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentRegisterationForm(instance=student_data)
    return render(request, 'school/update_data.html', context={'form': form})


def delete_data(request, id):
    if request.method == "POST":
        student_data = Student.objects.get(pk=id)
        student_data.delete()
        return HttpResponseRedirect('/')


# def student_login(request):
#     form = StudentLoginForm()
#     return render(request, 'school/login.html', context={'form': form})
