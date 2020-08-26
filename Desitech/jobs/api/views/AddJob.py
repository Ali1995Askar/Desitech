from rest_framework.generics import CreateAPIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status
from rest_framework.views import APIView

from accounts.models.User import User
from accounts.models.Country import Country
from accounts.models.City import City
from jobs.models import Job
from jobs.api.serializers.JobSerializer import JobSerializer


class AddJob(CreateAPIView):
  
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
   

    def post(self, request):
            
            if request.user.is_company :
                try:

                    serializer = self.serializer_class(data=request.data)

                    serializer.is_valid(raise_exception=True)

                    serializer.save()

                    status_code = status.HTTP_200_OK
                    response = {'success' : 'True'}

                except Exception as err:
                    status_code = status.HTTP_406_NOT_ACCEPTABLE
                    response = {'error' : str(err) }

                return Response(response, status=status_code)
            else:
                status_code = status.HTTP_406_NOT_ACCEPTABLE
                response = {'error' :'register as company' ,'status code' : status_code}



   