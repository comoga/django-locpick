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


template::

    ...
        <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>

    ...

    {{ place.location.render_map }}


Configuration
=============

 * `GMAPICKER_STATIC_URL` - URL that handles gmapicker static directory, defaults to STATIC_URL + 'gmapicker/'.
 * `GMAPICKER_DEFAULT_MAP_WIDTH` - Default frontend map width, defaults to 200 (rendered by `location.render_map()`)
 * `GMAPICKER_DEFAULT_MAP_HEIGHT` - Default frontend map height defaults to 200 (rendered by `location.render_map()`)


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
