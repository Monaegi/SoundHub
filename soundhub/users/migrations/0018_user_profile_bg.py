# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-16 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20171214_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_bg',
            field=models.ImageField(blank=True, upload_to=users.models.profile_bg_directory_path),
        ),
    ]
