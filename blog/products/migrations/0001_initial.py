# Generated by Django 3.1 on 2021-01-28 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uuid', models.UUIDField(blank=True, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('calories', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fats', models.DecimalField(decimal_places=2, max_digits=5)),
                ('carbohydrates', models.DecimalField(decimal_places=2, max_digits=5)),
                ('proteins', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ManyToManyField(to='products.Category')),
            ],
            options={
                'ordering': ('product_name',),
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
        ),
    ]
