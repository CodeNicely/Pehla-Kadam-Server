
from django.contrib import admin
import xadmin


from .models import *


# Register your models here.
class AboutUsDataAdmin(object):
    list_display = ["title_hindi","title_english","description_hindi","description_english"]


xadmin.site.register(AboutUsData,AboutUsDataAdmin)

# Register your models here.
