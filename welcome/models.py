from __future__ import unicode_literals

from django.db import models

# Create your models here.
class WelcomeData(models.Model):
    image = models.ImageField(upload_to='welcome/', default="/media/welcome/default.png")
    quote_english = models.CharField(max_length=240, blank=False, null=False)
    quote_hindi = models.CharField(max_length=240, blank=False, null=False)
    

    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

class WardData(models.Model):
	ward_name_english = models.CharField(max_length=500, blank=False, null=False)
	ward_name_hindi = models.CharField(max_length=500, blank=False, null=False)