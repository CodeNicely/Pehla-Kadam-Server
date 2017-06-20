from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AboutUsData(models.Model):
	title_hindi = models.CharField(max_length = 300, blank = False , null = False)
	title_english = models.CharField(max_length = 300, blank = False , null = False)
	description_english = models.TextField(blank= False, null=False)
	description_hindi = models.TextField(blank= False, null=False)
	image = models.ImageField(upload_to='about_us/' , default= '/media/about_us/default.png')	