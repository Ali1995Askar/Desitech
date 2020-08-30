

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from jobs.models import Job
from jobs.api.serializers.JobSerializer import JobSerializer
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class JobsByCompany(APIView):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    

    def get(self, request , format=None):
        try: 
            id = request.user.id
            jobs = Job.job_manger.filter(publish_By = id).order_by('-date')
            jobsByCompany = JobSerializer(jobs, many=True)
            status_code = status.HTTP_200_OK
            response = {'jobs' : jobsByCompany.data , }
            return Response(response , status_code)

        except Exception as err :
            status_code = status.HTTP_404_NOT_FOUND
            response = {'error' : str (err) , }
            return Response (response , status_code)
          
          

























