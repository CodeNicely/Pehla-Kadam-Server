# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-20 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutusdata',
            name='image',
            field=models.ImageField(default='/media/about_us/default.png', upload_to='about_us/'),
        ),
    ]
