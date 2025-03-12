from django.urls.conf import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
]
