from django.contrib import admin

import xadmin


from .models import *


# Register your models here.
class FeedbackDataAdmin(object):
    list_display = ["id","name","mobile","ward","feedback"]

xadmin.site.register(FeedbackData,FeedbackDataAdmin)

# Register your models here.

