from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CampaignData(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=120)
	date = models.DateField(auto_now_add=True)
	venue = models.CharField(max_length=120)
	description = models.TextField()