# Generated by Django 5.0.1 on 2024-01-13 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='الاسم')),
            ],
            options={
                'verbose_name': 'نوع',
                'verbose_name_plural': 'الأنواع',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم المتجر')),
                ('url', models.URLField(verbose_name='رابط المتجر')),
                ('phone_number', models.CharField(max_length=50, verbose_name='رقم التواصل')),
            ],
            options={
                'verbose_name': 'متجر',
                'verbose_name_plural': 'المتاجر',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='اسم المنتج')),
                ('purchasing_price', models.FloatField(verbose_name='سعر الشراء')),
                ('selling_price', models.FloatField(verbose_name='سعر البيع')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category', verbose_name='النوع')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.store', verbose_name='المتجر')),
            ],
            options={
                'verbose_name': 'منتج',
                'verbose_name_plural': 'المنتجات',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
