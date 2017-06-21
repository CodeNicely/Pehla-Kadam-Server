from __future__ import unicode_literals

from django.db import models
from login.models import UserData

# Create your models here.
class FeedbackData(models.Model):

	user_data = models.ForeignKey(UserData,null=True,blank=True)
	feedback = models.TextField(null=True,blank=True)
	visibility = models.BooleanField(default=True)
	date = models.DateField(auto_now_add=True,null = True)
	time = models.TimeField(auto_now_add=True,null=True)
		