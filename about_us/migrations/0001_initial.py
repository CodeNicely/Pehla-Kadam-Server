# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-17 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_hindi', models.CharField(max_length=300)),
                ('title_english', models.CharField(max_length=300)),
                ('description_english', models.TextField()),
                ('description_hindi', models.TextField()),
            ],
        ),
    ]
