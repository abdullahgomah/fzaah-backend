from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Info(models.Model): 
    service_description = RichTextField(config_name='awesome_ckeditor')
    public_policies = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    payment_methods = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)
    terms = RichTextField(config_name='awesome_ckeditor', null=True, blank=True)

    class Meta: 
        verbose_name = 'معلومات الموقع'
        verbose_name_plural = 'معلومات الموقع'