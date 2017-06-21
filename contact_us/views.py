

from __future__ import print_function
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from .models import *

from django.views.decorators.csrf import csrf_exempt
from splash_screen.models import ImageData
	
@csrf_exempt
def contact_us(request):
	if request.method == 'GET':
		try:
			lang = request.GET.get('lang_type')
			response_json = {}
			if(lang == '0'):
				
				o =  ContactUsData.objects.first()
				response_json['facebook'] = o.facebook
				response_json['address'] = o.address_english
				response_json['email'] = o.email
				response_json['mobile'] = o.mobile
				print('a')	
				image_link = ImageData.objects.get(key='contact_us').image
				image = request.scheme + '://' + request.get_host() + '/media/' + str(image_link)
				print('b')	
				response_json['image'] = image
				response_json['success'] = True
				response_json['message'] = 'Successful'
				
			if(lang == '1'):
				
				o =  ContactUsData.objects.first()
				response_json['facebook'] = o.facebook
				response_json['address'] = o.address_hindi
				response_json['email'] = o.email
				response_json['mobile'] = o.mobile
			
				image_link = ImageData.objects.get(key='contact_us').image
				image = request.scheme + '://' + request.get_host() + '/media/' + str(o.image_link)
				response_json['image'] = image
				response_json['success'] = True
				response_json['message'] = 'Successful'
				response_json['contact_us_list'] = response_json_list
				
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
