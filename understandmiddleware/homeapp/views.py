from django.shortcuts import render

# Create your views here.


def home(request):
    print("i am view")
    return render(request, 'homeapp/middlewareconcept.html')
