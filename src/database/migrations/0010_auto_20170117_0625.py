# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-17 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_auto_20170117_0609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.RemoveField(
            model_name='document',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='document',
            name='request_id',
            field=models.CharField(max_length=255),
        ),
    ]
