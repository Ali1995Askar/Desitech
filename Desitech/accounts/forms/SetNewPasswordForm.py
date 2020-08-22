from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import views as auth_views

class SetNewPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class': 'form-control', 'placeholder':"Enter New Password "}),
        strip=False,
    )

    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class': 'form-control', 'placeholder':"Enter  Password Confirmation"}),
    )

