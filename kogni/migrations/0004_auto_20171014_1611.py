# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kogni', '0003_scenariy_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenariy',
            name='image',
            field=models.ImageField(upload_to='kogni-images'),
        ),
    ]