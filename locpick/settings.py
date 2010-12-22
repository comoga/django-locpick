from django.conf import settings


DEFAULT_MAP_WIDTH = getattr(settings, 'LOCPICK_DEFAULT_MAP_WIDTH', 200)
DEFAULT_MAP_HEIGHT = getattr(settings, 'LOCPICK_DEFAULT_MAP_HEIGHT', 200)

