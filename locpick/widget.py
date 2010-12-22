from django import forms
from django.conf import settings


if hasattr(settings, 'LOCPICK_STATIC_URL'):
    STATIC_URL = settings.LOCPICK_STATIC_URL
else:
    STATIC_URL = settings.STATIC_URL + 'locpick/'


class LocationPickerWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                STATIC_URL + 'location_picker.css',
            )
        }
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js',
            'http://maps.google.com/maps/api/js?sensor=false',
            STATIC_URL + 'jquery.location_picker.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(LocationPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        if None == attrs:
            attrs = {}
        attrs['class'] = 'location_picker'
        return super(LocationPickerWidget, self).render(name, value, attrs)

