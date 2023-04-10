import re

from schematics.exceptions import ValidationError


def is_uppercase(value):
    if value.upper() != value:
        raise ValidationError('Field should be uppercase.')
    return value


def is_email_valid(value):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not re.fullmatch(regex, value):
        raise ValidationError('E-mail address invalid.')
    return value


def is_over_18(value):
    if value < 18:
        raise ValidationError('User cannot be underage.')
    return value
