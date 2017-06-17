from django.contrib import admin
import xadmin
# Register your models here.

from .models import  CampaignData

class CampaignDataModel(object):

    list_display=["id","name_hindi","date","venue_hindi","description_hindi"]


    class Meta:
        model=CampaignData

xadmin.site.register(CampaignData,CampaignDataModel)


