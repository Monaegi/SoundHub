# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20171130_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenttrack',
            name='instrument',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='instrument',
            field=models.CharField(max_length=100),
        ),
    ]
