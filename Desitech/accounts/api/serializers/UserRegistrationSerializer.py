from accounts.models.User import User

     
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from accounts.api.serializers.UserSerializer import UserSerializer
from rest_framework import serializers


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserRegistrationSerializer(serializers.ModelSerializer):
  
    user = UserSerializer(required=False)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ( 'user', 'token')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
       
        account_data = validated_data.pop('user')
      
        user = User.objects.create_user(
        email = account_data['email'] , 
        password= account_data['password'] ,  
        user_type = account_data['user_type'] , 
        )

        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        update_last_login(None, user)

        return {
            'email':user.email,
            'token': jwt_token , 
        } 

  