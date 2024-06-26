# Generated by Django 5.0.4 on 2024-05-05 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='CodeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_1', models.CharField(max_length=255)),
                ('code_2', models.CharField(max_length=255, null=True)),
                ('code_3', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('short_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StockProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_1', models.IntegerField()),
                ('stock_2', models.IntegerField(null=True)),
                ('stock_3', models.IntegerField(null=True)),
                ('product_year', models.CharField(max_length=15, null=True)),
                ('date_of_arrival', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whole_sale_price', models.FloatField()),
                ('retail_sale_price', models.FloatField()),
                ('sale_price_3to5', models.FloatField()),
                ('sale_price_5to10', models.FloatField()),
                ('sale_price_above10', models.FloatField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.state')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('alcohol_strength', models.FloatField()),
                ('case_bottles_number', models.IntegerField(default=12)),
                ('beverage', models.ManyToManyField(to='products.beverage')),
                ('code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.codeproduct')),
                ('country', models.ManyToManyField(to='products.country')),
                ('price', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.priceproduct')),
                ('region', models.ManyToManyField(to='products.region')),
                ('state', models.ManyToManyField(to='products.state')),
                ('stock', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.stockproduct')),
            ],
        ),
    ]
