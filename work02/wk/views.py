from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Student

def resMsg(req):
    res = Student.objects.all()
    return render(req,"studentShow.html",context={"msg":res,"title":'人员信息统计'})

def filter1(req):
    param = req.GET
    kw = param.get("kw")
    # res = Student.objects.filter(
    #     #     name__contains=kw
    #     # )
    # res = Student.objects.filter(
    #     age__in=[18]
    # )
    # res = Student.objects.filter(
    #     birthday__year=2018
    # )
    # res = Student.objects.filter(
    #     age__gt=18
    # )
    res = Student.objects.values('age')
    print(res)
    return render(req,"studentShow.html",context={"msg":res,"title":'筛选人'})


