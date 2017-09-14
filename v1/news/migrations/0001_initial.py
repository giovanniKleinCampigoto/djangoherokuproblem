# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-08 18:45
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('hero_image', cloudinary.models.CloudinaryField(blank=True, max_length=255)),
                ('text', models.TextField()),
            ],
            options={
                'ordering': ('publish_date',),
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('picture', cloudinary.models.CloudinaryField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Subject'),
        ),
    ]
