import os

from django.conf.urls.defaults import *
from django.contrib import admin

import locpick


admin.autodiscover()


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (
        r'^static/locpick/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': os.path.join(os.path.dirname(locpick.__file__), 'static', 'locpick'),
        }
    ),
    (r'^$', include('example.places.urls')),
)
