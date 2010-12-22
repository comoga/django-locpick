from django.conf import settings


DEFAULT_MAP_WIDTH = getattr(settings, 'GMAPICKER_DEFAULT_MAP_WIDTH', 200)
DEFAULT_MAP_HEIGHT = getattr(settings, 'GMAPICKER_DEFAULT_MAP_HEIGHT', 200)

