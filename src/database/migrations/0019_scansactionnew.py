# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-23 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_auto_20170123_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScAnsActionNew',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.FloatField()),
                ('action_id', models.FloatField()),
                ('req_id', models.FloatField()),
                ('a_date', models.DateField()),
            ],
            options={
                'db_table': 'sc_ans_action_new',
                'managed': True,
            },
        ),
    ]
