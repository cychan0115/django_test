#coding:utf-8
from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse(u'hello,cy!_中文也支持哦')

def add(request):
    a=request.GET['a']
    b=request.GET['b']
    c=int(a)+int(b)
    return HttpResponse(c)

def add2(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(c)

def home(request):
    return render(request, 'home.html')

def testdb(request):
    import myclass
    name=request.GET['name']
    age=request.GET['age']
    re=myclass.insert1(name,age)
    return HttpResponse(re)

def testdb_select(request):
    import myclass
    name=request.GET['name']
    re=myclass.name_get_age(name)
    return HttpResponse(re)