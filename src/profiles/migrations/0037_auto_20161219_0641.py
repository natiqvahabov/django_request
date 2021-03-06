# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-19 06:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0036_auto_20161212_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='profileRequest',
            fields=[
                ('name', models.CharField(default='name', max_length=120)),
                ('id', models.CharField(default='23', max_length=30, primary_key=True, serialize=False)),
                ('surname', models.CharField(default='surname', max_length=120)),
                ('fathername', models.CharField(default='father name', max_length=120)),
                ('department', models.CharField(blank=True, default='department', max_length=120, null=True)),
                ('par_us_name', models.CharField(blank=True, default='parent user name', max_length=120, null=True)),
                ('position', models.CharField(blank=True, default='position', max_length=120, null=True)),
                ('role', models.CharField(default='4', max_length=2)),
                ('ip', models.CharField(blank=True, default='192.168.1.1', max_length=20, null=True)),
                ('notif_ask', models.CharField(blank=True, max_length=3, null=True)),
                ('notif_answer', models.CharField(blank=True, max_length=3, null=True)),
                ('internal_tel_num', models.CharField(blank=True, max_length=30, null=True)),
                ('mob_tel_num', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.CharField(blank=True, max_length=300, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='department',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='fathername',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='internal_tel_num',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mob_tel_num',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='notif_answer',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='notif_ask',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='par_us_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='position',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='surname',
        ),
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Student'), (2, 'Teacher'), (3, 'Supervisor')], null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
