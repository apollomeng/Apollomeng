# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-25 11:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproject',
            name='project_man',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发起人'),
        ),
        migrations.AddField(
            model_name='userlove',
            name='love_man',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='关注人'),
        ),
        migrations.AddField(
            model_name='userlove',
            name='love_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects', verbose_name='关注项目'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]