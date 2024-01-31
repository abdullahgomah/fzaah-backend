from django.shortcuts import render

# Create your views here.
def index(request): 
    context= {} 
    return render(request, 'page/home.html', context={})


def about(request): 
    context=  {} 
    return render(request, 'page/about.html', context)