import jwt
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import StoryData
from login.models import UserData

# Create your views here.

@csrf_exempt
def stories(request):
    response_json={}

    lang_type = request.POST.get("lang_type")

    if request.method == "GET":
        try:
            access_token = request.GET.get('access_token')
            json = jwt.decode(str(access_token), '810810', algorithms=['HS256'])

            response_array=[]

            try:
                story_list = StoryData.objects.all()
                for x in story_list:
                    temp_json={}
                    user = UserData.objects.get(id=x.user_id)
                    temp_json['user_id'] = user.id
                    temp_json['user_image']=user.image
                    temp_json['date']=x.date
                    temp_json['time']=x.time
                    temp_json['likes']=x.likes
                    temp_json['shares']=x.shares

            except Exception as e:
                print e

        except Exception as e:
            print e










