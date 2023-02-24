from django.shortcuts import render

# Create your views here.


def home(request, template_name='nodraft/home.html'):
    return render(request, template_name, {})


def about(request, template_name='nodraft/about.html'):
    return render(request, template_name, {})


def stories(request, template_name='nodraft/stories.html'):
    return render(request, template_name, {})
