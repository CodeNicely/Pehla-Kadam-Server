from __future__ import unicode_literals

from django.db import models
from campaign.models import CampaignData

# Create your models here.

class ImageData(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='media/gallery/images/')
    caption_english=models.CharField(max_length=120)
    caption_hindi = models.CharField(max_length=120)
    campaign_id = models.ForeignKey(CampaignData,null=True)


class VideoData(models.Model):
    id = models.AutoField(primary_key=True)
    video = models.CharField(max_length=150)
    caption_english = models.CharField(max_length=120)
    caption_hindi = models.CharField(max_length=120)
    campaign_id = models.ForeignKey(CampaignData,null=True)



