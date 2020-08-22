from rest_framework import serializers
from accounts.models.Country import Country



class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id' , 'name')
