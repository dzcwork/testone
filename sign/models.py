#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#发布会表
class Event(models.Model):
    #casenumber=models.IntegerField()#用例编号
    #casetitle=models.CharField(max_length=100) #用例标题
    #casecontent=models.CharField(max_length=500)#用例步骤
    #casestatus=models.BooleanField()#用例状态
    #planresult=models.CharField(max_length=200)#预期结果
    #result=models.BooleanField()#测试结果
    #start_time=models.DateTimeField('event_time')#执行时间
    #creat_time=models.DateTimeField(auto_now=True)#创建时间
    name=models.CharField(max_length=100)#发布会标题
    limit=models.IntegerField()#参会人数
    status=models.BooleanField()#状态
    address=models.CharField(max_length=200)#发布会地址
    start_time = models.DateTimeField('event_time') #开始时间
    create_time = models.DateTimeField(auto_now=True) # 创建时间,自动获取当前时间

    def __str__(self):
        return self.name

#嘉宾表
class Guest(models.Model):
    event=models.ForeignKey(Event) #关联发布会id
    realname=models.CharField(max_length=64)#姓名
    phone=models.CharField(max_length=16)#手机号码
    email=models.EmailField()#邮箱
    sign=models.BooleanField()#签到状态
    create_time=models.DateTimeField(auto_now=True)#创建时间，自动获取当前时间

    class Meta:
        unique_together=("event","phone")

    def __str__(self):
        return self.realname