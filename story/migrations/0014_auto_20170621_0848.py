# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0013_auto_20170621_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlikedata',
            name='user_mobile',
        ),
        migrations.AlterField(
            model_name='userlikedata',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.UserData'),
        ),
    ]
