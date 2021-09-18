from django import template

from baskets.models import Basket

register = template.Library()

@register.filter(name='total_quantity')
def total_quantity(value,user):
    return Basket.total_quantity(user)

@register.filter(name='total_sum')
def total_sum(value,user):
    return Basket.total_sum(user)