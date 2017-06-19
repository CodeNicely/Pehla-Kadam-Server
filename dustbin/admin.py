from django.contrib import admin

import xadmin


from .models import *


# Register your models here.
class DustbinDataAdmin(object):
    list_display = ["id","latitude","longitude","location"]


xadmin.site.register(DustBinData,DustbinDataAdmin)

