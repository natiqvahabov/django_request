# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_auto_20161212_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='asdasd', max_length=120),
        ),
    ]
