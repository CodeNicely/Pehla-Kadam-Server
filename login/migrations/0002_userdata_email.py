# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-22 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]