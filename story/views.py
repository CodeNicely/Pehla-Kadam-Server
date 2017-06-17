
import os

import jwt
from django.views.decorators.csrf import csrf_exempt
from .models import StoryData, UserLikeData
from login.models import UserData

# Create your views here.

@csrf_exempt

def stories(request):

    response_json = {}

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
                    obj = UserData.objects.get(id=x.user_id)
                    temp_json['user_id'] = obj.id
                    temp_json['user_name']=obj.name
                    temp_json['user_image']= request.scheme + '://' + request.get_host() + '/media/shop/' + str(obj.image)

                    temp_json['date']=x.date
                    temp_json['time']=x.time
                    temp_json['likes']=x.likes
                    temp_json['shares']=x.shares
                    o = UserLikeData.objects.get(user_id = x.user_id, story_id = x.id )
                    if o.liked == True:
                        temp_json['mylike'] = True
                    if o.liked == False:
                        temp_json['mylike'] = False
                    if o.shared == True:
                        temp_json['myshare'] = True
                    if o.shared == False:
                        temp_json['myshare'] = False

                    response_array.append(temp_json)

                    response_json['story_list']= response_array
                    response_json['success']=True
                    response_json['message']="Story list created"

            except Exception as e:
                response_json['success'] = False
                response_json['message'] = "Story list not created"

        except Exception as e:
            response_json['success'] = False
            response_json['message'] = "Error"

    if request.method == "POST" :
        lang_type = request.POST.get("lang_type")

        try:
            access_token = request.GET.get('access_token')
            json = jwt.decode(str(access_token), '810810', algorithms=['HS256'])

            user = UserData.objects.get(mobile=int(json))



            try:
                title= request.POST.get("title")
                description=request.POST.get("description")

                try:
                    print "inside try"
                    image = request.FILES.get('image').name
                    print image
                    folder = 'media/' + '/story_image/'
                    print "folder"
                    full_filename = os.path.join(folder, image)
                    print("full name", full_filename)
                    print("image=", image)
                    fout = open(folder + image, 'w')
                    print "below fout"
                    file_content = request.FILES.get('company_logo').read()
                    print "below file content"
                    fout.write(file_content)
                    print "below write"
                    fout.close()
                    print "Done"
                except Exception as e:
                    image = 'image'
                    print(e)

                try:
                    if lang_type == 0:
                        StoryData.objects.create(

                            user_id=user.id,
                            image=image,
                            title_english=str(title),
                            description_english=str(description),
                        )

                    elif lang_type == 1:
                        StoryData.objects.create(

                            user_id=user.id,
                            image=image,
                            title_hindi=str(title),
                            description_hindi=str(description),
                        )

                    response_json['success'] = True
                    response_json['message'] = "Story created"
                except Exception as e:
                    response_json['success'] = False
                    response_json['message'] = "Story not created"
            except Exception as e:
                response_json['success'] = False
                response_json['message'] = "Details not received"
        except Exception as e:
            response_json['success'] = False
            response_json['message'] = "Access token not received"



@csrf_exempt
def like(request):

    response_json={}
    if request.method =="POST":
        access_token = request.GET.get('access_token')
        json = jwt.decode(str(access_token), '810810', algorithms=['HS256'])
        story_id = request.POST.get("story_id")

        try:
            user = UserData.objects.get(mobile=int(json))
            story = StoryData.objects.get(user_id=user)
            l = int(story.likes)

            try:
                obj = UserLikeData.objects.get(user_id=user,story_id=story)
                if obj.liked == True:
                    obj.liked=False
                elif obj.liked == False:
                    obj.liked=True

                obj.save()

                story.likes= l+1
                story.save()

                response_json['success']=True
                response_json['message']="status updated"
            except Exception as e:
                UserLikeData.objects.create(

                    user_id = user,
                    story_id=story,
                    liked=True

                )
                response_json['success'] = True
                response_json['message'] = "new status created"

        except Exception as e:
            response_json['success'] = False
            response_json['message'] = "Credentials not found"



@csrf_exempt
def share(request):

    response_json={}
    if request.method =="POST":
        access_token = request.GET.get('access_token')
        json = jwt.decode(str(access_token), '810810', algorithms=['HS256'])
        story_id = request.POST.get("story_id")

        try:
            user = UserData.objects.get(mobile=int(json))
            story = StoryData.objects.get(user_id=user)
            s = int(story.shares)

            try:
                obj = UserLikeData.objects.get(user_id=user,story_id=story)
                if obj.shared == True:
                    obj.shared=False
                elif obj.shared == False:
                    obj.shared=True

                obj.save()

                story.shares= s+1
                story.save()

                response_json['success']=True
                response_json['message']="status updated"
            except Exception as e:
                UserLikeData.objects.create(

                    user_id = user,
                    story_id=story,
                    shared=True

                )
                response_json['success'] = True
                response_json['message'] = "new status created"

        except Exception as e:
            response_json['success'] = False
            response_json['message'] = "Credentials not found"




