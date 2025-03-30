from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from main.forms import TaskForm
from main.models import Task
from main.serializers import TaskSerializer


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

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer