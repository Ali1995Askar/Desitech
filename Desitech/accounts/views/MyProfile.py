
from django.views import View
from django.shortcuts import HttpResponse , render , redirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.models.CompanyProfile import Company_profile
from accounts.models.JobSeekerProfile import job_seeker_profile
from Desitech.decorators import  have_profile

login_decorator = login_required (login_url = 'accounts:login')

@method_decorator(login_decorator, name='dispatch')
@method_decorator(have_profile, name='dispatch')

class MyProfile (View):

    def get (self , request):
        context = {'page_title' : 'my profile' , 'profile' : request.user.getProfile()}
     
        if request.user.is_company:
            return  render (request , 'CompanyProfile.html' , context )
        
        if request.user.is_job_seeker:
            return  render (request , 'JobSeekerProfile.html' , context )

    def post (self , request):
        pass

 

