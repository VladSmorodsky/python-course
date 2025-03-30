from django.urls.conf import path
from rest_framework.routers import DefaultRouter

from main import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='tasks')

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns += router.urls
