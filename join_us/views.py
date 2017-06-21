
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
				JoinUsData.objects.create(name=user_row.name,mobile=user_row.mobile,ward=user_row.ward,description=desc,visibility=True)
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
			join_id = request.POST.get('joinus_id')
			feed = JoinUsbackData.objects.get(id=join_id)
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
def joinus_list(request):
	response_json = {}
	if request.method =='GET':
		try :
			joinlist = JoinUsData.objects.filter(visibility=True)
			response_json['list'] = joinlist
			response_json['success'] = True
			template = get_template("joinusitem.html")
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


