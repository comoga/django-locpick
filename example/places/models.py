from django.db import models

from gmapicker.field import LocationField


class Place(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    location = LocationField()

    def __unicode__(self):
        return self.name
