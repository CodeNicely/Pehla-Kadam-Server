from __future__ import unicode_literals

from django.db import models

# Create your models here.
class OtpData(models.Model):
    mobile = models.CharField(max_length=240, blank=False, null=False)
    otp = models.IntegerField(default=0)
    flag = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)


class UserData(models.Model):
    fcm = models.CharField(max_length=240, blank=False, null=False)
    ward = models.CharField(max_length=500 ,blank=False ,null=False)
    mobile = models.CharField(max_length=16, blank=False, null=False)
    name = models.CharField(max_length=240, blank=False, null=False)
    image = models.ImageField(upload_to='profile/', default='/media/profile/default.png' )
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    email = models.CharField(max_length=150, blank=True, null = True)

    def __unicode__(self):
        return self.mobile
		