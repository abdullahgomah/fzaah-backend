from django.contrib import admin
from .models import * 

# Register your models here.




admin.site.register(OrderProduct) 


class OrderProductInline(admin.TabularInline):  # Use TabularInline or StackedInline based on your preference
    model = OrderProduct
    extra = 0  # Number of empty forms to display

class OrderFilter(admin.ModelAdmin): 
    list_filter = ('status', 'user', 'date')  
    search_fields = ['number', 'user__username', 'store__name']
    list_filter = ['status', 'date']
    inlines = [OrderProductInline]


admin.site.register(Order, OrderFilter) 
