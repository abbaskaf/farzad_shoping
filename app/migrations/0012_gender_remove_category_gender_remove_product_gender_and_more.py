# Generated by Django 4.2.7 on 2023-12-01 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_gender_category_gender_product_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='product',
            name='gender',
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('publish', 'Publish'), ('draft', 'Draft')], default='draft', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='genders',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.gender', verbose_name='gender'),
        ),
    ]
