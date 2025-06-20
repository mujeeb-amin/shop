from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from products.models import Product


def get_products(request: WSGIRequest):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})


def get_product(request: WSGIRequest, product_id: int):
    product = Product.objects.get(id=product_id)
    return render(request, "products/detail.html", {"product": product})
