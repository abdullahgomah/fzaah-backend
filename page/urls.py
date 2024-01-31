from django.urls import path 
from .views import * 

app_name= 'page'

urlpatterns = [
    path('', index, name='index'), 
    path('about/', about, name='about'), 
    path('terms-and-conditions/', terms_conditions, name='terms-conditions'), 
    path('return-policy/', return_policy, name='return-policy'), 
    path('privacy-policy/', privacy_policy, name='privacy-policy'), 
]