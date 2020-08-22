
from accounts.models.City import City
from django.shortcuts import render , HttpResponse
from jobs.models import Job

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'cards/city_list_options.html', {'cities': cities})


def JobsByRegion(request):
    try:
        city = City.objects.get (name= request.POST.get('city'))
        jobsByCity = Job.job_manger.filter (city=city)
        msg = 'No jobs to view in {} city'.format(str (city)) 
        jobsCount = len (jobsByCity)
        return render (request , 'JobSearh.html' , { 'jobs' : jobsByCity , 'jobsCount' : jobsCount, 'empty' :msg })
    except Exception as exc:
        return HttpResponse (exc)
    