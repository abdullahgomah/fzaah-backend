from django.urls import path 
from .views import * 

app_name= 'order' 

urlpatterns = [
    path('new/<int:store_id>/', new_order, name='new-order'), 
    path('new/select-store/', select_store, name='select-store'),
    path('order-sent/', order_sent, name='order-sent'), 
    path('update_products_select/<int:store_id>/', update_products_select, name='update-products-select'), 
    path('details/<str:number>/', show_order, name='show-order'), 
]