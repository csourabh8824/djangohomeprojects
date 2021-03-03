from django.shortcuts import render
from .forms import StudentForm
from django.views.generic import CreateView, UpdateView
from django.views.generic import TemplateView
from .models import Student
# Create your views here.


class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = "school/create_student.html"
    success_url = '/thanks/'


class ThanksView(TemplateView):
    template_name = "school/thanks.html"


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "school/create_student.html"
    success_url = '/thanksupdate/'


class ThanksUpdateView(TemplateView):
    template_name = "school/thanksupdate.html"
