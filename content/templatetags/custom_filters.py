# content/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def endswith(value, arg):
    """
    Returns True if the given string ends with the specified argument.
    Usage in template: {% if string|endswith:"suffix" %}
    """
    if isinstance(value, str):
        return value.endswith(arg)
    return False
