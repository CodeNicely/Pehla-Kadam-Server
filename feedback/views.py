
from __future__ import print_function
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from .models import *
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect,HttpResponse
import requests

from django.views.decorators.csrf import csrf_exempt
from login.models import UserData
import jwt
from splash_screen.models import KeysData

	
@csrf_exempt
def feedback(request):
	response_json = {}
	if request.method == 'GET':
	
		try:
			access_token = request.GET.get('access_token')
			feedback_receive = request.GET.get('feedback')
			if access_token is not None :
				json = jwt.decode(str(access_token), str(KeysData.objects.get(key='jwt').value), algorithms=['HS256'])
				mobile = str(json['mobile'])
				user_row = UserData.objects.get(mobile= mobile)
				feedback_create = FeedbackData.object.create(name=user_row.name,mobile=user_row.mobile,ward=user_row.ward,feedback=feedback_receive,visibility=True)
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
def feedback_visibility(request):
	response_json = {}
	if request.method == 'POST' :
		try:
			feed_id = request.POST.get('feedback_id')
			feed = FeedbackData.objects.get(id=feed_id)
			setattr(feed,'visibility',False)
			feed.save()
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


@csrf_exempt
def feedback_list(request):
	response_json = {}
	if request.method =='GET':
		try :
			feedlist = FeedbackData.objects.filter(visibility=True)
			response_json['list'] = feedlist
			response_json['success'] = True
			template = get_template("feedbackitem.html")
			context = Context(response_json)
			html = template.render(context)
			return HttpResponse(html)
		except Exception as e:
			template = get_template("error.html")
			context = Context(response_json)
			html = template.render(context)
			return HttpResponse(html)
	else:
		template = get_template("error.html")
		context = Context(response_json)
		html = template.render(context)
		return HttpResponse(html)


	