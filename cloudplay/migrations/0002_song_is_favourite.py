# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-24 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudplay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
