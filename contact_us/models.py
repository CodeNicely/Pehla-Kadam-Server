from __future__ import unicode_literals

from django.db import models

class ContactUsData(models.Model):
    email = models.CharField(max_length=150, blank=True, null=True)
    mobile = models.CharField(max_length=120, blank=True, null=True)
    address_hindi = models.CharField(max_length=200, blank=True, null=True)
    address_english= models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    
    
