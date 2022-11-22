from django import template

register = template.Library()


@register.filter(name='conc_str')
def conc_strings(str1, str2):
    return str(str1) + str(str2)


register.filter('conc_str', conc_strings)