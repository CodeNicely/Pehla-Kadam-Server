from django.contrib import admin
import xadmin

from .models import *


# Register your models here.
class WelcomeDataAdmin(object):
    list_display = ["id", "image", "quote_english", "quote_english"]


xadmin.site.register(WelcomeData,WelcomeDataAdmin)

class WardDataAdmin(object):
    list_display = ["id", "ward_name_english", "ward_name_hindi"]


xadmin.site.register(WardData, WardDataAdmin)
