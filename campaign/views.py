from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from .models import CampaignData

# Create your views here.

@csrf_exempt
def campaign(request):
    if request.method == "POST":
        try:
            lang_type = request.POST.get("lang_type")
            campaign_type = request.POST.get("campaign_type")
            time = date.today()
            before = "01-01-1000"
            after = "31-12-2099"
            print time
            response_json={}
            response_array=[]
            if lang_type == 0:
                try:
                    if campaign_type==0:
                        print "here"
                        obj = CampaignData.objects.filter(date__range=[before,time])
                        try:
                            for x in obj:
                                temp_json={}
                                print x.date

                                temp_json['id']= x.id
                                temp_json['name']=x.name_english
                                temp_json['date']=str(x.date)
                                temp_json['description']=x.description_english
                                temp_json['image']= request.scheme + '://' + request.get_host() + '/media/'+str(x.image)

                                response_array.append(temp_json)

                                response_json['campaign_list']=response_array
                                response_json['success'] = True
                                response_json['message'] = "List found"

                        except Exception as e:
                            response_json['success']=False
                            response_json['message']="List not found"

                    elif campaign_type == 1:
                        print "here"
                        obj = CampaignData.objects.filter(date__range=[time, after])
                        try:
                            for x in obj:
                                temp_json = {}
                                print x.date

                                temp_json['id'] = x.id
                                temp_json['name'] = x.name_english
                                temp_json['date'] = str(x.date)
                                temp_json['description'] = x.description_english
                                temp_json['image'] = request.scheme + '://' + request.get_host() + '/media/'+str(x.image)

                                response_array.append(temp_json)

                                response_json['campaign_list'] = response_array
                                response_json['success'] = True
                                response_json['message'] = "List found"

                        except Exception as e:
                            response_json['success'] = False
                            response_json['message'] = "List not found"

                except Exception as e:
                    response_json['success'] = False
                    response_json['message'] = "campaign type incorrect"



            if lang_type == 1:
                try:
                    if campaign_type == 0:
                        print "here"
                        obj = CampaignData.objects.filter(date__range=[before, time])
                        try:
                            for x in obj:
                                temp_json = {}
                                print x.date

                                temp_json['id'] = x.id
                                temp_json['name'] = x.name_hindi
                                temp_json['date'] = x.date
                                temp_json['description'] = x.description_hindi
                                temp_json['image'] = request.scheme + '://' + request.get_host() + '/media/'+str(x.image)

                                response_array.append(temp_json)

                                response_json['campaign_list'] = response_array
                                response_json['success'] = True
                                response_json['message'] = "List found"

                        except Exception as e:
                            response_json['success'] = False
                            response_json['message'] = "List not found"

                    elif campaign_type == 1:
                        print "here"
                        obj = CampaignData.objects.filter(date__range=[time, after])
                        try:
                            for x in obj:
                                temp_json = {}
                                print x.date

                                temp_json['id'] = x.id
                                temp_json['name'] = x.name_hindi
                                temp_json['date'] = x.date
                                temp_json['description'] = x.description_hindi
                                temp_json['image'] = request.scheme + '://' + request.get_host() + '/media/'+str(x.image)

                                response_array.append(temp_json)

                                response_json['campaign_list'] = response_array
                                response_json['success'] = True
                                response_json['message'] = "List found"

                        except Exception as e:
                            response_json['success'] = False
                            response_json['message'] = "List not found"

                except Exception as e:
                    response_json['success'] = False
                    response_json['message'] = "campaign type incorrect"

        except Exception as e:
            response_json['success'] = False
            response_json['message'] = "language type incorrect"

        print response_json
        return JsonResponse(response_json)





