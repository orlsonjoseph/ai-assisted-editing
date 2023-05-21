from django.urls import include, path

from document.views import dashboard, editor

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("editor/<int:document_id>/", editor, name="editor"),
]
