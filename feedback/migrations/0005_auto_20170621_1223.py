# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20170621_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackdata',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackdata',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]