from django.urls import include, path

from surveys.views import dashboard

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
]
