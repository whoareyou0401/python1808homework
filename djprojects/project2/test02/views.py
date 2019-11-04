# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Aws

# Create your views here.
def user(req):
    #查询包含李的用户
    # kw = req.GET.get("kw")
    # data = Aws.objects.filter(
    #     name__contains=kw
    # )
    #查询年龄是22的用户
    # data = Aws.objects.filter(
    #     age__in=[22]
    # )
    #查询2018年注册的用户
    # data = Aws.objects.filter(
    #     last_update__year=2018
    # )
    #查询年龄大于20的用户
    # data = Aws.objects.filter(
    #     age__gt=20
    # )
    data = Aws.objects.values(
        "name","age"
    )
    return render(req,"test02.html",{'users':data})