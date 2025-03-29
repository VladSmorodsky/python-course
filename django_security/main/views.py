from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect

from main.forms import LoginForm, RegisterForm

from main.models import CustomUser


# Create your views here.

def login_view(request: HttpRequest) -> HttpResponse:
    """
    Login view
    :param request:
    :return:
    """
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user_object = CustomUser.objects.filter(email=email).first()
            try:
                user = authenticate(username=user_object.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "You are now logged in")
                    return redirect('home')
                else:
                    messages.error(request, "Invalid a credentials")
            except AttributeError:
                messages.error(request, "Invalid b credentials")
    else:
        form = LoginForm()
    return render(request, 'main/auth_page.html', {'form': form, 'page_title': 'Login'})


def register_view(request: HttpRequest) -> HttpResponse:
    """
    Register view
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'main/auth_page.html', {'form': form, 'page_title': 'Register'})


@login_required
def logout_view(request: HttpRequest) -> HttpResponse:
    """
    Logout a user
    :param request:
    :return:
    """
    logout(request)
    return redirect("login")


def home_view(request: HttpRequest) -> HttpResponse:
    """
    Home view
    :param request:
    :return:
    """
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, 'main/home_page.html')
