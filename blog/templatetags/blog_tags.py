from django import template

register= template.Library()

@register.simple_tag

def hfunction(a):
    return a + 2