# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='media/story/images/')),

                ('title_english', models.CharField(blank=True, max_length=120, null=True)),
                ('title_hindi', models.CharField(blank=True, max_length=120, null=True)),
                ('description_english', models.CharField(blank=True, max_length=120, null=True)),
                ('description_hindi', models.CharField(blank=True, max_length=120, null=True)),

                ('likes', models.IntegerField(default=0)),
                ('shares', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.UserData')),
            ],
        ),
        migrations.CreateModel(
            name='UserLikeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField(default=False)),
                ('shared', models.BooleanField(default=False)),
                ('story_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.StoryData')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.UserData')),
            ],
        ),
    ]
