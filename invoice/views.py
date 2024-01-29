from django.shortcuts import render, redirect 
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from order.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def render_pdf_view(request, order_number):
    template_path = 'user_printer.html'
    order_obj = Order.objects.get(number=order_number)
    context = {'order': order_obj}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@login_required
def show_invoice(request, order_number):
    try: 
        order_obj = Order.objects.get(number=order_number)
    except Order.DoesNotExist: 
        return redirect('invoice:order-not-found') 
    context = {'order': order_obj}

    return render(request, 'user_printer.html', context)


def order_not_found(request): 
    context = {} 
    return render(request, 'order/not-found.html', context)