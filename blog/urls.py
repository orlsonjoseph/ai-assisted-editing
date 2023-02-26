from django.urls import include, path

from blog.views import Home

urlpatterns = [
    path('home', Home.as_view(), name='home'),
]
