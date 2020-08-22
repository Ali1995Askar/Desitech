from rest_framework import serializers
from accounts.models.JobSeekerProfile import job_seeker_profile
from accounts.models.CompanyProfile import Company_profile


class JobSeekerProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = job_seeker_profile
        fields = ('Name', 'surname' , 'country','city', 'country_of_residence' , 'birth_date',
                  'gender', 'zip_code' , 'street','house_number', 'personal_photo' , 'CV',
                   'cover_letter', 'phone_number' , 'mobile_number',)



class  CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company_profile
        fields = ('Name', 'country','city','zip_code' , 'street'
                  ,'building_number', 'phone_number' , 'mobile_number',)

