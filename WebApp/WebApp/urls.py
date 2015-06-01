"""WebApp URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from WebApp.Main.views import *
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Dash/$', AdminDashboard),
    url(r'^AdminSave/$',AdminSave),
    url(r'^AdminNewUser/$',AdminNewUser),
    url(r'^AdminRemoveUser/$',AdminUserRemove),
    url(r'^AdminNewOffer/$',AdminNewOffer),
    url(r'^AdminRemoveOffer/$',AdminOfferRemove),
	url(r'^AdminNewGroup/$',AdminNewGroup),
	url(r'^AdminNewArticle/$',AdminNewArticle),
	url(r'^AdminNewFriendship/$',AdminNewFriendship),
    url(r'^Upload/$',upload),
    url(r'^Upload/upload_pic/$',upload_pic),
    url(r'^setCookie/$',setCookie),
    url(r'^getCookie/$',getCookie),
    url(r'^Auth/$',AuthenticationApp),
    url(r'^Profile/$',Profile),
    url(r'^Offers/$',Offers),
    url(r'^LoginApp/$',LoginApp),
    url(r'^StartPageApp/$',StartPage),
    url(r'(?:.*?/)?(?P<path>(css|jquery|jscripts|images)/.+)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
]



