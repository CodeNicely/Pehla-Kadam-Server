from __future__ import unicode_literals

from django.db import models
from login.models import UserData

# Create your models here.
class JoinUsData(models.Model):
 
    ward = models.CharField(max_length=500 ,blank=False ,null=False)
    user_data = models.ForeignKey(UserData,null=True,blank=True)
    visibility = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True,null=True)
    time = models.TimeField(auto_now_add=True,null=True)
    description = models.TextField(null=True,blank=True)

    