# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170817_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hero_image',
            field=models.ImageField(blank=True, upload_to='pictures/%Y%m%d'),
        ),
    ]
