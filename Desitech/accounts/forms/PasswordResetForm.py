from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from accounts.models.User import User
from django.contrib.auth.forms import PasswordResetForm


class SendMailForm (PasswordResetForm) :
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs= {'class': 'form-control', 'placeholder':"Enter your email "})
    )
    
    def clean_email (self):
        data = self.cleaned_data['email']
        return data.lower()




