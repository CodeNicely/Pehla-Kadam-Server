from __future__ import print_function
from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

@csrf_exempt
def welcome(request):
	response_json = {}
	if request.method == 'GET':
		for x, y in request.GET.items():
			print("key,value ", x, ":", y)

		slider_list = []
		ward_list = []
		try:
			lang = request.GET.get('lang_type')


			if lang == '0':
				for o in WelcomeData.objects.all():
					welcome_details = {'id': str(o.id),
					'image': request.scheme + '://' + request.get_host() + '/media/' + str(o.image),
					'quote': str(o.quote_english)
					}
					slider_list.append(welcome_details)
				response_json['success'] = True
				response_json['message'] = 'Successful'
				response_json['welcome_page'] = slider_list
				for s in WardData.objects.all():
					ward_details = {'id': int(s.id),
					'name': str(s.ward_name_english)

					}
					ward_list.append(ward_details)
				response_json['ward_list'] = ward_list
			if lang == '1':
				for o in WelcomeData.objects.all():
					welcome_details = {'id': str(o.id),
					'image': request.scheme + '://' + request.get_host() + '/media/' + str(o.image),
					'quote': str(o.quote_hindi)
					}
					slider_list.append(welcome_details)
				response_json['success'] = True
				response_json['message'] = 'Successful'
				response_json['welcome_page'] = slider_list
				for s in WardData.objects.all():
					ward_details = {'id': int(s.id),
					'name': str(o.ward_name_hindi)

					}
					ward_list.append(ward_details)
				response_json['ward_list'] = ward_list
		except Exception(e):
			print(e)
			response_json['success'] = False
			response_json['message'] = str(e)


	else:
		response_json['success'] = False
		response_json['message'] = "not get method"
	print(response_json)
	return JsonResponse(response_json)
