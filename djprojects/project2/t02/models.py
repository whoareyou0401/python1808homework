# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class Categray(models.Model):
#     name = models.CharField(
#         max_length=20,
#         verbose_name="分类名"
#     )
# class Item(models.Model):
#     name = models.CharField(
#         max_length=30,
#         verbose_name="商品名",
#         db_index=True
#     )
#     barcode = models.CharField(
#         max_length=15,
#         null=True,
#         verbose_name="条形码",
#     )
#     price = models.FloatField(
#         max_length=8,
#         verbose_name="售价"
#     )
#     in_price = models.DecimalField(
#         max_length=13,
#         decimal_places=2,
#         verbose_name="进价"
#     )
#     come_in_time = models.DateField(
#         auto_now_add=True,
#         verbose_name="创建时间"
#     )
#     update_time = models.DateField(
#         auto_now_add=True,
#         verbose_name="修改时间"
#     )
#     icon = models.CharField(
#         max_length=249,
#         null=True,
#         verbose_name="封面"
#     )
#     categary = models.ForeignKey(
#         Categray,
#         verbose_name="所属分类",
#         db_index=True
#     )
class FireCart(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    speed = models.IntegerField(
        verbose_name="时速",
        default=300,
        db_column="my_speed"
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="出厂日期"
    )
    last_update = models.DateField(
        auto_now=True
    )
    is_used = models.BooleanField(
        default=True,
        verbose_name="是否在用"
    )
    def __str__(self):
        return self.name+str(self.speed)
    class Meta:
        verbose_name="火车类"
        db_table="huocart"
