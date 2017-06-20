from __future__ import unicode_literals

from django.db import models
from login.models import UserData





class StoryData(models.Model):
    user_mobile = models.ForeignKey(UserData,null=True)
    user_id = models.IntegerField(default=0,editable=False)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/story/images/')
    title = models.CharField(max_length=120,null=True,blank=True)
    
    description = models.CharField(max_length=120,null=True,blank=True)
    approve = models.BooleanField(default=False)
    
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.user_id = self.user_mobile.id
        super(StoryData, self).save(*args, **kwargs)


class UserLikeData(models.Model):
    user_mobile = models.ForeignKey(UserData,null = True)
    user_id = models.IntegerField(default=0,editable=False)
    story_id = models.ForeignKey(StoryData)
    liked=models.BooleanField(default=False)
    
    #shared has to be deleted

    def save(self, *args, **kwargs):
        self.user_id = self.user_mobile.id
        super(UserLikeData, self).save(*args, **kwargs)

class UserShareData(models.Model):
    user_mobile = models.ForeignKey(UserData,null = True)
    user_id = models.IntegerField(default=0,editable=False)
    story_id = models.ForeignKey(StoryData)
   
    shared =models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.user_id = self.user_mobile.id
        super(UserShareData, self).save(*args, **kwargs)

