from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect

from main.forms import LoginForm

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
                print(user)
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

@login_required
def home_view(request: HttpRequest) -> HttpResponse:
    """
    Home view
    :param request:
    :return:
    """
    return render(request, 'main/home_page.html')