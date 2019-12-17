from django import template

register = template.Library()

"""
@register ist ein decorator aus python lesson two

"""

@register.filter(name="cut")
def cut(value, arg):
    """
    this cuts out all values of arg from the String
    """

    return value.replace(arg, "")

# register.filter("cut", cut)
