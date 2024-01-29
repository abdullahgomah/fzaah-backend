from django.db import models
from order.models import * 

# Create your models here.

class Invoice(models.Model): 
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta: 
        verbose_name = 'فاتورة' 
        verbose_name_plural= 'الفواتير'