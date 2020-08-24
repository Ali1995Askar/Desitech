from accounts.models.City import City
from django.shortcuts import render , HttpResponse ,redirect
from jobs.models import Job
from accounts.models.CompanyProfile import Company_profile

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
        context = { 'jobs' : jobsByCity , 'jobsCount' : jobsCount, 'empty' :msg ,}
        return render (request , 'JobSearh.html' , context)

    except Exception as exc:
        return redirect ('jobs:all-jobs-list')

 
    
def JobsByCompany(request):

    try:
        company = Company_profile.objects.get (Name= request.POST.get('company'))
        jobsBycompany = Job.job_manger.filter (publish_By=company.user)
        msg = 'No jobs published By  {} company'.format(str (company.Name)) 
        jobsCount = len (jobsBycompany)
        context = { 'jobs' : jobsBycompany , 'jobsCount' : jobsCount, 'empty' :msg , }
        return render (request , 'JobSearh.html' , context)

    except Exception as exc:
        return redirect ('jobs:all-jobs-list')