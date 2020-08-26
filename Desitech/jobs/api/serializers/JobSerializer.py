from rest_framework import serializers
from jobs.models import Job



class JobSerializer(serializers.ModelSerializer):
    # tracks = serializers.RelatedField(source='publish_By.email', read_only=True)
    company_Name = serializers.ReadOnlyField(source = 'publish_By.getProfile.Name')
    class Meta:
        model = Job
        fields = ('company_Name' , 'id' , 'publish_By' ,'title', 'skills', 'abstract', 'description', 'country', 'city', 'date')


    # company_name = serializers.RelatedField(source='company_profile', read_only=True)
