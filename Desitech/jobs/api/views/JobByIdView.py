
from jobs.models import Job
from jobs.api.serializers.JobSerializer import JobSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



class JobById(APIView):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    
    def get(self, request, pk ,  format=None):

        try:

            job= Job.job_manger.get( pk=pk)
            jobDeatils = JobSerializer(job)
            status_code = status.HTTP_200_OK
            response = {'job' : jobDeatils.data ,}
            return Response(response , status_code)

        except Exception as err:
            status_code = status.HTTP_404_NOT_FOUND
            response = {'error' : str (err) ,}
            return Response (response , status_code)






# class JobDeatils(APIView):
  
#     def get(self, request , pk, format=None ):
#         jobs = job.job_manger.get( pk=pk)
#         jobq = JOBSerializer(jobs)
#         return Response(jobq.data)



























