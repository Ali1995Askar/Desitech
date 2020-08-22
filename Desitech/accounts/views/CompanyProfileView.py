
from django.shortcuts import render , HttpResponse , redirect
from django.views import View
from django.contrib.auth import login , logout 
from accounts.forms import UserForm , CompanyForm
from accounts.models.User import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from Desitech.decorators import is_company , doesnt_have_profile



login_decorator = login_required (login_url = 'accounts:login')


@method_decorator(login_decorator, name='dispatch')
@method_decorator(is_company, name='dispatch')
@method_decorator(doesnt_have_profile, name='dispatch')


# Create your views here.

class signup (View):

    def get(self, request):
        
       
        company_profile_form = CompanyForm.signup_form ()

        context = {'company_profile_form' : company_profile_form , 'page_title' : 'company profile' }
        return render (request , 'company_signup.html' , context)

    def post (self, request):

      
        company_profile_form = CompanyForm.signup_form (request.POST)
        
        if  company_profile_form.is_valid():
             
                company_profile = company_profile_form.save(commit=False)

               
                company_profile.user = request.user
                company_profile.save()

              
                return redirect ('/' )
        else:
            context = {'company_profile_form' : company_profile_form , 'page_title' : 'company profile' }
            return render (request , 'company_signup.html' , context)
      
