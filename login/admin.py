from django.contrib import admin

# Register your models here.
import xadmin
from login.models import UserData


class UserDataModel(object):

    list_display=["id"]


    class Meta:
        model = UserData

xadmin.site.register(UserData,UserDataModel)
