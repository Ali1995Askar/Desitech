from rest_framework.generics import CreateAPIView 
from accounts.models.CompanyProfile import Company_profile
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status
from rest_framework.views import APIView
from accounts.api.serializers.ProfileSerializer import CompanySerializer
from accounts.models.Country import Country
from accounts.models.City import City

class CompanyInformationView(CreateAPIView):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    
    def post(self, request):
    
        if request.user.is_company :
           
            try:
                Company_profile.objects.create(
                    user=request.user ,   
                    Name = request.data['Name'] ,
                    zip_code = request.data['zip_code'] ,
                    street = request.data['street'] ,
                    building_number = request.data['building_number'] ,
                    phone_number = request.data['phone_number'] ,
                    mobile_number = request.data['mobile_number'] ,
                    country = Country.objects.get (id = int(request.data['country'])) ,
                    city =  City.objects.get (id = int(request.data['city'])) ,

                    )
                status_code = status.HTTP_200_OK
                response = {'success' : 'True',}
            except Exception as err:
               
                status_code = status.HTTP_406_NOT_ACCEPTABLE
                response = {'error' : str(err) ,}
        

            return Response(response, status=status_code)


   