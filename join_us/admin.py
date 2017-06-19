from django.contrib import admin
import xadmin


from .models import *



class JoinUsDataAdmin(object):
    list_display = ["id","name","mobile","ward"]


xadmin.site.register(JoinUsData,JoinUsDataAdmin)


