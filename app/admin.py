from django.contrib import admin
from .models import Category, Product, Gender


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['gender']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'genders', 'category', 'price', 'brand']
