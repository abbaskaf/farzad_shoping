from django.shortcuts import render
from .models import Category, Product


def HomeView(request):
    post = Product.objects.all()
    return render(request, 'index.html', {'post': post})


def ShopView(request):
    return render(request,'shop.html')


def AboutView(request):
    return render(request, 'about.html')


def ContactView(request):
    return render(request, 'contact.html')


def ShopSingleView(request):
    return render(request, 'shop-single.html')