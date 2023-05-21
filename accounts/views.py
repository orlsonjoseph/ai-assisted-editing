from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import TemplateView

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from accounts.models import CustomUser


class Login(TemplateView):
    template_name = "accounts/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect("portal:home")

        messages.error(request, "Invalid email or password.")
        return HttpResponse(status=401, reason="Invalid email or password.")


class Register(TemplateView):
    template_name = "accounts/register.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        password = request.POST.get("password")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return HttpResponse(status=401, reason="Email already registered.")

        user = CustomUser.objects.create_user(email=email, password=password)
        messages.success(request, "Successfully registered.")

        login(request, user)
        return redirect("portal:home")
