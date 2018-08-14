from django.http import HttpResponse
from django.shortcuts import render
from .models import Tvideo
# Create your views here.
def my_videos(req):
    data=Tvideo.objects.filter(playno__gt=3000)

    result={
        "vtitle":"鬼畜区",
        "sp":data
    }
    return render(req,"videos.html",result)

def search_by_vn(req):
    param=req.GET
    kw=param.get("kw")
    # res=Tvideo.objects.filter(
    #     name__contains=kw
    # )
    # res=Tvideo.objects.filter(
    #     name__endswith=kw
    # )
    # res=Tvideo.objects.filter(
    #     playno__in=[52300,5000]
    # )
    res=Tvideo.objects.filter(
        birthday__month=8
    )
    return render(req,"videos.html",{"sp":res})
