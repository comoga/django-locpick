from django.db import models

from gmapicker.widget import LocationPickerWidget
from django.template import loader



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
        return Map.from_db(instance.__dict__[self.field.name])

    def __set__(self, instance, value):
        instance.__dict__[self.field.name] = value


class Map(object):

    def __init__(self, position, center, zoom):
        self.position = position
        self.center = center
        self.zoom = zoom

    @classmethod
    def from_db(cls, value):
        values = value.split(',')
        return cls(
            position=(float(values[0]), float(values[1])),
            center=(float(values[2]), float(values[3])),
            zoom=int(values[4]),
        )

    def render_map(self, width=200, height=200):
        return loader.render_to_string(
            'gmapicker/map.html',
            {
                'map': self,
                'width': width,
                'height': height,
            }
        )



try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    pass
else:
    add_introspection_rules([], [r"^gmapicker\.field\.LocationField"])
