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


class DocumentShowView(DocumentBaseView, DetailView):
    """View to show a particular document"""

    template_name = "document/show.html"


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
        delta = request.POST.get("delta")
        delta = json.loads(delta)

        state = request.POST.get("state")
        state = json.loads(state)

        print(delta, state)

        current_document = Document.objects.get(pk=pk)
        services.update_document(current_document, delta, state)

        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "error"})
