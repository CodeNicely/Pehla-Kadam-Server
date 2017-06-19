

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
				detail_list = []
				contact_us_list =  ContactUsData.objects.all()
				for o in contact_us_list:
					detail = { }
					detail['name'] = o.name_english
					detail['address'] = o.address_english
					detail['email'] = o.email
					detail['mobile'] = o.mobile
					detail_list.append(detail)
				# image_link = ImageData.objects.get(key='about_us').image
				# image = request.scheme + '://' + request.get_host() + '/media/' + str(o.image_link)
				# response_json['image'] = image
				response_json['success'] = True
				response_json['message'] = 'Successful'
				response_json['contact_us_list'] = detail_list
			if(lang == '1'):
				detail_list = []
				contact_us_list =  ContactUsData.objects.all()
				for o in contact_us_list:
					detail = { }
					detail['name'] = o.name_hindi
					detail['address'] = o.address_hindi
					detail['email'] = o.email
					detail['mobile'] = o.mobile
					detail_list.append(detail)
				# image_link = ImageData.objects.get(key='about_us').image
				# image = request.scheme + '://' + request.get_host() + '/media/' + str(o.image_link)
				# response_json['image'] = image
				response_json['success'] = True
				response_json['message'] = 'Successful'
				response_json['contact_us_list'] = detail_list
				
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
