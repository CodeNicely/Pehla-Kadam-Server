import json
from django.template import Context
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.
from story.models import StoryData
from django.template.loader import get_template

@csrf_exempt
def home_stories(request):

    response_json={}
    data=''
    if request.method=="POST":
        
        try:
            story_list = StoryData.objects.filter(approve=False)
            response_array=[]
            try:
                for story in story_list:
                    # temp_json={}
                    # temp_json['image']=story.image
                    # temp_json['title']=story.title
                    # temp_json['description']=story.description
                    print story.image

                    response_array.append(story)

                response_json['story_list']=response_array
                response_json['success']=True
                response_json['message']="Story list created"

            except Exception as e:
                print e
                response_json['success'] = False
                response_json['message'] = "Story list not created"
        except Exception as e:
            print e
            response_json['success'] = False
            response_json['message'] = "Story list not created"

        if response_json['success'] == True:
            template = get_template("storycards.html")
            context = Context(
                response_json)  # response_json is the context data that is sent to the html file to render the output.
            html = template.render(context)
            print response_json
            return HttpResponse(html)
        else:
            template = get_template("error.html")
            context = Context(response_json)
            html = template.render(context)
            print response_json
            return HttpResponse(html)


    if request.method=="GET":
        return render(request,"home.html")



@csrf_exempt
def home_feedback(request):

    print "feeeeeeeee"

    return render(request,"home.html")


@csrf_exempt
def home_joinus(request):

    print "jooooooooooooooo"
    return render(request,"storycards.html")

