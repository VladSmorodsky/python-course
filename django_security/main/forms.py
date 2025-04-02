from django import forms

from main.models import CustomUser
from main.validators import validate_password_confirmation, validate_unique_email


class LoginForm(forms.Form):
    """
    Login form
    """
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

    def clean_email(self) -> str:
        """
        Validate email value
        :return:
        """
        email = self.cleaned_data['email']
        validate_unique_email(email)
        return email

    def clean_password2(self) -> str:
        """
        Validate password confirmation
        :return:
        """
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password2 = cleaned_data['password2']
        validate_password_confirmation(password, password2)
        return password2
