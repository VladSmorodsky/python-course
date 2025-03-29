from django import forms

from main.models import CustomUser


def validate_unique_email(email: str) -> None:
    """
    Validates that the email is exists.
    :param email:
    :return:
    """
    existed_emails = CustomUser.objects.filter(email=email).first()
    if existed_emails:
        raise forms.ValidationError('Email already exists')


def validate_password_confirmation(password: str, password_confirmed: str) -> None:
    """
    Check password confirmation.
    :param password:
    :param password_confirmed:
    :return:
    """
    if password and password_confirmed and password != password_confirmed:
        raise forms.ValidationError("Passwords do not match.")