# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-26 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0021_auto_20170124_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScRequestsNew',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=4000, null=True)),
                ('rtype', models.CharField(blank=True, max_length=100, null=True)),
                ('file_path', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('solution_desc', models.CharField(blank=True, max_length=4000, null=True)),
                ('ans_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('sender', models.CharField(blank=True, max_length=200, null=True)),
                ('ins_date', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'sc_requests_new',
                'managed': True,
            },
        ),
    ]
