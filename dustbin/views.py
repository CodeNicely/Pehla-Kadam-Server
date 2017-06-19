
from __future__ import print_function
from django.shortcuts import render


from django.http import JsonResponse

from .models import *

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def maps(request):
	response_json = {}
	if request.method == 'GET':
		lat = float(request.GET.get('latitude'))
		lon = float(request.GET.get('latitude'))
	# for o in Maps.objects.all():
	# 	dist = 