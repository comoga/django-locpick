import os

from django.conf.urls.defaults import *
from django.contrib import admin

import gmapicker


admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (
        r'^static/gmapicker/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': os.path.join(os.path.dirname(gmapicker.__file__), 'static', 'gmapicker'),
        }
    ),
    (r'^$', include('example.places.urls')),
)
