from django.shortcuts import render

from django.http import JsonResponse

from .models import *
from __future__ import print_function
from django.views.decorators.csrf import csrf_exempt
from splash_screen.models import ImageData
	
@csrf_exempt
def about_us(request):
	if request.method == 'GET':
		try:
			lang = request.GET.get('lang_type')
			response_json = {}
			if(lang == '0'):
				detail_list = []
				about_us_list =  AboutUsData.objects.all()
				for o in about_us_list:
					detail={ }
					detail['title']= o.title_english
					detail['description'] = o.description_english
					detail_list.append(detail)
				image_link = ImageData.objects.get(key='about_us').image
				image = request.scheme + '://' + request.get_host() + '/media/' + str(o.image_link)
				response_json['image'] = image
				response_json['success'] = True
				response_json['message'] = 'Successful'
				response_json['about_us_list'] = detail_list
			if(lang == '1'):
				detail_list = []
				about_us_list =  AboutUsData.objects.all()
				for o in about_us_list:
					detail={ }
					detail['title']= o.title_hindi
					detail['description'] = o.description_hindi
					detail_list.append(detail)
				image_link = ImageData.objects.get(key='about_us').image
				image = request.scheme + '://' + request.get_host() + '/media/' + str(o.image_link)
				response_json['image'] = image
				response_json['success'] = True
				response_json['message'] = 'Successful'
				response_json['about_us_list'] = detail_list
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