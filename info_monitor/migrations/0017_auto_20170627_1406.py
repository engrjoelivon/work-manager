# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-27 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_monitor', '0016_auto_20170627_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infos',
            name='status',
            field=models.NullBooleanField(default=False),
        ),
    ]
