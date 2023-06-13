from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# from .include import generate_request


@login_required
def summarize(request, pk, template_name=None, endpoint="summarize"):
    content = request.POST.get("content")

    response = generate_request(content, endpoint)
    response = response["choices"]

    # TODO handle sad paths and not return primary key in context
    return JsonResponse(
        {
            "status": "ok",
            "response": response,
            "endpoint": endpoint,
        }
    )
