from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from .base import DocumentBaseView


class DocumentShowView(DocumentBaseView, View):
    """View to show a particular document"""

    template_name = "document/show.html"

    def get(self, request, pk):
        return render(
            request, self.template_name, {"document": self.model.objects.get(pk=pk)}
        )

    def post(self, request, pk):
        if request.method == "POST":
            content = self.model.objects.get(pk=pk).get_content()
            return JsonResponse(content, safe=False)
