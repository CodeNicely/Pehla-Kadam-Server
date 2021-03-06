# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='media/gallery/images/')),
                ('caption_english', models.CharField(max_length=120)),
                ('caption_hindi', models.CharField(max_length=120)),
                ('campaign_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='campaign.CampaignData')),
            ],
        ),
        migrations.CreateModel(
            name='VideoData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('video', models.CharField(max_length=150)),
                ('caption_english', models.CharField(max_length=120)),
                ('caption_hindi', models.CharField(max_length=120)),
                ('campaign_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='campaign.CampaignData')),
            ],
        ),
    ]
