from accounts.models.User import User

     
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from accounts.api.serializers.UserSerializer import UserSerializer
from rest_framework import serializers




JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginSerializer(serializers.Serializer):
  

    email = serializers.EmailField(max_length=255 , write_only = True)
    password = serializers.CharField(max_length=128, write_only=True)

    user_id = serializers.CharField(max_length=128, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)


    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
      
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
       
      
        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        update_last_login(None, user)
         
        return {'user_id':str(user.id),'token': jwt_token } 




    

   