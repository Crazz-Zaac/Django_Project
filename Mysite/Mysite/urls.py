"""Mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
#from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index #importing index file from the views.py
from .views import about #importing about file from the views.py
from .views import news #importing news file from the views.py
from .views import coding
from .views import materials



#admin.autodiscover()
admin.site.site_header = 'House of admin'
admin.site.site_title = 'Bytes Nepal admin'
admin.site.site_url = ''
admin.site.index_title = 'Bytes Nepal administration'
admin.empty_value_display = '**Empty**'


urlpatterns = [
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^$',index),
    url(r'^About/$',about), #lower/upper case sensitive..Must match with the one in base.html file
    url(r'^News/$',news),
    url(r'^Coding/$',coding),
    url(r'^Materials/$',materials),
    url(r'^admin/', admin.site.urls),
] 

