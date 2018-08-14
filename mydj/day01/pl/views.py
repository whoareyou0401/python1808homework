from django.http import HttpResponse
from django.shortcuts import render
from .models import Bcyy
# Create your views here.

def bc(request):
    return HttpResponse("嘿嘿哒！！")

def i_ht(rew):
    return render(rew,'l_index.html')

def get_kf(rew):

    data=Bcyy.objects.all()
    print(data)
    return render(rew,"l_index.html",context={"my_data1":data})