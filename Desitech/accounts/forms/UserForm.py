
from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from accounts.models.User import User



class signup_form (UserCreationForm) :

    email = forms.EmailField(
        label= "email" , 
        widget=forms.EmailInput(attrs= {'class': 'form-control', 'placeholder':"Enter your email "}),
    )

    password1 = forms.CharField(
        label= "Password" ,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class': 'form-control', 'placeholder': "Password"}),
    )
    
    password2 = forms.CharField(
        label="Password confirmation" ,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class': 'form-control', 'placeholder': "Password confirmation"}),
        strip=False,
    )

    user_type = forms.ChoiceField(
        choices = User._TYPE ,
        label="User Type" ,
        widget=forms.Select(attrs= {'class': 'form-control'}),
 
       
    )
   
    class Meta:
        model = User
        fields = ('email', 'password1' , 'password2' , 'user_type')
    
    def clean_email (self):
        data = self.cleaned_data['email']
        return data.lower()





