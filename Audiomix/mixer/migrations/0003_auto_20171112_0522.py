# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixer', '0002_auto_20171112_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='author',
            field=models.CharField(default='nachwon', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commit',
            name='instrument',
            field=models.CharField(choices=[('V', 'Vocal'), ('G', 'Guitar'), ('B', 'Bass'), ('D', 'Drums'), ('K', 'Keyboard'), ('O', 'Others')], default='G', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='test title', max_length=100),
            preserve_default=False,
        ),
    ]
