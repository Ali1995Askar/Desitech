from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from accounts.models.CompanyProfile import Company_profile
from accounts.models.City import City
from django.utils.safestring import mark_safe


class signup_form (forms.ModelForm):

    class Meta:
        model = Company_profile
        fields = ("Name" , 'country' , 'city' 
        , "zip_code" , "street" , "building_number" , "phone_number" , "mobile_number")
       
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Company Name "} , ),
            'country': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': "country"}),
            'city': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': "city "}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "zip/ postal code "}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "street"}),
            'building_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "building number "}),
            'phone_number': forms.NumberInput(attrs=
                                {    'class': 'form-control', 
                                     'placeholder': "phone Number", 
                                     'type': 'tel' , 
                                     'data-format':"+1 (ddd) ddd-dddd" , 
                                     'ata-country':"countryregion"}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "mobile Number", 'type': 'tel'}),
        }

        labels = {
                'Name': 'Company Name',
                'country': 'country/region',
                'city': 'city',
                'zip_code': 'zip code',
                'street': 'street',
                'building_number': 'building number',
                'phone_number': 'phone number',
                'mobile_number': 'mobile number',
            }








        def __init__(self, *args, **kwargs):
            super(signup_form, self).__init__(*args, **kwargs)
            self.fields['city'].queryset = City.objects.none()



        
            if 'country' in self.data:
                try:
                    country_id = int(self.data.get('country'))
                    self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
                except (ValueError, TypeError):
                    pass  
            elif self.instance.pk:
                self.fields['city'].queryset = self.instance.country.city_set.order_by('name')