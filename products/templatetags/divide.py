import decimal
from django import template

register = template.Library()


@register.simple_tag
def divide(a, b):
    division = decimal.Decimal(a) / decimal.Decimal(b)
    return division


@register.simple_tag
def multiply(a, b):
    return a * b
