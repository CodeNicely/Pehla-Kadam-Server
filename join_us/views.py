
from django.http import JsonResponse

from .models import *

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from login.models import UserData

	
@csrf_exempt
def join_us(request):
	if request.method == 'GET':
		response_json = {}
		try:
			access_token = request.GET.get('lang_type')
			desc = request.GET.get('description')
		
			if access_token is not None :
				json = jwt.decode(str(access_token), str(KeysData.objects.get(key='jwt').value), algorithms=['HS256'])
				mobile = str(json['mobile'])
				user_row = UserData.objects.get(mobile = mobile)
				JoinUsData.objects.create(name=user_row.name,mobile=user_row.mobile,ward=user_row.ward,description=desc)
				response_json['success'] = True
				response_json['message'] = 'Successful'
			else:
				response_json['success'] = False
				response_json['message'] = 'access token not exist'
		except Exception as e:
			print(e)
			response_json['success'] = False
			response_json['message'] = str(e)
	else:
		response_json['success'] = False
		response_json['message'] = "Wrong request"
		print('wrong request')
	print(str(response_json))
	return JsonResponse(response_json)


