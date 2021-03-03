from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from .forms import StudentForm
from .models import Student
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = "school/studentcreate.html"
    success_url = '/thanks/'


class StudentView(TemplateView):
    template_name = "school/thanks.html"


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "school/studentcreate.html"
    success_url = '/thanksupdate/'


class ThanksUpdate(TemplateView):
    template_name = 'school/thanksupdate.html'


class StudentDeleteView(DeleteView):
    model = Student
    # by default it take's default template as modelname_confirm_delete.html
    success_url = '/studentdeleted/'


class StudentDeletedView(SuccessMessageMixin, TemplateView):
    success_message = 'Student successfully deleted'
    template_name = 'school/deleted.html'
