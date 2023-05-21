from django.urls import include, path

from editor.views import dashboard

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
]
