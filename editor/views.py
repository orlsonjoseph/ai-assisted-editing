from django.shortcuts import render
from django.decorators import login_required


@login_required
def dashboard(request, template_name="editor/dashboard.html"):
    return render(request, template_name, {})
