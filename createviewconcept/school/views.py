from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
# Create your views here.


class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/createstudent.html'
    success_url = '/thanks/'


class StudentView(TemplateView):
    template_name = "school/thanks.html"
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = self.model.objects.all()
        return context
