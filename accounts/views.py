from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from accounts.models import CustomUser
# Create your views here.


class Login(TemplateView):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('nodraft:dashboard')
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('nodraft:dashboard')

        messages.error(request, 'Invalid Credentials')
        return render(request, self.template_name, {})


class Register(TemplateView):
    template_name = 'accounts/register.html'
