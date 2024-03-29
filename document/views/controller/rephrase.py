from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .include import generate_request


@login_required
def rephrase(request, pk, template_name=None, endpoint="rephrase"):
    content = request.POST.get("content")

    response = generate_request(content, endpoint)
    response = response["choices"]

    for item in response:
        item["text"] = item["text"].strip()

    return JsonResponse(
        {
            "status": "ok",
            "response": response,
            "endpoint": endpoint,
        }
    )
