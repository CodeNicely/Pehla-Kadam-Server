
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
				
				about_us=  AboutUsData.objects.all()
				about_team_list= AboutTheTeam.objects.all()
				print('2')
				
				response_json['introduction']= about_us.introduction_english
				response_json['vision'] = about_us.vision_english
				response_json['achievements'] = about_us.achievements_english
				response_json['image'] = request.scheme + '://' + request.get_host() + '/media/' + str(o.image)
				

				team_array=[]
				for x in about_team_list:
					temp_json={}
					temp_json['image']=request.scheme + '://' + request.get_host() + '/media/' + str(x.image)
					temp_json['name']=x.name_english
					temp_json['email']=x.email
					temp_json['mobile']=x.mobile
					team_array.append(temp_json)

				response_json['about_us_list']=team_array
				response_json['success'] = True
				response_json['message'] = 'Successful'
				
			if lang == '1':

				print("hindi")
				about_us=  AboutUsData.objects.all()
				about_team_list= AboutTheTeam.objects.all()

				response_json['introduction']= about_us.introduction_hindi
				response_json['vision'] = about_us.vision_hindi
				response_json['achievements'] = about_us.achievements_hindi
				response_json['image'] = request.scheme + '://' + request.get_host() + '/media/' + str(x.image)
				

				team_array=[]
				for x in about_team_list:
					temp_json={}
					temp_json['image']=request.scheme + '://' + request.get_host() + '/media/' + str(x.image)
					temp_json['name']=x.name_hindi
					temp_json['email']=x.email
					temp_json['mobile']=x.mobile
					team_array.append(temp_json)

				response_json['about_us_list']=team_array
				response_json['success'] = True
				response_json['message'] = 'Successful'
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
