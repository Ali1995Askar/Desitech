from rest_framework.generics import CreateAPIView 
from accounts.models.JobSeekerProfile import job_seeker_profile
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser

from accounts.api.serializers.ProfileSerializer import JobSeekerProfileSerializer
from accounts.models.Country import Country
from accounts.models.City import City
import json

class JobSeekerInformationView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    parser_classes = (MultiPartParser,)

    def post(self, request):
       
        
        if request.user.is_job_seeker :
            try:
            
                jsonsString = request.data['data']

                jsonString = jsonsString.replace ("\'" , "\"")
               
                data = json.loads(jsonString)
                
                job_seeker_profile.objects.create(
                    user=request.user , 
                    Name = data['Name'] ,
                    surname = data['surname'] ,
                    country = Country.objects.get (id = int(data['country'])) ,
                    city =  City.objects.get (id = int(data['city'])) ,
                    nationality =  data['nationality'] ,
                    birth_date =  data['birth_date'] ,
                    gender = data['gender'] ,
                    zip_code =  data['zip_code'] ,
                    street =  data['street'] ,
                    house_number =  data['house_number'] ,
                    personal_photo =  request.FILES['personal_photo'] ,
                    CV =  request.FILES['CV'] ,
                    cover_letter =  data['cover_letter'] ,
                    phone_number =  data['phone_number'] ,
                    mobile_number =  data['mobile_number'] ,    
                    )

                status_code = status.HTTP_200_OK
                response = {'success' : 'True'}
            except Exception as err:
             
                status_code = status.HTTP_406_NOT_ACCEPTABLE
                response = {'error' : str(err) }
        

            return Response(response, status=status_code)
        else:
            response = {'error' : 'this url is only for job seeker user , check auth or type of user.' }

   