from django import forms
from django.contrib.auth.forms import AuthenticationForm

from main.models import CustomUser


def validate_email(email: str) -> None:
    """
    Validates that the email is exists.
    :param email:
    :return:
    """
    existed_emails = CustomUser.objects.get(email=email)
    if existed_emails.count():
        raise forms.ValidationError('Email already exists')


class LoginForm(forms.Form):
    """
    Login form
    """
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    # class Meta:
    #     model = CustomUser
    #     fields = ('email', 'password')