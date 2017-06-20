
import os

import jwt
from django.views.decorators.csrf import csrf_exempt
from .models import StoryData, UserLikeData,UserShareData
from login.models import UserData
from datetime import date,timedelta
from django.http import JsonResponse
# Create your views here.

@csrf_exempt

def stories(request):

    response_json = {}

    
    if request.method == "GET":
        try:
            print '1'
            # access_token = request.GET.get('access_token')
            # print access_token
            # json = jwt.decode(str(access_token), '810810', algorithms=['HS256'])
            # mobile = str(json['mobile'])

            today = date.today()
            print 'today',today
            yesterday = today - timedelta(days=1)
            print yesterday
            response_array=[]

            try:
                print '2'
                story_list = StoryData.objects.filter(approve=True)
                for x in story_list:
                    print 'xtime',x.time
                    print 'xtimehour',x.time.hour
                    print 'xtimehour',x.time.minute
                    print str(x.time.hour) + ':'+str(x.time.minute)

                    temp_json={}
                    temp_json['description'] = x.description
                    temp_json['title'] = x.title
                    temp_json['story_id'] = x.id
                    temp_json['image'] =  request.scheme + '://' + request.get_host() + '/media/' + str(x.image)
                    obj = UserData.objects.get(id=x.user_id)
                    temp_json['user_id'] = obj.id
                    temp_json['user_name']=obj.name
                    temp_json['user_image']= request.scheme + '://' + request.get_host() + '/media/' + str(obj.image)
                    print 'xdate',x.date
                    if str(x.date) == str(today) :
                        print "today success"
                        temp_json['date']="Today"
                    elif str(x.date) == str(yesterday) :
                        temp_json['date']="Yesterday"
                    else:
                        print '3'
                        temp_json['date']=str(x.date)
                    temp_json['time']= str(x.time.hour) + ':'+str(x.time.minute)
                    temp_json['likes']=x.likes
                    temp_json['shares']=x.shares
                    print '4'
                    try:
                        o = UserLikeData.objects.get(user_id = x.user_id, story_id = x.id )
                        print '5'
                        if o.liked == True:
                            temp_json['liked'] = True
                        if o.liked == False:
                            temp_json['liked'] = False
                    except:
                            temp_json['liked'] = False
                    try:
                        q = UserShareData.objects.get(user_id = x.user_id, story_id = x.id)
                        if q.shared == True:
                            temp_json['shared'] = True
                        if q.shared == False:
                            temp_json['shared'] = False
                    except:
                            temp_json['shared'] = False
                    
                    response_array.append(temp_json)

                    response_json['stories_list']= response_array
                    response_json['success']=True
                    response_json['message']="Story list created"

            except Exception as e:
                print str(e)
                response_json['success'] = False
                response_json['message'] = "Story list not created"

        except Exception as e:
            response_json['success'] = False
            response_json['message'] = "Error"

    print str(response_json)
    return JsonResponse(response_json)

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
                    
                    StoryData.objects.create(

                        user_id=user.id,
                        image=image,
                        title=str(title),
                        description=str(description),
                        approve=False,
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

    print str(response_json)
    return JsonResponse(response_json)



@csrf_exempt
def like(request):

    response_json={}
    if request.method =="POST":
        access_token = request.GET.get('access_token')
        json = jwt.decode(str(access_token), '810810', algorithms=['HS256'])
        mobile = str(json['mobile'])
        story_id = request.POST.get("story_id")

        try:
            user = UserData.objects.get(mobile=mobile)
            story = StoryData.objects.get(id=story_id)
            l = int(story.likes)

            try:
                obj = UserLikeData.objects.get(user_id=user,story_id=story.id)
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
                story.likes= l+1
                story.save()
                response_json['success'] = True
                response_json['message'] = "new status created"

        except Exception as e:
            response_json['success'] = False
            response_json['message'] = "Credentials not found"

    print str(response_json)
    return JsonResponse(response_json)



@csrf_exempt
def share(request):
    response_json={}
    if request.method =="POST":
        access_token = request.GET.get('access_token')
        json = jwt.decode(str(access_token), '810810', algorithms=['HS256'])
        mobile = str(json['mobile'])
        story_id = request.POST.get("story_id")

        try:
            user = UserData.objects.get(mobile=mobile)
            story = StoryData.objects.get(id=story_id)
            l = int(story.likes)

            try:
                obj = UserShareData.objects.get(user_id=user,story_id=story.id)
                if obj.shared == True:
                    obj.shared=False
                elif obj.shared == False:
                    obj.shared=True

                obj.save()

                story.shares= l+1
                story.save()

                response_json['success']=True
                response_json['message']="status updated"
            except Exception as e:
                UserShareData.objects.create(

                    user_id = user,
                    story_id=story,
                    shared=True

                )
                story.shares= l+1
                story.save()
                response_json['success'] = True
                response_json['message'] = "new status created"

        except Exception as e:
            response_json['success'] = False
            response_json['message'] = "Credentials not found"

    print str(response_json)
    return JsonResponse(response_json)


  


