from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Gender
from django.views.generic import TemplateView, DetailView, ListView


def HomeView(request, **kwargs):
    post = Product.objects.filter(status=Product.StatusChoices.publish)[0:3]
    post1 = Product.objects.filter(status=Product.StatusChoices.publish)[3:6]
    return render(request, 'index.html', {'post': post, 'post1': post1})


def AllShop(request):
    post = Product.objects.all()
    return render(request, 'shop.html', {'post': post})


class ShopView(TemplateView):
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gender_slug = kwargs['gender_slug']
        gender = get_object_or_404(Gender, gender=gender_slug)
        post = Product.objects.filter(genders=gender)
        context['gender'] = gender
        context['post'] = post
        return context


def SportShop(request, **kwargs):
    category_slug = kwargs['category_slug']
    cate = get_object_or_404(Category, title=category_slug)
    post = Product.objects.filter(category=cate)
    return render(request, 'sport.html', {'cate': cate, 'post': post}, )


class SportView(TemplateView):
    template_name = 'sport.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        gender_slug = kwargs['gender_slug']
        category_slug = kwargs['category_slug']
        category = get_object_or_404(Category, title=category_slug)
        gender = get_object_or_404(Gender, gender=gender_slug)
        post = Product.objects.filter(genders=gender, category=category)
        context['gender'] = gender
        context['category'] = category
        context['post'] = post
        return context


def LuxShop(request, **kwargs):
    category_slug = kwargs['category_slug']
    cate = get_object_or_404(Category, title=category_slug)
    post = Product.objects.filter(category=cate)
    return render(request, 'lux.html', {'cate': cate, 'post': post}, )


class LuxView(TemplateView):
    template_name = 'lux.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        gender_slugs = kwargs['gender_slugs']
        category_slugs = kwargs['category_slugs']
        category = get_object_or_404(Category, title=category_slugs)
        gender = get_object_or_404(Gender, gender=gender_slugs)
        post = Product.objects.filter(genders=gender, category=category)
        context['gender'] = gender
        context['category'] = category
        context['post'] = post
        return context


def AboutView(request):
    return render(request, 'about.html')


def ContactView(request):
    return render(request, 'contact.html')


class ShopSingle(DetailView):
    model = Product
    template_name = 'shop-single.html'

    def get_context_data(self, **kwargs, ):
        context = super().get_context_data()
        posts = Product.objects.filter(status=Product.StatusChoices.publish)[:8]
        context['posts'] = posts
        return context
