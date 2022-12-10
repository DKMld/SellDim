from django import template

from Selldim.products.models import Products

register = template.Library()


@register.simple_tag
def get_db_object(value):
    return Products.objects.filter(id=value).get()


# register.simple_tag(get_db_object)