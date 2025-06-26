from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from products.models import Product, Category
from django.urls import reverse


def get_products(request: WSGIRequest):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})


def get_product(request: WSGIRequest, product_id: int):
    product = Product.objects.get(id=product_id)
    return render(request, "products/detail.html", {"product": product})


def create_product(request: WSGIRequest):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "products/create.html", {"categories": categories})

    title = request.POST.get("title")
    price = request.POST.get("price")
    is_published = request.POST.get("is_published")
    type = request.POST.get("type")
    category_id = request.POST.get("category")

    category = Category.objects.get(id=category_id)

    Product.objects.create(
        title=title,
        price=price,
        is_published=True if is_published == "on" else False,
        type=type,
        category=category,
    )

    return redirect(reverse("products:product_list"))


def update_product(request: WSGIRequest, product_id):
    if request.method == "GET":
        categories = Category.objects.all()
        product = Product.objects.get(id=product_id)
        return render(
            request,
            "products/update.html",
            {"categories": categories, "product": product},
        )

    title = request.POST.get("title")
    price = request.POST.get("price")
    is_published = request.POST.get("is_published")
    type = request.POST.get("type")
    category_id = request.POST.get("category")

    category = Category.objects.get(id=category_id)

    Product.objects.filter(id=product_id).update(
        title=title,
        price=price,
        is_published=True if is_published == "on" else False,
        type=type,
        category=category,
    )

    return redirect(reverse("products:product_get", kwargs={"product_id": product_id}))


def delete_product(request: WSGIRequest, product_id: int):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect(reverse("products:product_list"))
