from django.shortcuts import render

# Create your views here.
from .models import Hero


def Hero_u(request):
    #拿数据
    data =Hero.objects.order_by("power")
    #准备返回数据,去创建Html文件
    result = {
        "title": "英雄表",
        "hero_user": data
    }
    return render(request,"hero.html",result)
def Hero_all(request):
    param = request.GET
    kw = param.get("kw")
    res = Hero.objects.filter(
        name__contains=kw
    )
    return render(request,'hero.html',{"hero_user":res})