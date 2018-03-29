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
from django.contrib.auth import views as auth_views

app_name='login'

'''urlpatterns = [
    url(r'^login/', auth_views.login, {'template_name': 'index.html'},name='login'),
    url(r'register/$',views.register, name='register'),
    url(r'password_reset/$', auth_views.password_reset, name='password_reset'),
    #url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password_reset/$', auth_views.password_reset, {'post_reset_redirect' : '/password_reset_done/'}, name='password_reset'),
     url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
     #url(r'password_reset/$', auth_views.password_reset,{'email_template_name':'accounts/registration/password_reset_email.html',
         #                                           'subject_template_name':'accounts/registration/password_reset_subject.txt',
       #                                             'post_reset_redirect':'accounts:password_reset_done',
      #                                              'from_email':'accounts@django.com',
      #                                              },name='password_reset'),

    url(r'password_reset_done/$', auth_views.password_reset_done, name='password_reset_done')]
#url(r'^logout/$', auth_views.logout,name='logout'),
#rl(r'^logg/',include('loginex.urls')),
#url(r'^log/',include(loginex.urs)) ]
'''

'''urlpatterns = [
    url(r'^login/', auth_views.login, {'template_name': 'index.html'},name='login'),
    url(r'register/$',views.register, name='register'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    
'''



urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'index.html'},name='login'),
    url(r'register/$',views.register, name='register'),
    url(r'logout/$',auth_views.logout,{'next_page': '/login'}),
    #url(r'logout/$',auth_views.LogoutView.as_view(template_name='logout.html')),
    url(r'password_change/$',auth_views.PasswordChangeView.as_view(template_name='registration\password_change.html',success_url='/password_change_done')),
    url(r'password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration\password_change_done.html')),
    url(r'password_reset/$',auth_views.PasswordResetView.as_view(template_name='registration\password_reset_form.html',email_template_name='password_reset_email.html',subject_template_name='registration\password_reset_subject.txt',success_url='/password_reset_done/',from_email='support@yoursite.ma')),
    url(r'password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='registration\password_reset_done.html')),
    url(r'password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(template_name='registration\password_reset_confirm.html',success_url='/password_reset_complete/')),
    url(r'password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration\password_reset_complete.html')),
    url(r'book/$',views.book_detail,name='book'),
    url(r'^add_book/$',views.add_book,name='AddBook')
]