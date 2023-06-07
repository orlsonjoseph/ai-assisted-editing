from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from document.models import Document
from document.services import DocumentService

import json


@login_required
def edit(request, pk, template_name=None):
    if request.method == "POST":
        current_document = Document.objects.get(pk=pk)

        operations, content = request.POST.get("operations"), request.POST.get(
            "content"
        )

        operations = json.loads(operations)
        content = json.loads(content)

        DocumentService().update_document(current_document, operations, content)

        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "error"})
