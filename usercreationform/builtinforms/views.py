from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Form submitted</h1>")
    else:
        form = RegistrationForm()
    return render(request, 'builtinforms/register.html', context={'form': form})
