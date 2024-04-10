from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        # print(json_data)
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'} 
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_error = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_error, content_type='application/json')

