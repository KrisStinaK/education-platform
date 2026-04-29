from django import template
from django.utils.safestring import mark_safe

import markdown

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.filter
def get_range(value):
    return range(1, value + 1)


@register.filter
def len_f(value):
    return len_f(value)