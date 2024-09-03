from django import template

register = template.Library()

@register.filter
def multiply(arg, value):
    result = round(arg * value, 2)
    result_str = "{:.2f}".format(result).rstrip('0').rstrip('.').replace(".", ",")
    return result_str
