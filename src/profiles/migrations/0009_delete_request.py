# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-28 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20161128_0525'),
    ]

    operations = [
        migrations.DeleteModel(
            name='request',
        ),
    ]