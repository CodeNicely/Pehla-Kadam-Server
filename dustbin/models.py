from __future__ import unicode_literals

from django.db import models

# Create your models here.

class DustBinData(models.Model):
	latitude = models.FloatField(null=False , blank=False)
	longitude = models.FloatField(null=False , blank=False)
	location = models.CharField(max_length=200, null=False , blank=False)