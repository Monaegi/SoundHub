# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='commenttrack',
            name='created_data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created_data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]