from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


def homePage(request):
    products = Product.objects.all()

    context = {"products": products}
    return render(request, "base/frontpage.html", context)

def aboutPage(request):
    return render(request, 'base/about.html')

def productPage(request, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {"product": product}
    return render(request, "base/product_detail.html", context)


