from django.shortcuts import render
from .models import Student
from .serilaizers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.


# view function for single complex data type
def student_detail(request, pk):
    """
    This function tells us how we can serialize single model object(complex data) i.e single row of a database table.
    In this function first we'll grab single model object then we'll convert it into python native data 
    type using our serializer class. And then convert python_data to json_data using JSONRenderer()
    and then finally we'll return a http response.  
    """
    stu = Student.objects.get(
        id=pk)      # stu is a complex single model object (complex data type).
    print("type of stu:complex data type", type(stu))
    serializer = StudentSerializer(stu)
    """ StudentSerializer is a class that we have created in serializers.py .This serializer class converts
    complex model data type to python native data type for example dict,list etc.. 
    So finally we have python data in serializer variable
    Now we will convert it into json_data in next step and then return httpresponse
    """
    print("python dictionary data",
          serializer.data)  # serializer.data displays python data
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data,safe = True)  #safe = True when we will dict in response
    # line no 28 and 29 can be replaced by 30 if we want to use shortcut


# this view function is for queryset complex data type
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # many =True says that it's a queryset more then one data
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serializer.data, safe=False)
    # safe is false if we will get data type other then dict
    # line no 39 and 40 can be replaced by 41 if we want to use shortcut
