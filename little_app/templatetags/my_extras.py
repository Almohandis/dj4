from django import template

register = template.Library()


@register.filter("cute")
def cut(value, arg):
    return value.replace(arg, "")


# register.filter("cute", cut) or using decorators