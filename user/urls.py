from django.urls import path 
from .views import * 

app_name = 'user' 

urlpatterns = [
    path('login/', custom_login, name='custom-login'), 
    path('enter-otp/', enter_otp, name='enter-otp'), 
    path('signup/', signup, name='signup'),
    # path('profile/', profile, name='profile'), 
    path('profile/orders/', user_orders, name='user-orders'), 
    path('logout/', custom_logout, name='custom-logout'), 
    path('profile/', edit_profile,name='profile'), 
]