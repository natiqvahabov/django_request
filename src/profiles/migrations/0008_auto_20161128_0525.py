# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-28 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScComments',
            fields=[
                ('id', models.FloatField(blank=True, null=True, primary_key=True, serialize=False)),
                ('req_id', models.FloatField(blank=True, null=True)),
                ('ans_id', models.CharField(blank=True, max_length=200, null=True)),
                ('ins_date', models.CharField(blank=True, max_length=40, null=True)),
                ('file_path', models.CharField(blank=True, max_length=2000, null=True)),
                ('comment_text', models.CharField(blank=True, max_length=4000, null=True)),
            ],
            options={
                'db_table': 'sc_comments',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
