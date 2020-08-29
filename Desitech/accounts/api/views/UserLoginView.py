from accounts.api.serializers.UserLoginSerializer import UserLoginSerializer 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.generics import  RetrieveAPIView


class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
   
    def post(self, request):
      
        try:
           
            serializer = self.serializer_class(data=request.data)
            
            serializer.is_valid(raise_exception=True)
         
            response = {
               
                'user_id' : serializer.data['user_id'] ,
                'user_type' :  serializer.data['user_type'] ,
                'token' : serializer.data['token'],
                'completed' :  serializer.data['completed'] ,
                }
          
            status_code = status.HTTP_200_OK
        except Exception as err:
            status_code = status.HTTP_406_NOT_ACCEPTABLE
            response = {'error' : str (err)}
        return Response(response, status=status_code)