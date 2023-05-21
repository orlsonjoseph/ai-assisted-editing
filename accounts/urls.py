from django.urls import include, path

from accounts.views import Login, Register

urlpatterns = [
    path("login", Login.as_view(), name="login"),
    path("register", Register.as_view(), name="register"),
]
