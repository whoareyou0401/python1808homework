# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 21:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wk', '0003_auto_20180814_2031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '人类'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='Person',
        ),
    ]
