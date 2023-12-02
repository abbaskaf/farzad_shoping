# Generated by Django 4.2.7 on 2023-11-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women')], default='men', max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('publish', 'Publish'), ('draft', 'Draft')], default='draft', max_length=30, verbose_name='status'),
        ),
    ]
