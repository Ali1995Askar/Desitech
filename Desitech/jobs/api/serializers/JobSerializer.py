from rest_framework import serializers
from jobs.models import Job



class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('title', 'skills', 'abstract', 'description', 'country', 'city', 'date')
