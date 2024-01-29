from django.db import models

# Create your models here.

class Store(models.Model):

    name = models.CharField(max_length=100, verbose_name="اسم المتجر") 
    url = models.URLField(verbose_name="رابط المتجر") 
    phone_number = models.CharField(max_length=50, verbose_name="رقم التواصل") 

    def __str__(self):
        return self.name 

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'متجر'
        verbose_name_plural = 'المتاجر'


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="الاسم") 
    

    def __str__(self):
        return self.name 

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'نوع'
        verbose_name_plural = 'الأنواع'

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name="المتجر") 
    name = models.CharField(max_length=200, verbose_name="اسم المنتج") 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="النوع")  
    purchasing_price  = models.FloatField(verbose_name="سعر الشراء") 
    selling_price = models.FloatField(verbose_name="سعر البيع")

    def __str__(self):
        return self.name 

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'منتج'
        verbose_name_plural = 'المنتجات'