from django.shortcuts import render, HttpResponse, JSONResponse
from .models import students
from .serializers import studentsserializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

# model


def students_detail(request):
    stu = students.objects.all()
    serializer = studentsserializer(stu, many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")
    # return JSONResponse(serializer.data)


def students_details(request, pk):
    stu = students.objects.get(id=pk)
    serializer = studentsserializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")
