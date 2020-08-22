from django import forms
from jobs.models import Job, City
from django.forms import ModelChoiceField

class JobForm(forms.ModelForm):
    city = forms.ModelChoiceField (queryset = City.objects.all(),widget=forms.Select(attrs={'class' : 'form-control'}))
    class Meta:
        model = Job
        fields = ( 'title', 'skills' , 'abstract' , 'description', 'country' , 'city')
        widgets = { 
                    'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Job Title "}),

                    'abstract': forms.Textarea(attrs={
                                                    'class': 'form-control', 
                                                    'placeholder': "abstract of job", 
                                                    'rows':"6" , 
                                                    'style':'resize: none;'}),
                    'skills': forms.Textarea(attrs={
                                                    'class': 'form-control', 
                                                    'placeholder': "Skills Required", 
                                                    'rows':"6" , 
                                                    'style':'resize: none;'}),
                    'description': forms.Textarea(attrs={
                                                    'class': 'form-control', 
                                                    'placeholder': "Other Information", 
                                                    'rows':"6" , 
                                                    'style':'resize: none;'}),

                    'country': forms.Select(attrs={'class': 'form-control select', 'placeholder': "country"}),
                    'city': forms.Select(attrs={'class': 'form-control select', 'placeholder': "city "}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
       
        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
               
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')