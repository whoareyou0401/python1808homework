# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Engineer(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    age = models.IntegerField(
        default=18
    )
    def __str__(self):
        return self.name
#车的模型
class Cart(models.Model):
    name = models.CharField(
        max_length=30
    )
    color = models.CharField(
        max_length=30
    )
    def __str__(self):
        return self.name
#司机的模型
class Siji(models.Model):
    name = models.CharField(
        max_length=30
    )
    #指定外键
    cart = models.ForeignKey(
        Cart,
        verbose_name="车"
    )