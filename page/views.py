from django.shortcuts import render
from page.models import Info 
from order.models import Review 

# Create your views here.
def index(request): 
    reviews = Review.objects.all()[:3]
    context= {
        'reviews': reviews 
    } 
    return render(request, 'page/home.html', context)


def about(request): 
    context=  {} 
    return render(request, 'page/about.html', context)



def terms_conditions(request): 
    info = Info.objects.first() 
    context=  {
        'info': info, 
    } 
    return render(request, 'page/terms-conditions.html', context)



def return_policy(request): 
    info = Info.objects.first() 
    context=  {
        'info': info, 
    } 
    return render(request, 'page/return_policy.html', context)



def privacy_policy(request): 
    info = Info.objects.first() 
    context=  {
        'info': info, 
    } 
    return render(request, 'page/privacy-policy.html', context)