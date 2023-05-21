from django import template

from config import settings

register = template.Library()


@register.filter
def letter_limit(value):
    return value[:99]


@register.filter
def mediapath(file_path):
    return "{}{}".format(settings.MEDIA_URL, file_path)


@register.simple_tag
def mediapath(file_path):
    return "{}{}".format(settings.MEDIA_URL, file_path)
