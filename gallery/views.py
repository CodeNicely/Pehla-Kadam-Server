from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ImageData,VideoData
# Create your views here.


@csrf_exempt
def gallery_image(request):
    response_json = {}
    if request.method == "GET":
        lang_type = request.POST.get("lang_type")
        try:
            image_list = ImageData.objects.all()
            response_array=[]

            try:
                for x in image_list:
                    temp_json={}
                    temp_json['id']= x.id
                    temp_json['image']=x.image

                    if lang_type==0:
                        temp_json['caption']=x.caption_english
                    elif lang_type==1:
                        temp_json['caption'] = x.caption_hindi

                    response_array.append(temp_json)
                response_json['image_list']=response_array
                response_json['success']=True
                response_json['message']="List created"
            except Exception as e:
                response_json['success'] = False
                response_json['message'] = "List not created"
        except Exception as e:
            response_json['success'] = False
            response_json['message'] = "ImageData not found"

    return JsonResponse(response_json)


@csrf_exempt
def gallery_video(request):
    if request.method == "GET":
        lang_type = request.POST.get("lang_type")
        try:
            image_list = VideoData.objects.all()
            response_array = []
            response_json = {}
            try:
                for x in image_list:
                    temp_json = {}
                    temp_json['id'] = x.id
                    temp_json['image'] = x.video

                    if lang_type == 0:
                        temp_json['caption'] = x.caption_english
                    elif lang_type == 1:
                        temp_json['caption'] = x.caption_hindi

                    response_array.append(temp_json)

                response_json['image_list'] = response_array
                response_json['success'] = True
                response_json['message'] = "List created"
            except Exception as e:
                response_json['success'] = False
                response_json['message'] = "List not created"
        except Exception as e:
            response_json['success'] = False
            response_json['message'] = "VideoData not found"

    return JsonResponse(response_json)


