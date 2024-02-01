from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Info(models.Model): 
    service_description = RichTextField(config_name='awesome_ckeditor')
    public_policies = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    payment_methods = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    terms = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    terms_conditions = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    return_policy = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    privacy_policy = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    email = models.EmailField(blank=True, null=True, verbose_name='البريد الإلكتروني') 
    whatsapp_number = models.CharField(max_length=20, verbose_name='رقم الواتساب', null=True, blank=True) 
    primary_number = models.CharField(max_length=20, verbose_name='رقم اتصال أساسي', null=True, blank=True) 
    secondary_number = models.CharField(max_length=20, verbose_name='رقم اتصال ثانوي', null=True, blank=True) 
    

    class Meta: 
        verbose_name = 'معلومات الموقع'
        verbose_name_plural = 'معلومات الموقع'