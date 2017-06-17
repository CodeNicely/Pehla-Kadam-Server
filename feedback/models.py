from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FeedbackData(models.Model):
 
    ward = models.CharField(max_length=500 ,blank=False ,null=False)
    mobile = models.CharField(max_length=16, blank=False, null=False)
    name = models.CharField(max_length=240, blank=False, null=False)
   	feedback = models.TextField(null=False,blank=False)

    