# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-19 06:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0037_auto_20161219_0641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilerequest',
            name='user',
        ),
        migrations.DeleteModel(
            name='profileRequest',
        ),
    ]