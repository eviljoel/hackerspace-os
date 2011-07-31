from django.conf.urls.defaults import *
from hos import settings

urlpatterns = patterns('',
    (r'^$', 'hos.announce.views.announce'),
)
