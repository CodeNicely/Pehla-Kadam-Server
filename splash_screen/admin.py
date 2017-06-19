from django.contrib import admin

import xadmin
# Register your models here.
from .models import *


# Register your models here.
class FcmDataAdmin(object):
    list_display = ["id", "fcm", "modified", "created"]


xadmin.site.register(FcmData, FcmDataAdmin)


class KeysDataAdmin(object):
    list_display = ["key", "value", "modified", "created"]


xadmin.site.register(KeysData, KeysDataAdmin)

class ImageDataAdmin(object):
	list_display = ["id", "key","image",'modified','created']
xadmin.site.register(ImageData,ImageDataAdmin)