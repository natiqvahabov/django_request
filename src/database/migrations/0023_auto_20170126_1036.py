# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-26 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0022_screquestsnew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screquestsnew',
            name='description',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
