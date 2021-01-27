from django import template
from decimal import Decimal

register = template.Library()

@register.filter(name='saleprice')
def saleprice(item):
    return (item.price - item.price*Decimal(item.sale/100)).quantize(Decimal('1.00'))