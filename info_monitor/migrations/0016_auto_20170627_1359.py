# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-27 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_monitor', '0015_infos_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infos',
            name='status',
            field=models.NullBooleanField(),
        ),
    ]
