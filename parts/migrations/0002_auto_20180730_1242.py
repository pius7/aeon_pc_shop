# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-30 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='parts_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('url', models.CharField(default='', max_length=254)),
                ('category', models.CharField(default='', max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='parts_urls',
        ),
    ]
