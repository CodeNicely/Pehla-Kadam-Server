from django.contrib import admin

# Register your models here.
import xadmin
from .models import VideoData,ImageData

class ImageDataModel(object):

    list_display=["id","image","caption_hindi","caption_english"]


    class Meta:
        model = ImageData

xadmin.site.register(ImageData,ImageDataModel)

class VideoDataDataModel(object):

    list_display=["id","video","caption_hindi","caption_english"]


    class Meta:
        model = VideoData

xadmin.site.register(VideoData,VideoDataDataModel)

