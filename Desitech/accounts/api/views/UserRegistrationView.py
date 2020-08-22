from accounts.api.serializers.UserRegistrationSerializer import UserRegistrationSerializer 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.generics import CreateAPIView 


class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
         
           
            serializer.is_valid(raise_exception=True)
            print (serializer.is_valid())
          
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {'token' : serializer.data['token'],}
                
        except Exception as err:
            status_code = status.HTTP_409_CONFLICT
            response = {'error' : str (err)}

        return Response(response, status=status_code)
