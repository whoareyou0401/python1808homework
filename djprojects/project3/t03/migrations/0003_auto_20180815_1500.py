# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-15 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('t03', '0002_auto_20180815_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='idcard',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='t03.IdCard'),
        ),
    ]
