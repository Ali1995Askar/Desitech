
from django import forms 
from django.contrib.auth.forms import  AuthenticationForm
from django.db import transaction
from accounts.models.User import User



class Login_Form (AuthenticationForm) :

    username = forms.EmailField(
        label= "email" , 
        widget=forms.EmailInput(attrs= {'class': 'form-control', 'placeholder':"Enter your email "}),
    )

    password = forms.CharField(
        label= "Password" ,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class': 'form-control', 'placeholder': "Password"}),
    )
    






