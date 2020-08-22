
from accounts.models.Country import Country
from accounts.api.serializers.CountrySerializer import CountrySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny 






class AllCountries(APIView):
    permission_classes = (AllowAny,)
   
    def get(self, request,  format=None):

        try:

            countries= Country.objects.all()
            
            countriesDeatils = CountrySerializer(countries, many=True)
           
            status_code = status.HTTP_200_OK
            response = {'countries' : countriesDeatils.data ,}
            return Response(response , status_code)

        except Exception as err:
            status_code = status.HTTP_404_NOT_FOUND
            response = {'error' : str (err) ,}
            return Response (response , status_code)


























