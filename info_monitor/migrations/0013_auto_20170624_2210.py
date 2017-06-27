# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-25 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_monitor', '0012_infos_where'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infos',
            name='where',
            field=models.CharField(choices=[('retirement', 'RET'), ('CARDING', 'CD')], max_length=50, null=True),
        ),
    ]
