from django.contrib import admin

# Register your models here.
import xadmin


from .models import *


# Register your models here.
class ContactUsDataAdmin(object):
    list_display = ["id","name_hindi","name_english","mobile","email","address_hindi","address_english"]


xadmin.site.register(ContactUsData,ContactUsDataAdmin)

# Register your models here.
