# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-20 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20170620_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackdata',
            name='visibility',
            field=models.BooleanField(default=True),
        ),
    ]
