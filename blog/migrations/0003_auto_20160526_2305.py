# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='About')),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-create_date'], 'verbose_name': 'Manual', 'verbose_name_plural': 'Manuals'},
        ),
    ]
