# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-13 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0002_auto_20181113_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='alchemicalmaterial',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
