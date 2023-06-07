from django.urls import include, path
from django.conf import settings

from document.views import (
    # Class based views
    DocumentCreateView,
    DocumentListView,
    DocumentShowView,
    DocumentDeleteView,
    # Function based views
    edit,
    update,
    # API endpoints
    rephrase,
)

urlpatterns = [
    path(settings.EMPTY_STRING, DocumentListView.as_view(), name="list"),
    path("create/", DocumentCreateView.as_view(), name="create"),
    path("<int:pk>/show/", DocumentShowView.as_view(), name="show"),
    path("<int:pk>/delete/", DocumentDeleteView.as_view(), name="delete"),
    path("<int:pk>/edit/", edit, name="edit"),
    path("<int:pk>/update/", update, name="update"),
    # API endpoints
    path("<int:pk>/api/rephrase/", rephrase, name="rephrase"),
]
