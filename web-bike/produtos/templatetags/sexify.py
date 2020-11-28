# -*- coding: utf-8 -*-
from django import template
from django.utils.translation import to_locale, get_language
from babel.numbers import format_decimal

register = template.Library()


def sexy_number(context, number, locale=None):
    if locale is None:
        locale = to_locale(get_language())
        # print(locale)
        number = number.replace(",", ".")
    return format_decimal(number, locale=locale)


register.simple_tag(takes_context=True)(sexy_number)

