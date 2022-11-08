from django.urls import include, path

from nodraft.views import home, about, features, pricing
from nodraft.views import dashboard

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('features', features, name='features'),
    path('pricing', pricing, name='pricing'),

    path('dashboard', dashboard, name='dashboard'),
]
