# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 05:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0009_storydata_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storydata',
            name='approved',
        ),
    ]