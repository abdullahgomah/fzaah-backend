from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied 
from .utils import send_otp, generate_otp 
from .models import CustomUser 
from .forms import SignupForm, UpdateUserForm
from order.models import * 

# Create your views here.
def custom_login(request): 
    if request.user.is_authenticated: 
        return redirect('page:index')
    else: 
        if request.POST: 
            phone_number = request.POST['phone_number']
            user = CustomUser.objects.filter(phone_number=phone_number).first() 
            if user:                 
                otp = generate_otp() 
                send_otp(phone_number, otp)
                request.session['otp'] = otp 
                request.session['phone_number'] = phone_number 

                return redirect('user:enter-otp')
            else: 
                messages.error(request, "رقم الهاتف غير صحيح") 


    context = {}
    return render(request, 'user/login.html', context)

def enter_otp(request): 
    if request.user.is_authenticated: 
        return redirect('user:profile') 
    else: 
        if request.POST: 
            otp = request.POST['otp'] 
            stored_otp= request.session['otp']
            phone_number = request.session['phone_number']
            user = CustomUser.objects.filter(phone_number=phone_number).first() 

            if str(otp) == str(stored_otp): 
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f"أهلا، {user.username}")
                return redirect('page:index') 

    context = {} 
    return render(request, 'user/enter-otp.html', context=context)


def signup(request): 
    if request.POST: 
        form = SignupForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            # redirect to login page 
            return redirect('user:custom-login') 
    else: 
        form = SignupForm() 
    context = {
        'form': form 
    } 
    return render(request, 'user/signup.html', context= context)


@login_required(login_url='/user/login/')
def profile(request): 
    form = UpdateUserForm(instance=request.user) 
    if request.POST: 
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid(): 
            form.save() 
            return redirect('user:profile') 
    context = {
        'form': form
    } 
    return render(request, 'user/profile.html', context=context)


def custom_logout(request): 
    logout(request) 
    context = {} 
    return render(request, 'user/logged-out.html', context) 


@login_required
def user_orders(request): 
    user = request.user 

    orders = Order.objects.filter(user=user) 

    context = {
        'orders': orders 
    }

    return render(request, 'user/profile-orders.html', context)


@login_required
def edit_profile(request):
    form = UpdateUserForm(instance=request.user) 
    if request.POST:
        form = UpdateUserForm(request.POST, instance=request.user) 
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "تم حفظ التعديلات بنجاح")
            return redirect('user:edit-profile')
    context = {
        'form': form, 
    } 
    return render(request, 'user/profile-edit.html', context)