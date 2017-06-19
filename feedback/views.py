
from __future__ import print_function
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from .models import *

from django.views.decorators.csrf import csrf_exempt
from login.models import UserData

	
@csrf_exempt
def feedback(request):
	if request.method == 'GET':
		response_json = {}
		try:
			access_token = request.GET.get('access_token')
			feedback_receive = request.GET.get('feedback')
			if access_token is not None :
				json = jwt.decode(str(access_token), str(KeysData.objects.get(key='jwt').value), algorithms=['HS256'])
				mobile = str(json['mobile'])
				user_row = UserData.objects.get(mobile= mobile)
				feedback_create = FeedbackData.object.create(name=user_row.name,mobile=user_row.mobile,ward=user_row.ward,feedback=feedback_receive)
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