from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.

def home_view(request) -> HttpResponse:
    """
    Home page view
    :param request:
    :return:
    """
    return render(request, 'home/home.html', {
        "message": 'Welcome to Main Page'
    })


def about_view(request) -> HttpResponse:
    """
    About page view
    :param request:
    :return:
    """
    return render(request, 'home/about.html', {
        "message": 'About us'
    })


def contact_view(request) -> HttpResponse:
    """
    Contact page view
    :param request:
    :return:
    """
    return render(request, 'home/contact.html', {
        "message": 'Contact us'
    })


def post_view(request, post_id: int) -> HttpResponse:
    """
    Post page view
    :param request:
    :param post_id:
    :return:
    """
    return render(request, 'home/post.html', {
        "post_id": post_id
    })


def profile_view(request, username: str) -> HttpResponse:
    """
    Profile page view
    :param request:
    :param username:
    :return:
    """
    return render(request, 'home/profile.html', {
        "username": username
    })


def event_view(request, year: int, month: int, day: int) -> HttpResponse:
    """
    Event page view
    :param request:
    :param year:
    :param month:
    :param day:
    :return:
    """
    return render(request, 'home/event.html', {
        "event_date": f"{year}-{month}-{day}"
    })
