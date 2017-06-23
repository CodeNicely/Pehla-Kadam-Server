from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AboutUsData(models.Model):
	image = models.ImageField(upload_to='about_us/' , default= '/media/about_us/default.png')
	introduction_english=models.TextField(default="")
	introduction_hindi=models.TextField(default="")
	vision_english=models.TextField(default="")
	vision_hindi=models.TextField(default="")
	achievements_english=models.TextField(default="")
	achievements_hindi=models.TextField(default="")



class AboutTheTeam(models.Model):
	name_english=models.CharField(max_length=50,null=True,blank=True)
	name_hindi=models.CharField(max_length=120,null=True,blank=True)
	email=models.EmailField(null=True,blank=True)
	mobile=models.IntegerField()
	image=models.ImageField(upload_to='about_us/')