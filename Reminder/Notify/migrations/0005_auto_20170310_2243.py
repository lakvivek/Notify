# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 22:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Notify', '0004_auto_20170310_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 10, 22, 43, 54, 228521, tzinfo=utc)),
        ),
    ]
