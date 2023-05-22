# Generated by Django 4.2.1 on 2023-05-12 22:10

import datetime
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('category_description', models.CharField(max_length=250, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('product_description', models.CharField(max_length=250, verbose_name='Описание')),
                ('product_image', models.ImageField(max_length=150, upload_to='', verbose_name='Изображение(превью)')),
                ('product_sale_price', models.FloatField(verbose_name='Цена за покупку')),
                ('create_date', models.DateField(default=datetime.date(2023, 5, 12), verbose_name='Дата создания')),
                ('update_date', models.DateField(default=datetime.date(2023, 5, 12), verbose_name='Дата изменения')),
                ('product_category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
        ),
    ]
