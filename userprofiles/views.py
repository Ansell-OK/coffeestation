from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Shop, Userprofile
from base.models import Product



def profilePage(request):
    return render(request, 'base/profilepage.html')

def shopPage(request, slug):
    shop = get_object_or_404(Shop, slug=slug)
    shop_products = shop.user.products.all()
    context = {"shop": shop, "products": shop_products}

    return render(request, 'base/vendorpage.html', context )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = Userprofile.objects.create(user=user)

            return redirect('home')
    else: 
        form = UserCreationForm()
    

    return render(request, 'base/signup.html', {'form': form})
