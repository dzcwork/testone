from django.conf.urls import url
from HelloWorld.view import hello
from django.contrib import admin
from sign import views

urlpatterns = [
	url(r'^hello/$', hello),
	url(r'^admin/', admin.site.urls),
	url(r'^index/$', views.index),
    url(r'^login_action/$', views.login_action),
	url(r'^event_manage/$',views.event_manage),
	url(r'^search_name/$',views.search_name),
	url(r'^guest_manage/$',views.guest_manage),
	url(r'^logout/$',views.logout),
]
