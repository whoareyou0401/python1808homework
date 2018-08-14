# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Aws(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="姓名"
    )
    age = models.IntegerField(
        verbose_name="年龄"
    )
    set_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="注册日期详细信息"
    )
    last_update = models.DateField(
        auto_now=True,
        verbose_name="修改日期"
    )
    is_used = models.BooleanField(
        default=True,
        verbose_name="是否在用"
    )
    p = models.CharField(
        max_length=20
    )
    # def __str__(self):
    #     return self.name+str(self.age)+str(self.set_time)+str(self.last_update)+self.is_used
    class Meta:
        verbose_name="用户表"
        db_table="aws_users"