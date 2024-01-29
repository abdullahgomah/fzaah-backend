from django.shortcuts import render, redirect 
from .models import * 
from django.contrib.auth.decorators import login_required
import json 
from page.models import *

# Create your views here.

@login_required(login_url='/user/login/') 
def new_order(request, store_id): 
    info = Info.objects.first() 
    store = Store.objects.get(id=store_id) 
    products = Product.objects.filter(store=store) 


    if request.POST: 
        products_list = request.POST.get('products_list') 
        order_number= request.POST.get('order_number')
        if products_list is not None: 

            total_counter = 0 
            order = Order.objects.create(
                user=request.user, 
                store=store, 
                status='new', 
                number=order_number 
            ) 
            
            lst = products_list.split('-') 
            for i in lst: 
                sub_list = i.split(',') 
                if sub_list[0] !="" and len(sub_list) > 1: 
                    product_id = sub_list[0] 
                    product_qty = sub_list[1] 
                    total = sub_list[2]
                    order_product = OrderProduct.objects.create( 
                    order =order, product=Product.objects.get(id=product_id), 
                    qty = product_qty, 
                    total=total 
                )
                elif sub_list[0] == "" and len(sub_list) > 1: 
                    product_id = sub_list[1] 
                    product_qty = sub_list[2] 
                    total = sub_list[3]
                    order_product = OrderProduct.objects.create( 
                        order =order, product=Product.objects.get(id=product_id), 
                        qty = product_qty, 
                        total=total 
                    )
                
            
            for product in order.products.all(): 
                total_counter += product.total 
            
            order.total = total_counter

            tax = 15/100 
            commission = 5/ 100 

            commission_value = order.total * commission 
            tax_vlaue = commission_value * tax 

            order.total_with_tax = order.total + tax_vlaue + commission_value
            order.commission_value = commission_value 
            order.commission_tax_value = tax_vlaue

            order.save() 


    context = {
        'info': info, 
        'products': products, 
        'store_id': store_id

    } 
    return render(request, 'order/new-order.html', context) 


def order_sent(request): 
    context=  {} 
    return render(request, 'order/order-sent.html', context)

def update_products_select(request, store_id): 
    store = Store.objects.get(id=store_id) 
    products = Product.objects.filter(store=store) 

    context = { 
        'products': products, 
    }

    return render(request, 'order/products-select.html', context)


def select_store(request): 
    stores = Store.objects.all() 
    if request.POST: 
        store_input = request.POST.get('store-input') 
        if store_input is not None: 
            return redirect('order:new-order', store_input)
    context = {
        'stores': stores, 
    }
    return render(request, 'order/select-store.html', context)