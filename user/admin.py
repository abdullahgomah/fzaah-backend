from django.contrib import admin
from .models import CustomUser, Bank

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Bank)