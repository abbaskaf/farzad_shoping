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


class Product(models.Model):

    class GenderChoices(models.Choices):
        men='men'
        women='women'
    class StatusChoices(models.Choices):
        publish = _('publish')
        draft = _('draft')

    image = models.ImageField(upload_to='posts/', verbose_name='image_product', )
    name = models.CharField(max_length=100, null=True, blank=False)
    about = models.TextField(verbose_name='about_product')
    price = models.IntegerField()
    gender = models.CharField(max_length=5,choices=GenderChoices.choices,default=GenderChoices.men)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    status= models.CharField(max_length=30,choices=StatusChoices.choices,default=StatusChoices.draft,verbose_name='status')
