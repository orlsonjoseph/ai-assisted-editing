from django.shortcuts import render

# Create your views here.


def home(request, template_name='nodraft/home.html'):
    return render(request, template_name, {})


def about(request, template_name='nodraft/about.html'):
    return render(request, template_name, {})


def features(request, template_name='nodraft/features.html'):
    return render(request, template_name, {})


def pricing(request, template_name='nodraft/pricing.html'):
    return render(request, template_name, {})
