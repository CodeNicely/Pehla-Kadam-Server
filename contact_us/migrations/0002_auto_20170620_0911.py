# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-20 09:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactusdata',
            old_name='name_english',
            new_name='facebook',
        ),
        migrations.RemoveField(
            model_name='contactusdata',
            name='name_hindi',
        ),
    ]