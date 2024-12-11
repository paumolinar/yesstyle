from django.shortcuts import render
from app import models

def home(request):
    products = models.Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "home.html", context)
