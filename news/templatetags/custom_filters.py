from django import template

register = template.Library()

@register.filter
def split(value, key):
    """
    Splits a string by the given key.
    Usage: {{ value|split:"," }}
    """
    if not value:
        return []
    return value.split(key)

@register.filter
def trim(value):
    """
    Removes leading and trailing spaces from a string.
    Usage: {{ tag|trim }}
    """
    if not value:
        return ""
    return value.strip()
