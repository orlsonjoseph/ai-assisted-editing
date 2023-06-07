from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from document.models import Document
from document.services import DocumentService


@login_required
def update(request, pk, template_name=None):
    if request.method == "POST":
        current_document = Document.objects.get(pk=pk)
        title = request.POST.get("title")

        DocumentService().update_title(current_document, title)
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "error"})
