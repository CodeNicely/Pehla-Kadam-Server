from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CampaignData(models.Model):
	id = models.AutoField(primary_key=True)
	name_english = models.CharField(max_length=120)
	name_hindi = models.CharField(max_length=120)
	date = models.DateField(auto_now_add=True)
	venue_engilsh = models.CharField(max_length=120)
	venue_hindi = models.CharField(max_length=120)
	description_english = models.TextField()
	description_hindi = models.TextField()
	image = models.ImageField(upload_to='media/campaign_images', blank=True)


