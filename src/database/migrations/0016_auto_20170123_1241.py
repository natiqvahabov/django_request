# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-23 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_scactionnotif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scactionnotif',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]