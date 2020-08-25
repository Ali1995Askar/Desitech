from django.urls import path , include
from accounts.views import (
                                CompanyProfileView , JobSeekerProfileView , RegisterUserView ,
                                LogView , ResetPasswordView , MyProfile)
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from accounts.forms.SetNewPasswordForm import SetNewPasswordForm
from accounts.api.views.CountryView import AllCountries
from accounts.api.views.CityView import (AllCities , CitiesOfCountry)
from accounts.api.views.UserRegistrationView import UserRegistrationView
from accounts.api.views.UserLoginView import UserLoginView
from accounts.api.views.CompanyInformationView import CompanyInformationView
from accounts.api.views.JobSeekerInformationView import JobSeekerInformationView

app_name = "accounts"

urlpatterns = [

    path('rigester/', RegisterUserView.signup.as_view(), name='Register-User'),
    path('companyProfile/', CompanyProfileView.signup.as_view(), name='Company-profile'),
    path('jobSeekerProfile/', JobSeekerProfileView.signup.as_view(), name='JobSeeker-profile'),
    path('MyProfile/', MyProfile.MyProfile.as_view(), name='My-profile'),
    
    path('login/', LogView.log_user.as_view(), name='login'),
    path('logout/', LogView.logout_user, name='logout'),
   
   


    path("password_reset/", ResetPasswordView.ResetPassword.as_view(), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view
    (
        template_name="password/password_reset_confirm.html" , 
        success_url = reverse_lazy ('accounts:password_reset_complete') ,
        form_class = SetNewPasswordForm
    ),  name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html') , name='password_reset_complete') ,
    


    path ('api/Country/All/' , AllCountries.as_view() , name = 'api-Country-All' ) ,
    path ('api/City/All/' , AllCities.as_view() , name = 'api-City-All' ) ,
    path ('api/CitiesOfCountry/<int:pk>/' , CitiesOfCountry.as_view() , name = 'api-Cities-Of-Country-All' ) ,

    path ('api/user/register/' , UserRegistrationView.as_view() , name = 'api-user-register' ) ,
    path ('api/user/login/' , UserLoginView.as_view() , name = 'api-user-login' ) ,
    path ('api/user/register/CompanyProfile/' , CompanyInformationView.as_view() , name = 'api-company-profile' ) ,
    path ('api/user/register/JobSeekerProfile/' , JobSeekerInformationView.as_view() , name = 'api-job-seeker-profile' ) ,
    ]

   