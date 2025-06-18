from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from products.models import Product


def get_products(request: WSGIRequest):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})
