from django.urls import include, path
from django.conf import settings

from portal.views import home

urlpatterns = [
    path(settings.EMPTY_STRING, home, name="home"),
]
