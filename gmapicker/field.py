from django.db import models
from django.template import loader

from gmapicker import settings
from gmapicker.widget import LocationPickerWidget


class LocationField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 100
        return super(LocationField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = LocationPickerWidget
        return super(LocationField, self).formfield(**kwargs)

    def contribute_to_class(self, cls, name):
        super(LocationField, self).contribute_to_class(cls, name)
        setattr(cls, self.name, LocationFieldDescriptor(self))


class LocationFieldDescriptor(object):

    def __init__(self, field):
        self.field = field

    def __get__(self, instance=None, owner=None):
        if instance is None:
            raise AttributeError(
                "The '%s' attribute can only be accessed from %s instances."
                % (self.field.name, owner.__name__))
        return Map(instance.__dict__[self.field.name])

    def __set__(self, instance, value):
        instance.__dict__[self.field.name] = value


class Map(object):

    def __init__(self, value):
        self.value = value
        self.position = None
        self.center = None
        self.zoom = None
        if value:
            values = value.split(',')
            self.position = (float(values[0]), float(values[1]))
            self.center = (float(values[2]), float(values[3]))
            self.zoom = int(values[4])

    def __str__(self):
        return str(self.value)

    def __unicode__(self):
        return unicode(self.value)

    def __repr__(self):
        return unicode(self)

    def __nonzero__(self):
        return bool(self.value)

    def render_map(self, width=settings.DEFAULT_MAP_WIDTH, height=settings.DEFAULT_MAP_HEIGHT):
        return loader.render_to_string(
            'gmapicker/map.html',
            {
                'id': id(self),
                'map': self,
                'width': width,
                'height': height,
            }
        )

    @property
    def external_url(self):
        return "http://maps.google.com/?ll=%s,%s&z=%s&q=%s,%s" % (
            self.center[0],
            self.center[1],
            self.zoom,
            self.position[0],
            self.position[1],
        )



try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    pass
else:
    add_introspection_rules([], [r"^gmapicker\.field\.LocationField"])
