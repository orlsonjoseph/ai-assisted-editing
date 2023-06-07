from django.views import View

from document.models import Document


class DocumentBaseView(View):
    model = Document
    fields = "__all__"
