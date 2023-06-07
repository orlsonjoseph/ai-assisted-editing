from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .base import DocumentBaseView

from document.services import DocumentService


class DocumentCreateView(DocumentBaseView, View):
    """View to create a new document"""

    def get(self, request):
        self.object = DocumentService().create(request.user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("document:show", kwargs={"pk": self.object.pk})
