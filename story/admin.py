from django.contrib import admin

# Register your models here.
import xadmin
from .models import StoryData,UserLikeData,UserShareData

class StoryDataModel(object):

    list_display=["id","user_data","date","time","likes","shares","approve"]


    class Meta:
        model = StoryData

xadmin.site.register(StoryData,StoryDataModel)

class UserLikeDataModel(object):

    list_display=["id","user_id","story_id","liked"]


    class Meta:
        model = UserLikeData

xadmin.site.register(UserLikeData,UserLikeDataModel)

class UserShareDataModel(object):

    list_display=["id","user_id","story_id","shared"]


    class Meta:
        model = UserShareData

xadmin.site.register(UserShareData,UserShareDataModel)