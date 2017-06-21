from django.contrib import admin

import xadmin


from .models import *


# Register your models here.
class FeedbackDataAdmin(object):
    list_display = ["id","feedback"]

xadmin.site.register(FeedbackData,FeedbackDataAdmin)

# Register your models here.

