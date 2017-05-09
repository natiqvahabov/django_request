# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-08 13:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20161208_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.FloatField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]