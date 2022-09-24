from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class Login(TemplateView):
    template_name = 'accounts/login.html'


class Register(TemplateView):
    template_name = 'accounts/register.html'
