#coding:utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse(u'hello,cy!_中文也支持哦')