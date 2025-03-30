from datetime import datetime

from django import forms
from pytz import timezone


def validate_title(value: str) -> str:
    """
    Validate title
    :param value:
    :return:
    """
    if value.strip() == "":
        raise forms.ValidationError("Title cannot be empty")
    return value


def validate_due_date(value: datetime) -> datetime:
    """
    Validates due date value
    :param value:
    :return:
    """
    due_date = value

    if due_date < datetime.now().replace(tzinfo=timezone('UTC')):
        raise forms.ValidationError('Due date must be in the future')
    return due_date
