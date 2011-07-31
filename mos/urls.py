import settings

from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from mos.cal.feeds import EventFeed


feeds = {
        'events': EventFeed,
        }

admin.autodiscover()

urlpatterns = patterns('',
   (r'^feeds/(?P<url>.*)/$',
      'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

    (r'^calendar/', include('mos.cal.urls')),
    (r'^rss/', include('mos.rss.urls')),

    (r'^project/', include('mos.projects.urls')),

    (r'^$', 'mos.web.views.display_main_page'),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^member/', include('mos.members.urls')),

    (r'^wiki/.*$', 'mos.web.views.wikipage'),
#    (r'^usbherelist/', include('mos.usbherelist.urls')),

    (r'^announce/$', include('mos.announce.urls')),

    (r'^cellardoor/', 'mos.web.views.display_cellardoor'),
)

urlpatterns += staticfiles_urlpatterns()
