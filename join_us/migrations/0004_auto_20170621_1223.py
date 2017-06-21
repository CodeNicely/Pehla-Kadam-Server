# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('join_us', '0003_joinusdata_visibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinusdata',
            name='description',
        ),
        migrations.RemoveField(
            model_name='joinusdata',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='joinusdata',
            name='name',
        ),
        migrations.AddField(
            model_name='joinusdata',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='joinusdata',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='joinusdata',
            name='user_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.UserData'),
        ),
    ]
