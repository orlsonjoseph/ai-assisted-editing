from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# from .include import generate_request


@login_required
def complete(request, pk, template_name=None, endpoint="complete"):
    content = request.POST.get("content")

    response = generate_request(content, endpoint)
    response = response["choices"]

    return JsonResponse(
        {
            "status": "ok",
            "response": response,
            "endpoint": endpoint,
        }
    )
