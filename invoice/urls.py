from django.urls import path 
from .views import * 
app_name = 'invoice'  


urlpatterns = [
    path('export/<str:order_number>/', render_pdf_view, name='export-invoice'), 
    path('show/<str:order_number>/', show_invoice, name='show-invoice'), 
    path('not-found/', order_not_found, name='order-not-found'), 
]