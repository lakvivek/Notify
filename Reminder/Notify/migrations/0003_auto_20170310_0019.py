# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 00:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Notify', '0002_auto_20170309_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 10, 0, 19, 39, 195974, tzinfo=utc)),
        ),
    ]