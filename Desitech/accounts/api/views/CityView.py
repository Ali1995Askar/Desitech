
from accounts.models.City import City
from accounts.api.serializers.CitySerializer import CitySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny 



class CitiesOfCountry(APIView):
    permission_classes = (AllowAny,)
   
    def get(self, request, pk ,  format=None):

        try:

            cities= City.objects.filter(country=pk)
          
            citiesDeatils = CitySerializer(cities , many=True)
            status_code = status.HTTP_200_OK
            response = { 'cities' : citiesDeatils.data , }
            return Response(response , status_code)

        except Exception as err:
            status_code = status.HTTP_404_NOT_FOUND
            response = {'error' : str (err) ,}
            return Response (response , status_code)


class AllCities(APIView):
    permission_classes = (AllowAny,)
   
    def get(self, request ,  format=None):

        try:

            cities= City.objects.all()
            
            citiesDeatils = CitySerializer(cities, many=True)
           
            status_code = status.HTTP_200_OK
            response = {'cities' : citiesDeatils.data ,}
            return Response(response , status_code)

        except Exception as err:
            status_code = status.HTTP_404_NOT_FOUND
            response = {'error' : str (err) ,}
            return Response (response , status_code)










 















