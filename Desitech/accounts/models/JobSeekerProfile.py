from django.db import models
from accounts.models.User import User
from django.core.validators import FileExtensionValidator
from accounts.models.Country import Country
from accounts.models.City import City
from django.conf import settings
from django.core.validators import RegexValidator
from datetime import datetime



class job_seeker_profile (models.Model):
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , primary_key=True)
    Name = models.CharField(max_length=30 , null=False)
    surname = models.CharField(max_length=30 , null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    nationality = models.CharField(max_length=50 , null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES , null=True)
    zip_code =  models.CharField("ZIP / Postal code", max_length=12,null=True)
    street =models.CharField(max_length=128 , null=True)
    house_number = models.IntegerField(null=True)
    personal_photo =models.ImageField(upload_to='images/' , null=True)
    CV = models.FileField(upload_to='CV/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])] , null=True) 
    cover_letter = models.TextField(null=True)
   
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    
    phone_number = models.CharField( validators=[phone_regex] , max_length=17 , null=True) 
    mobile_number = models.CharField( validators=[phone_regex] ,max_length=17 , null=True)  


    @property
    def age(self):
        return int((datetime.now().date() - self.birth_date).days / 365.25)
    
    @property
    def sex(self):
        if self.gender == 'M':
            return 'Male'
        if self.gender == 'F':
             return 'FeMale'
