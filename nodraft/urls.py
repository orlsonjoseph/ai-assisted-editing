from django.urls import include, path

from nodraft.views import home, about, stories

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('stories', stories, name='stories'),
]
