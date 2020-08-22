from rest_framework import serializers
from accounts.models.User import User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'user_type' , )
