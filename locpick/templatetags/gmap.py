from django import template

from locpick import settings


register = template.Library()


class LocpickNode(template.Node):
    def __init__(self, field, width=settings.DEFAULT_MAP_WIDTH, height=settings.DEFAULT_MAP_HEIGHT):
        self.field_name = field
        self.width = width
        self.height = height

    def render(self, context):
        field = template.Variable(self.field_name).resolve(context)
        return field.render_map(width=self.width, height=self.height)


@register.tag
def gmap(parser, token):
    bits = token.split_contents()
    if len(bits) == 2:
        return LocpickNode(field=bits[1])
    elif len(bits) == 4:
        return LocpickNode(field=bits[1], width=bits[2], height=bits[3])
    else:
        raise template.TemplateSyntaxError('{% locpick instance.location_field %} or {% locpick instance.location_field WIDTH HEIGHT %}')
