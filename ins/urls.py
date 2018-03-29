"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLcon
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .import views as views

app_name='login'

urlpatterns = [
     url(r'^$',views.insert),
     url(r'register/$',views.register),
    #url(r'^logout/$', auth_views.logout,name='logout'),
    #rl(r'^logg/',include('loginex.urls')),
    #url(r'^log/',include(loginex.urs))
]