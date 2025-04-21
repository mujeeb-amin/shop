from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest

def home(request: WSGIRequest):
    
    return HttpResponse("Home Page")