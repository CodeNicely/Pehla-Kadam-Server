

from __future__ import print_function
from django.http import JsonResponse

from .models import *
from django.http import JsonResponse

from .models import *
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect,HttpResponse
import requests

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from login.models import UserData
import jwt
from splash_screen.views import KeysData

	
@csrf_exempt
def join_us(request):
	if request.method == 'GET':
		response_json = {}
		try:
			access_token = request.GET.get('access_token')
			desc = request.GET.get('description')
			email = request.GET.get('email')
			
			print(desc,email,access_token)
		
			if access_token is not None :
				json = jwt.decode(str(access_token), str(KeysData.objects.get(key='jwt').value), algorithms=['HS256'])
				mobile = str(json['mobile'])
				user_row = UserData.objects.get(mobile = mobile)
				
				setattr(user_row,'email',email)
				user_row.save()
				JoinUsData.objects.create(user_data=user_row,description=desc,visibility=True)
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

@csrf_exempt
def joinus_visibility(request):
	response_json = {}
	if request.method == 'POST' :
		try:
			join_id = request.POST.get('id')
			feed = JoinUsData.objects.get(id=join_id)
			setattr(feed,'visibility',False)
			feed.save()
			response_json['success'] = True
			response_json['message'] = 'Successful'
			print('aman')
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


@csrf_exempt
def joinus_list(request):
	response_json = {}
	if request.method =='POST':
		try :
			joinlist = JoinUsData.objects.filter(visibility=True)
			print('1.2')
			response_json['list'] = joinlist
			print('1.3')
			response_json['success'] = True
			print('1.4')
			template = get_template("joinus_item.html")
			print('1.5')
			context = Context(response_json)
			html = template.render(context)
			return HttpResponse(html)
		except Exception as e:
			print('2.2')
			template = get_template("error.html")
			context = Context(response_json)
			html = template.render(context)
			return HttpResponse(html)
	else:
		print('3.2')
		template = get_template("error.html")
		context = Context(response_json)
		html = template.render(context)
		return HttpResponse(html)


