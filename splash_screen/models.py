from __future__ import unicode_literals

from django.db import models

# Create your models here.
class KeysData(models.Model):
    value = key = models.CharField(max_length=200, blank=True, null=True)
    key = models.CharField(max_length=120, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
class FcmData(models.Model):
    fcm = models.CharField(max_length=255, unique=True)
  
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

class ImageData(models.Model):
	image = models.ImageField(upload_to = 'images/',default='/media/images/default.png')
	key = models.CharField(max_length=120, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
