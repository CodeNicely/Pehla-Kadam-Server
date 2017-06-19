

from __future__ import print_function
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from .models import *
from django.views.decorators.csrf import csrf_exempt
from login.models import UserData
import jwt
@csrf_exempt
def splash_screen(request):
	response_json = {}
	if request.method == 'GET':
		try:
			access_token1 = request.GET.get('access_token')
			access_token = str(access_token1)
			fcm = request.GET.get('fcm')
			print('aaaa')
			print(fcm)
			print(access_token)
			if access_token == '1' :
				print('b')
				p,created = FcmData.objects.get_or_create(fcm=fcm)
				print ('aman---------')
				if created:
					response_json['message'] = "fcm added"
				if not created:
					response_json['message'] = "fcm already exsists"
			else :
            	
				json = jwt.decode(str(access_token), str(KeysData.objects.get(key='jwt').value), algorithms=['HS256'])
				mobile = str(json['mobile'])
				user_row = UserData.objects.get(mobile= mobile)
				setattr(user_row,'fcm',fcm)
				user_row.save()
				response_json['message'] = 'fcm linked to user'

			version = int(KeysData.objects.get(key='version').value)
			print(version)
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
			response_json['success'] = True
		except Exception as e:
			print("Exception Error", str(e))
			response_json['success'] = False
			response_json['message'] = "Something went Wrong"
	else:
		response_json['success'] = False
		response_json['message'] = "Not get method"
	print(response_json)
	return JsonResponse(response_json)

