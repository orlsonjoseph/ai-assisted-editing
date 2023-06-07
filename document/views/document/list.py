from django.views import View
from django.views.generic.list import ListView

from .base import DocumentBaseView


class DocumentListView(DocumentBaseView, ListView):
    """View to list the documents owned by <request.user>"""

    template_name = "document/list.html"

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)
