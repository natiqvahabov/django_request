# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 06:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_auto_20161208_1328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='profile',
            table='profile',
        ),
    ]
