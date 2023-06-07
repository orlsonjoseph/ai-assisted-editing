from django.views.generic.edit import DeleteView

from .base import DocumentBaseView


class DocumentDeleteView(DocumentBaseView, DeleteView):
    """View to delete a document"""

    template_name = None
