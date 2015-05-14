from django.conf.urls import patterns, include, url
from django.contrib import admin
from HerokuFBLogin.Main.views import *
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HerokuFBLogin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', index),
    url(r'hacking/',hacking),
    url(r'(?:.*?/)?(?P<path>(css|jquery|jscripts|images)/.+)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT})
)
