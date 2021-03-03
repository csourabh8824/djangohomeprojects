from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Student
# Create your views here.


class Home(TemplateView):
    template_name = 'school/home.html'
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.model.objects.all()
        return context


class StudentDetailView(DetailView):
    model = Student
    # default template name = 'appname/ModelClassName_detail.html' in our case it's school/student_detail.html
    # default context name = 'ModelClassName' in our case it's student
    # to use custom template: template_name = 'appname/anyname.html'
    # to use custom context: context_object_name = 'anyname'
    # To use id or any other name instead of pk in urls.py path() then define pk_url_kwarg = 'anyname' now you can use path('student/<int:anyname>')
