# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-19 06:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0038_auto_20161219_0642'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='profile',
            new_name='RequestUsers',
        ),
    ]