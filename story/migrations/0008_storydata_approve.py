# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-20 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0007_auto_20170620_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='storydata',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
