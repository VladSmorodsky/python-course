from django.urls.conf import path

from main import views

urlpatterns = [
    path('', views.home, name='home'),
]