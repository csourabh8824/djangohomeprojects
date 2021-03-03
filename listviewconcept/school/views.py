from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.


class StudentListView(ListView):
    model = Student
    ordering = ['course']
    # default_template_name = ModelClassName_list.html here it is student_list.html
    # default_context_name = ModelClassName_list or object_list here it is student_list
    # to set custom template name: template_name = 'appname/'AnyNameYouWantToGive.html''
    # to set custom context name: context_object_name = 'Any Name You Want To Give'
    # to change suffix of template: template_name_suffix = '_get' this _get will replace _list
    # ordering : Order according to given field name

    # To filter the data from database use get_queryset() function:
    def get_queryset(self):
        return Student.objects.filter(course="python")

    # To add more data to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(1111111111, kwargs)
        context["new_context"] = Student.objects.all().order_by("roll")
        return context
