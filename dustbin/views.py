
from __future__ import print_function
from django.shortcuts import render


from django.http import JsonResponse

from .models import *

from django.views.decorators.csrf import csrf_exempt
from math import sin, cos, asin, sqrt, radians
import numpy as np

@csrf_exempt
def maps(request):
	response_json = {}
	temp_list = []
	if request.method == 'GET':
		try:
			latitude = (request.GET.get('latitude'))
			longitude = (request.GET.get('longitude'))
			try:
				for o in DustBinData.objects.all():
					print(latitude,longitude,o.latitude,o.longitude)
				
					distance = get_distance(np.float32(latitude), np.float32(longitude),
					np.float32(o.latitude), np.float32(o.longitude))
					print(distance)
					temp_json = {}
					temp_json['distance'] = distance
					temp_json['latitude'] = o.latitude
					temp_json['longitude'] = o.longitude
					temp_json['name'] = o.location
					temp_list.append(temp_json)
				response_json['dustbin_list'] = temp_list
				response_json['success'] = True
				response_json['message'] = "Successful"
				response_json["dustbin_list"] = sorted(response_json["dustbin_list"], key=lambda x: x['distance'], reverse=False)
			except Exception as e :
				print(str(e))
				response_json['success'] = False
				response_json['message'] = str(e)

		except Exception as e :
			print(str(e))
			response_json['success'] = False
			response_json['message'] = "latitude or longitude not received"
	else:
		response_json['success'] = False
		response_json['message'] = "not a get request"
	print(str(response_json))
	return JsonResponse(response_json)




def get_distance(lat1, lon1, lat2, lon2):
    try:
       
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        km = 6367 * c
        # print "Km is ", km
        return km
    except Exception as e:
        print(e)
        return 100.0