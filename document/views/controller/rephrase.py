from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings

from .prompts import REPHRASE_PROMPT

import openai

openai.api_key = settings.OPENAI_API_KEY


@login_required
def rephrase(request, pk, template_name=None):
    content = request.POST.get("content")

    # Commented out for now because we dont actually need to rephrase

    # response = openai.Completion.create(
    #     prompt=REPHRASE_PROMPT.format(sentence=content),
    #     # Model
    #     model=settings.MODEL,
    #     # Parameters
    #     temperature=settings.TEMPERATURE,
    #     max_tokens=settings.MAX_TOKENS,
    #     top_p=settings.TOP_P,
    #     frequency_penalty=settings.FREQUENCY_PENALTY,
    #     presence_penalty=settings.PRESENCE_PENALTY,
    #     n=settings.SAMPLES,
    # )

    response = {
        "choices": [
            {
                "finishReason": "stop",
                "index": 0,
                "logprobs": None,
                "text": "The quick brown fox jumps over the lazy dog.",
            },
            {
                "finishReason": "stop",
                "index": 1,
                "logprobs": None,
                "text": "The quick brown fox jumps over the lazy dog.",
            },
        ],
    }

    response = response["choices"]

    return JsonResponse({"status": "ok", "response": response})
