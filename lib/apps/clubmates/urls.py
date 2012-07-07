from django.conf.urls.defaults import *

urlpatterns = patterns('clubmates.lib.apps.clubmates.views',
    url(r'^$', 'index', name="default-view"),
	url(r'^places/(?P<loc>.+?)/$', 'show_location', {}, "default-location"),
)