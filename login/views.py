from __future__ import print_function
from __future__ import print_function
from django.shortcuts import render

from random import randint
from django.shortcuts import render

import jwt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from splash_screen.models import KeysData
from sms import send_sms1
from welcome.views import WardData

from .models import *


@csrf_exempt
def login(request):
	response_json = {}
	if request.method == 'GET':
		for x, y in request.GET.items():
			print("key,value", x, ":", y)
		otp = randint(100000, 999999)
		mobile = str(request.GET.get("mobile"))
		message = "OTP for the App is " + str(otp)
		send_sms1(mobile, message)
		response_json['success'] = True
		otp_row, created = OtpData.objects.get_or_create(mobile=mobile)
		setattr(otp_row, 'otp', int(otp))
		setattr(otp_row, 'flag', False)
		otp_row.save()
		response_json['message'] = 'Otp Sent'
	if request.method == 'POST':
		print('aa')
		for x, y in request.POST.items():
			print ("key,value", x, ":", y)
		mobile = str(request.POST.get("mobile"))
		name = str(request.POST.get("name"))
		ward = str(request.POST.get("ward"))
		otp = str(request.POST.get("otp"))
		print('aman1')
		print(mobile,otp,ward,name)
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



@csrf_exempt
def profile(request):
	response_json = {}
	if request.method == 'GET':
		for x, y in request.GET.items():
			print("key,value", x, ":", y)
		try:
			access_token1 = request.GET.get('access_token')
			lang_type = request.GET.get('lang_type')
			access_token = str(access_token1)
			json = jwt.decode(str(access_token), str(KeysData.objects.get(key='jwt').value), algorithms=['HS256'])
			mobile = str(json['mobile'])
			user_row = UserData.objects.get(mobile= mobile)
			response_json['name'] = user_row.name
			response_json['mobile'] = user_row.mobile
			response_json['ward'] = user_row.ward
			response_json['image'] = request.scheme + '://' + request.get_host() + '/media/' + str(user_row.image)
			if lang_type == '1' :
				for s in WardData.objects.all():
					ward_details = {'id': int(s.id),
					'name': str(s.ward_name_hindi)
					}
					ward_list.append(ward_details)
				response_json['ward_list'] = ward_list
			if lang_type == '0':
				for s in WardData.objects.all():
					ward_details = {'id': int(s.id),
					'name': str(o.ward_name_hindi)
					}
					ward_list.append(ward_details)
				response_json['ward_list'] = ward_list
			response_json['success'] = True
			response_json['mesage'] ="Successful"
		except Exception as e :
			print(str(e))
			response_json['success'] = False
			response_json['message'] = str(e)
	print(str(response_json))
	return JsonResponse(response_json)

	if request.method == 'POST':
		for x, y in request.POST.items():
			print("key,value", x, ":", y)
		try:
			access_token1 = request.GET.get('access_token')
			name = request.GET.get('name')
			ward = request.GET.get('ward')
			

			access_token = str(access_token1)
			json = jwt.decode(str(access_token), str(KeysData.objects.get(key='jwt').value), algorithms=['HS256'])
			mobile = str(json['mobile'])
			user_row = UserData.objects.get(mobile= mobile)
			setattr(user_row,'name',name)
			setattr(user_row,'ward',ward)
			user_row.save()
			try:
				print("inside try")
				image = request.FILES.get('image').name
				
				folder = 'media/' + '/profile/'
				print("folder")
				full_filename = os.path.join(folder, image)
				print("full name", full_filename)
				print("image=", image)
				fout = open(folder + image, 'w')
				print("below fout")
				file_content = request.FILES.get('image').read()
				print("below file content")
				fout.write(file_content)
				
				fout.close()
				
			except Exception as e:
				image = 'image'
				print(e)
		except Exception as e :
			print(str(e))
			response_json['success'] = False
			response_json['message'] = str(e)
	print(str(response_json))
	return JsonResponse(response_json)

