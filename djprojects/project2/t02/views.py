# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import FireCart
# Create your views here.
def my_carts(req):
    #拿火车数据
    data = FireCart.objects.filter(speed__lte=270).order_by('-speed')
    #准备返回数据
    result = {
        "title":"火cart",
        "carts":data
    }
    return render(req,"trains.html",result)
def search_by_name(req):
    #获取get请求参数
    param = req.GET
    kw = param.get("kw")
    #根据参数 去搜索数据
    #查询包含kw的条件
    # res = FireCart.objects.filter(
    #     name__contains=kw
    # )
    #查询以kw结尾的条件
    # res = FireCart.objects.filter(
    #     name__endswith=kw
    # )
    #查询属于在in里面的条件
    # res = FireCart.objects.filter(speed__in=[300,265])
    #根据时间查询
    res = FireCart.objects.filter(create_date__month=8)
    return render(req,'trains.html',{'carts':res})

