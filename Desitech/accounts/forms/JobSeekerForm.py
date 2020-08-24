from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from accounts.models.JobSeekerProfile import job_seeker_profile
from accounts.models.City import City

class signup_form (forms.ModelForm):

    class Meta:
        model = job_seeker_profile
        fields = ( 'Name' , 'surname' , 'country' , 'city'  , 'nationality' ,'birth_date' , 'CV' ,
                    'gender' , 'street' , 'zip_code' , 'phone_number' ,
                    'house_number' , 'personal_photo' ,'cover_letter' ,'mobile_number' ,)
      
    
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name "}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Surname"}),
            'country': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': "country"}),
            'city': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': "city "}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Country Of Residence"}),
            'birth_date': forms.DateInput(attrs={'type':'date' , 'class': 'form-control select', 'placeholder': "birth date"}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': "Gender"}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Zip Code"}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Street "}),
            'house_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "House Number"}),
            'personal_photo':  forms.FileInput(attrs={'type':"file" , 'class': 'form-control fa fa-cloud-upload ' , 'style':'color:cyan'}),
            'CV': forms.FileInput(attrs={'type':"file" , 'class': 'form-control fa fa-cloud-upload ' , 'style':'color:cyan'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Cover Letter", 'rows':"6" , 'style':'resize: none;'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "phone Number like '+999999999'", 'type': 'tel'}),

            'mobile_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "mobile Number like '+999999999'", 'type': 'tel'}),
        }

        labels = {
                'Name': 'Name',
                'surname': 'sur name',
                'country': 'country/region',
                'city': 'city',
                'country_of_residence': 'nationality',
                'age': 'date of birth',
                'gender': 'gender',
                'zip_code': 'zip code',
                'street': 'street',
                'house_number': 'house number',
                'personal_photo': 'personal photo',
                'CV': 'Upload Your CV',
                'cover_letter': 'cover letter',
                'phone_number': 'phone number',
                'mobile_number': 'mobile number', 
            }     

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['city'].queryset = City.objects.none()
        
            if 'country' in self.data:
                try:
                    country_id = int(self.data.get('country'))
                    self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
                except (ValueError, TypeError):
                    pass 
            elif self.instance.pk:
                self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
