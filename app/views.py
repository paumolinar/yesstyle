from django.shortcuts import render
from app import models

def home(request):
    products = models.Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "home.html", context)


def product_detail(request, product_id):
    print(f'product id: {product_id}')
    product = models.Product.objects.get(id=product_id)
    print(f'product: {product}')
    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)

def shopping_bag(request):
    return render(request, "shopping_bag.html")