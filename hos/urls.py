import settings

from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from hos.cal.feeds import EventFeed


feeds = {
        'events': EventFeed,
        }

admin.autodiscover()

urlpatterns = patterns('',
   (r'^feeds/(?P<url>.*)/$',
      'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

    (r'^calendar/', include('hos.cal.urls')),
    (r'^rss/', include('hos.rss.urls')),

    (r'^project/', include('hos.projects.urls')),

    (r'^$', 'hos.web.views.display_main_page'),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^member/', include('hos.members.urls')),

    (r'^wiki/.*$', 'hos.web.views.wikipage'),
#    (r'^usbherelist/', include('hos.usbherelist.urls')),

    (r'^announce/$', include('hos.announce.urls')),

    (r'^cellardoor/', 'hos.web.views.display_cellardoor'),
)

urlpatterns += staticfiles_urlpatterns()
