from __future__ import unicode_literals

from django.db import models

# Create your models here.

from campaign.models import CampaignData


class ImageData(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='media/gallery/images/')
    caption_english=models.CharField(max_length=120,null=True,blank=True)
    caption_hindi = models.CharField(max_length=120,null=True,blank=True)
    campaign_id = models.ForeignKey(CampaignData,null=True)


class VideoData(models.Model):
    id = models.AutoField(primary_key=True)
    video = models.FileField(upload_to='media/gallery/video/')
    caption_english = models.CharField(max_length=120,null=True,blank=True)
    caption_hindi = models.CharField(max_length=120,null=True,blank=True)
    campaign_id = models.ForeignKey(CampaignData,null=True)