Show where your business, venue, party, etc. is on Google Maps.

Features
========

* ``LocationField`` to hold a location plus a color marker in the database.
* A template tag to display the map to your users.
* Admin interface to create, edit, and edit the map preview with the map
  marker.


Installation
============

Install from here using ``pip``::

    pip install -e git+git://github.com/comoga/django-locpick#egg=django-locpick


Quick Setup
===========

With ``django.contrib.staticfiles`` (from Django 1.3)::

    INSTALLED_APPS = (
        ...
        'django.contrib.staticfiles',
        'locpick',
    )

    STATIC_URL = ... # see staticfiles documentation

Without ``django.contrib.staticfiles``::

    INSTALLED_APPS = (
        ...
        'locpick',
    )

    LOCPICK_STATIC_URL = ... # 'LOCPICK_CHECKOUT_DIR/locpick/static/locpick/'


Usage
=====

Add ``LocationField`` to your ``models.py``::

    from locpick.field import LocationField

    class Place(models.Model)
        ...
        location = LocationField()


To display the map on the frontend, include this javascript code::

    <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>


Then, use ``LocationField.render_map()``::

    {{ place.location.render_map }}


Or use the template tag ``gmap`` to display and specify the map's size::

    {% load gmap %}
    {% gmap place.location WIDTH HEIGHT %}


Additional features
-------------------

Display an external link (Google Maps) to the map::

    <a href="{{ place.location.external_url }}">Map</a>


Configuration
=============

Customize the default configuration in your ``settings.py``::

 * `LOCPICK_STATIC_URL` - URL that handles locpick static directory, defaults to STATIC_URL + 'locpick/'.
 * `LOCPICK_DEFAULT_MAP_WIDTH` - Default frontend map width, defaults to 200 (rendered by `location.render_map()`)
 * `LOCPICK_DEFAULT_MAP_HEIGHT` - Default frontend map height, defaults to 200 (rendered by `location.render_map()`)


Screenshots
===========

.. figure:: https://github.com/aleszoulek/django-locpick/raw/master/doc/screenshot_admin.png

   The admin's changeform.

.. figure:: https://github.com/aleszoulek/django-locpick/raw/master/doc/screenshot_frontend.png

   A map rendered on the frontend.



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
