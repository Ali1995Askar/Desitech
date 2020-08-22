from rest_framework import serializers
from accounts.models.City import City



class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'country' , 'name',)
