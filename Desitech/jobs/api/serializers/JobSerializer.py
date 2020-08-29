from rest_framework import serializers
from jobs.models import Job
from accounts.models.City import City
from accounts.models.Country import Country

class JobSerializer(serializers.ModelSerializer):
    
    company_Name = serializers.ReadOnlyField(source = 'publish_By.getProfile.Name')
    country_Name = serializers.ReadOnlyField(source = 'country.getName')
    city_Name = serializers.ReadOnlyField(source = 'city.getName')
    class Meta:
        model = Job
        fields = ('id', 'company_Name' , 'publish_By' ,'title',
                    'skills', 'abstract', 'description', 'country', 'country_Name' ,  'city', 
                    'city_Name', 'date')


