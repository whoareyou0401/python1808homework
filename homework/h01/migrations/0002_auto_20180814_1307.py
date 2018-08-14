# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('h01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=18, max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='teacher',
        ),
    ]
