# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 21:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kogni', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scenariy',
            name='image',
        ),
    ]
