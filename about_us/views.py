
from __future__ import print_function
from django.shortcuts import render

from django.http import JsonResponse

from .models import *

from django.views.decorators.csrf import csrf_exempt
from splash_screen.models import ImageData
	
@csrf_exempt
def about_us(request):
	if request.method == 'GET':
		try:
			print('1')
			lang = request.GET.get('lang_type')
			response_json = {}
			if lang == '0':
				detail_list = []
				about_us_list =  AboutUsData.objects.all()
				print('2')
				for o in about_us_list:
					detail={ }
					detail['title']= o.title_english
					detail['description'] = o.description_english
					detail['image'] = request.scheme + '://' + request.get_host() + '/media/' + str(o.image)
					detail_list.append(detail)
				image_link = ImageData.objects.get(key='about_us').image
				image = request.scheme + '://' + request.get_host() + '/media/' + str(image_link)
				response_json['image'] = image
				response_json['success'] = True
				response_json['message'] = 'Successful'
				response_json['about_us_list'] = detail_list
			if lang == '1':
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

def developer(request):
    response_body = {}
    company_data = {}
    response_body['success'] = True
    response_body['message'] = "Successful"
    company_data['company'] = "CodeNicely"
    company_data['address'] = "Raipur , Chhattisgarh"
    company_data['email'] = "codenicely@gmail.com"
    company_data['facebook'] = "http://www.facebook.com/CodeNicely"
    company_data['contact'] = "+91 8109109457"
    company_data[
        'about'] = "We Code StartUps \n\n CodeNicely is a Raipur based Startup.\n We provide all types of IT " \
                   "Solutions. We are a team of some geeky geeks from NIT Raipur and we Love Coding. "
    company_data[
        'companyImage'] = request.scheme + '://' + request.get_host() + "/media/developers/codenicely_full_logo.png"
    company_data['website'] = "http://www.codenicely.in"
    response_body['developer_data'] = company_data
    return JsonResponse(response_body)
