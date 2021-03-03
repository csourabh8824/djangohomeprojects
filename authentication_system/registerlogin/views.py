from django.shortcuts import render, redirect
from .forms import RegisterationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Registered</h1>")
    elif request.method == "GET":
        form = RegisterationForm()
    return render(request, 'registerlogin/register.html', context={"form": form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('register')

    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        print("here")

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # print(111111111111111111111111, user.email)
        if user is not None:
            login(request, user)
            return HttpResponse("<h1> Logged in </h1>")
        else:
            return HttpResponse("<h1> You may have written wrong username and password </h1>")
    elif request.method == "GET":
        form = AuthenticationForm()
    return render(request, 'registerlogin/login.html', context={"form": form})


def logout_user(request):
    logout(request)
    return redirect('register')
