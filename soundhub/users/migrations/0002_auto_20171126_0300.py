# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='instrument',
            field=models.CharField(blank=True, choices=[('G', 'Guitar'), ('B', 'Base'), ('D', 'Drums'), ('V', 'Vocals'), ('K', 'Keyboard'), ('O', 'Others')], max_length=1, null=True),
        ),
    ]
