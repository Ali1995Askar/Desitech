from django.db import models
from django.contrib.auth.models import AbstractBaseUser  , PermissionsMixin
from accounts import models as mo
from accounts.models.UserManger import UserManager

class User (AbstractBaseUser , PermissionsMixin):

    email = models.EmailField(unique=True , null=False)


    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
  
   
    COMPANY = 1
    JOB_SEEKER = 2
    
    REQUIRED_FIELDS = ['user_type']
    USERNAME_FIELD = 'email' 

    _TYPE = ((COMPANY , 'company') , (JOB_SEEKER , 'job_seeker') )
    user_type  = models.PositiveSmallIntegerField (choices=_TYPE  )

    @property
    def is_company (self):
      
        if self.user_type == 1:
            return True
        return False
    @property
    def is_job_seeker (self) :
        if self.user_type == 2:
            return True
        return False

    def getProfile (self):
        try:
            if self.user_type == 1:
                profile = mo.CompanyProfile.Company_profile.objects.get (user = self)
                return profile
            elif self.user_type == 2 :
                profile = mo.JobSeekerProfile.job_seeker_profile.objects.get (user = self)
                return  profile
        except Exception :
            return None
       
    
    objects = UserManager ()