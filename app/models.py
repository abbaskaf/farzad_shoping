from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=50, null=True, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Gender(models.Model):
    gender = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.gender


class Product(models.Model):
    class StatusChoices(models.Choices):
        publish = _('publish')
        draft = _('draft')

    image = models.ImageField(upload_to='posts/', verbose_name='image_product', null=False, blank=False)
    image1 = models.ImageField(upload_to='posts/', verbose_name='image_product', default='1')
    image2 = models.ImageField(upload_to='posts/', verbose_name='image_product', default='2')
    image3 = models.ImageField(upload_to='posts/', verbose_name='image_product', default='3')
    name = models.CharField(max_length=100, null=True, blank=False)
    brand = models.CharField(max_length=100, null=True, blank=False)
    genders = models.ForeignKey(Gender, on_delete=models.CASCADE, verbose_name='gender', null=True)
    about = models.TextField(verbose_name='about_product')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=StatusChoices.choices, default=StatusChoices.draft)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
