# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='FcmData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcm', models.CharField(max_length=255, unique=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=200, null=True)),
                ('key', models.CharField(blank=True, max_length=120, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(

            name='KeysData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=200, null=True)),
                ('key', models.CharField(blank=True, max_length=120, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
