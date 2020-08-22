
from django.shortcuts import render , HttpResponse , redirect
from django.views import View
from django.contrib.auth import login , logout 
from accounts.forms import UserForm , JobSeekerForm
from accounts.models.User import User

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from Desitech.decorators import is_job_seeker , has_profile



login_decorator = login_required (login_url = 'accounts:login')


@method_decorator(login_decorator, name='dispatch')
@method_decorator(is_job_seeker, name='dispatch')
@method_decorator(has_profile, name='dispatch')
# Create your views here.

class signup (View):

    def get(self, request):
        
       
        JobSeeker_profile_form = JobSeekerForm.signup_form ()

        context = {'JobSeeker_profile_form' : JobSeeker_profile_form ,  'page_title' : 'job seeker signup' }
        return render (request , 'jobseeker_signup.html' , context)

    def post (self, request):

        JobSeeker_profile_form = JobSeekerForm.signup_form (request.POST  , request.FILES)
        
        if  JobSeeker_profile_form.is_valid():
         
            job_seeker_profile = JobSeeker_profile_form.save(commit=False)

            job_seeker_profile.user = request.user

            JobSeeker_profile_form.save()

            return redirect ('/' )
        else:
            context = {'JobSeeker_profile_form' : JobSeeker_profile_form , 'page_title' : 'job seeker signup' }
            return render (request , 'jobseeker_signup.html' , context)
      
