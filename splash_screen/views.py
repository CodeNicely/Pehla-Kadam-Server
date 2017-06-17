from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from .models import *
from __future__ import print_function


def splash_screen(request):
    response_json = {}
    if request.method == 'GET':
        try:
          
            version = int(KeysData.objects.get(key='version').value)
            print ('a2')
            compulsory_update = KeysData.objects.get(key='compulsory_update').value
            print ('a5')
            response_json['version'] = version
            print ('a3')
            if int(compulsory_update) == 1:
                response_json['compulsory_update'] = True
                print ('a4')
            if int(compulsory_update) == 0:
                response_json['compulsory_update'] = False
                print ('a5')
        except Exception as e:
            print("Exception Error", str(e))
            response_json['success'] = False
            response_json['message'] = "Something went Wrong"
    else:
        response_json['success'] = False
        response_json['message'] = "Not get method"
    print(response_json)
    return JsonResponse(response_json)

