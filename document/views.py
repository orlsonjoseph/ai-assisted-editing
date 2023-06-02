from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Document

import document.services as services
import json


class DocumentBaseView(View):
    model = Document
    fields = "__all__"


class DocumentListView(DocumentBaseView, ListView):
    """View to list the documents owned by <request.user>"""

    template_name = "document/list.html"

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class DocumentShowView(DocumentBaseView, View):
    """View to show a particular document"""

    template_name = "document/show.html"

    def get(self, request, pk):
        current_document = self.model.objects.get(pk=pk)

        content = current_document.get_content()
        content = json.dumps(content)

        return render(
            request,
            self.template_name,
            {"document": current_document, "content": content},
        )


class DocumentDeleteView(DocumentBaseView, DeleteView):
    """View to delete a document"""

    template_name = None


class DocumentCreateView(DocumentBaseView, View):
    """View to create a new document"""

    def get(self, request):
        services.create_document(request.user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("document:show", kwargs={"document_id": self.object.pk})


# AJAX view for updating a document
@login_required
def update(request, pk, template_name=None):
    if request.method == "POST":
        operations = request.POST.get("operations")
        operations = json.loads(operations)

        content = request.POST.get("content")
        content = json.loads(content)

        current_document = Document.objects.get(pk=pk)
        services.update_document(current_document, operations, content)

        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "error"})
