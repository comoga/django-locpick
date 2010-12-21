from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^$', 'example.places.views.index'),
)

