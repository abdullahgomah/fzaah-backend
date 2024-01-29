from django.db import models
from product.models import * 
from user.models import CustomUser 

# Create your models here.

ORDER_STATUS_CHOICES = (
    ('new', 'جديد'), 
    ('approved', 'مقبول'), 
    ("disapproved", "غير مقبول"), 
    ("done", 'مكتمل'), 
)

class Order(models.Model): 
    user = models.ForeignKey(CustomUser, verbose_name='المستخدم', on_delete =models.SET_NULL, null=True, blank=True)   
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, verbose_name='المتجر')
    # products = models.ManyToManyField(Product, verbose_name="المنتجات") 
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, verbose_name="حالة الطلب", null=True, blank=True)
    number = models.CharField(max_length=255, verbose_name='رقم الطلب في المتجر')
    date= models.DateTimeField(verbose_name="التاريخ", auto_now_add=True) 
    total = models.FloatField(verbose_name='الإجمالي', null=True, blank=True) 
    commission_value = models.FloatField(verbose_name='قيمة العمولة', null=True, blank=True) 
    commission_tax_value = models.FloatField(verbose_name='قيمة ضريبة العمولة', null=True,blank=True)
    total_with_tax = models.FloatField(verbose_name='الإجمالي مع ضريبة العمولة', null=True, blank=True)

    def __str__(self): 
        return str(self.number) 
    
    class Meta: 
        verbose_name = 'طلب' 
        verbose_name_plural = 'الطلبات' 


class OrderProduct(models.Model): 
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='رقم الطلب', related_name='products')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name="المنتج")
    qty= models.IntegerField(default=1, verbose_name="الكمية") 
    total = models.FloatField(verbose_name='المجموع', blank=True) 

    class Meta: 
        verbose_name_plural = 'المنتجات المطلوبة'