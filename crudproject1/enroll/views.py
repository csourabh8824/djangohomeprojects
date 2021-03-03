from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistration
from .models import User
# Create your views here.


# This function will add and show all records
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pwd)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    student_info = User.objects.all()
    return render(request, 'enroll/addandshow.html', context={'form': fm, 'student_information': student_info})


# This function will delete student record
def delete_data(request, id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')


# This function will update student information
def update_student(request, id):
    student_record = User.objects.get(pk=id)
    if request.method == "POST":
        fm = StudentRegistration(request.POST, instance=student_record)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = StudentRegistration(instance=student_record)
    return render(request, 'enroll/updatestudent.html', {'form': fm})
