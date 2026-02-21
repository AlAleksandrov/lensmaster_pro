from decimal import Decimal, InvalidOperation

from django import template

register = template.Library()

@register.filter(name='eur')
def eur(value):

    if value is None or value == '':
        return '€0.00'

    try:
        dec = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        return f'€{value}'

    return f'€{dec:.2f}'
