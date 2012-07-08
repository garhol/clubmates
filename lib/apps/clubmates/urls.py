from django.conf.urls.defaults import *

urlpatterns = patterns('clubmates.lib.apps.clubmates.views',
    url(r'^$', 'index', name="default-view"),
    url(r'^places/$', 'index', name="redir"),
    url(r'^places/(?P<loc>.+?)/$', 'show_location', {}, "default-location"),
    url(r'^venue/(?P<loc>.+?)/$', 'show_venue', {}, "default-venue"),
)