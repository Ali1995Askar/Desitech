from django.core.exceptions import PermissionDenied
from functools import wraps
from accounts.models.JobSeekerProfile import job_seeker_profile
from accounts.models.CompanyProfile import Company_profile
from jobs.models import Job



def company_is_publish_job(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        _job = Job.job_manger.get(pk=kwargs['pk'])
        if _job.publish_By_id == request.user.id:
             return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
  return wrap

def is_admin(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        if  request.user.is_superuser:
             return function(request, *args, **kwargs)
        else:
             raise PermissionDenied
  return wrap

def is_company(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        if  request.user.user_type == 1  :
             return function(request, *args, **kwargs)
        else:
             raise PermissionDenied
  return wrap

def is_job_seeker(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        if  request.user.user_type == 2:
             return function(request, *args, **kwargs)
        else:
             raise PermissionDenied
  return wrap

def is_company_or_admin(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        if  request.user.is_superuser or request.user.user_type == 1 :
             return function(request, *args, **kwargs)
        else:
             raise PermissionDenied
  return wrap

def has_profile(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
          if request.user.user_type == 1 :
               profile  = Company_profile.objects.filter (user = request.user.id)
             
               if len(profile) <  1:
                    return function(request, *args, **kwargs)
               else:
                    raise PermissionDenied
          if request.user.user_type == 2 :
               profile  = job_seeker_profile.objects.filter (user = request.user.id)
               if len(profile) <  1:
                    return function(request, *args, **kwargs)
               else:
                    raise PermissionDenied
  return wrap