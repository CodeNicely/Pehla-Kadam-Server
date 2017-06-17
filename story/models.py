from __future__ import unicode_literals

from django.db import models
from login.models import UserData



# Create your models here.


class StoryData(models.Model):
    user_id = models.ForeignKey(UserData)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/story/images/')
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)



class UserLikeData(models.Model):
    user_id = models.ForeignKey(UserData)
    story_id = models.ForeignKey(StoryData)
    liked=models.BooleanField(default=False)
    shared =models.BooleanField(default=False)