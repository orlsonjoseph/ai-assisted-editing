from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from django.contrib import messages
# Create your views here.


class Home(TemplateView):
    template_name = 'blog/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
