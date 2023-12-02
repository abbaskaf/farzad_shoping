# Generated by Django 4.2.7 on 2023-11-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_brand_alter_product_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women')], default='men', max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='image_product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('publish', 'Publish'), ('draft', 'Draft')], default='draft', max_length=30, verbose_name='status'),
        ),
    ]