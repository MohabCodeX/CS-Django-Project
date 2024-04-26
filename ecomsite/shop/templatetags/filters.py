# filters.py

from django import template

register = template.Library()

def format_price(value):
    return "{:,.0f}".format(value)

register.filter('format_price', format_price)
