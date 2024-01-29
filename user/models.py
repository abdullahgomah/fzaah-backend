from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Bank(models.Model): 
    name = models.CharField(max_length=255, verbose_name="اسم البنك", null = True, blank=True)

    def __str__(self): 
        return self.name 
    
    class Meta: 
        verbose_name= 'بنك'
        verbose_name_plural = 'البنوك'

class CustomUser(AbstractUser): 
    phone_number = models.CharField(max_length=30, verbose_name="رقم الهاتف") 
    # commercial_registration_img = models.ImageField(upload_to='uploads/commercial-registrations/', verbose_name='صورة السجل التجاري')
    full_name = models.CharField(max_length=255, verbose_name="الاسم بالكامل", null=True, blank=True)
    bank_name = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='اسم البنك') 
    iban = models.CharField(max_length=255, verbose_name="ايبان", null=True, blank=True)
    id_number = models.CharField(max_length=255, verbose_name="رقم الهوية", null=True, blank=True) 
    swift_code = models.CharField(max_length=255, verbose_name='SWIFT CODE', null=True, blank=True)