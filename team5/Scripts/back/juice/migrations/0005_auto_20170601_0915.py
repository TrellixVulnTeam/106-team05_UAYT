# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-01 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juice', '0004_auto_20170525_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='list',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
