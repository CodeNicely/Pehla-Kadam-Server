# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WardData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_name_english', models.CharField(max_length=500)),
                ('ward_name_hindi', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='WelcomeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='/media/welcome/default.png', upload_to='welcome/')),
                ('quote_english', models.CharField(max_length=240)),
                ('quote_hindi', models.CharField(max_length=240)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
