from django.urls import include, path

from blog.views import Home, Show

urlpatterns = [
    path('home', Home.as_view(), name='home'),
    # Show a single post
    path('show/<int:pk>', Show.as_view(), name='show'),
]
