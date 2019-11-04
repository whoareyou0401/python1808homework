# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Engineer

def index(request):
    #很多的逻辑
    return HttpResponse("Django 呵呵哒!!")

def my_html(req):
    data = Engineer.objects.all()
    print(data)
    return render(req,'my_index.html',context={"my_data":data})

def get_data(req):
    #获取数据
    data = Engineer.objects.all()
    print(data)
    return render(req,"my_index1.html",context={"my_data":data})

