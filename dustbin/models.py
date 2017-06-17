from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Maps(Model.models):
	latitude = models.FloatField(null=False , blank=False)
	longitude = models.FloatField(null=False , blank=False)
	location = models.CharField(null=False , blank=False)