from __future__ import unicode_literals

from django.db import models
from login.models import UserData





class StoryData(models.Model):
    user_data = models.ForeignKey(UserData,null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/media/story/images/')
    title = models.CharField(max_length=120,null=True,blank=True)
    
    description = models.CharField(max_length=120,null=True,blank=True)
    approve = models.BooleanField(default=False)
    
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)


class UserLikeData(models.Model):
    user_id = models.ForeignKey(UserData,null=True)
    story_id = models.ForeignKey(StoryData,null=True)
    liked=models.BooleanField(default=False)
    
    #shared has to be deleted

class UserShareData(models.Model):
    user_id = models.ForeignKey(UserData,null = True)
    story_id = models.ForeignKey(StoryData)
    shared =models.BooleanField(default=False)