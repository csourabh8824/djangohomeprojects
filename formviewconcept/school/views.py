from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponse
# Create your views here.


class ContactFormView(FormView):
    # there is no default template for formview so we have to pass custom template
    template_name = 'school/contact.html'
    # It's iportant to define "form_class" in this class based view. It tells that with which form the view will interact
    form_class = ContactForm
    # initial is used to set default value to the form fields
    initial = {'name': "sourabh", "email": "sourabh@gmail.com",
               "message": "Post any message"}
    # When the form successfully get submitted then to render another template we use "success_url"
    success_url = '/thankyou/'

    def form_valid(self, form):
        print(111111111111111111, form)
        print(222222222222222, form.cleaned_data)
        print(33333333333333, form.cleaned_data['name'])
        print(44444444444444, form.cleaned_data['email'])
        print(555555555555555, form.cleaned_data['message'])
        return HttpResponse('message is sent')


class ThankyouView(TemplateView):
    template_name = 'school/thankyou.html'
