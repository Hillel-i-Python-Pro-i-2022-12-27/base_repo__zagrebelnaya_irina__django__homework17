from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def about(request: WSGIRequest):
    return render(
        request=request,
        template_name="about.html",
    )
