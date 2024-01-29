from django import forms
from .models import CustomUser 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 

class SignupForm(UserCreationForm): 
    # email = forms.EmailField(max_length=254,label='البريد الإلكتروني', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # username = forms.CharField(label='اسم المستخدم', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phone_number = forms.CharField(label="رقم الجوال", widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password1 = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.CharField(label="تأكيد كلمة المرور", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta: 
        model = CustomUser 
        fields = ['email', 'username', 'phone_number', 'password1', 'password2']



class UpdateUserForm(UserChangeForm): 
    class Meta: 
        model = CustomUser 
        fields = [
            'email', 'username', 'phone_number', 'full_name', 'bank_name', 'iban', 'id_number', 'swift_code'
        ]
        exclude = ('password1', 'password2')