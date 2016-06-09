# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
            ],
        ),
    ]