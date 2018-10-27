from django import template

register = template.Library()

@register.filter(name='resto')
def resto(value, arg):
     return int(value) % int(arg)


