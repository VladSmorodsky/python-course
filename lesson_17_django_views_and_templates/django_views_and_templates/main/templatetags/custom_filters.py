import random

from django import template

register = template.Library()


@register.filter(name='random_id')
def random_id(value: str) -> str:
    """
    Custom template's filter that return random number
    :param value: str
    :return:
    """
    if value is None or value == '':
        value = 'item'
    number = random.randint(1, 1000)
    return f"{value}-{number}"
