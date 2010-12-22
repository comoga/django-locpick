Installation
============

Install from here using ``pip``::

    pip install -e git+git://github.com/comoga/django-gmapicker#egg=django-gmapicker


Quick Setup
===========

With `django.contrib.staticfiles` (from Django 1.3)::

    INSTALLED_APPS = (
        ...
        'django.contrib.staticfiles',
        'gmapicker',
    )

    STATIC_URL = ... # see staticfiles documentation


Other::

    INSTALLED_APPS = (
        ...
        'gmapicker',
    )

    GMAPICKER_STATIC_URL = ... # 'GMAPICKER_CHECKOUT_DIR/gmapicker/static/gmapicker/'


Usage
=====

models.py::

    from gmapicker.field import LocationField

    class Place(models.Model)
        ...
        location = LocationField()


display map on frontend::

    ...
        <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>

    ...

    {{ place.location.render_map }}

    or if you want a non-default map dimensions, you can use:

    {% load gmap %}
    {% gmap place.location WIDTH HEIGHT %}

display link to the map::

    <a href="{{ place.location.external_url }}">Map</a>



Configuration
=============

 * `GMAPICKER_STATIC_URL` - URL that handles gmapicker static directory, defaults to STATIC_URL + 'gmapicker/'.
 * `GMAPICKER_DEFAULT_MAP_WIDTH` - Default frontend map width, defaults to 200 (rendered by `location.render_map()`)
 * `GMAPICKER_DEFAULT_MAP_HEIGHT` - Default frontend map height defaults to 200 (rendered by `location.render_map()`)


Screenshots
===========

.. figure:: https://github.com/aleszoulek/django-gmapicker/raw/master/doc/screenshot_admin.png

   The admin's changeform.

.. figure:: https://github.com/aleszoulek/django-gmapicker/raw/master/doc/screenshot_frontend.png

   Map rended on frontend.




Changelog
=========

0.3
---
 * Added Django 1.2 backwards compatibility
 * Removed frontend jQuery dependency
 * Added this README file
 * Added support for multiple maps on one page
 * Added example project
 * Added GMAPICKER_DEFAULT_MAP_WIDTH and GMAPICKER_DEFAULT_MAP_HEIGHT settings options
 * Added template tag `gmap`
 * Added `external_url` field property
