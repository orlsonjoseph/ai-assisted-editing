from django.urls import include, path

from nodraft.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home')
]
