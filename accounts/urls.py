from django.urls import include, path

from accounts.views import Login, Logout, Profile, Register

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),

    path('profile', Profile.as_view(), name='profile'),

    path('register', Register.as_view(), name='register'),

]
