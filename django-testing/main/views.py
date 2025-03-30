from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from main.forms import TaskForm


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    """
    Renders the home page with form
    :param request:
    :return:
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()
    return render(request, 'main/home_page.html', {'form': form})
