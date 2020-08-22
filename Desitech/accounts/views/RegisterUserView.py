from django.shortcuts import render , HttpResponse , redirect
from django.views import View
from django.contrib.auth import login , logout 
from accounts.forms import UserForm , CompanyForm
from accounts.models.User import User

class signup (View):

    def get(self, request):
        
        user_form = UserForm.signup_form ()
        context = {'user_form' : user_form ,  'page_title' : 'user signup' }
        return render (request , 'user_signup.html' , context)

    def post (self, request):

        user_form = UserForm.signup_form(request.POST)
        
        if user_form.is_valid() :
            user = user_form.save()

            login(request , user)
            if user.user_type == User.COMPANY:
                return redirect ('/accounts/companyProfile/' )
            if user.user_type == User.JOB_SEEKER:
                return redirect ('/accounts/jobSeekerProfile/' )
        else:
            context = {'user_form' : user_form  , 'page_title' : 'user signup' }
            return render (request , 'user_signup.html' , context)
      
