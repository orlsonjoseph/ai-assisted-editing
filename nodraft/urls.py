from django.urls import include, path

from nodraft.views import home, about, features, pricing

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('features', features, name='features'),
    path('pricing', pricing, name='pricing'),
]
