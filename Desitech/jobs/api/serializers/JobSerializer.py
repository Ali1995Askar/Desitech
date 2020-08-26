from rest_framework import serializers
from jobs.models import Job



class JobSerializer(serializers.ModelSerializer):
    
    company_Name = serializers.ReadOnlyField(source = 'publish_By.getProfile.Name')
    class Meta:
        model = Job
        fields = ('company_Name' , 'id' , 'publish_By' ,'title', 'skills', 'abstract', 'description', 'country', 'city', 'date')


