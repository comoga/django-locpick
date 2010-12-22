Installation
============

Install from here using ``pip``::

    pip install -e git+git://github.com/comoga/django-locpick#egg=django-locpick


Quick Setup
===========

With `django.contrib.staticfiles` (from Django 1.3)::

    INSTALLED_APPS = (
        ...
        'django.contrib.staticfiles',
        'locpick',
    )

    STATIC_URL = ... # see staticfiles documentation


Other::

    INSTALLED_APPS = (
        ...
        'locpick',
    )

    LOCPICK_STATIC_URL = ... # 'LOCPICK_CHECKOUT_DIR/locpick/static/locpick/'


Usage
=====

models.py::

    from locpick.field import LocationField

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

 * `LOCPICK_STATIC_URL` - URL that handles locpick static directory, defaults to STATIC_URL + 'locpick/'.
 * `LOCPICK_DEFAULT_MAP_WIDTH` - Default frontend map width, defaults to 200 (rendered by `location.render_map()`)
 * `LOCPICK_DEFAULT_MAP_HEIGHT` - Default frontend map height defaults to 200 (rendered by `location.render_map()`)


Screenshots
===========

.. figure:: https://github.com/aleszoulek/django-locpick/raw/master/doc/screenshot_admin.png

   The admin's changeform.

.. figure:: https://github.com/aleszoulek/django-locpick/raw/master/doc/screenshot_frontend.png

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
 * Added LOCPICK_DEFAULT_MAP_WIDTH and LOCPICK_DEFAULT_MAP_HEIGHT settings options
 * Added template tag `gmap`
 * Added `external_url` field property
