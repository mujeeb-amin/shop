from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


# def home(request: WSGIRequest):

#     return HttpResponse("<h1>Home Page</h1>")


def home(request):

    return render(request, "index.html")
