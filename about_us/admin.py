
from django.contrib import admin
import xadmin


from .models import *


# Register your models here.



xadmin.site.register(AboutUsData)
xadmin.site.register(AboutTheTeam)

# Register your models here.
