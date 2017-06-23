from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CampaignData(models.Model):
	id = models.AutoField(primary_key=True)
	name_english = models.CharField(max_length=50,null=True,blank=True)
	name_hindi = models.CharField(max_length=50,null=True,blank=True)
	date = models.DateField()
	venue_engilsh = models.CharField(max_length=120,null=True,blank=True)
	venue_hindi = models.CharField(max_length=120,null=True ,blank=True)
	description_english = models.TextField(null=True,blank=True)
	description_hindi = models.TextField(null=True,blank=True)
	image = models.ImageField(upload_to='media/campaign_images', blank=True)

	def __unicode__(self):
		return str(self.id)


