from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import TemplateView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from surveys.models import Survey

# Create your views here.


@login_required
def dashboard(request, template_name='surveys/dashboard.html'):
    surveys = request.user.surveys.all()
    return render(request, template_name, {'surveys': surveys})


@method_decorator(login_required, name='dispatch')
class Create(TemplateView):
    template_name = 'surveys/create.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')

        survey = Survey.objects.create(
            author=request.user,
            title=title,
            description=description,
        )
        if survey:
            return redirect('surveys:edit', id=survey.id)
        else:
            messages.error(request, 'Error creating survey')
            return render(request, self.template_name, {})


@method_decorator(login_required, name='dispatch')
class Edit(TemplateView):
    template_name = 'surveys/edit.html'

    def get(self, request, *args, **kwargs):
        survey = Survey.objects.get(pk=kwargs.get('id'))
        return render(request, self.template_name, {
            'survey': survey,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
