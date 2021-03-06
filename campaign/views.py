from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from datetime import date,timedelta
from django.views.decorators.csrf import csrf_exempt
from .models import CampaignData
from gallery.models import ImageData

# Create your views here.

@csrf_exempt
def campaign(request):
    if request.method == "POST":
        response_json={}
        try:
            print "-----++++++----------"
            lang_type = int(request.POST.get("lang_type"))
            campaign_type = int(request.POST.get("campaign_type"))
            time = date.today()
            before = "1000-01-01"
            after = "2099-12-31"
            print time
            print lang_type,type(lang_type)
            print campaign_type, type(campaign_type)

            today=date.today()
            print 'today',today
            yesterday = today - timedelta(days=1)
            print yesterday
            
            response_array=[]
            if lang_type == 0:    
                print "kakakakakakak"            
                if campaign_type==0:
                    print "here"
                    print time
                    print after
                    print before


                    obj = CampaignData.objects.filter(date__range=[before,time])
                    print "------------a----------"
                    try:
                        for x in obj:
                            temp_json={}
                            print x.date


                            image_list = ImageData.objects.filter(campaign_id=x)
                            print "______0000000---------"

                            image_arr=[]
                            for image in image_list:
                                image_json={}
                                image_json['id']=image.id
                                image_json['url']=request.scheme + '://' + request.get_host() + '/media/'+str(image.image)
                                image_arr.append(image_json)
                                print "_9__________"



                            temp_json['id']= x.id
                            temp_json['name']=x.name_english
                            print "date date"
                            if str(x.date) == str(today):
                                print "today success"
                                temp_json['date']="Today"
                            elif str(x.date) == str(yesterday) :
                                temp_json['date']="Yesterday"
                            else:
                                print '3'
                                temp_json['date']=str(x.date)
                            temp_json['venue']=str(x.venue_engilsh)
                            temp_json['description']=x.description_english
                            temp_json['image']= request.scheme + '://' + request.get_host() + '/media/'+str(x.image)
                            temp_json['image_list']=image_arr
                        response_array.append(temp_json)
                        # response_array.append(image_arr)

                        # response_json['image_list']=image_arr
                        response_json['campaign_list']=response_array
                        response_json['success'] = True
                        response_json['message'] = "List found"

                    except Exception as e:
                        print e
                        response_json['success']=False
                        response_json['message']="List not found"

                elif campaign_type==1:
                    print "here"
                    obj = CampaignData.objects.filter(date__range=[time, after])
                    print obj
                    try:
                        for x in obj:
                            temp_json = {}
                            print x.date

                            image_list = ImageData.objects.filter(campaign_id=x)
                            print "______0000000---------"

                            image_arr=[]
                            for image in image_list:
                                image_json={}
                                image_json['id']=image.id
                                image_json['url']=request.scheme + '://' + request.get_host() + '/media/'+str(image.image)
                                image_arr.append(image_json)
                                print "_9__________"

                            temp_json['id'] = x.id
                            temp_json['name'] = x.name_english
                            if str(x.date) == str(today):
                                print "today success"
                                temp_json['date']="Today"
                            elif str(x.date) == str(yesterday) :
                                temp_json['date']="Yesterday"
                            else:
                                print '3'
                                temp_json['date']=str(x.date)
                            temp_json['venue']=str(x.venue_engilsh)
                            temp_json['description'] = x.description_english
                            temp_json['image'] = request.scheme + '://' + request.get_host() + '/media/'+str(x.image)
                            temp_json['image_list']=image_arr
                            response_array.append(temp_json)

                        response_json['campaign_list'] = response_array
                        response_json['success'] = True
                        response_json['message'] = "List found"

                    except Exception as e:
                        print e
                        response_json['success'] = False
                        response_json['message'] = "List not found"


            elif lang_type == 1:
            
                if campaign_type == 0:
                    print "here"
                    obj = CampaignData.objects.filter(date__range=[before, time])
                    try:
                        for x in obj:
                            temp_json = {}
                            print x.date

                            image_list = ImageData.objects.filter(campaign_id=x)
                            print "______0000000---------"

                            image_arr=[]
                            for image in image_list:
                                image_json={}
                                image_json['id']=image.id
                                image_json['url']=request.scheme + '://' + request.get_host() + '/media/'+str(image.image)
                                image_arr.append(image_json)
                                print "_9__________"

                            temp_json['id'] = x.id
                            temp_json['name'] = x.name_hindi
                            temp_json['venue']=str(x.venue_hindi)
                            if str(x.date) == str(today):
                                print "today success"
                                temp_json['date']="Today"
                            elif str(x.date) == str(yesterday) :
                                temp_json['date']="Yesterday"
                            else:
                                print '3'
                                temp_json['date']=str(x.date)
                            temp_json['description'] = x.description_hindi
                            temp_json['image'] = request.scheme + '://' + request.get_host() + '/media/'+str(x.image)
                            temp_json['image_list']=image_arr
                            response_array.append(temp_json)

                            response_json['campaign_list'] = response_array
                            response_json['success'] = True
                            response_json['message'] = "List found"

                    except Exception as e:
                        print e
                        response_json['success'] = False
                        response_json['message'] = "List not found"

                elif campaign_type == 1:
                    print "here"
                    obj = CampaignData.objects.filter(date__range=[time, after])
                    try:
                        for x in obj:
                            temp_json = {}
                            print x.date

                            image_list = ImageData.objects.filter(campaign_id=x)
                            print "______0000000---------"

                            image_arr=[]
                            for image in image_list:
                                image_json={}
                                image_json['id']=image.id
                                image_json['url']=request.scheme + '://' + request.get_host() + '/media/'+str(image.image)
                                image_arr.append(image_json)
                                print "_9__________"

                            temp_json['id'] = x.id
                            temp_json['name'] = x.name_hindi
                            if str(x.date) == str(today):
                                print "today success"
                                temp_json['date']="Today"
                            elif str(x.date) == str(yesterday) :
                                temp_json['date']="Yesterday"
                            else:
                                print '3'
                                temp_json['date']=str(x.date)
                            temp_json['venue']=str(x.venue_hindi)
                            temp_json['description'] = x.description_hindi
                            temp_json['image'] = request.scheme + '://' + request.get_host() + '/media/'+str(x.image)
                            temp_json['image_list']=image_arr
                            response_array.append(temp_json)

                            response_json['campaign_list'] = response_array
                            response_json['success'] = True
                            response_json['message'] = "List found"

                    except Exception as e:
                        print e
                        response_json['success'] = False
                        response_json['message'] = "List not found"

        except Exception as e:
            print e
            response_json['success'] = False
            response_json['message'] = "campaign type incorrect"    

        print response_json
        return JsonResponse(response_json)





