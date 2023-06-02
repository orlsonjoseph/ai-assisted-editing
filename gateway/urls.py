from django.urls import include, path
from django.conf import settings

from gateway.views import home

urlpatterns = [
    path(settings.EMPTY_STRING, home, name="home"),
]
