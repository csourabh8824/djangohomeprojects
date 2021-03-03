from django.shortcuts import render
import io
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body  # body contains json data name,roll,city
        print("request.body", request.body)
        stream = io.BytesIO(json_data)  # converting json data to byte stream
        python_data = JSONParser().parse(stream)  # converting byte to python dict data
        serializer = StudentSerializer(data=python_data)
        # serializer converting python dict data into complex data type i.e model object
        if serializer.is_valid():
            serializer.save()
            # now returning back the response(python dict):
            response = {'msg': 'Data Inserted!'}
            json_data = JSONRenderer().render(response)  # converting python dict to json
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
