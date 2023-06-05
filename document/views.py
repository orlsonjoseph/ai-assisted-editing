from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Document
from .services import (
    ChangeService,
    DocumentService,
    SnapshotService,
    VersionService,
)

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
        document = self.model.objects.get(pk=pk)
        context = {"document": document}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        if request.method == "POST":
            content = self.model.objects.get(pk=pk).get_content()
            return JsonResponse(content, safe=False)


class DocumentDeleteView(DocumentBaseView, DeleteView):
    """View to delete a document"""

    template_name = None


class DocumentCreateView(DocumentBaseView, View):
    """View to create a new document"""

    def get(self, request):
        self.object = DocumentService().create(request.user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("document:show", kwargs={"pk": self.object.pk})


# AJAX view for updating a document
# TODO unsafe keys from client


@login_required
def update(request, pk, template_name=None):
    if request.method == "POST":
        current_document = Document.objects.get(pk=pk)
        target = request.POST.get("target")

        if target == "title":
            title = request.POST.get("title")

            DocumentService().update_title(current_document, title)
        elif target == "content":
            operations = request.POST.get("operations")
            operations = json.loads(operations)

            content = request.POST.get("content")
            content = json.loads(content)

            DocumentService().update_document(current_document, operations, content)
        else:
            return JsonResponse({"status": "error"})
        return JsonResponse({"status": "ok"})


# update title
# put url in title element
# refactor javascript code to isolate components
@login_required
def update_title(request, pk, template_name=None):
    if request.method == "POST":
        current_document = Document.objects.get(pk=pk)
        title = request.POST.get("title")

        DocumentService().update_title(current_document, title)
        return JsonResponse({"status": "ok"})
