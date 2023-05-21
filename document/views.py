from django.shortcuts import render
from django.decorators import login_required


@login_required
def dashboard(request, template_name="document/dashboard.html"):
    return render(request, template_name, {})


# Views for a particular document
@login_required
def editor(request, document_id, template_name="document/editor.html"):
    return render(request, template_name, {})
