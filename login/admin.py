from django.contrib import admin

import xadmin

from .models import *


# Register your models here.
class OtpDataAdmin(object):
    list_display = ["id", "mobile", "otp", "flag",'modified','created']


xadmin.site.register(OtpData,OtpDataAdmin)

class UserDataAdmin(object):
    list_display = ["id", "name", "mobile",'ward','fcm','image','modified','created']


xadmin.site.register(UserData, UserDataAdmin)

