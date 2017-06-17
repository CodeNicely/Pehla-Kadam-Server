from django.shortcuts import render

from __future__ import print_function
from __future__ import print_function

from random import randint

import jwt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from sms import send_sms1

from .models import *


@csrf_exempt
def login(request):
    response_json = {}
    if request.method == 'GET':
        for x, y in request.POST.items():
            print("key,value", x, ":", y)
        otp = randint(100000, 999999)
        mobile = str(request.POST.get("mobile"))
        message = "OTP for the App is " + str(otp)
        send_sms1(mobile, message)
        response_json['success'] = True
        otp_row, created = OtpData.objects.get_or_create(mobile=mobile)
        setattr(otp_row, 'otp', int(otp))
        setattr(otp_row, 'flag', False)
        otp_row.save()
        response_json['message'] = 'Otp Sent'


	if request.method == 'POST':
		for x, y in request.POST.items():
		    print ("key,value", x, ":", y)
		    mobile = str(request.POST.get("mobile"))
		    name = str(request.POST.get("name"))
		    ward = str(request.POST.get("ward"))
		    otp = str(request.POST.get("otp"))
		    print('aman1')
		    print(mobile,otp)
		    otp_list = OtpData.objects.get(mobile=mobile)
		    print(mobile,otp)
		    if otp_list.otp == int(otp):
		        setattr(otp_list, 'flag', True)
		        access_token = jwt.encode({'mobile': str(mobile)}, str(KeysData.objects.get(key='jwt').value),
		                                  algorithm='HS256')
		        otp_list.save()
		        user_row, created = UserData.objects.get_or_create(mobile=mobile)
		        setattr(user_row, 'name', name)
		        setattr(user_row, 'ward',ward)
		        user_row.save()
		        # print ("new_name", user_row.name)
		        response_json['access_token'] = str(access_token)
		        print ('Access Token Created')
		        response_json['success'] = True
		        response_json['message'] = 'Successful'
		    else:
		        response_json['success'] = False
		        response_json['message'] = 'Invalid Otp'
    print(response_json)
    return JsonResponse(response_json)


# @csrf_exempt
# def verify(request):
#     response_json = {}
#     if request.method == 'POST':
#         for x, y in request.POST.items():
#             print ("key,value", x, ":", y)
#             mobile = str(request.POST.get("mobile"))
#             #name = str(request.POST.get("name"))
#             otp = str(request.POST.get("otp"))
#             print('aman1')
#             print(mobile,otp)
#             otp_list = OtpData.objects.get(mobile=mobile)
#             print(mobile,otp)
#             if otp_list.otp == int(otp):
#                 setattr(otp_list, 'flag', True)
#                 access_token = jwt.encode({'mobile': str(mobile)}, str(KeysData.objects.get(key='jwt').value),
#                                           algorithm='HS256')
#                 otp_list.save()
#                 user_row, created = UserData.objects.get_or_create(mobile=mobile)
#                 # setattr(user_row, 'name', name)
#                 user_row.save()
#                 # print ("new_name", user_row.name)
#                 response_json['access_token'] = str(access_token)
#                 print ('Access Token Created')
#                 response_json['success'] = True
#                 response_json['message'] = 'Successful'
#             else:
#                 response_json['success'] = False
#                 response_json['message'] = 'Invalid Otp'
#     else:
#         response_json['success'] = False
#         response_json['message'] = "not post method"

#     print (str(response_json))
#     return JsonResponse(response_json)
