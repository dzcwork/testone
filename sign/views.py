#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
# Create your views here.

def index(request):
    return render(request,"index.xhtml")

# 登录动作
def login_action(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
       # if username=='admin'and password=='admin10000':
        if user is not None:
            auth.login(request,user)
            request.session['user']=username
            response=HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',username,3600)#添加浏览器cookie
            request.session['user']=username #将session信息记录到浏览器
            return  response
        else:
            return render(request,'index.xhtml',{'error':'帐号或密码错误!'})

#  接口测试管理
#限制某个视图函数必须登录才能访问，在这个函数的前面加上@login_required
@login_required
def event_manage(request):
    #username=request.COOKIES.get('user','')
    event_list=Event.objects.all()
    username=request.session.get('user','')
    return  render(request,'event_manage.xhtml',{"user":username,"events":event_list})
    #读取发布会信息，通过render()函数返回给客户端

#发布会名称搜索
@login_required
def search_name(request):
    username=request.session.get('user','')
    search_name=request.GET.get("name","")
    event_list=Event.objects.filter(name__contains=search_name)
    return render(request,"event_manage.xhtml",{"user":username,"events":event_list})

#退出登录
@login_required
def logout(request):
    auth.logout(request)
    response=HttpResponseRedirect('/index/')
    return response

#嘉宾管理
@login_required
def guest_manage(request):
    guest_list=Guest.objects.all()
    username=request.session.get('user','')
    paginator=Paginator(guest_list,2)
    page=request.GET.get('page')
    try:
        contacts=paginator.page(page)
    except PageNotAnInteger:
        # if page is not an iteger,deliver first page
        contacts=paginator.page(1)
    except EmptyPage:
        # if page is out of range(e.g.9999),deliver last page of results
        contacts=paginator.page(paginator.num_pages)
    return render(request,"guest_manage.xhtml",{"user":username,"guests":contacts})

# Create your views here.
