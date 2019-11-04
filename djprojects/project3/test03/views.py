# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def get_data(req):
    name=req.GET

    name1 = name.get("cx")
    if len(name) < 1:
        data = ""
    elif name1=="all":
        data = Languages.objects.all()
    else:
        data = Languages.objects.filter(
            name__contains=name1
        )
    return render(req,"language.html",{"datas":data})