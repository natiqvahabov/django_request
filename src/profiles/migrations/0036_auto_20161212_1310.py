# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0035_auto_20161212_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id',
            field=models.CharField(default='23', max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='name', max_length=120),
        ),
    ]
