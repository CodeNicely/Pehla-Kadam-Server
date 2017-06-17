from django.contrib import admin

# Register your models here.
import xadmin


from .models import *


# Register your models here.
class ContactUsDataAdmin(object):
    list_display = ["title_hindi","title_english","description_hindi","description_english"]


xadmin.site.register(ContactUsData,ContactUsDataAdmin)

# Register your models here.
