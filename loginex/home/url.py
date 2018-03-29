from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

#from .import loginex
app_name='home'

urlpatterns = [
    url(r'^$', views.dis),
    #url(r'^login/base/$',VIEWS.index)
]
