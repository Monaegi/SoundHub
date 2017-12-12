# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_commenttrack_mixed_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenttrack',
            name='is_mixed',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='liked_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]