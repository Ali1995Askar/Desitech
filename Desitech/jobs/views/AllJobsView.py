from django.views.generic import ListView
from jobs.models import Job
from accounts.models.CompanyProfile import Company_profile
from accounts.models.City import City


class AllJobsView(ListView):

    model = Job
    template_name = 'list_jobs.html'
    context_object_name = 'jobs'
    ordering = ['date']
    jobs = Job.job_manger.all()
    
    def get_context_data(self, **kwargs):
        context = super(AllJobsView, self).get_context_data(**kwargs)
        
        Cities = City.objects.all()
        Companies = Company_profile.objects.all()
        jobs = self.get_queryset()
        
        context['jobs'] = jobs
        context['jobsCount'] = len (jobs)

        context['Cities'] = Cities
        context['Companies'] = Companies

        return context