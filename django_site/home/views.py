from pyexpat.errors import messages

from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.

def home_view(request) -> HttpResponse:
    """
    Home page view
    :param request:
    :return:
    """
    return render(request, 'home.html', {
        "message": 'Welcome to Main Page'
    })


def about_view(request) -> HttpResponse:
    """
    About page view
    :param request:
    :return:
    """
    return render(request, 'about.html', {
        "message": 'About us'
    })


def contact_view(request) -> HttpResponse:
    """
    Contact page view
    :param request:
    :return:
    """
    return render(request, 'contact.html', {
        "message": 'Contact us'
    })


def post_view(request, post_id: int) -> HttpResponse:
    """
    Post page view
    :param request:
    :param post_id:
    :return:
    """
    return render(request, 'post.html', {
        "post_id": post_id
    })


def profile_view(request, username: str) -> HttpResponse:
    return render(request, 'profile.html', {
        "username": username
    })


def event_view(request, year: int, month: int, day: int) -> HttpResponse:
    return render(request, 'event.html', {
        "event_date": f"{year}-{month}-{day}"
    })
    # return HttpResponse(f'Event date: {year}-{month}-{day}')
