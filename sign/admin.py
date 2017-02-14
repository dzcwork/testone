#coding=utf-8
from django.contrib import admin
from sign.models import Event,Guest

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time','id']#列表
    search_fields = ['name']#搜索标题
    list_filter = ['status']#筛选状态

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone','email','sign','create_time','event']
    search_fields = ['realname']#搜索参会者
    list_filter = ['sign']#筛选是否签到

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)