# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import languagename
# Create your views here.
def language(req):
    data = languagename.objects.all()

    return render(req,'index.html',context={"my_data":data})
